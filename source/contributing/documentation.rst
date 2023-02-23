Documentation contributions
===========================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

To modify or add new pages to `microhh.readthedocs.io <https://microhh.readthedocs.io>`_, you first need to install `sphinx` and the theme that we use:



.. code-block:: shell

   pip install sphinx sphinx_rtd_theme

Next, make a fork of the documentation at https://github.com/microhh/readthedocs, and clone your fork:

.. code-block:: shell

   git clone https://github.com/your_user_name/readthedocs.git
   # or
   git clone git@github.com:your_user_name/readthedocs.git

From the `readthedocs` directory, you can compile the code using:

.. code-block:: shell

   make html

This should provide the html pages in `build/html` (or `_build/html`). When finished, commit the changes, push them to your fork, and create a pull request at https://github.com/microhh/readthedocs/pulls .
