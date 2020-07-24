import os
import logging
import datetime

now_time = datetime.datetime.now().strftime('%Y-%m-%d')

LOG_FILE = os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))),
                        "log")
if not os.path.isdir(LOG_FILE):
    os.makedirs(LOG_FILE, exist_ok=True)

LOG_FILE = "log/operation.log." + now_time
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_FILE)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console.setFormatter(formatter)
logger.addHandler(handler)


def logg(url="", request="", response=""):
    logger.info("request URL:{}".format(url))
    logger.info("request body:{}".format(request))
    logger.info("response body:{}".format(response))
    logger.info("\n"*3)
