# -*- coding: utf-8 -*-

name = 'turret_server'

version = '1.1.0'

authors = ['wen.tan',
           'ben.skinner',
           'daniel.flood']

requires = ['pyzmq', 'turret_resolver']

build_requires = ['python']

build_command = 'rez env python -c "python {root}/rezbuild.py {install}"'


def commands():
    env.PATH.append('{root}/bin')
    env.TURRET_SERVER.set('{root}/bin/turret-server.bat')
    env.TURRET_SRC.set('{root}/src')
    env.PYTHONPATH.append(env.TURRET_SRC)
