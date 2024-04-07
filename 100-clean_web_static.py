#!/usr/bin/python3
"""Module contain function that deletes out-of-date archives"""
import os
from fabric.api import *


env.hosts = ['54.158.176.162', '100.25.199.183']

def do_clean(number=0):
    """deletes out-of-date archives"""
    archives_to_keep = max(number, 1)

    with lcd("versions") as local_context:
        archive_list = sorted(os.listdir("."))
        archives_for_removal = archive_list[:-archives_to_keep]
        for archive in archives_for_removal:
            local("rm ./{}".format(archive))

    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        matching_archives = [archive for archive in remote_archives if "web_static_" in archive]
        archives_for_removal = matching_archives[:-archives_to_keep]
        for archive in archives_for_removal:
            run("rm -rf ./{}".format(archive))
