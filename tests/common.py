import sys

import pytest

literal_support = pytest.mark.skipif(sys.version_info < (3, 7), reason="requires Python 3.7")
init_var_type_support = pytest.mark.skipif(sys.version_info < (3, 8), reason="requires Python 3.8")
