#!/usr/bin/python3
"""module contains the function do_pack that generates a .tgz archive"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p versions')
    result = local(f'tar -czvf versions/web_static_{str_time}.tgz web_static')
    if result.succeeded:
        return f"versions/web_static_{str_time}.tgz"
    else:
        return None
