==================
sphinxcontrib-sass
==================

Overview
========

Sphinx extension to compile sass to css in running sphinx-build.

Install
=======

.. code-block:: bash

   pip install sphinxcontrib-sass

Usage
=====

#. Install from source
#. Edit ``conf.py``

   * Set ``sphinxcontrib.sass`` into ``extensions``
   * Configure for ``sphinxcontrib.sass`` (see example)
#. Run ``sphinx-build``

Options
-------

``sass_src_dir``
  Root directory of SASS source files.

``sass_out_dir``
  Root directory to output compiled css files.

``sass_targets``
  File map of sources and outputs

``sass_output_style``
  Output style to generate css by libsass.

``sass_include_paths``
  Include path configuration for libsass.

Example
=======

.. code-block:: python

   extensions = [
       "sphinxcontrib.sass",
   ]
   html_css_files = ["css/custom.css"]

   sass_src_dir = "_sass"
   sass_out_dir = "_static/css"
   sass_targets = {
    "custom.scss": "custom.css"
   }

License
=======

Apache 2.0. See `it <./LICENSE>`_.
