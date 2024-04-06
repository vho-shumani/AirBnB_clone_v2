#!/usr/bin/python3
"""Modules contains function that distributes
an archive to your web servers."""
from fabric.api import *
import os


env.hosts = ['54.158.176.162', '100.25.199.183']


def do_deploy(archive_path):
    """ distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive = os.path.basename(archive_path)
        folder = f'/data/web_static/releases/{archive.split(".")[0]}'
        run(f"mkdir -p {folder}")
        run(f"tar -xzf /tmp/{archive} -C {folder}")
        run(f"rm /tmp/{archive}")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {folder}/ /data/web_static/current")
        return True
    except Exception as e:
        print(e)
        return False
