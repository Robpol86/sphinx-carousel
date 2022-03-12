"""A Sphinx extension for creating slideshows using Bootstrap Carousels.

https://sphinx-carousel.readthedocs.io
https://github.com/Robpol86/sphinx-carousel
https://pypi.org/project/sphinx-carousel
"""
from typing import Dict, List

from docutils.nodes import Element, image as docutils_image
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx

from sphinx_carousel import __version__
from sphinx_carousel.nodes import CarouselInnerNode, CarouselItemNode, CarouselSlideNode


class Carousel(Directive):
    """Main directive."""

    has_content = True

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
        main_div = CarouselSlideNode("", inner_div)
        return [main_div]


def setup(app: Sphinx) -> Dict[str, str]:
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    """
    app.add_directive("carousel", Carousel)
    app.add_node(CarouselInnerNode, html=(CarouselInnerNode.html_visit, CarouselInnerNode.html_depart))
    app.add_node(CarouselItemNode, html=(CarouselItemNode.html_visit, CarouselItemNode.html_depart))
    app.add_node(CarouselSlideNode, html=(CarouselSlideNode.html_visit, CarouselSlideNode.html_depart))
    return dict(version=__version__)
