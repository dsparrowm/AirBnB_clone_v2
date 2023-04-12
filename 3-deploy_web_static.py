#!/usr/bin/python3
"""Fabric script that generates an archive
   from web_static folder
"""
from datetime import datetime
from fabric.api import *
import os.path


env.hosts = ['54.152.54.253', '100.25.48.219']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Transfers an archive to my web servers.
       Args:
        archive_path: Path to an achrived file.
    """
    #  check for existence of archive
    if os.path.isfile(archive_path):
        try:
            #  transfer the archive to remote /tmp/
            put("{}".format(archive_path), "/tmp/")
            release = '/data/web_static/releases/'
            cur = "/data/web_static/current"
            arch = archive_path.split('/')[1].split('.')[0]
            #  Uncompress the archive to the release folder
            run("mkdir -p {}{}/".format(release, arch))
            run("tar -xzf /tmp/{} -C {}{}/".format(archive_path.split('/')[1],
                                                   release,
                                                   arch))
            #  Delete the archive
            run("rm /tmp/{}".format(archive_path.split('/')[1]))
            # Move Uncompressed files to release dir
            run("mv {}{}/web_static/* {}{}".format(release, arch,
                                                   release, arch))
            run("rm -rf {}{}/web_static/".format(release, arch))
            #  Delete current link.
            run("rm -rf {}".format(cur))
            #  Create a new link
            run("ln -sf {}{} {}".format(release, arch, cur))
            return True
        except Exception as e:
            return False
    else:
        return False

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

def deploy():
    """
     Creates and transfers an archive to my servers
    """
    path_to_archive = do_pack()
    if path_to_archive is None:
        return False
    return do_deploy(path_to_archive)
