"""Tests."""
import pytest
from bs4 import BeautifulSoup


@pytest.mark.sphinx("html", testroot="static-on")
def test_on(index_html: BeautifulSoup):
    """Test."""
    link_tags = index_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags]
    assert "_static/bootstrap.min.css" in hrefs

    script_tags = index_html.find_all("script")
    sources = [t.get("src") for t in script_tags]
    assert "_static/bootstrap.min.js" in sources


@pytest.mark.sphinx("html", testroot="static-off")
def test_off(index_html: BeautifulSoup):
    """Test."""
    link_tags = index_html.find_all("link")
    hrefs = [t.get("href") for t in link_tags]
    assert "_static/bootstrap.min.css" not in hrefs

    script_tags = index_html.find_all("script")
    sources = [t.get("src") for t in script_tags]
    assert "_static/bootstrap.min.js" not in sources
