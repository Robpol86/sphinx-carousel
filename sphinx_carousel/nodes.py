"""Docutils nodes."""
# pylint: disable=keyword-arg-before-vararg
from abc import abstractmethod

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


class BaseNode(nodes.Element):
    """Base node class."""

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

    def __init__(self, div_id: str, data_ride: str = "", rawsource: str = "", *children, **attributes):
        """Constructor.

        :param div_id: <div id="...">.
        :param data_ride: <div data-ride="...">.
        :param rawsource: Passed to parent class.
        :param children: Passed to parent class.
        :param attributes: Passed to parent class.
        """
        super().__init__(rawsource, *children, **attributes)
        self.div_id = div_id
        self.data_ride = data_ride

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselMainNode"):
        """Append opening tags to document body list."""
        attributes = {"CLASS": "carousel slide", "ids": [node.div_id]}
        if node.data_ride:
            attributes["data-ride"] = node.data_ride
        writer.body.append(writer.starttag(node, "div", "", **attributes))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>")


class CarouselInnerNode(BaseNode):
    """Secondary div that contains the image divs."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselInnerNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", "", **{"CLASS": "carousel-inner"}))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>")


class CarouselItemNode(BaseNode):
    """Div that contains an image."""

    def __init__(self, active: bool, rawsource="", *children, **attributes):
        """Constructor.

        :param active: Append active class to div, needed for first image.
        :param rawsource: Passed to parent class.
        :param children: Passed to parent class.
        :param attributes: Passed to parent class.
        """
        super().__init__(rawsource, *children, **attributes)
        self.active = active

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselItemNode"):
        """Append opening tags to document body list."""
        classes = ["carousel-item"]
        if node.active:
            classes.append("active")
        writer.body.append(writer.starttag(node, "div", "", **{"CLASS": " ".join(classes)}))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>")


class CarouselControlNode(BaseNode):
    """Previous/next buttons."""

    def __init__(self, div_id: str, prev: bool = False, rawsource: str = "", *children, **attributes):
        """Constructor.

        :param div_id: <div id="...">.
        :param prev: Previous button if True, else Next button.
        :param rawsource: Passed to parent class.
        :param children: Passed to parent class.
        :param attributes: Passed to parent class.
        """
        super().__init__(rawsource, *children, **attributes)
        self.div_id = div_id
        self.prev = prev

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselControlNode"):
        """Append opening tags to document body list."""
        attributes_button = {
            "CLASS": f"carousel-control-{'prev' if node.prev else 'next'}",
            "type": "button",
            "data-target": f"#{node.div_id}",
            "data-slide": "prev" if node.prev else "next",
        }
        writer.body.append(writer.starttag(node, "button", "", **attributes_button))
        attributes_span = {
            "CLASS": f"carousel-control-{'prev' if node.prev else 'next'}-icon",
            "aria-hidden": "true",
        }
        writer.body.append(writer.starttag(node, "span", "", **attributes_span))
        writer.body.append("</span>")
        writer.body.append(writer.starttag(node, "span", "", **{"CLASS": "sr-only"}))
        writer.body.append("Previous" if node.prev else "Next")
        writer.body.append("</span>")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</button>")
