"""pytest fixtures."""
from pathlib import Path
from typing import List

import pytest
from bs4 import BeautifulSoup, element
from sphinx.testing.path import path
from sphinx.testing.util import SphinxTestApp

pytest_plugins = "sphinx.testing.fixtures"  # pylint: disable=invalid-name


@pytest.fixture(scope="session")
def rootdir() -> path:
    """Used by sphinx.testing, return the directory containing all test docs."""
    return path(__file__).parent.abspath() / "test_docs"


@pytest.fixture(name="sphinx_app")
def _sphinx_app(app: SphinxTestApp) -> SphinxTestApp:
    """Instantiate a new Sphinx app per test function."""
    app.build()
    yield app


@pytest.fixture(name="outdir")
def _outdir(sphinx_app: SphinxTestApp) -> Path:
    """Return the Sphinx output directory with HTML files."""
    return Path(sphinx_app.outdir)


@pytest.fixture(name="index_html")
def _index_html(outdir: Path) -> BeautifulSoup:
    """Read and parse generated test index.html."""
    text = (outdir / "index.html").read_text(encoding="utf8")
    return BeautifulSoup(text, "html.parser")


@pytest.fixture(name="unused_html")
def _unused_html(outdir: Path) -> BeautifulSoup:
    """Read and parse generated test unused.html."""
    text = (outdir / "unused.html").read_text(encoding="utf8")
    return BeautifulSoup(text, "html.parser")


@pytest.fixture(name="carousels")
def _carousels(index_html: BeautifulSoup) -> List[element.Tag]:
    """Return all top-level carousels in index.html."""
    return index_html.find_all("div", ["carousel", "scbs-carousel"])  # carousel OR scbs-carousel


@pytest.fixture()
def carousel(carousels: List[element.Tag]) -> element.Tag:
    """Return first carousel in index.html."""
    return carousels[0]
