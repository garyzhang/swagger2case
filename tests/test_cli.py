import pytest
import sys
import io
from swagger2case.cli import main
from swagger2case.__about__ import __version__
from pytest import raises


class TestCli(object):

    def test_show_version(self):
        capture_ouput = io.StringIO()
        sys.stdout = capture_ouput
        sys.argv = ["swagger2case", "-V"]
        with raises(SystemExit):
            main()
        assert __version__ == capture_ouput.getvalue().strip()

    


