#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""
from fabric.operations import local
from datetime import datetime
def do_pack():
    time = datetime.now()
    str_time = strftime(%Y%m%d%H%M%S)
    local('mkdir -p versions')
    result = local(f'tar -czvf versions/web_static_{str_time}.tgz web_static')
    if result.succeeded:
        return f"versions/web_static_{str_time}.tgz"
    else:
        return None
