# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------
This source file is part of OSTIS (Open Semantic Technology for Intelligent Systems)
For the latest info, see http://www.ostis.net

Copyright (c) 2011 OSTIS

OSTIS is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OSTIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OSTIS.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------------
"""
import sys
import py2exe

from distutils.core import setup
from scnl_2_scs import *
from lxml import etree 

sys.path.append('.')

py2exe_options = dict(
    includes = [u'code_generator',u'grammar',u'utils']
)

setup(
    version = u'0.1.0',
    # targets to build
    description = u'scnl_2_scs',
    name = u'scnl_2_scs.exe',
    # targets to build
    console = ['scnl_2_scs.py'],
	options = dict(py2exe = py2exe_options)
)

