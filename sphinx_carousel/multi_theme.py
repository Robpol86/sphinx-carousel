"""Stealth Sphinx extension unrelated and out of scope of the main project.

Code here is placed temporarily until I have enough time to move it to its own separate project.
"""
import inspect
import os
from typing import List, Optional, Tuple

from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from sphinx.util import ensuredir, logging


class MultiTheme:  # noqa
    """Build multiple themes."""

    DIRECTORY_PREFIX = "theme_"

    @staticmethod
    def get_sphinx_app() -> Optional[Sphinx]:  # pragma: no-fork-no-cover
        """Inspect call stack and return the Sphinx app instance if found."""
        for frame in inspect.stack():
            app = frame[0].f_locals.get("self", None)
            if app and isinstance(app, Sphinx):
                return app
        return None

    @classmethod
    def modify_sphinx_app(cls, app: Sphinx, subdir: str):  # pragma: no-fork-no-cover
        """Make changes to the Sphinx app.

        :param app: Sphinx app instance to modify.
        :param subdir: Build docs into this subdirectory.
        """
        log = logging.getLogger(__file__)
        old_outdir = app.outdir
        old_doctreedir = app.doctreedir

        # Set the output directory.
        new_outdir = os.path.join(old_outdir, subdir)
        ensuredir(new_outdir)
        log.info(">>> Changing outdir from %s to %s", old_outdir, new_outdir)
        app.outdir = new_outdir

        # Set the doctree directory.
        new_doctreedir = old_doctreedir.replace(old_outdir, new_outdir)
        if new_doctreedir == old_doctreedir:
            new_doctreedir = os.path.join(old_doctreedir, subdir)
        log.info(">>> Changing doctreedir from %s to %s", old_doctreedir, new_doctreedir)
        app.doctreedir = new_doctreedir

        # Exit after Sphinx finishes building before it sends Python up the call stack (e.g. during sphinx.testing).
        os_exit = os._exit  # noqa pylint: disable=protected-access
        app.connect("build-finished", lambda *_: os_exit(0), priority=999)

    @staticmethod
    def fork() -> bool:  # pragma: no-fork-no-cover
        """Fork the Python process and wait for the child process to finish.

        :return: True if this is the child process, False if this is still the original/parent process.
        """
        pid = os.fork()  # noqa  # pylint: disable=no-member
        if pid < 0:
            raise SphinxError(f"Fork failed ({pid})")
        if pid == 0:  # This is the child process.
            return True

        # This is the parent (original) process. Wait (block) for child to finish.
        exit_status = os.waitpid(pid, 0)[1] // 256  # https://code-maven.com/python-fork-and-wait
        if exit_status != 0:
            raise SphinxError(f"Child process {pid} failed with status {exit_status}")

        return False

    @classmethod
    def parse_themes(cls, themes: List[str]) -> Tuple[str, List[str], List[str]]:
        """Determine subdirectory names for each theme.

        :param themes: List of themes requested.

        :return: Primary (first) theme, secondary (remaining) themes, unique subdirs for secondary themes.
        """
        primary_theme = themes[0]
        secondary_themes = themes[1:]
        subdirs = []
        visited = set()

        for theme in secondary_themes:
            subdir = f"{cls.DIRECTORY_PREFIX}{theme}"
            if subdir in visited:
                i = 2
                while f"{subdir}{i}" in visited:
                    i += 1
                subdir = f"{subdir}{i}"
            subdirs.append(subdir)
            visited.add(subdir)

        return primary_theme, secondary_themes, subdirs

    @classmethod
    def select_theme(cls, themes: List[str]) -> str:
        """Build copies of all docs using multiple themes in separate subdirectories.

        The first theme in the list is the default/primary theme. All other themes will be built in a forked process into a
        prefixed subdirectory. At the end of the function the primary theme is returned to the main process and Sphinx will
        continue building it in the original output directory.

        :param themes: List of theme names as expected by the `html_theme` Sphinx config value.

        :return: The theme to use for the current build.
        """
        log = logging.getLogger(__file__)
        primary_theme, secondary_themes, subdirs = cls.parse_themes(themes)

        # Skip conditionals.
        if not secondary_themes:
            return primary_theme
        if os.environ.get("SPHINX_MULTI_THEME", "").lower() == "false":
            log.info(">>> Disabling multi-theme build mode <<<")
            return primary_theme
        if not hasattr(os, "fork"):
            log.warning(">>> Platform does not support forking, disabling multi-theme build <<<")
            return primary_theme

        # Get Sphinx app instance.
        app = cls.get_sphinx_app()
        if not app:  # pragma: no-fork-no-cover
            log.warning(">>> Unable to locate Sphinx app instance from here <<<")
            return primary_theme

        # Build secondary themes into subdirectories.
        log.info(">>> Entering multi-theme build mode <<<")
        for idx, theme in enumerate(secondary_themes):  # pragma: no-fork-no-cover
            subdir = subdirs[idx]
            log.info(">>> Building docs with theme %s into %s <<<", theme, subdir)
            if cls.fork():
                cls.modify_sphinx_app(app, subdir)
                return theme  # This is the child process.
            log.info(">>> Done with theme: %s <<<", theme)
        log.info(">>> Exiting multi-theme build mode <<<")

        return primary_theme
