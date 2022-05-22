"""Tests."""
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp

ROOTS = ("static/off", "static/on")


@pytest.mark.parametrize("testroot", [pytest.param(r, marks=pytest.mark.sphinx("html", testroot=r)) for r in ROOTS])
def test_copied(sphinx_app: SphinxTestApp, testroot: str):
    """Test."""
    path_custom_css = Path(sphinx_app.outdir) / "_static" / "carousel-custom.css"
    assert path_custom_css.is_file()

    path_bs_css = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.min.css"
    path_bs_js = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.min.js"
    if testroot.endswith("on"):
        assert path_bs_css.is_file()
        assert path_bs_js.is_file()
    else:
        assert not path_bs_css.is_file()
        assert not path_bs_js.is_file()


@pytest.mark.parametrize("_", [pytest.param(r, marks=pytest.mark.sphinx("latex", testroot=r)) for r in ROOTS])
def test_copied_latex(sphinx_app: SphinxTestApp, _):
    """Test."""
    path_custom_css = Path(sphinx_app.outdir) / "_static" / "carousel-custom.css"
    assert not path_custom_css.is_file()

    path_bs_css = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.min.css"
    path_bs_js = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.min.js"
    assert not path_bs_css.is_file()
    assert not path_bs_js.is_file()


@pytest.mark.parametrize("testroot", [pytest.param(r, marks=pytest.mark.sphinx("html", testroot=r)) for r in ROOTS])
def test_index(index_html: BeautifulSoup, testroot: str):
    """Test."""
    link_tags = index_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags if "stylesheet" in t.get("rel")]
    script_tags = index_html.find_all("script")
    sources = [t.get("src") for t in script_tags]

    assert "_static/carousel-custom.css" in hrefs
    if testroot.endswith("on"):
        assert "_static/bootstrap-carousel.min.css" in hrefs
        assert "_static/bootstrap-carousel.min.js" in sources
    else:
        assert "_static/bootstrap-carousel.min.css" not in hrefs
        assert "_static/bootstrap-carousel.min.js" not in sources


@pytest.mark.parametrize("_", [pytest.param(r, marks=pytest.mark.sphinx("html", testroot=r)) for r in ROOTS])
def test_unused(unused_html: BeautifulSoup, _):
    """Test."""
    link_tags = unused_html.find_all("link")
    hrefs = "\n".join(t.get("href", "") for t in link_tags if "stylesheet" in t.get("rel"))
    assert "basic.css" in hrefs
    assert "carousel" not in hrefs

    script_tags = unused_html.find_all("script")
    sources = "\n".join(t.get("src", "") for t in script_tags)
    assert "jquery.js" in sources
    assert "carousel" not in sources
