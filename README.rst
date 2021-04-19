=================
sphinxontrib-sass
=================

Overview
========

Sphinx extension to compile sass to css in running sphinx-build.

Install
=======

This is alpha product, and does not yet registered in public PyPI.
You can get it from my private PyPI (not need authenticated).

.. code-block:: bash

   $ pip install -i https://pypi.attakei.net/simple/ sphinxcontrib-sass

Usage
=====

#. Install from source
#. Edit ``conf.py``

   * Set ``sphinxcontrib.sass`` into ``extensions``
   * Configure for ``sphinxcontrib.sass`` (see example)
#. Run ``sphinx-build``

Example
=======

.. code-block:: python

   extensions = [
       "sphinxcontrib.sass",
   ]
   html_css_files = ["css/custom.css"]

   sass_out_dir = "_static/css"
   sass_targets = {
    "_sass/custom.scss": "_static/css/custom.css"
   }


License
=======

Apache 2.0. See `it <./LICENSE>`_.
