"""Tests."""
from typing import List

import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="data-ride")
def test(carousels: List[element.Tag]):
    """Test."""
    carousel = carousels[0]
    assert carousel.has_attr("data-ride")
    assert carousel["data-ride"] == "carousel"

    carousel = carousels[1]
    assert not carousel.has_attr("data-ride")
