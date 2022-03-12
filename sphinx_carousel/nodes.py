"""Docutils nodes."""
from docutils import nodes
from sphinx.writers.html5 import HTML5Translator


class CarouselSlideNode(nodes.Element):
    """Main div."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselSlideNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", "", **{"CLASS": "carousel slide", "data-ride": "carousel"}))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.extend(["</div>"])


class CarouselInnerNode(nodes.Element):
    """Secondary div that contains the image divs."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselInnerNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", "", **{"CLASS": "carousel-inner"}))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.extend(["</div>"])


class CarouselItemNode(nodes.Element):
    """Div that contains an image."""

    def __init__(self, active: bool, rawsource="", *children, **attributes):  # pylint: disable=keyword-arg-before-vararg
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
        writer.body.extend(["</div>"])
