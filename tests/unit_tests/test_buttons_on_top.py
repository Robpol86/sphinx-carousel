"""Tests."""
from typing import List

import pytest
from bs4 import element

ROOTS = ("buttons-on-top/default", "buttons-on-top/sphinx-conf")


@pytest.mark.parametrize("testroot", [pytest.param(r, marks=pytest.mark.sphinx("html", testroot=r)) for r in ROOTS])
def test(carousels: List[element.Tag], testroot: str):
    """Test."""
    indicators = carousels[0].find_all("div", ["scbs-carousel-indicators"])[0]
    control_prev = carousels[0].find_all("button", ["scbs-carousel-control-prev"])[0]
    control_next = carousels[0].find_all("button", ["scbs-carousel-control-next"])[0]
    assert indicators["class"] == ["scbs-carousel-indicators", "scbs-my-4", "scc-top-i"]
    assert control_prev["class"] == ["scbs-carousel-control-prev", "scbs-my-4", "scc-top-c"]
    assert control_next["class"] == ["scbs-carousel-control-next", "scbs-my-4", "scc-top-c"]

    indicators = carousels[1].find_all("div", ["scbs-carousel-indicators"])[0]
    control_prev = carousels[1].find_all("button", ["scbs-carousel-control-prev"])[0]
    control_next = carousels[1].find_all("button", ["scbs-carousel-control-next"])[0]
    assert indicators["class"] == ["scbs-carousel-indicators"]
    assert control_prev["class"] == ["scbs-carousel-control-prev"]
    assert control_next["class"] == ["scbs-carousel-control-next"]

    indicators = carousels[2].find_all("div", ["scbs-carousel-indicators"])[0]
    control_prev = carousels[2].find_all("button", ["scbs-carousel-control-prev"])[0]
    control_next = carousels[2].find_all("button", ["scbs-carousel-control-next"])[0]
    if testroot.endswith("conf"):
        assert indicators["class"] == ["scbs-carousel-indicators", "scbs-my-4", "scc-top-i"]
        assert control_prev["class"] == ["scbs-carousel-control-prev", "scbs-my-4", "scc-top-c"]
        assert control_next["class"] == ["scbs-carousel-control-next", "scbs-my-4", "scc-top-c"]
    else:
        assert indicators["class"] == ["scbs-carousel-indicators"]
        assert control_prev["class"] == ["scbs-carousel-control-prev"]
        assert control_next["class"] == ["scbs-carousel-control-next"]

    indicators = carousels[3].find_all("div", ["scbs-carousel-indicators"])
    control_prev = carousels[3].find_all("button", ["scbs-carousel-control-prev"])
    control_next = carousels[3].find_all("button", ["scbs-carousel-control-next"])
    assert not indicators
    assert not control_prev
    assert not control_next
