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

Advection ``[advec]``
---------------------

The ``Advec`` class computes the advection tendencies using the chosen scheme.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``swadvec``                     | swspatialorder     | | Advection scheme                              |
|                                 |                    | | ``2``:   2nd-order                            |
|                                 |                    | | ``2i4``: 2nd-order (4th-order interpolation)  |
|                                 |                    | | ``4``:   4th-order (high accuracy)            |
|                                 |                    | | ``4m``:  4th-order (energy conserving)        |
+---------------------------------+--------------------+-------------------------------------------------+
| ``cflmax``                      | ``1.0``            | Maximum CFL for adaptive time stepping          |
+---------------------------------+--------------------+-------------------------------------------------+


Grid ``[grid]``
---------------

The ``Grid`` class contains the grid configuration.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``itot``                        | *None*             | Numbers of grid points in x (-)                 |
+---------------------------------+--------------------+-------------------------------------------------+
| ``jtot``                        | *None*             | Numbers of grid points in y (-)                 |
+---------------------------------+--------------------+-------------------------------------------------+
| ``ktot``                        | *None*             | Numbers of grid points in z (-)                 |
+---------------------------------+--------------------+-------------------------------------------------+
| ``xsize``                       | *None*             | Size of the domain in x (m)                     |
+---------------------------------+--------------------+-------------------------------------------------+
| ``ysize``                       | *None*             | Size of the domain in y (m)                     |
+---------------------------------+--------------------+-------------------------------------------------+
| ``zsize``                       | *None*             | Size of the domain in z (m)                     |
+---------------------------------+--------------------+-------------------------------------------------+
| ``swspatialorder``              | *None*             | | Spatial order of the finite differences (-)   |
|                                 |                    | | ``2``: Second-order grid                      |
|                                 |                    | | ``4``: Fourth-order grid                      |
+---------------------------------+--------------------+-------------------------------------------------+
| ``utrans``                      | ``0.``             | Galilean translation velocity in x (m s-1)      |
+---------------------------------+--------------------+-------------------------------------------------+
| ``vtrans``                      | ``0.``             | Galilean translation velocity in y (m s-1)      |
+---------------------------------+--------------------+-------------------------------------------------+


Master ``[master]``
-------------------

The ``Master`` class contains the configuration for parallel runs.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``npx``                         | ``1``              | Numbers of processes in x (-)                   |
+---------------------------------+--------------------+-------------------------------------------------+
| ``npy``                         | ``1``              | Numbers of processes in y (-)                   |
+---------------------------------+--------------------+-------------------------------------------------+
| ``wallclocklimit``              | ``1.E8``           | Maximum run duration in wall clock time (h)     |
+---------------------------------+--------------------+-------------------------------------------------+


.. math::

    z = \sqrt{x^2 + y^2}
