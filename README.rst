Neterial Documentation (Sphinx)
=============================

This documentation is built using [Sphinx](https://www.sphinx-doc.org/), with all sources in reStructuredText (.rst) format.

Setup
-----
1. Install Python 3.x
2. Install dependencies:
   ::

      pip install -r requirements.txt

3. (If not installed) Install Pandoc for .md to .rst conversion (already done for this repo).

Building the Docs
-----------------
1. Change to the Sphinx source directory:
   ::

      cd source

2. Build the HTML documentation:
   ::

      make html

3. The output will be in `source/build/html`. Open `index.html` in your browser.

Navigation
----------
- All documentation is in `.rst` files in `source/source/`.
- Images are in `source/source/_static/img/`.
- The main navigation is controlled by `index.rst` and the Sphinx toctree.

Contributing
------------
- Edit or add `.rst` files in `source/source/`.
- Add images to `source/source/_static/img/` and reference them as `_static/img/your-image.png` in your `.rst` files.
- Run `make html` after changes to preview the documentation.

Legacy Docs
-----------
- The original Markdown files and structure are preserved in the `old-docs/` directory for reference. 