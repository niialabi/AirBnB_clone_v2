#!/usr/bin/python3
from fabric.api import run, local
"""fabfile that compresses web_static dir"""


def do_pack():
    """fab file that compreses dir"""
    current_datetime = local('date +"%Y%m%d%H%M%S"', capture=True)
    file_name = f"web_static_{current_datetime}.tgz"
    local("mkdir -p versions")
    store_path = "./versions"

    if local(f"tar -czvf {store_path}/{file_name} web_static"):
        return ("versions/{}".format(file_name))
    return None
