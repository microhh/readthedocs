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


Grid ``[grid]``
---------------

The ``Grid`` class contains the grid configuration.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``itot``                        |                    | Numbers of grid points in x (-)                 |
+---------------------------------+--------------------+-------------------------------------------------+
| ``jtot``                        |                    | Numbers of grid points in y (-)                 |
+---------------------------------+--------------------+-------------------------------------------------+
| ``ktot``                        |                    | Numbers of grid points in z (-)                 |
+---------------------------------+--------------------+-------------------------------------------------+
| ``xsize``                       |                    | Size of the domain in x (m)                     |
+---------------------------------+--------------------+-------------------------------------------------+
| ``ysize``                       |                    | Size of the domain in y (m)                     |
+---------------------------------+--------------------+-------------------------------------------------+
| ``zsize``                       |                    | Size of the domain in z (m)                     |
+---------------------------------+--------------------+-------------------------------------------------+
| ``swspatialorder``              |                    | | Spatial order of the finite differences (-)   |
|                                 |                    | | ``2``: Second-order grid                      |
|                                 |                    | | ``4``: Fourth-order grid                      |
+---------------------------------+--------------------+-------------------------------------------------+
| ``utrans``                      | ``0.``             | Galilean translation velocity in x (m s-1)      |
+---------------------------------+--------------------+-------------------------------------------------+
| ``vtrans``                      | ``0.``             | Galilean translation velocity in x (m s-1)      |
+---------------------------------+--------------------+-------------------------------------------------+


.. math::

    z = \sqrt{x^2 + y^2}
