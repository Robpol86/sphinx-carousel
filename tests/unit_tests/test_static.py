"""Tests."""
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="static-on")
def test_on(sphinx_app: SphinxTestApp, index_html: BeautifulSoup, unused_html: BeautifulSoup):
    """Test."""
    path_css = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.css"
    assert path_css.is_file()
    path_js = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.js"
    assert path_js.is_file()

    link_tags = index_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags]
    assert "_static/bootstrap-carousel.css" in hrefs

    script_tags = index_html.find_all("script")
    sources = [t.get("src") for t in script_tags]
    assert "_static/bootstrap-carousel.js" in sources

    link_tags = unused_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags]
    assert "_static/bootstrap-carousel.css" not in hrefs
    script_tags = unused_html.find_all("script")
    sources = [t.get("src") for t in script_tags]
    assert "_static/bootstrap-carousel.js" not in sources


@pytest.mark.sphinx("html", testroot="static-off")
def test_off(sphinx_app: SphinxTestApp, index_html: BeautifulSoup, unused_html: BeautifulSoup):
    """Test."""
    path_css = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.css"
    assert not path_css.exists()
    path_js = Path(sphinx_app.outdir) / "_static" / "bootstrap-carousel.js"
    assert not path_js.exists()

    link_tags = index_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags]
    assert "_static/bootstrap-carousel.css" not in hrefs

    script_tags = index_html.find_all("script")
    sources = [t.get("src") for t in script_tags]
    assert "_static/bootstrap-carousel.js" not in sources

    link_tags = unused_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags]
    assert "_static/bootstrap-carousel.css" not in hrefs
    script_tags = unused_html.find_all("script")
    sources = [t.get("src") for t in script_tags]
    assert "_static/bootstrap-carousel.js" not in sources
