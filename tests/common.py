import sys

import pytest

literal_support = pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python 3.7")
