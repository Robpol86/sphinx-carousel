"""Tests."""
from io import StringIO
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="no-image-warn")
def test(carousels: List[element.Tag], warning: StringIO):
    """Test."""
    assert not carousels
    warnings = warning.getvalue().strip()
    assert "index.rst:3: WARNING: No images specified in carousel." in warnings
