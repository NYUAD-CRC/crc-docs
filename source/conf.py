# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

project = 'CRC Documentation'
copyright = '2020, Center for Research Computing'
author = 'Nasser Alansari'

extensions = [
    "sphinx_rtd_theme",
]
templates_path = ['_templates']
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
html_logo = 'img/crc-wordmark-light.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    # 'style_nav_header_background':'#57068C',
}
html_favicon = "img/favicon.ico"
