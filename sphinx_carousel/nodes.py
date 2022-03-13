"""Docutils nodes."""
# pylint: disable=keyword-arg-before-vararg
from docutils import nodes
from sphinx.writers.html5 import HTML5Translator


class CarouselSlideNode(nodes.Element):
    """Main div."""

    def __init__(self, div_id: str = "", data_ride: str = "", rawsource: str = "", *children, **attributes):
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
    def html_visit(writer: HTML5Translator, node: "CarouselSlideNode"):
        """Append opening tags to document body list."""
        attributes = {"CLASS": "carousel slide"}
        if node.div_id:
            attributes["ids"] = [node.div_id]
        if node.data_ride:
            attributes["data-ride"] = node.data_ride
        writer.body.append(writer.starttag(node, "div", "", **attributes))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>")


class CarouselInnerNode(nodes.Element):
    """Secondary div that contains the image divs."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselInnerNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", "", **{"CLASS": "carousel-inner"}))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>")


class CarouselItemNode(nodes.Element):
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
