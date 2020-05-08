The ``.ini`` file
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


File structure
--------------

The ``.ini`` is consists of blocks like

.. code-block:: ini
   :linenos:

   [advec]
   swadvec=2
   cflmax=1.0

The name ``[advec]`` refers to the ``Advec`` class that uses the settings. This class is found in the source file with the corresponding name (``advec.cxx``).
Below the block name are the options consisting of names and values separated by ``=``.


Option cheat sheet
------------------

.. math::
   
    z = \sqrt{x^2 + y^2}

