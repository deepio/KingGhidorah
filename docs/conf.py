# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Import statements -------------------------------------------------------

import os
import subprocess

# RTD doesn't want to install with poetry all that well... so we're going to
# install this manually :)
if os.environ.get("READTHEDOCS") == "True":
  subprocess.check_output(["pip", "install", "m2r"])
  subprocess.check_output(["pip", "install", "kingghidorah"])

import kingghidorah

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "King Ghidorah"
copyright = "2020, Alex Daigle"
author = "Alex Daigle"

# The full version, including alpha/beta/rc tags
release = kingghidorah.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'alabaster',
  # 'recommonmark', Removed in favor of the more featured m2r
  'm2r',
  'sphinx.ext.autodoc'
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autosectionlabel_prefix_document = True
source_suffix = [".rst", ".md"]
# [Autodoc] Order documentation by source order, not alphabetically.
autodoc_member_order = 'bysource'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
