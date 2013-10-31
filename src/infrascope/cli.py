# -*- coding: utf-8 -*-
""" Command Line Interface.
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

from cliff.app import App
from cliff.commandmanager import CommandManager

from infrascope import pkg_info


class InfrascopeCLI(App):
    """ The main `infrascope` command line application.
    """

    log = logging.getLogger(__name__)

    def __init__(self):
        """Set up main command."""
        project = pkg_info()
        super(InfrascopeCLI, self).__init__(
            description=project["description"],
            version='0.1', # TODO: need to get version at runtime
            command_manager=CommandManager('infrascope.cli'),
        )

    def initialize_app(self, argv):
        """Called after main argument parsing, but before command processing."""
        self.log.debug('initialize_app: %r', argv)

    def prepare_to_run_command(self, cmd):
        """Called after command identification, and before executing it."""
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        """Called after command execution; `err` is an unhandled exception, or `None`."""
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('got an error: %s', err)


def run(argv=None):
    """Main CLI entry point."""
    cli = InfrascopeCLI()
    sys.exit(cli.run(argv if argv is None else sys.argv[1:]))


if __name__ == "__main__":
    # When started via "python -m"
    run()
