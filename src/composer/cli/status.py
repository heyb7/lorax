#
# Copyright (C) 2018  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import logging
log = logging.getLogger("composer-cli")

import json

from composer import http_client as client
from composer.cli.help import status_help

def status_cmd(opts):
    """Process status commands

    :param opts: Cmdline arguments
    :type opts: argparse.Namespace
    :returns: Value to return from sys.exit()
    :rtype: int
    """
    if opts.args[1] == "help" or opts.args[1] == "--help":
        print(status_help)
        return 0
    elif opts.args[1] != "show":
        log.error("Unknown status command: %s", opts.args[1])
        return 1

    result = client.get_url_json(opts.socket, "/api/status")
    if opts.json:
        print(json.dumps(result, indent=4))
        return 0

    return 0