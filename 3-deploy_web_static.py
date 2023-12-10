#!/usr/bin/python3
from fabric.decorators import task
from fabric.api import *
import os

"""fabfile that compresses web_static dir"""


env.hosts = ['54.197.82.133', '54.87.180.34']
env.user = 'ubuntu'


@task
def deploy():
    """auto live deploy to all servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)



@task
def do_deploy(archive_path):
    """fbfile distributes an archive to your web servers:"""
    try:
        if not os.path.exists(archive_path):
            return False
        arc_name = (archive_path.split("/"))[-1]
        file_name = (arc_name.split("."))[0]
        dest_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/{}".format(arc_name))
        run("mkdir -p {}/{}".format(dest_path, file_name))
        run("tar -xzf /tmp/{} -C {}/{}".format(arc_name, dest_path, file_name))
        run("rm /tmp/{}".format(arc_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(dest_path, file_name))
        run("rm -rf {}{}/web_static".format(dest_path, file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dest_path, file_name))
        return True
    except Exception:
        return False


@runs_once
def do_pack():
    """fab file that compreses dir"""
    current_datetime = local('date +"%Y%m%d%H%M%S"', capture=True)
    file_name = f"web_static_{current_datetime}.tgz"
    local("mkdir -p versions")
    store_path = "./versions"

    if local(f"tar -czvf {store_path}/{file_name} web_static"):
        return ("versions/{}".format(file_name))
    return None
