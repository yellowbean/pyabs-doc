# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'AbsBox'
copyright = '2022, Xiaoyu,Zhang'
author = 'xiaoyu, zhang'

release = '0.1.2'
version = '0.1.0'


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    #'css/custom.css',
]

html_js_files = [
    'js/baidu.js',
]

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_toolbox.installation',
    'sphinx_toolbox.collapse',
    'sphinx_design'
    #'myst_parser'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
