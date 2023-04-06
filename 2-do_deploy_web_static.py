#!/usr/bin/python3
"""decompress webstatic package"""
from fabric.api import *
import os


env.hosts = ['54.152.54.253', '100.25.48.219']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/p_key'

def do_deploy(archive_path):
    """
    make sure he archive path exists
    """
    try:
        if not os.path.exists(archive_path):
            return False
        #upload the archive to the /tmp directory
        put(archive_path, '/tmp/')
        #get the archive name without the extension
        arch_name = archive_path[-18:-4]
        #uncompress the archive to the folder specified
        run("sudo mkdir -p /data/web_static/releases/{}".format(arch_name))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/\
releases/{}/".format(arch_name, arch_name))
        #Delete the archive from the web server
        run("sudo rm -rf /tmp/{}.tgz".format(arch_name))
        #delete the symbolic link /data/web_static/current
        run("sudo rm -rf /data/web_static/current")
        #Create a new the symbolic link
        run("sudo ln -s /data/web_static/releases/{}/\
 /data/web_static/current".format(arch_name))
    except:
        return False
    #return true on success
    return True
