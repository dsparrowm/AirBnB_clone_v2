#!/usr/bin/python3
"""bric script that generates a .tgz archive from the
   contents of the web_static folder
"""
from datetime import datetime
from fabric.api import *
import os.path


env.hosts = ['54.152.54.253', '100.25.48.219']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to my servers.
       Args:
        archive_path: Path to an achrived file.
    """
    #  check if archive exist
    if os.path.isfile(archive_path):
        try:
            #  Upload the archive to remote /tmp/
            put("{}".format(archive_path), "/tmp/")
            release = '/data/web_static/releases/'
            current = "/data/web_static/current"
            arch = archive_path.split('/')[1].split('.')[0]
            #  Uncompressed archive
            run("mkdir -p {}{}/".format(release, arch))
            run("tar -xzf /tmp/{} -C {}{}/"
                .format(archive_path.split('/')[1], release,arch))
            #  Delete the archive
            run("rm /tmp/{}".format(archive_path.split('/')[1]))
            # Move Uncompressed files 
            run("mv {}{}/web_static/* {}{}"
                .format(release, arch, release, arch))
            run("rm -rf {}{}/web_static/".format(release, arch))
            #  Delete current link
            run("rm -rf {}".format(current))
            #  Create a new the link
            run("ln -sf {}{} {}".format(release, arch, current))
            return True
        except Exception as e:
            return False
    else:
        return False

