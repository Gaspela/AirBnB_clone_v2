#!/usr/bin/python3
"""Fabric script"""
from fabric.api import *
from os.path import isfile

env.hosts = ["34.73.95.63", "54.242.72.84"]
env.user = "ubuntu"



def do_deploy(archive_path):
    """Deploy file"""

    if not isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(filename)
        run("mkdir {}".format(path))
        run("tar -zxvf /tmp/{}.tgz -C {}/".format(filename, path))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo rm /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(filename))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static/".format(filename))
        return True
    except:
        return False
