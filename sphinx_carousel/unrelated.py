"""Code unrelated and out of scope of the main project.

Code here is placed temporarily until I have enough time to move it to its own separate project.
"""
import inspect
import os
from typing import List, Optional

from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from sphinx.util import ensuredir, logging


class MultiTheme:  # noqa
    """Build multiple themes."""

    DIRECTORY_PREFIX = "theme_"

    @staticmethod
    def get_sphinx_app() -> Optional[Sphinx]:  # pragma: no cover
        """Inspect call stack and return the Sphinx app instance if found."""
        for frame in inspect.stack():
            app = frame[0].f_locals.get("self", None)
            if app and isinstance(app, Sphinx):
                return app
        return None

    @classmethod
    def modify_sphinx_app(cls, app: Sphinx, theme: str):  # pragma: no cover
        """Make changes to the Sphinx app.

        :param app: Sphinx app instance to modify.
        :param theme: Current theme being used.
        """
        log = logging.getLogger(__file__)
        subdir = f"{cls.DIRECTORY_PREFIX}{theme}"
        old_outdir = app.outdir
        old_doctreedir = app.doctreedir

        new_outdir = os.path.join(old_outdir, subdir)
        ensuredir(new_outdir)
        log.info(">>> Changing outdir from %s to %s", old_outdir, new_outdir)
        app.outdir = new_outdir

        new_doctreedir = old_doctreedir.replace(old_outdir, new_outdir)
        if new_doctreedir == old_doctreedir:
            new_doctreedir = os.path.join(old_doctreedir, subdir)
        log.info(">>> Changing doctreedir from %s to %s", old_doctreedir, new_doctreedir)
        app.doctreedir = new_doctreedir

    @staticmethod
    def fork() -> bool:  # pragma: no cover
        """Fork Python process and wait for the child process to finish.

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
    def select_theme(cls, themes: List[str]) -> str:
        """Build copies of all docs using multiple themes in separate subdirectories.

        The first theme in the list is the default/root theme. All other themes will be built in a forked process into a
        prefixed subdirectory. At the end of the function the root theme is returned to the main process and Sphinx will
        continue building it in the original output directory.

        :param themes: List of theme names as expected by the `html_theme` Sphinx config value.

        :return: The theme to use for the current build.
        """
        log = logging.getLogger(__file__)

        # Skip conditionals.
        if len(themes) < 2:
            return themes[0]
        if os.environ.get("SPHINX_MULTI_THEME") == "false":
            log.info(">>> Disabling multi-theme build mode <<<")
            return themes[0]
        if not hasattr(os, "fork"):
            log.warning(">>> Platform does not support forking, disabling multi-theme build <<<")
            return themes[0]

        # Get Sphinx app instance.
        app = cls.get_sphinx_app()
        if not app:
            log.warning(">>> Unable to locate Sphinx app instance from here <<<")
            return themes[0]

        # Build secondary themes into subdirectories.
        log.info(">>> Entering multi-theme build mode <<<")
        for theme in themes[1:]:
            log.info(">>> Building docs with theme: %s <<<", theme)
            if cls.fork():
                cls.modify_sphinx_app(app, theme)
                return theme  # This is the child process.
            log.info(">>> Done with theme: %s <<<", theme)
        log.info(">>> Exiting multi-theme build mode <<<")

        return themes[0]
