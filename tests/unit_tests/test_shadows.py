"""Tests."""
from typing import List

import pytest
from bs4 import element

ROOTS = ("shadows/default", "shadows/sphinx-conf")


@pytest.mark.parametrize("testroot", [pytest.param(r, marks=pytest.mark.sphinx("html", testroot=r)) for r in ROOTS])
def test(carousels: List[element.Tag], testroot: str):
    """Test."""
    indicator = carousels[0].find_all("div", ["scbs-carousel-indicators"])[0].find_all("button")[0]
    control_prev = carousels[0].find_all("button", ["scbs-carousel-control-prev"])[0]
    control_next = carousels[0].find_all("button", ["scbs-carousel-control-next"])[0]
    assert indicator["class"] == ["scbs-active", "scc-shadow-indicator"]
    assert control_prev["class"] == ["scbs-carousel-control-prev", "scc-shadow-control"]
    assert control_next["class"] == ["scbs-carousel-control-next", "scc-shadow-control"]

    indicator = carousels[1].find_all("div", ["scbs-carousel-indicators"])[0].find_all("button")[1]
    control_prev = carousels[1].find_all("button", ["scbs-carousel-control-prev"])[0]
    control_next = carousels[1].find_all("button", ["scbs-carousel-control-next"])[0]
    assert "class" not in indicator
    assert control_prev["class"] == ["scbs-carousel-control-prev"]
    assert control_next["class"] == ["scbs-carousel-control-next"]

    indicator = carousels[2].find_all("div", ["scbs-carousel-indicators"])[0].find_all("button")[2]
    control_prev = carousels[2].find_all("button", ["scbs-carousel-control-prev"])[0]
    control_next = carousels[2].find_all("button", ["scbs-carousel-control-next"])[0]
    if testroot.endswith("conf"):
        assert indicator["class"] == ["scc-shadow-indicator"]
        assert control_prev["class"] == ["scbs-carousel-control-prev", "scc-shadow-control"]
        assert control_next["class"] == ["scbs-carousel-control-next", "scc-shadow-control"]
    else:
        assert "class" not in indicator
        assert control_prev["class"] == ["scbs-carousel-control-prev"]
        assert control_next["class"] == ["scbs-carousel-control-next"]

    indicators = carousels[3].find_all("div", ["scbs-carousel-indicators"])
    control_prev = carousels[3].find_all("button", ["scbs-carousel-control-prev"])
    control_next = carousels[3].find_all("button", ["scbs-carousel-control-next"])
    assert not indicators
    assert not control_prev
    assert not control_next
