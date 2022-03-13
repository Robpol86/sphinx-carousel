"""A Sphinx extension for creating slideshows using Bootstrap Carousels.

https://sphinx-carousel.readthedocs.io
https://github.com/Robpol86/sphinx-carousel
https://pypi.org/project/sphinx-carousel
"""
import shutil
from pathlib import Path
from typing import Dict, List

from docutils.nodes import Element, image as docutils_image
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx

from sphinx_carousel import __version__
from sphinx_carousel.nodes import CarouselInnerNode, CarouselItemNode, CarouselSlideNode


class Carousel(Directive):
    """Main directive."""

    has_content = True
    option_spec = {
        "no_data_ride": directives.flag,
    }
    optional_arguments = 1

    def run(self) -> List[Element]:
        """Main method."""
        directive_content = Element()
        directive_content.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, directive_content)

        items = []
        for idx, image in enumerate(directive_content.traverse(docutils_image)):
            image["classes"] += ["d-block", "w-100"]
            items.append(CarouselItemNode(idx == 0, "", image))

        inner_div = CarouselInnerNode("", *items)
        div_id = self.arguments[0] if self.arguments else ""
        data_ride = "" if "no_data_ride" in self.options else "carousel"
        main_div = CarouselSlideNode(div_id, data_ride, "", inner_div)
        return [main_div]


def add_static(app: Sphinx):
    """Conditionally add CSS and JS files.

    :param app: Sphinx application object.
    """
    if not app.config.carousel_add_bootstrap_css_js:
        return

    static_in = Path(__file__).parent / "_static"
    static_out = Path(app.outdir) / "_static_carousel"
    static_out.mkdir(exist_ok=True)
    app.config.html_static_path.append(str(static_out))

    shutil.copy(static_in / "bootstrap.min.css", static_out / "bootstrap.min.css")
    app.add_css_file("bootstrap.min.css")

    shutil.copy(static_in / "bootstrap.min.js", static_out / "bootstrap.min.js")
    app.add_js_file("bootstrap.min.js")


def setup(app: Sphinx) -> Dict[str, str]:
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    """
    app.add_config_value("carousel_add_bootstrap_css_js", True, "html")
    app.add_directive("carousel", Carousel)
    app.add_node(CarouselInnerNode, html=(CarouselInnerNode.html_visit, CarouselInnerNode.html_depart))
    app.add_node(CarouselItemNode, html=(CarouselItemNode.html_visit, CarouselItemNode.html_depart))
    app.add_node(CarouselSlideNode, html=(CarouselSlideNode.html_visit, CarouselSlideNode.html_depart))
    app.connect("builder-inited", add_static)
    return dict(version=__version__)
