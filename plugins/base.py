#!/usr/bin/env python
# coding : utf-8 
# author : 'Zend'
# team   : "gogobirds"

import sys
import os
from imp import find_module, load_module, acquire_lock, release_lock

pluginmap = {}
plugin_dirs = []
pwd = os.path.dirname(__file__)


def register_plugin(name):
    def inner(func):
        pluginmap[name] = func
        return func
    return inner


def load_plugins():
    for dirs in get_dir_list(pwd):
        full_path_dir = os.path.join(pwd, dirs)
        plugin_dirs.append(full_path_dir)
    plugins = []
    for plugin_dir in plugin_dirs:
        try:
            for f in os.listdir(plugin_dir):
                if f.endswith(".py") and f != "__init__.py":
                    plugins.append((f[:-3], plugin_dir))
        except OSError:
            print "Failed to access: %s" % plugin_dir
            continue

    fh = None
    for (name, dirs) in plugins:
        try:
            acquire_lock()
            fh, filename, desc = find_module(name, [dirs])
            old = sys.modules.get(name)
            if old is not None:
                del sys.modules[name]
            load_module(name, fh, filename, desc)
        finally:
            if fh:
                fh.close()
            release_lock()


def get_dir_list(p):
    p = str(p).replace("/", "\\")
    p += "\\" if p[-1] != "\\" else p
    return [x for x in os.listdir(p) if os.path.isdir(p + x)]

