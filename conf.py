#!/usr/bin/env python3
"""
Template conf.py to copy into your Sphinx project.
It then loads the generic config and you can tweak whichever parameter you want after the import.
"""
import os
import sys
import builtins

import sphinx_rtd_theme

sys.path.append(os.path.abspath('.'))

## These must be defined before the import:
project    = 'I rant therefore I am'
author     = 'XonqNopp'
master_doc = 'index'
builtins.project    = project
builtins.author     = author
builtins.master_doc = master_doc

#builtins.gitRootPath = os.path.abspath('.')  # not working since we need to commit output files

## Import generic config:
from root_conf import *

## These override an option in the rootConf:
html_theme = 'sphinx_rtd_theme'

#extensions.append('sphinx.ext.inheritance_diagram')

