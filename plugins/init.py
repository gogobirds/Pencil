#!/usr/bin/env python
# coding : utf-8 
# author : 'Zend'
# team   : "gogobirds"

import sys, os
from imp import find_module, load_module, acquire_lock, release_lock

pluginmap = {}
default_directory = os.path.join(os.path.dirname(__file__), "test")
config = {}
directories = config.get("directories", (default_directory,))


def load_plugins():
    plugins = []
    for dir in directories:
        try:
            for f in os.listdir(dir):
                if f.endswith(".py") and f != "__init__.py":
                    plugins.append((f[:-3], dir))
        except OSError:
            print "Failed to access: %s" % dir
            continue

    fh = None
    mod = None
    for (name, dir) in plugins:
        try:
            acquire_lock()
            fh, filename, desc = find_module(name, [dir])
            old = sys.modules.get(name)
            if old is not None:
                # make sure we get a fresh copy of anything we are trying
                # to load from a new path
                del sys.modules[name]
            mod = load_module(name, fh, filename, desc)
        finally:
            if fh:
                fh.close()
            release_lock()


def register_plugin(name):
    def _inner(func):
        pluginmap[name] = func
        return func
    return _inner
