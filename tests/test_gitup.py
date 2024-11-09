import os
import tempfile
from typing import cast
from unittest import mock

from gitup import config as gitup_config

import gitupdater
from gitupdater import ModuleParams

default_config_path = gitup_config.get_default_config_path()
tmp_dir = tempfile.mkdtemp()
tmp_dir2 = tempfile.mkdtemp()


class TestFunction:
    @mock.patch("gitupdater.AnsibleModule")
    def test_mock(self, AnsibleModule: mock.MagicMock):
        module = AnsibleModule.return_value
        module.params = cast(
            ModuleParams,
            {
                "path": tmp_dir,
                "state": "present",
                "cleanup": False,
            },
        )
        module.check_mode = False
        gitupdater.main()

        expected = dict(
            path=dict(default=False),
            state=dict(default="present", choices=["present", "absent"]),
            cleanup=dict(default=False, type="bool"),
        )

        assert (
            mock.call(argument_spec=expected, supports_check_mode=True)
            == AnsibleModule.call_args
        )

        assert tmp_dir in open(default_config_path).read()

        # Delete
        module.params["state"] = "absent"
        gitupdater.main()
        assert tmp_dir not in open(default_config_path).read()

        # Add
        module.params["state"] = "present"
        module.params["path"] = tmp_dir2
        gitupdater.main()
        assert tmp_dir2 in open(default_config_path).read()

        # cleanup
        os.rmdir(tmp_dir2)
        module.params["path"] = False
        module.params["cleanup"] = True
        gitupdater.main()
        assert tmp_dir2 not in open(default_config_path).read()
