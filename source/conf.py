# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.append(os.path.abspath("../extensions"))

from cs1302.bootstrap_icons import BootstrapIcons
from cs1302.dictutils import dict_read
from cs1302.pyproject import load_pyproject
from pkg_resources import parse_version

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

pyproject = load_pyproject("..")
project = "DRY"
copyright = "2023, Michael E. Cotterell"
author = "Michael E. Cotterell"
version = dict_read(pyproject, "tool.poetry.version")
parsed_version = parse_version(version)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx_cs1302_utils",
]

templates_path = ["_templates"]
exclude_patterns = []

# Figures, tables and code-blocks are automatically numbered if they have a caption.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-numfig
numfig = True

# Prefix each section label with the name of the document it is in, followed by a colon.
# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#confval-autosectionlabel_prefix_document
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

icons = BootstrapIcons()

html_title = "Don't Repeat Yourself"
html_static_path = ["_static"]
html_output_encoding = "utf-8"
html_permalinks = True
html_permalinks_icon = "¶"

html_theme = "furo"
html_theme_options = {
    "footer_icons": [
        {
            "name": "CC-BY-NC-SA-4.0 License",
            "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
            "html": icons.get("cc-circle-fill"),
            "class": "",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/cs1302/dry",
            "html": icons.get("github"),
            "class": "",
        },
    ],
}

if parsed_version.pre:
    announcement_message = (
        f"This page belongs to a pre-release version ({version}) of the book."
    )
    html_theme_options["announcement"] = announcement_message
