import pymysql

from django.conf import settings
from .log_kit import getLogger

logger = getLogger('dbhelper')


class DBHelper(object):
    """数据库连接类
    """
    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWD, DB_CHARSET, DB_SQLMODE, DB_INIT_COMMAND = "", "", "", "", "", "", "", ""

    def __init__(self):
        self._conn = None
        try:
            self.DB_HOST = settings.DB_HOST
            self.DB_PORT = settings.DB_PORT
            self.DB_NAME = settings.DB_NAME
            self.DB_USER = settings.DB_USER
            self.DB_PASSWD = settings.DB_PASSWD
            self.DB_CHARSET = settings.DB_CHARSET
            self.reconnect()
        except pymysql.Error as e:
            logger.error("Cannot connect to MySQL on %s")

    def reconnect(self):
        self.close()
        self._conn = pymysql.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            passwd=self.DB_PASSWD,
            db=self.DB_NAME,
            port=self.DB_PORT,
            charset=self.DB_CHARSET,
        )
        self._conn.autocommit(True)

    def getConn(self):
        """ 获取数据库连接 """
        if self._conn is None: self.reconnect()
        try:
            self._conn.ping()
        except:
            self.reconnect()

        return self._conn

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    def close(self):
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def begin(self):
        if self._conn is not None:
            try:
                self.execute("BEGIN")
            except Exception as e:
                logger.error("Can not begin transaction")

    def commit(self):
        if self._conn is not None:
            try:
                self._conn.ping()
            except:
                self.reconnect()
            try:
                self._conn.commit()
            except Exception as e:
                self._conn.rollback()
                logger.exception("Can not commit", e)

    def rollback(self):
        if self._conn is not None:
            try:
                self._conn.rollback()
            except Exception as e:
                logger.error("Can not rollback")

    def execute(self, sql, parameters=None):
        cursor = self._cursor()
        try:
            rowcount = self._execute(cursor, sql, parameters)
            return rowcount
        finally:
            cursor.close()

    def executeAndGetId(self, sql, parameters=None):
        cursor = self._cursor()
        try:
            self._execute(cursor, sql, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def readOne(self, sql, parameters=None):
        cursor = self._cursor()
        try:
            rowcount = self._execute(cursor, sql, parameters)
            if rowcount > 0:
                res = cursor.fetchone()
            else:
                res = None
            return res
        finally:
            cursor.close()

    def readList(self, sql, parameters=None):
        cursor = self._cursor()
        try:
            rowcount = self._execute(cursor, sql, parameters)
            if rowcount > 0:
                res = cursor.fetchall()
            else:
                res = None
            return res
        finally:
            cursor.close()

    def _cursor(self):
        if self._conn is None: self.reconnect()
        try:
            self._conn.ping()
        except:
            self.reconnect()
        return self._conn.cursor()

    def _execute(self, cursor, sql, parameters=None):
        try:
            if parameters is None:
                res = cursor.execute(sql)
            else:
                res = cursor.execute(sql, parameters)
            return res
        except pymysql.Error as e:
            logger.error('Mysql Error:%s\nSQL:%s' % (e, sql))
            self.close()
            raise

    def batch_execute(self, sql_list):
        cursor = self._cursor()
        try:
            for sql in sql_list:
                cursor.execute(sql)
            cursor.close()
            self.commit()
        except Exception as e:
            cursor.close()
            self.rollback()
            raise e


if __name__ == "__main__":
    result = DBHelper().readOne("select * from account_meta limit 1")
    print(result)
