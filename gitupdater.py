#!/usr/bin/python

# (c) 2017, Josef Friedrich <josef@friedrich.rocks>
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {
    "metadata_version": "1.0",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: gitupdater
short_description: Ansible module for the git-repo-updater (gitup)
description:
    - gitup U(https://github.com/earwig/git-repo-updater) is a console
      script that allows you to easily update multiple git repositories
      at once.

version_added: "1.0"
author: "Josef Friedrich (@Josef-Friedrich)"
options:
    cleanup:
        description:
            - Clean up the repositories that have been deleted.
        required: false
        default: false
    path:
        description:
            - Full path to the git repository.
        required: false
        default: false
    state:
        description:
            - State of the gitup configuration for this repository. The
              git repository itself is not affected.
        required: false
        default: present
        choices:
            - present
            - absent
requirements:
    - git-repo-updater
"""

EXAMPLES = """
# Bookmark a repository, state can be omitted
- gitupdater:
    path: /var/repos/project

# Bookmark a repository
- gitupdater:
    path: /var/repos/project
    state: present

# Delete bookmark
- gitupdater:
    path: /var/repos/project
    state: absent

# Delete non-existent repositories
- gitupdater:
    cleanup: yes
"""

RETURN = """
path:
    description: Full path to the git repository
    returned: always
    type: string
    sample: /path/to/repository
state:
    description: State of the gitup configuration for this repository
    returned: always
    type: string
    sample: present

"""

import sys
from io import StringIO

from ansible.module_utils.basic import AnsibleModule
from gitup import config as gitup_conf


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


def main():
    module = AnsibleModule(
        argument_spec=dict(
            cleanup=dict(default=False, type="bool"),
            path=dict(default=False),
            state=dict(default="present", choices=["present", "absent"]),
        ),
        supports_check_mode=True,
    )

    p = module.params
    changed = False
    if p["cleanup"]:
        gitup_conf.clean_bookmarks()

    if p["state"] == "present" and p["path"]:
        with Capturing() as output:
            gitup_conf.add_bookmarks([p["path"]])

        if "Added" in output[0]:
            changed = True

    if p["state"] == "absent" and p["path"]:
        with Capturing() as output:
            gitup_conf.delete_bookmarks([p["path"]])

        if "Deleted" in output[0]:
            changed = True

    module.exit_json(changed=changed, path=str(p["path"]), state=str(p["state"]))


if __name__ == "__main__":
    main()
