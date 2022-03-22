"""Docutils nodes."""
# pylint: disable=keyword-arg-before-vararg
from abc import abstractmethod
from typing import Dict

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


class BaseNode(nodes.Element, nodes.General):
    """Base node class."""

    def __init__(self, rawsource: str = "", *children, prefix: str = "", **attributes):
        """Constructor.

        :param rawsource: Passed to parent class.
        :param children: Passed to parent class.
        :param prefix: Prefix each HTML class tag with this.
        :param attributes: Passed to parent class.
        """
        super().__init__(rawsource, *children, **attributes)
        self.prefix = prefix

    @staticmethod
    @abstractmethod
    def html_visit(writer: HTML5Translator, node: "BaseNode"):
        """Append opening tags to document body list."""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        raise NotImplementedError

    @classmethod
    def add_node(cls, app: Sphinx):
        """Convenience method that adds the subclass node to the Sphinx app.."""
        app.add_node(cls, html=(cls.html_visit, cls.html_depart))


class CarouselMainNode(BaseNode):
    """Main div."""

    def __init__(self, div_id: str, attributes: Dict[str, str], *args, **kwargs):
        """Constructor.

        :param div_id: <div id="...">.
        :param attributes: Div attributes (e.g. {"data-bs-ride": "carousel", ...}.
        :param args: Passed to parent class.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.div_id = div_id
        self.attributes = attributes

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselMainNode"):
        """Append opening tags to document body list."""
        attributes = dict(node.attributes, CLASS=f"{node.prefix}carousel {node.prefix}slide", ids=[node.div_id])
        writer.body.append(writer.starttag(node, "div", **attributes))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselInnerNode(BaseNode):
    """Secondary div that contains the image divs."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselInnerNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", CLASS=f"{node.prefix}carousel-inner"))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselItemNode(BaseNode):
    """Div that contains an image."""

    def __init__(self, active: bool, *args, **kwargs):
        """Constructor.

        :param active: Append active class to div, needed for first image.
        :param args: Passed to parent class.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.active = active

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselItemNode"):
        """Append opening tags to document body list."""
        classes = [f"{node.prefix}carousel-item"]
        if node.active:
            classes.append(f"{node.prefix}active")
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes)))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselControlNode(BaseNode):
    """Previous/next buttons."""

    def __init__(self, div_id: str, prev: bool = False, *args, **kwargs):
        """Constructor.

        :param div_id: Corresponding CarouselMainNode div ID.
        :param prev: Previous button if True, else Next button.
        :param args: Passed to parent class.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.div_id = div_id
        self.prev = prev

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselControlNode"):
        """Append opening tags to document body list."""
        attributes_button = {
            "CLASS": f"{node.prefix}carousel-control-{'prev' if node.prev else 'next'}",
            "type": "button",
            "data-bs-target": f"#{node.div_id}",
            "data-bs-slide": "prev" if node.prev else "next",
        }
        writer.body.append(writer.starttag(node, "button", **attributes_button))
        attributes_span = {
            "CLASS": f"{node.prefix}carousel-control-{'prev' if node.prev else 'next'}-icon",
            "aria-hidden": "true",
        }
        writer.body.append(writer.emptytag(node, "span", **attributes_span))
        writer.body.append(writer.starttag(node, "span", CLASS=f"{node.prefix}visually-hidden"))
        writer.body.append("Previous" if node.prev else "Next")
        writer.body.append("\n</span>\n")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</button>\n")


class CarouselIndicatorsNode(BaseNode):
    """Indicators."""

    def __init__(self, div_id: str, count: int, *args, **kwargs):
        """Constructor.

        :param div_id: Corresponding CarouselMainNode div ID.
        :param count: Number of images.
        :param args: Passed to parent class.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.div_id = div_id
        self.count = count

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselIndicatorsNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", CLASS=f"{node.prefix}carousel-indicators"))
        for i in range(node.count):
            attributes = {
                "type": "button",
                "data-bs-target": f"#{node.div_id}",
                "data-bs-slide-to": f"{i}",
                "aria-label": f"Slide {i+1}",
            }
            if i == 0:
                attributes["CLASS"] = f"{node.prefix}active"
                attributes["aria-current"] = "true"
            writer.body.append(writer.emptytag(node, "button", **attributes))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselCaptionNode(BaseNode):
    """Captions."""

    def __init__(self, title: str = "", description: str = "", *args, **kwargs):
        """Constructor.

        :param title: Caption heading.
        :param description: Caption paragraph.
        :param args: Passed to parent class.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.title = title
        self.description = description

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselCaptionNode"):
        """Append opening tags to document body list."""
        classes = [f"{node.prefix}carousel-caption", f"{node.prefix}d-none", f"{node.prefix}d-md-block"]
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes)))

        writer.body.append(writer.starttag(node, "h5"))
        writer.body.append(node.title)
        writer.body.append("\n</h5>\n")

        if node.description:
            writer.body.append(writer.starttag(node, "p"))
            writer.body.append(node.description)
            writer.body.append("\n</p>\n")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")
