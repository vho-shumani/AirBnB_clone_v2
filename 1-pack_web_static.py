#!/usr/bin/python3
"""Generate .tgz archive"""
from fabric.api import local
from datetime import datetime
def do_pack():
    "generates a .tgz archive from the contents of the web_static folder"
    time = datetime.now()
    str_time = strftime(%Y%m%d%H%M%S)
    local('mkdir -p versions')
    result = local(f'tar -czvf versions/web_static_{str_time}.tgz web_static')
    if result.succeeded:
        return f"versions/web_static_{str_time}.tgz"
    else:
        return None
