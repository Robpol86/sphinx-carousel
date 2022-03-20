"""A Sphinx extension for creating slideshows using Bootstrap Carousels.

https://sphinx-carousel.readthedocs.io
https://github.com/Robpol86/sphinx-carousel
https://pypi.org/project/sphinx-carousel
"""
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from docutils.nodes import document, Element, image as docutils_image, reference
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
        "no_indicators": directives.flag,
        "show_indicators": directives.flag,
    }

    def images(self) -> List[Tuple[docutils_image, Optional[reference]]]:
        """Return list of image nodes and other associated data used in the directive.

        :return: Image node and parent reference node if :target: was specified.
        """
        directive_content = Element()
        directive_content.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, directive_content)

        images = []
        for image in directive_content.traverse(docutils_image):
            # Handle linked images.
            linked_image = image.parent if image.parent.hasattr("refuri") else None
            # Done with image.
            images.append((image, linked_image))

        return images

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
        main_div_id = f"carousel-{self.env.new_serialno('carousel')}"
        data_ride = "" if "no_data_ride" in self.options else "carousel"
        main_div = nodes.CarouselMainNode(main_div_id, data_ride)
        images = self.images()

        # Build indicators.
        if self.config_eval_bool("indicators"):
            main_div.append(nodes.CarouselIndicatorsNode(main_div_id, len(images)))

        # Build carousel-inner div.
        items = []
        for idx, (image, linked_image) in enumerate(images):
            image["classes"] += ["d-block", "w-100"]
            items.append(nodes.CarouselItemNode(idx == 0, "", linked_image or image))
        inner_div = nodes.CarouselInnerNode("", *items)
        main_div.append(inner_div)

        # Build control buttons.
        if self.config_eval_bool("controls"):
            main_div.append(nodes.CarouselControlNode(main_div_id, prev=True))
            main_div.append(nodes.CarouselControlNode(main_div_id))

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
    app.add_config_value("carousel_show_indicators", False, "html")
    app.add_directive("carousel", Carousel)
    app.connect("builder-inited", copy_static)
    app.connect("html-page-context", include_static_on_demand)
    nodes.CarouselControlNode.add_node(app)
    nodes.CarouselIndicatorsNode.add_node(app)
    nodes.CarouselInnerNode.add_node(app)
    nodes.CarouselItemNode.add_node(app)
    nodes.CarouselMainNode.add_node(app)
    return dict(version=__version__)
