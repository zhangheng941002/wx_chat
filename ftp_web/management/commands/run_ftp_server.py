#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2020/7/24 13:49
# @Author : Zh
# @Project : yk_wx
# @File   : run_ftp_server.py
# @Software: PyCharm


from django.core.management.base import BaseCommand, CommandError
from utils.ftp_server import ftp_server_run


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--ftp', dest='ftp', action='store_true', default="--ftp")

    def handle(self, *args, **options):
        print('run ftp server ......')
        if options['ftp']:
            ftp_server_run()
