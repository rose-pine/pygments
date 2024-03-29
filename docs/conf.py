# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import datetime as dt
from pathlib import Path
import sys

sys.path.insert(0, str(Path("..").resolve()))

from src import __author__, __version__  # noqa: E402


# -- Project information -----------------------------------------------------

changelog_mtime = Path("../CHANGELOG.md").stat().st_mtime
copyright_year = dt.datetime.utcfromtimestamp(changelog_mtime)

project = "pygments-rose-pine"
author = __author__
release = __version__
version = ".".join(release.split(".", 2)[:2])
copyright = f"{copyright_year:%Y}, {author}"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "Rose Piné for Pygments"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#b4637a",
        "color-brand-content": "#b4637a",
    },
    "dark_css_variables": {
        "color-brand-primary": "#b4637a",
        "color-brand-content": "#b4637a",
    },
}
