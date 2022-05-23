"""Tests."""
# pylint: disable=too-many-statements
import pytest
from bs4 import element


@pytest.mark.sphinx("html", testroot="figure-carousel")
def test(carousel: element.Tag):
    """Test."""
    carousel_inner = carousel.find_all("div", ["scbs-carousel-inner"])[0]
    carousel_items = carousel_inner.find_all("div", ["scbs-carousel-item"])
    carousel_items.pop(0)  # Remove first .. image:: with scbs-active.

    item_b0 = carousel_items.pop(0)
    item_b1 = carousel_items.pop(0)
    item_b2 = carousel_items.pop(0)
    assert item_b0 == item_b1
    assert item_b0 == item_b2
    assert "https://i.imgur.com/b.jpg" in str(item_b0)

    item_c0 = carousel_items.pop(0)
    item_c1 = carousel_items.pop(0)
    assert item_c0 == item_c1
    assert "https://i.imgur.com/c.jpg" in str(item_c0)

    assert not carousel_items
