# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Neterial Docs'
copyright = '2025, Neterial'
author = 'Neterial'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# Add _templates to the templates_path if not already present
if '_templates' not in templates_path:
    templates_path.append('_templates')

# -- Internationalization ------------------------------------------------

language = 'en'
locale_dirs = ['locales/']   # path is relative to the conf.py directory
gettext_compact = False      # optional: keeps .po files in separate folders per document

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
