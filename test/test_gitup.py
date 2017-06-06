from __future__ import (absolute_import, division)
from ansible.compat.tests import unittest
# import unittest
import mock
import gitupdater

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
