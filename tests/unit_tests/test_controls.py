"""Tests."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("html", testroot="controls")
def test(index_html: BeautifulSoup):
    """Test."""
    carousel_with_controls = list(index_html.find_all("div", ["carousel", "slide"])[0])
    assert carousel_with_controls[0]["class"] == ["carousel-inner"]
    assert carousel_with_controls[1]["class"] == ["carousel-control-prev"]
    assert carousel_with_controls[2]["class"] == ["carousel-control-next"]

    carousel_sans_controls = list(index_html.find_all("div", ["carousel", "slide"])[1])
    assert carousel_sans_controls[0]["class"] == ["carousel-inner"]
    assert len(carousel_sans_controls) == 1
