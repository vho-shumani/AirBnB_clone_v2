#!/usr/bin/python3
"""Module contain function that creates
and distributes an archive to web servers"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ['54.158.176.162', '100.25.199.183']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p versions')
    result = local(f'sudo tar -czvf versions/web_static_{time}.tgz web_static')
    if result.succeeded:
        return f"versions/web_static_{time}.tgz"
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to web servers"""
    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        archive = os.path.basename(archive_path)
        folder = f'/data/web_static/releases/{archive.split(".")[0]}'
        run(f"mkdir -p {folder}/")
        run(f"tar -xzf /tmp/{archive} -C {folder}/")
        run(f"rm /tmp/{archive}")
        run(f"mv {folder}/web_static/* {folder}/")
        run(f"rm -rf {folder}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {folder}/ /data/web_static/current")
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    return False
