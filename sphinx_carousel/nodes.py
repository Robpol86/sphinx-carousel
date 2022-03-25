"""Docutils nodes."""
# pylint: disable=keyword-arg-before-vararg
from abc import ABCMeta, abstractmethod
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
        app.add_node(
            cls,
            html=(cls.html_visit, cls.html_depart),
            latex=(lambda *_: None, lambda *_: None),  # TODO https://github.com/Robpol86/sphinx-carousel/issues/50
            man=(lambda *_: None, lambda *_: None),  # TODO https://github.com/Robpol86/sphinx-carousel/issues/51
            texinfo=(lambda *_: None, lambda *_: None),  # TODO https://github.com/Robpol86/sphinx-carousel/issues/51
            text=(lambda *_: None, lambda *_: None),  # TODO https://github.com/Robpol86/sphinx-carousel/issues/51
        )


class CarouselMainNode(BaseNode):
    """Main div."""

    def __init__(
        self,
        *args,
        div_id: str = "",
        prefix: str = "",
        attributes: Dict[str, str] = None,
        fade: bool = False,
        dark: bool = False,
        **kwargs,
    ):
        """Constructor.

        :param args: Passed to parent class.
        :param div_id: <div id="...">.
        :param prefix: Bootstrap class' prefix.
        :param attributes: Div attributes (e.g. {"data-bs-ride": "carousel", ...}.
        :param fade: Fade between images instead of using a slide transition.
        :param dark: Carousel dark variant.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.div_id = div_id
        self.prefix = prefix
        self.attributes = attributes
        self.fade = fade
        self.dark = dark

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselMainNode"):
        """Append opening tags to document body list."""
        classes = [f"{node.prefix}carousel", f"{node.prefix}slide"]
        if node.fade:
            classes.append(f"{node.prefix}carousel-fade")
        if node.dark:
            classes.append(f"{node.prefix}carousel-dark")
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes), ids=[node.div_id], **node.attributes))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class SubNode(BaseNode, metaclass=ABCMeta):
    """Base class for child nodes under main node."""

    @property
    def main_node(self) -> CarouselMainNode:
        """Return the main carousel node instance."""
        return self.parent  # noqa

    @property
    def prefix(self) -> str:
        """Return Bootstrap class' prefix."""
        return self.main_node.prefix


class CarouselInnerNode(SubNode):
    """Secondary div that contains the image divs."""

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselInnerNode"):
        """Append opening tags to document body list."""
        writer.body.append(writer.starttag(node, "div", CLASS=f"{node.prefix}carousel-inner"))

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselItemNode(SubNode):
    """Div that contains an image."""

    def __init__(self, *args, active: bool = False, **kwargs):
        """Constructor.

        :param args: Passed to parent class.
        :param active: Append active class to div, needed for first image.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.active = active

    @property
    def main_node(self) -> CarouselMainNode:
        """Return the main carousel node instance."""
        return self.parent.parent  # noqa

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


class CarouselControlNode(SubNode):
    """Previous/next buttons."""

    NEXT_ICON = "carousel-control-next"
    PREV_ICON = "carousel-control-prev"

    def __init__(self, *args, prev: bool = False, top: bool = False, shadow: bool = False, **kwargs):
        """Constructor.

        :param args: Passed to parent class.
        :param prev: Previous button if True, else Next button.
        :param top: Display controls at the top of the image instead of the middle.
        :param shadow: Show a shadow around the icons for better visibility when an image is a similar color.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.prev = prev
        self.top = top
        self.shadow = shadow

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselControlNode"):
        """Append opening tags to document body list."""
        classes = [f"{node.prefix}{node.PREV_ICON if node.prev else node.NEXT_ICON}"]
        if node.top:
            classes.extend([f"{node.prefix}my-4", "scc-top-control"])
        if node.shadow:
            classes.append("scc-shadow-control")
        writer.body.append(
            writer.starttag(
                node,
                "button",
                CLASS=" ".join(classes),
                type="button",
                **{"data-bs-target": f"#{node.main_node.div_id}", "data-bs-slide": "prev" if node.prev else "next"},
            )
        )

        # Nested icon.
        writer.body.append(
            writer.starttag(
                node,
                "span",
                "",
                CLASS=f"{node.prefix}carousel-control-{'prev' if node.prev else 'next'}-icon",
                **{"aria-hidden": "true"},
            )
        )
        writer.body.append("</span>\n")

        # Nested hidden text for screen readers.
        writer.body.append(writer.starttag(node, "span", "", CLASS=f"{node.prefix}visually-hidden"))
        writer.body.append("Previous" if node.prev else "Next")
        writer.body.append("</span>\n")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</button>\n")


class CarouselIndicatorsNode(SubNode):
    """Indicators."""

    def __init__(self, *args, count: int = 0, top: bool = False, shadow: bool = False, **kwargs):
        """Constructor.

        :param args: Passed to parent class.
        :param count: Number of images.
        :param top: Display indicators at the top of the image instead of the middle.
        :param shadow: Show a shadow around the icons for better visibility when an image is a similar color.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.count = count
        self.top = top
        self.shadow = shadow

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselIndicatorsNode"):
        """Append opening tags to document body list."""
        classes = [f"{node.prefix}carousel-indicators"]
        if node.top:
            classes.extend([f"{node.prefix}my-4", "scc-top-indicator"])
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes)))

        # Add indicator buttons.
        classes_b = []
        if node.shadow:
            classes_b.append("scc-shadow-indicator")
        for i in range(node.count):
            attributes = {
                "data-bs-target": f"#{node.main_node.div_id}",
                "data-bs-slide-to": f"{i}",
                "aria-label": f"Slide {i+1}",
            }
            if i == 0:
                attributes["CLASS"] = " ".join([f"{node.prefix}active"] + classes_b)
                attributes["aria-current"] = "true"
            elif classes_b:
                attributes["CLASS"] = " ".join(classes_b)
            writer.body.append(writer.starttag(node, "button", "", type="button", **attributes))
            writer.body.append("</button>\n")

    @staticmethod
    def html_depart(writer: HTML5Translator, _):
        """Append closing tags to document body list."""
        writer.body.append("</div>\n")


class CarouselCaptionNode(SubNode):
    """Captions."""

    BELOW_BG_DARK = "bg-dark"
    BELOW_BG_LIGHT = "bg-light"

    def __init__(self, *args, title: str = "", description: str = "", below: bool = False, **kwargs):
        """Constructor.

        :param args: Passed to parent class.
        :param title: Caption heading.
        :param description: Caption paragraph.
        :param below: Display caption below image instead of overlayed on top.
        :param kwargs: Passed to parent class.
        """
        super().__init__(*args, **kwargs)
        self.title = title
        self.description = description
        self.below = below

    @property
    def main_node(self) -> CarouselMainNode:
        """Return the main carousel node instance."""
        return self.parent.parent.parent  # noqa

    @staticmethod
    def html_visit(writer: HTML5Translator, node: "CarouselCaptionNode"):
        """Append opening tags to document body list."""
        classes = [f"{node.prefix}carousel-caption"]
        if node.below:  # From: https://scottdorman.blog/2019/03/02/bootstrap-carousel-caption-placement/
            classes.extend(
                [
                    f"{node.prefix}{node.BELOW_BG_LIGHT if node.main_node.dark else node.BELOW_BG_DARK}",
                    f"{node.prefix}d-sm-block",
                    "scc-below-control",
                ]
            )
        else:
            classes.extend([f"{node.prefix}d-none", f"{node.prefix}d-md-block"])
        writer.body.append(writer.starttag(node, "div", CLASS=" ".join(classes)))

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
