from glob import glob
import os

import pkg_resources
import setuptools_scm

__version__ = setuptools_scm.get_version(root='..', relative_to=__file__)

config = {
    "defaults": {
        "VERSION": __version__,
        "XBLOCK_VERSION": "3.2.1",
        "XBLOCK_DOCKER_IMAGE": "hastexo/hastexo-xblock:{{ HASTEXO_XBLOCK_VERSION }}",
        "GUACD_DOCKER_IMAGE": "guacamole/guacd:0.9.13-incubating",
        "XBLOCK_SETTINGS": {},
        "XBLOCK_HOST": "hastexo-xblock.{{ LMS_HOST }}",
        "BROKER_READ_TIMEOUT": 10,
        "BROKER_WRITE_TIMEOUT": 10,
    },
}

templates = pkg_resources.resource_filename("tutorhastexo", "templates")
hooks = {
    "build-image": {"hastexo": "{{ HASTEXO_XBLOCK_DOCKER_IMAGE }}"},
    "remote-image": {"hastexo": "{{ HASTEXO_XBLOCK_DOCKER_IMAGE }}"},
}


def patches():
    all_patches = {}
    filename = pkg_resources.resource_filename("tutorhastexo", "patches")
    for path in glob(os.path.join(filename, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
