# -*- coding: utf-8 -*-
""" Configuration handling.

    References:
        - http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
        - http://freedesktop.org/wiki/Software/pyxdg/
        - https://github.com/ActiveState/appdirs
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
from __future__ import absolute_import, with_statement

import sys
import logging
import ConfigParser


class Configuration(object):
    """ Reads and manages the configuation.
    """

    # Singleton instance
    instance = None


    @classmethod
    def create(cls, config_file=None):
        """ Return the default configuration.
        """
        if cls.instance is None:
            cls.instance = cls(config_file)

            # Load config file, possibly overwriting the defaults
            cls.instance.load_ini()

        if config_file and config_file != cls.instance.config_file:
            raise RuntimeError("Configuration initialized a second time with a different file!")

        return cls.instance


    def __init__(self, config_file=None):
        """ Initialize configuration.
        """
        self.config_file = config_file

        # Set defaults
        #self.default("apt", "repositories", "primary", list)
        #self.default("apt", "repositories", "secondary", list)
        self._validate()


    def _validate(self):
        """ Validate a loaded configuration.
        """
        #if isinstance(self.foobar, basestring):
        #    try:
        #        self.foobar = int(self.foobar, 10)
        #    except (ValueError, TypeError), exc:
        #        raise ValueError("Bad foobar %r: %s" % (self.foobar, exc))


    def load_ini(self):
        """ Load the given .INI file.
        """
        if not self.config_file:
            return

        # Load INI file
        ini_file = ConfigParser.SafeConfigParser()
        if not ini_file.read(self.config_file):
            raise ConfigParser.ParsingError("Global configuration file %r not found!" % (
                self.config_file,
            ))

        """
        # Make sure there's our global settings section
        if not ini_file.has_section(self.SECTION):
            raise ConfigParser.ParsingError("%r needs to have a [%s] section!" % (
                self.config_file, self.SECTION,
            ))

        # Get the given values
        for key, val in ini_file.items(self.SECTION):
            # Ensure that all names are known (to prevent uncaught typos)
            if key not in self.KEYS:
                raise ConfigParser.ParsingError("%r has an unknown key %s in the [%s] section!" % (
                    self.config_file, key, self.SECTION,
                ))

            # Do some shell-like path expansion
            val = os.path.expanduser(os.path.expandvars(val))

            # Set as attribute for easy access
            setattr(self, key, val)
        """

        self._validate()
