#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Creates a compressed archive of the web_static contents
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static/".format(archive_path))
        return archive_path
    except Exception as e:
        return None
