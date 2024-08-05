# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Project Reality Documentation'
copyright = '2024, The Project Reality Team'
author = 'The Project Reality Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_sidebars = {
    '**': [
        'about.html',
        'searchfield.html',
        'navigation.html',
        'relations.html',
        'donate.html',
    ]
}
html_theme_options = {
    'fixed_sidebar': 'true',
    'show_relbar_top': 'true',
    'page_width': '1200px',
    'sidebar_width': '400px',
    'code_font_family': 'Noto Sans Mono',
    'font_family': 'Noto Sans',
    'head_font_family': 'Noto Sans',
    'caption_font_family': 'Noto Sans'
}
