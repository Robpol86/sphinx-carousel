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

ImageTuple = Tuple[docutils_image, Optional[reference], Optional[str], Optional[str]]


class Carousel(SphinxDirective):
    """Main directive."""

    has_content = True
    option_spec = {
        # Div data attributes.
        "data-bs-interval": directives.unchanged,
        "data-bs-keyboard": directives.unchanged,
        "data-bs-pause": directives.unchanged,
        "data-bs-ride": directives.unchanged,
        "data-bs-wrap": directives.unchanged,
        "data-bs-touch": directives.unchanged,
        # Crossfade/dark.
        "no_fade": directives.flag,
        "show_fade": directives.flag,
        "no_dark": directives.flag,
        "show_dark": directives.flag,
        # Controls/indicators.
        "no_buttons_on_top": directives.flag,
        "show_buttons_on_top": directives.flag,
        "no_controls": directives.flag,
        "show_controls": directives.flag,
        "no_indicators": directives.flag,
        "show_indicators": directives.flag,
        "no_shadows": directives.flag,
        "show_shadows": directives.flag,
        # Captions.
        "no_captions_below": directives.flag,
        "show_captions_below": directives.flag,
    }

    def images(self) -> List[ImageTuple]:
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

    def create_inner_node(self, images: List[ImageTuple], dark: bool) -> Element:
        """Return carousel-inner div node along with child nodes such as images and captions.

        :param images: Output of self.images().
        :param dark: Carousel dark variant.
        """
        prefix = self.config["carousel_bootstrap_prefix"]
        captions_below = self.config_read_flag("captions_below")
        items = []

        for idx, (image, linked_image, title, description) in enumerate(images):
            image["classes"] += [f"{prefix}d-block", f"{prefix}w-100"]
            child_nodes = [linked_image or image]
            if title or description:
                child_nodes.append(nodes.CarouselCaptionNode(title, description, below=captions_below, dark=dark))
            items.append(nodes.CarouselItemNode(idx == 0, "", *child_nodes))

        return nodes.CarouselInnerNode("", *items)

    def run(self) -> List[Element]:
        """Main method."""
        main_div_id = f"carousel-{self.env.new_serialno('carousel')}"
        dark_variant = self.config_read_flag("dark")
        main_div = nodes.CarouselMainNode(
            main_div_id,
            attributes={k: v for k, v in self.options.items() if k.startswith("data-")},
            fade=self.config_read_flag("fade"),
            dark=dark_variant,
        )
        images = self.images()
        buttons_on_top = self.config_read_flag("buttons_on_top")
        shadows = self.config_read_flag("shadows")

        # Build indicators.
        if self.config_read_flag("indicators"):
            main_div.append(nodes.CarouselIndicatorsNode(main_div_id, len(images), top=buttons_on_top, shadow=shadows))

        # Build carousel-inner div.
        main_div.append(self.create_inner_node(images, dark_variant))

        # Build control buttons.
        if self.config_read_flag("controls"):
            main_div.append(nodes.CarouselControlNode(main_div_id, top=buttons_on_top, shadow=shadows, prev=True))
            main_div.append(nodes.CarouselControlNode(main_div_id, top=buttons_on_top, shadow=shadows))

        return [main_div]


def copy_static(app: Sphinx):
    """Install CSS and JS files into the output directory.

    :param app: Sphinx application object.
    """
    if app.builder.format != "html":
        return

    static_in = Path(__file__).parent / "_static"
    static_out = Path(app.builder.outdir) / "_static"
    static_out.mkdir(exist_ok=True)

    if app.config.carousel_bootstrap_add_css_js:
        copy_asset_file(str(static_in / "bootstrap-carousel.css"), str(static_out))
        copy_asset_file(str(static_in / "bootstrap-carousel.js"), str(static_out))

    context = {
        "bootstrap_prefix": app.config["carousel_bootstrap_prefix"],
    }
    copy_asset_file(str(static_in / "carousel-custom.css_t"), str(static_out), context)


def include_static_on_demand(app: Sphinx, _: str, __: str, ___: dict, doctree: document):
    """Add CSS and JS files to <head /> only on specific pages that use the directive.

    :param app: Sphinx application object.
    :param _: Unused.
    :param __: Unused.
    :param ___: Unused.
    :param doctree: Tree of docutils nodes.
    """
    if not doctree or not doctree.traverse(nodes.CarouselMainNode):
        return

    if app.config.carousel_bootstrap_add_css_js:
        app.add_css_file("bootstrap-carousel.css")
        app.add_js_file("bootstrap-carousel.js")

    app.add_css_file("carousel-custom.css")


def setup(app: Sphinx) -> Dict[str, str]:
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    """
    app.add_config_value("carousel_bootstrap_add_css_js", True, "html")
    app.add_config_value("carousel_bootstrap_prefix", "scbs-", "html")
    app.add_config_value("carousel_show_buttons_on_top", False, "html")
    app.add_config_value("carousel_show_captions_below", False, "html")
    app.add_config_value("carousel_show_controls", False, "html")
    app.add_config_value("carousel_show_dark", False, "html")
    app.add_config_value("carousel_show_fade", False, "html")
    app.add_config_value("carousel_show_indicators", False, "html")
    app.add_config_value("carousel_show_shadows", False, "html")
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
