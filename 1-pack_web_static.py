#!/usr/bin/python3
"""Fabric script"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Create tarball """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = ("versions/web_static_{}.tgz").format(date)
    local("sudo tar -cvzf {} web_static".format(file))
    return file
