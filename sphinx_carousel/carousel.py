"""A Sphinx extension for creating slideshows using Bootstrap Carousels.

https://sphinx-carousel.readthedocs.io
https://github.com/Robpol86/sphinx-carousel
https://pypi.org/project/sphinx-carousel
"""
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from docutils.nodes import caption, document, Element, image as docutils_image, legend, reference
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx.util.fileutil import copy_asset_file

from sphinx_carousel import __version__, nodes


class Carousel(SphinxDirective):
    """Main directive."""

    has_content = True
    option_spec = {
        "data-bs-interval": directives.unchanged,
        "data-bs-keyboard": directives.unchanged,
        "data-bs-pause": directives.unchanged,
        "data-bs-ride": directives.unchanged,
        "data-bs-wrap": directives.unchanged,
        "data-bs-touch": directives.unchanged,
        "no_controls": directives.flag,
        "show_controls": directives.flag,
        "no_indicators": directives.flag,
        "show_indicators": directives.flag,
    }

    def images(self) -> List[Tuple[docutils_image, Optional[reference], Optional[str], Optional[str]]]:
        """Return list of image/figure nodes along with other associated data.

        :return: Image node, parent reference node if :target: was specified, and figure's title/description if available.
        """
        # Create temporary empty document to dump nested image/figure directives into.
        directive_content = Element()
        directive_content.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, directive_content)

        images = []
        for image in directive_content.traverse(docutils_image):
            # Handle linked images.
            linked_image = image.parent if image.parent.hasattr("refuri") else None
            # Handle captions.
            node = (linked_image or image).next_node(caption, siblings=True, ascend=False, descend=False)
            title = node.astext() if node else None
            node = (linked_image or image).next_node(legend, siblings=True, ascend=False, descend=False)
            description = node.astext() if node else None
            # Done with image.
            images.append((image, linked_image, title, description))

        return images

    def config_read_flag(self, name: str) -> bool:
        """Evaluate a directive flag option and the corresponding Sphinx conf.py entry as fallback.

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
        prefix = self.config["carousel_bootstrap_prefix"]
        main_div = nodes.CarouselMainNode(
            main_div_id,
            attributes={k: v for k, v in self.options.items() if k.startswith("data-")},
            prefix=prefix,
        )
        images = self.images()

        # Build indicators.
        if self.config_read_flag("indicators"):
            main_div.append(nodes.CarouselIndicatorsNode(main_div_id, len(images), prefix=prefix))

        # Build carousel-inner div.
        items = []
        for idx, (image, linked_image, title, description) in enumerate(images):
            image["classes"] += [f"{prefix}d-block", f"{prefix}w-100"]
            child_nodes = [linked_image or image]
            if title or description:
                child_nodes.append(nodes.CarouselCaptionNode(title, description, prefix=prefix))
            items.append(nodes.CarouselItemNode(idx == 0, "", *child_nodes, prefix=prefix))
        inner_div = nodes.CarouselInnerNode("", *items, prefix=prefix)
        main_div.append(inner_div)

        # Build control buttons.
        if self.config_read_flag("controls"):
            main_div.append(nodes.CarouselControlNode(main_div_id, prefix=prefix, prev=True))
            main_div.append(nodes.CarouselControlNode(main_div_id, prefix=prefix))

        return [main_div]


def copy_static(app: Sphinx):
    """Install CSS and JS files into the output directory.

    :param app: Sphinx application object.
    """
    if not app.config.carousel_bootstrap_add_css_js or app.builder.format != "html":
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
    if not app.config.carousel_bootstrap_add_css_js:
        return
    if doctree and doctree.traverse(nodes.CarouselMainNode):
        app.add_css_file("bootstrap.css")
        app.add_js_file("bootstrap.js")


def setup(app: Sphinx) -> Dict[str, str]:
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    """
    app.add_config_value("carousel_bootstrap_add_css_js", True, "html")
    app.add_config_value("carousel_bootstrap_prefix", "scbs-", "html")
    app.add_config_value("carousel_show_controls", False, "html")
    app.add_config_value("carousel_show_indicators", False, "html")
    app.add_directive("carousel", Carousel)
    app.connect("builder-inited", copy_static)
    app.connect("html-page-context", include_static_on_demand)
    nodes.CarouselCaptionNode.add_node(app)
    nodes.CarouselControlNode.add_node(app)
    nodes.CarouselIndicatorsNode.add_node(app)
    nodes.CarouselInnerNode.add_node(app)
    nodes.CarouselItemNode.add_node(app)
    nodes.CarouselMainNode.add_node(app)
    return dict(version=__version__)
