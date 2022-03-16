"""A Sphinx extension for creating slideshows using Bootstrap Carousels.

https://sphinx-carousel.readthedocs.io
https://github.com/Robpol86/sphinx-carousel
https://pypi.org/project/sphinx-carousel
"""
import uuid
from pathlib import Path
from typing import Dict, List

from docutils.nodes import document, Element, image as docutils_image
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset_file

from sphinx_carousel import __version__, nodes


class Carousel(SphinxDirective):
    """Main directive."""

    has_content = True
    option_spec = {
        "no_data_ride": directives.flag,
        "no_controls": directives.flag,
        "show_controls": directives.flag,
    }

    def images(self) -> List[docutils_image]:
        """Return list of image nodes used in the directive."""
        directive_content = Element()
        directive_content.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, directive_content)
        return list(directive_content.traverse(docutils_image))

    def config_eval_bool(self, name: str) -> bool:
        """Evaluate boolean parameters from directive options and Sphinx conf.py entries.

        :param name: Suffix.
        """
        if f"show_{name}" in self.options:
            return True
        if f"no_{name}" in self.options:
            return False
        if self.config[f"carousel_show_{name}"] is True:
            return True
        return False

    def run(self) -> List[Element]:
        """Main method."""
        div_id = f"carousel-{uuid.uuid4()}"
        child_nodes = []

        # Build carousel-inner div.
        items = []
        for idx, image in enumerate(self.images()):
            image["classes"] += ["d-block", "w-100"]
            items.append(nodes.CarouselItemNode(idx == 0, "", image))
        inner_div = nodes.CarouselInnerNode("", *items)
        child_nodes.append(inner_div)

        # Build control buttons.
        if self.config_eval_bool("controls"):
            buttons = [nodes.CarouselControlNode(div_id, prev=True), nodes.CarouselControlNode(div_id)]
            child_nodes.extend(buttons)

        data_ride = "" if "no_data_ride" in self.options else "carousel"
        main_div = nodes.CarouselMainNode(div_id, data_ride, "", *child_nodes)
        return [main_div]


def copy_static(app: Sphinx):
    """Install CSS and JS files into the output directory.

    :param app: Sphinx application object.
    """
    if not app.config.carousel_add_bootstrap_css_js or app.builder.format != "html":
        return

    static_in = Path(__file__).parent / "_static"
    static_out = Path(app.builder.outdir) / "_static"
    static_out.mkdir(exist_ok=True)

    copy_asset_file(str(static_in / "bootstrap.css"), str(static_out))
    copy_asset_file(str(static_in / "bootstrap.js"), str(static_out))


def include_static_on_demand(app: Sphinx, _: str, __: str, ___: dict, doctree: document):
    """Add CSS and JS files to <head /> only on specific pages that use the directive.

    :param app: Sphinx application object.
    :param _: Unused.
    :param __: Unused.
    :param ___: Unused.
    :param doctree: Tree of docutils nodes.
    """
    if not app.config.carousel_add_bootstrap_css_js:
        return
    if doctree and doctree.traverse(nodes.CarouselMainNode):
        app.add_css_file("bootstrap.css")
        app.add_js_file("bootstrap.js")


def setup(app: Sphinx) -> Dict[str, str]:
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    """
    app.add_config_value("carousel_add_bootstrap_css_js", True, "html")
    app.add_config_value("carousel_show_controls", False, "html")
    app.add_directive("carousel", Carousel)
    app.connect("builder-inited", copy_static)
    app.connect("html-page-context", include_static_on_demand)
    nodes.CarouselControlNode.add_node(app)
    nodes.CarouselInnerNode.add_node(app)
    nodes.CarouselItemNode.add_node(app)
    nodes.CarouselMainNode.add_node(app)
    return dict(version=__version__)
