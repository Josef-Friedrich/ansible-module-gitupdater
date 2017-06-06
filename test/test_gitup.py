from __future__ import (absolute_import, division)
from ansible.compat.tests import unittest
# import unittest
import mock
import gitupdater

from gitup import config as gitup_config

default_config_path = gitup_config.get_default_config_path()

class TestFunction(unittest.TestCase):

    @mock.patch("gitupdater.AnsibleModule")
    def test_mock(self, AnsibleModule):
        module = AnsibleModule.return_value
        module.params = {
            'path': '/tmp',
            'state': 'present',
        }
        module.check_mode = False
        gitupdater.main()

        expected = dict(
            path=dict(required=True, aliases=['src']),
            state=dict(default='present', choices=['present', 'absent']),
        )

        assert(mock.call(argument_spec=expected,
               supports_check_mode=True) == AnsibleModule.call_args)

        self.assertTrue('/tmp' in open(default_config_path).read())
