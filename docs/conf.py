# -- Path setup --------------------------------------------------------------

# -- Project information -----------------------------------------------------
project = 'sphinxcontrib-sass example'
copyright = '2021, Kazuya Takei'
author = 'Kazuya Takei'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinxcontrib.sass',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['css/custom.css']

sass_src_dir = '_sass'
sass_out_dir = '_static/css'
sass_targets = {
    'custom.scss': 'custom.css',
}
sass_output_style = 'compressed'
