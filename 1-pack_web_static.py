#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime
def do_pack():
    time = datetime.now()
    str_time = strftime(%Y%m%d%H%M%S)
    print(str_time)

