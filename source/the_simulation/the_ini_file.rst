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

    [master]
    npx=2
    npy=4

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
| ``swadvec``                     | ``swspatialorder`` | | Advection scheme                              |
|                                 |                    | | ``2``:   2nd-order                            |
|                                 |                    | | ``2i4``: 2nd-order (4th-order interpolation)  |
|                                 |                    | | ``4``:   4th-order (high accuracy)            |
|                                 |                    | | ``4m``:  4th-order (energy conserving)        |
+---------------------------------+--------------------+-------------------------------------------------+
| ``cflmax``                      | ``1.0``            | Maximum CFL for adaptive time stepping          |
+---------------------------------+--------------------+-------------------------------------------------+


Boundary conditions ``[boundary]``
----------------------------------

The ``Boundary`` class computes the boundary conditions. It has a derived class ``Boundary_surface`` that extends the base class in case the surface model is enabled.

+---------------------------------+--------------------+--------------------------------------------------------+
| Name                            | Default            | Description and options                                |
+=================================+====================+========================================================+
| ``swboundary``                  | *None*             | | Boundary discretization                              |
|                                 |                    | | ``default``: resolved boundaries                     |
|                                 |                    | | ``surface``: MOST-based surface model                |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``mbcbot``                      | *None*             | | Bottom boundary type for momentum variables          |
|                                 |                    | | ``no-slip``: Dirichlet BC with ``u,v = 0``           |
|                                 |                    | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``   |
|                                 |                    | | ``ustar``: Fixed ustar at bottom                     |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``mbctop``                      | *None*             | | Top boundary type for momentum variables             |
|                                 |                    | | ``no-slip``: Dirichlet BC with ``u,v = 0``           |
|                                 |                    | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``   |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``sbcbot``                      | *None*             | | Bottom boundary type for scalar variables. Types     |
|                                 |                    | | can be specified per scalar (``sbot[thl]=flux``)     |
|                                 |                    | | ``dirchlet``: Dirichlet BC                           |
|                                 |                    | | ``neumann``: Neumann BC                              |
|                                 |                    | | ``flux``: Fixed-flux BC                              |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``sbctop``                      | *None*             | | Top boundary type for scalar variables. Types        |
|                                 |                    | | can be specified per scalar (``stop[qt]=neumann``)   |
|                                 |                    | | ``dirchlet``: Dirichlet BC                           |
|                                 |                    | | ``neumann``: Neumann BC                              |
|                                 |                    | | ``flux``: Fixed-flux BC                              |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``sbot``                        | *None*             | | Bottom boundary value for scalar variables. Values   |
|                                 |                    | | can be specified per scalar (``sbot[thl]=300``)      |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``stop``                        | *None*             | | Top boundary value for scalar variables. Values      |
|                                 |                    | | can be specified per scalar (``stop[s]=4.``)         |
+---------------------------------+--------------------+--------------------------------------------------------+
| ``sbot_2d_list``                | *Empty list*       | | Comma-separate list of scalars that provide a binary |
|                                 |                    | | file (``sbot_thl.0000000``) with 2D slice            |
+---------------------------------+--------------------+--------------------------------------------------------+
+---------------------------------+--------------------+--------------------------------------------------------+





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
