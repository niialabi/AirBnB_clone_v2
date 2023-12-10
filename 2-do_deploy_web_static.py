#!/usr/bin/python3
from fabric.api import *
import os

"""fabfile that compresses web_static dir"""


env.hosts = ['54.197.82.133', '54.87.180.34']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """fbfile distributes an archive to your web servers, using the function do_deploy:"""
    if not os.path.exists(archive_path):
        return False
    arc_name = (archive_path.split("/"))[-1]
    file_name = (arc_name.split("."))[0]
    dest_path = "/data/web_static/releases/"
    put(archive_path, "/tmp/{}".format(arc_name))
    run("mkdir -p {}/{}".format(dest_path, file_name))
    run("tar -xzf /tmp/{} -C {}/{}".format(arc_name, dest_path, file_name))
    run("rm /tmp/{}".format(arc_name))
    run("rm -rf /data/web_static/current || true")
    run("ln -s {}{}/ /data/web_static/current".format(dest_path, file_name))
   

def do_pack():
    """fab file that compreses dir"""
    current_datetime = local('date +"%Y%m%d%H%M%S"', capture=True)
    file_name = f"web_static_{current_datetime}.tgz"
    local("mkdir -p versions")
    store_path = "./versions"

    if local(f"tar -czvf {store_path}/{file_name} web_static"):
        return file_name
    return None
