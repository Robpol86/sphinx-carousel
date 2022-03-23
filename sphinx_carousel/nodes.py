"""Docutils nodes."""
# pylint: disable=keyword-arg-before-vararg
from abc import abstractmethod
from typing import Dict

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


class BaseNode(nodes.Element, nodes.General):
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
        prefix = writer.config["carousel_bootstrap_prefix"]
        writer.body.append(
            writer.starttag(node, "div", CLASS=f"{prefix}carousel {prefix}slide", ids=[node.div_id], **node.attributes)
        )

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselInnerNode(BaseNode):
    """Secondary div that contains the image divs."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselInnerNode"):
        """Append opening tags to document body list."""
        prefix = writer.config["carousel_bootstrap_prefix"]
        writer.body.append(writer.starttag(node, "div", CLASS=f"{prefix}carousel-inner"))

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
        prefix = writer.config["carousel_bootstrap_prefix"]
        classes = [f"{prefix}carousel-item"]
        if node.active:
            classes.append(f"{prefix}active")
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes)))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselControlNode(BaseNode):
    """Previous/next buttons."""

    NEXT_ICON = "carousel-control-next"
    PREV_ICON = "carousel-control-prev"

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
        prefix = writer.config["carousel_bootstrap_prefix"]

        writer.body.append(
            writer.starttag(
                node,
                "button",
                CLASS=f"{prefix}{node.PREV_ICON if node.prev else node.NEXT_ICON}",
                type="button",
                **{"data-bs-target": f"#{node.div_id}", "data-bs-slide": "prev" if node.prev else "next"},
            )
        )

        # Nested icon.
        writer.body.append(
            writer.starttag(
                node,
                "span",
                "",
                CLASS=f"{prefix}carousel-control-{'prev' if node.prev else 'next'}-icon",
                **{"aria-hidden": "true"},
            )
        )
        writer.body.append("</span>\n")

        # Nested hidden text for screen readers.
        writer.body.append(writer.starttag(node, "span", "", CLASS=f"{prefix}visually-hidden"))
        writer.body.append("Previous" if node.prev else "Next")
        writer.body.append("</span>\n")

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
        prefix = writer.config["carousel_bootstrap_prefix"]
        writer.body.append(writer.starttag(node, "div", CLASS=f"{prefix}carousel-indicators"))

        # Add indicator buttons.
        for i in range(node.count):
            attributes = {
                "data-bs-target": f"#{node.div_id}",
                "data-bs-slide-to": f"{i}",
                "aria-label": f"Slide {i+1}",
            }
            if i == 0:
                attributes["CLASS"] = f"{prefix}active"
                attributes["aria-current"] = "true"
            writer.body.append(writer.starttag(node, "button", "", type="button", **attributes))
            writer.body.append("</button>\n")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselCaptionNode(BaseNode):
    """Captions."""

    BELOW_BG_COLOR = "bg-dark"
    BELOW_STYLES = [
        "position: relative",
        "left: 0",
        "top: 0",
        "font-family: var(--bs-font-sans-serif)",
    ]

    def __init__(self, title: str = "", description: str = "", below: bool = False, *args, **kwargs):
        """Constructor.

        :param title: Caption heading.
        :param description: Caption paragraph.
        :param below: Display caption below image instead of overlayed on top.
        :param args: Passed to parent class.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.title = title
        self.description = description
        self.below = below

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselCaptionNode"):
        """Append opening tags to document body list."""
        prefix = writer.config["carousel_bootstrap_prefix"]
        classes = [f"{prefix}carousel-caption"]
        if node.below:  # From: https://scottdorman.blog/2019/03/02/bootstrap-carousel-caption-placement/
            classes.extend([f"{prefix}{node.BELOW_BG_COLOR}", f"{prefix}d-sm-block"])
            attributes = {"style": "; ".join(node.BELOW_STYLES)}
        else:
            classes.extend([f"{prefix}d-none", f"{prefix}d-md-block"])
            attributes = {}
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes), **attributes))

        writer.body.append(writer.starttag(node, "h5", ""))
        writer.body.append(node.title)
        writer.body.append("</h5>\n")

        if node.description:
            writer.body.append(writer.starttag(node, "p"))
            writer.body.append(node.description)
            writer.body.append("\n</p>\n")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")
