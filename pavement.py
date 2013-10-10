# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import, unused-wildcard-import, invalid-name, unused-import
""" Tools for Infrastructure Transparency.

    This is the main build script for Paver.
"""
# Copyright © 2013 1&1 Internet AG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import re
import sys

from paver.easy import *
from paver.setuputils import setup
from setuptools import find_packages


#
# Project Description
#
projectdir = path(__file__).dirname().abspath()
try:
    import infrascope
except ImportError:
    # Special bootstrap in our own project, in absence of an initialized virtualenv
    sys.path.insert(0, projectdir / "src")
    import infrascope
from cobblestones import tools

changelog = (projectdir / "debian" / "changelog").text("UTF-8")
project = tools.bunchify(infrascope.pkg_info())
project.update(
    # TODO: find ways to get at these during runtime, within "infrascope.pkg_info"
    version = re.search(r"(?<=\()[^)]+(?=\))", changelog).group(), # DRY principle
    packages = find_packages(projectdir / "src", exclude=["tests"]),
)


#
# Tasks
#

@task
@needs(["paver.misctasks.generate_setup", "setuptools.command.develop"])
def init():
    """initial project setup"""


#
# Continuous Integration
#

@task
@needs(["build", "doc"])
def travis_ci():
    """continuous integration tasks for Travis"""


#
# Register with Paver
#
setup(**project)
