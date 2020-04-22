import pytest
import sys
import io
from swagger2case.cli import main


class Test_Cli(object):

    @classmethod
    def setup_class(cls):
        cls.capture_ouput = io.StringIO()
        sys.stdout = cls.capture_ouput

    def test_show_version(self):
        sys.argv = ["swagger2case", "-V"]

        from swagger2case.__about__ import __version__
        assert __version__ == self.capture_ouput


