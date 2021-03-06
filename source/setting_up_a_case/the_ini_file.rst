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

The name ``[advec]`` refers for instance to the ``Advec`` class that uses the settings.
This class is found in the source file with the corresponding name (``advec.cxx``).
Below the block name are the options consisting of names and values separated by ``=``.

----


Advection ``[advec]``
---------------------

The ``Advec`` class computes the advection tendencies using the chosen scheme.
Note that the ``2i3`` scheme has hyperdiffusion included that results in a smooth solution.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``swadvec``                     | ``swspatialorder`` | | Advection scheme                              |
|                                 |                    | | ``0``:   Disabled                             |
|                                 |                    | | ``2``:   2nd-order                            |
|                                 |                    | | ``2i3``: 2nd-order (3rd-order interpolation)  |
|                                 |                    | | ``2i4``: 2nd-order (4th-order interpolation)  |
|                                 |                    | | ``4``:   4th-order (high accuracy)            |
|                                 |                    | | ``4m``:  4th-order (energy conserving)        |
+---------------------------------+--------------------+-------------------------------------------------+
| ``cflmax``                      | ``1.0``            | Max. CFL for adaptive time stepping             |
+---------------------------------+--------------------+-------------------------------------------------+

----


Boundary conditions ``[boundary]``
----------------------------------

The ``Boundary`` class computes the boundary conditions.
It has a derived class ``Boundary_surface`` that extends the base class in case the surface model is enabled.
Setting ``swboundary=surface`` requires ``z0m`` and ``z0h`` to be set.
Setting ``swboundary=surface_bulk`` requires ``bulk_cm`` and ``bulk_cs`` to be set.

+---------------------------------+--------------------+-----------------------------------------------------------------+
| Name                            | Default            | Description and options                                         |
+=================================+====================+=================================================================+
| ``swboundary``                  | *None*             | | Boundary discretization                                       |
|                                 |                    | | ``default``: resolved boundaries                              |
|                                 |                    | | ``surface``: MOST-based surface model                         |
|                                 |                    | | ``surface_bulk``: Surface model with prescribed drag coefs    |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``mbcbot``                      | *None*             | | Bottom boundary type for momentum variables                   |
|                                 |                    | | ``no-slip``: Dirichlet BC with ``u,v = 0``                    |
|                                 |                    | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``            |
|                                 |                    | | ``ustar``: Fixed ustar at bottom                              |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``mbctop``                      | *None*             | | Top boundary type for momentum variables                      |
|                                 |                    | | ``no-slip``: Dirichlet BC with ``u,v = 0``                    |
|                                 |                    | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``            |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``sbcbot``                      | *None*             | | Bottom boundary type for scalar variables. Types              |
|                                 |                    | | can be specified per scalar (``sbot[thl]=flux``)              |
|                                 |                    | | ``dirchlet``: Dirichlet BC                                    |
|                                 |                    | | ``neumann``: Neumann BC                                       |
|                                 |                    | | ``flux``: Fixed-flux BC                                       |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``sbctop``                      | *None*             | | Top boundary type for scalar variables. Types                 |
|                                 |                    | | can be specified per scalar (``stop[qt]=neumann``)            |
|                                 |                    | | ``dirchlet``: Dirichlet BC                                    |
|                                 |                    | | ``neumann``: Neumann BC                                       |
|                                 |                    | | ``flux``: Fixed-flux BC                                       |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``ubot``                        | ``0.``             | | Bottom boundary value for east-west velocity (m s-1)          |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``utop``                        | ``0.``             | | Top boundary value for east-west velocity (m s-1)             |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``vbot``                        | ``0.``             | | Bottom boundary value for north-south velocity (m s-1)        |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``vtop``                        | ``0.``             | | Bottom boundary value for north-south velocity (m s-1)        |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``sbot``                        | *None*             | | Bottom boundary value for scalar variables. Values            |
|                                 |                    | | can be specified per scalar (``sbot[thl]=300``)               |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``stop``                        | *None*             | | Top boundary value for scalar variables. Values               |
|                                 |                    | | can be specified per scalar (``stop[s]=4.``)                  |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``sbot_2d_list``                | *Empty list*       | | Comma-separate list of scalars that provide a binary          |
|                                 |                    | | file (``sbot_thl.0000000``) with 2D slice                     |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``z0m``                         | *None*             | Roughness length of momentum (m)                                |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``z0h``                         | *None*             | Roughness length of scalars (m)                                 |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``ustar``                       | *None*             | Value of the friction velocity (m s-1)                          |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``bulk_cm``                     | *None*             | Drag coefficient for momentum (-)                               |
+---------------------------------+--------------------+-----------------------------------------------------------------+
| ``bulk_cs``                     | *None*             | Drag coefficient for scalars (-)                                |
+---------------------------------+--------------------+-----------------------------------------------------------------+

----


Budget statistics ``[budget]``
------------------------------

The ``Budget`` class contains the computation of the statistics of the budgets of the second order moments.
It contains the entire Reynolds-stress tensor, the variances of the buoyancy variable, and the budget of the buoyancy flux.
The switch ``swbudget`` can only be set to ``4`` if ``[grid]`` has ``swspatialorder=4``.

+---------------------------------+--------------------+--------------------------------------------------------+
| Name                            | Default            | Description and options                                |
+=================================+====================+========================================================+
| ``swbudget``                    | ``0``              | | Switch for the budget statistics                     |
|                                 |                    | | ``2``: Budget statistics with second-order accuracy  |
|                                 |                    | | ``4``: Budget statistics with fourth-order accuracy  |
+---------------------------------+--------------------+--------------------------------------------------------+

----


Buffer layer ``[buffer]``
------------------------------

The ``Buffer`` class contains the implementation of the buffer layer in the top of the domain that prevents the reflection of gravity waves back into the domain.
The strength of the buffering is defined per layer as
:math:`\sigma ( (z - z_\textrm{start}) / ( z_\textrm{size} - z_\textrm{start}) )^\beta`.
A logical choice for ``sigma`` is :math:`(2 \pi) / N`, where :math:`N` is the Brunt-Vaisala frequency in the sponge layer.

+---------------------------------+--------------------+--------------------------------------------------------------------+
| Name                            | Default            | Description and options                                            |
+=================================+====================+====================================================================+
| ``swbuffer``                    | ``0``              | | Switch for buffer layer                                          |
|                                 |                    | | ``0``: Buffer layer disabled                                     |
|                                 |                    | | ``1``: Buffer layer enabled                                      |
+---------------------------------+--------------------+--------------------------------------------------------------------+
| ``swupdate``                    | ``0``              | | Switch whether to update the buffer with actual mean profiles    |
|                                 |                    | | ``0``: Updating disabled                                         |
|                                 |                    | | ``1``: Updating enabled                                          |
+---------------------------------+--------------------+--------------------------------------------------------------------+
| ``zstart``                      | *None*             | Height in domain at which the buffer layer starts (m)              |
+---------------------------------+--------------------+--------------------------------------------------------------------+
| ``sigma``                       | *None*             | Damping frequency of buffer layer (rad s-1)                        |
+---------------------------------+--------------------+--------------------------------------------------------------------+
| ``beta``                        | ``2.``             | Exponent of strength reduction function (-)                        |
+---------------------------------+--------------------+--------------------------------------------------------------------+

----


Cross sections ``[cross]``
--------------------------

The ``Cross`` class contains the settings for the cross sections.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``swcross``                     | ``0.``             | Switch for cross sections                       |
+---------------------------------+--------------------+-------------------------------------------------+
| ``sampletime``                  | *None*             | Time between consecutive samples (s)            |
+---------------------------------+--------------------+-------------------------------------------------+
| ``crosslist``                   | *None*             | List of cross sections to be made               |
+---------------------------------+--------------------+-------------------------------------------------+
| ``xy``                          | *None*             | List of z-levels for xy-cross sections          |
+---------------------------------+--------------------+-------------------------------------------------+
| ``xz``                          | *None*             | List of y-levels for xz-cross sections          |
+---------------------------------+--------------------+-------------------------------------------------+
| ``yz``                          | *None*             | List of x-levels for yz-cross sections          |
+---------------------------------+--------------------+-------------------------------------------------+

The table below shows an overview of potential cross sections and the class that provides them.
If a wildcard ``*`` is used, variables can be filled in according to the description.

+----------------------------+---------------------------------------------------------------------------------+
| Name                       | Description                                                                     |
+============================+=================================================================================+
| *Always available*                                                                                           |
+----------------------------+---------------------------------------------------------------------------------+
| ``*``                      | Any prognostic or diagnostic variable                                           |
+----------------------------+---------------------------------------------------------------------------------+
| ``*path``                  | Density-weighted vertical integral of any prognostic or diagnostic variable     |
+----------------------------+---------------------------------------------------------------------------------+
| ``*bot``                   | Bottom boundary value of any prognostic variable                                |
+----------------------------+---------------------------------------------------------------------------------+
| ``*top``                   | Top boundary value of any prognostic variable                                   |
+----------------------------+---------------------------------------------------------------------------------+
| ``*fluxbot``               | Bottom boundary flux of any prognostic variable                                 |
+----------------------------+---------------------------------------------------------------------------------+
| ``*fluxtop``               | Top boundary flux of any prognostic variable                                    |
+----------------------------+---------------------------------------------------------------------------------+
| ``*lngrad``                | Logarithm of the length of the gradient vector for any prognostic variable      |
+----------------------------+---------------------------------------------------------------------------------+
|                                                                                                              |
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[boundary]`` *has* ``swboundary=surface``                                                    |
+----------------------------+---------------------------------------------------------------------------------+
| ``ustar``                  | Friction velocity (m s-1)                                                       |
+----------------------------+---------------------------------------------------------------------------------+
| ``obuk``                   | Obukhov length (m)                                                              |
+----------------------------+---------------------------------------------------------------------------------+
|                                                                                                              |
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[ib]`` *has* ``swib=1``                                                                      |
+----------------------------+---------------------------------------------------------------------------------+
| ``*fluxbot_ib``            | Bottom boundary flux of any prognostic variable at DEM surface                  |
+----------------------------+---------------------------------------------------------------------------------+
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[microphys]`` *has* ``swmicrophys=nsw6`` or ``swmicrophys=warm_2mom``                        |
+----------------------------+---------------------------------------------------------------------------------+
| ``rr_bot``                 | Surface rain rate (kg s-1)                                                      |
+----------------------------+---------------------------------------------------------------------------------+
|                                                                                                              |
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[microphys]`` *has* ``swmicrophys=nsw6``                                                     |
+----------------------------+---------------------------------------------------------------------------------+
| ``rg_bot``                 | Surface graupel rate (kg s-1)                                                   |
+----------------------------+---------------------------------------------------------------------------------+
| ``rs_bot``                 | Surface snow rate (kg s-1)                                                      |
+----------------------------+---------------------------------------------------------------------------------+
|                                                                                                              |
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[radiation]`` *has* ``swradiation=rrtmgp``                                                   |
+----------------------------+---------------------------------------------------------------------------------+
| ``sw_flux_down``           | Downwelling flux for shortwave radiation (W m-2)                                |
+----------------------------+---------------------------------------------------------------------------------+
| ``sw_flux_up``             | Upwelling flux for shortwave radiation (W m-2)                                  |
+----------------------------+---------------------------------------------------------------------------------+
| ``lw_flux_down``           | Downwelling flux for longwave radiation (W m-2)                                 |
+----------------------------+---------------------------------------------------------------------------------+
| ``lw_flux_up``             | Upwelling flux for longwave radiation (W m-2)                                   |
+----------------------------+---------------------------------------------------------------------------------+
| ``sw_flux_down_clear``     | Downwelling clear-sky flux for shortwave radiation (W m-2)                      |
+----------------------------+---------------------------------------------------------------------------------+
| ``sw_flux_up_clear``       | Upwelling clear-sky flux for shortwave radiation (W m-2)                        |
+----------------------------+---------------------------------------------------------------------------------+
| ``lw_flux_down_clear``     | Downwelling clear-sky flux for longwave radiation (W m-2)                       |
+----------------------------+---------------------------------------------------------------------------------+
| ``lw_flux_up_clear``       | Upwelling clear-sky flux for longwave radiation (W m-2)                         |
+----------------------------+---------------------------------------------------------------------------------+
|                                                                                                              |
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[thermo]`` *has* ``swthermo=thermo_moist``                                                   |
+----------------------------+---------------------------------------------------------------------------------+
| ``ql``                     | Liquid water concentration (kg kg-1)                                            |
+----------------------------+---------------------------------------------------------------------------------+
| ``qi``                     | Ice concentration (kg kg-1)                                                     |
+----------------------------+---------------------------------------------------------------------------------+
| ``qlbase``                 | Cloud base height (m)                                                           |
+----------------------------+---------------------------------------------------------------------------------+
| ``qltop``                  | Cloud top height (m)                                                            |
+----------------------------+---------------------------------------------------------------------------------+
| ``qlpath``                 | Density-weighted vertical integral of liquid water concentration (kg m-2)       |
+----------------------------+---------------------------------------------------------------------------------+
| ``qipath``                 | Density-weighted vertical integral of ice concentration (kg m-2)                |
+----------------------------+---------------------------------------------------------------------------------+
| ``qsatpath``               | Density-weighted vertical integral of saturated specific humidity (kg m-2)      |
+----------------------------+---------------------------------------------------------------------------------+
| ``w500hpa``                | Vertical velocity at the 500 hPa level (m s-1)                                  |
+----------------------------+---------------------------------------------------------------------------------+

----


Diffusion ``[diff]``
--------------------

The ``Diff`` class computes the tendencies related to molecular, and in case of LES, of eddy diffusion.
If ``swdiff=smag2``, LES mode is enabled and the user can choose ``cs`` and/or ``tPr``.

+---------------------------------+--------------------+------------------------------------------------------------+
| Name                            | Default            | Description and options                                    |
+=================================+====================+============================================================+
| ``swdiff``                      | ``0``              | | Switch for diffusion type                                |
|                                 |                    | | ``0``: Disabled                                          |
|                                 |                    | | ``2``: 2nd-order                                         |
|                                 |                    | | ``4``: 4th-order                                         |
|                                 |                    | | ``smag2``: 2nd-order Smagorinsky for LES                 |
+---------------------------------+--------------------+------------------------------------------------------------+
| ``dnmax``                       | ``0.4``            | Max. diffusion number for adaptive time stepping           |
+---------------------------------+--------------------+------------------------------------------------------------+
| ``cs``                          | ``0.23``           | Smagorinsky constant                                       |
+---------------------------------+--------------------+------------------------------------------------------------+
| ``tPr``                         | ``1./3.``          | Turbulent Prandtl number                                   |
+---------------------------------+--------------------+------------------------------------------------------------+

----


Dump of 3D fields ``[dump]``
----------------------------

The ``Dump`` class contains the settings for 3D field dumps.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``swdump``                      | ``0.``             | Switch for 3D dumps                             |
|                                 |                    | | ``0``: Disabled                               |
|                                 |                    | | ``1``: Enabled                                |
+---------------------------------+--------------------+-------------------------------------------------+
| ``sampletime``                  | *None*             | Time between consecutive samples (s)            |
+---------------------------------+--------------------+-------------------------------------------------+
| ``dumplist``                    | *None*             | List of 3D dumps to be made                     |
+---------------------------------+--------------------+-------------------------------------------------+

The table below shows an overview of potential dump variables and the class that provides them.
If a wildcard ``*`` is used, variables can be filled in according to the description.

+----------------------------+---------------------------------------------------------------------------------+
| Name                       | Description                                                                     |
+============================+=================================================================================+
| *Always available*                                                                                           |
+----------------------------+---------------------------------------------------------------------------------+
| ``*``                      | Any prognostic or diagnostic variables                                          |
+----------------------------+---------------------------------------------------------------------------------+
|                                                                                                              |
+----------------------------+---------------------------------------------------------------------------------+
| *Availabe if* ``[thermo]`` *has* ``swthermo=thermo_moist``                                                   |
+----------------------------+---------------------------------------------------------------------------------+
| ``ql``                     | Liquid water concentration (kg kg-1)                                            |
+----------------------------+---------------------------------------------------------------------------------+
| ``qi``                     | Ice concentration (kg kg-1)                                                     |
+----------------------------+---------------------------------------------------------------------------------+
| ``T``                      | Absolute temperature (K)                                                        |
+----------------------------+---------------------------------------------------------------------------------+

----


Fields ``[fields]``
----------------------------

The ``Fields`` class initializes and contains the 3D fields that are passed around in the model.
This class generates passive scalars, which are prognostic variables that are not initialized by other classes.
It is also responsible for the generation of the random perturbation in the init.

+---------------------------------+--------------------+----------------------------------------------------------+
| Name                            | Default            | Description and options                                  |
+=================================+====================+==========================================================+
| ``slist``                       | *Empty list*       | List of passive scalars to be initialized                |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``visc``                        | *None*             | Kinematic viscosity (m2 s-1)                             |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``svisc``                       | *None*             | Diffusivity of scalars (m2 s-1)                          |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``rndseed``                     | ``0``              | Seed of random number generator (-)                      |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``rndamp``                      | ``0.``             | Amplitude of perturbations. Value can be specified per   |
|                                 |                    | prognostic variable, for instance ``rndamp[s] = 0.1``    |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``rndz``                        | ``0.``             | Height until which perturbations applied (m)             |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``rndexp``                      | ``0.``             | Decay of perturbation amplitude with height              |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``vortexnpair``                 | ``0.``             | Number of pairs of counter rotating vortices (-)         |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``vortexamp``                   | ``0.``             | Maximum vortex velocity (m s-1)                          |
+---------------------------------+--------------------+----------------------------------------------------------+
| ``vortexaxis``                  | ``y``              | | Orientation of axis vortices                           |
|                                 |                    | | ``x``: Rotation of vortices in xz-plane                |
|                                 |                    | | ``y``: Rotation of vortices in yz-plane                |
+---------------------------------+--------------------+----------------------------------------------------------+

----


Large-scale forcings ``[force]``
--------------------------------

The ``Force`` class provides the tendencies for all forms of large-scale forcings.

+---------------------------------+----------+--------------------------------------------------------------------------+
| Name                            | Default  | Description and options                                                  |
+=================================+==========+==========================================================================+
| ``swlspres``                    | ``0``    | | Switch for large-scale pressure force                                  |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``geo``: Geostrophic wind and rotation                                 |
|                                 |          | | ``dpdx``: Fixed pressure gradient in x                                 |
|                                 |          | | ``uflux``: Fixed volume flux through domain                            |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swtimedep_geo``               | ``0``    | | Time-dependent geostrophic wind (if ``swlspres=geo``)                  |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``fc``                          | *None*   | Coriolis parameter (s-1) (if ``swlspres=geo``)                           |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``dpdx``                        | *None*   | Fixed pressure gradient in x (Pa m-1) (if ``swlspres=dpdx``)             |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``uflux``                       | *None*   | Fixed volume-mean velocity (m s-1)                                       |
|                                 |          | (if ``swlspres=uflux``)                                                  |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swls``                        | ``0``    | | Switch for large-scale advective tendencies                            |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``lslist``                      | ``0``    | List of variables for which tendencies are given                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swtimedep_ls``                | ``0``    | | Time-dependent large-scale forcings (if ``swls=1``)                    |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``timedeplist_ls``              | *None*   | List of scalars with time-dependent large-scale                          |
|                                 |          | forcings specified                                                       |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swwls``                       | ``0``    | | Switch for large-scale vertical velocity                               |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swtimedep_wls``               | ``0``    | | Time-dependent large-scale vertical velocity (if ``swwls=1``)          |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swnudge``                     | ``0``    | | Switch for nudging                                                     |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``nudgelist``                   | ``0``    | List of variables to which nudging is applied                            |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``scalednudgelist``             | ``0``    | List of variables to which a nudging scale is applied                    |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``swtimedep_nudge``             | ``0``    | | Time-dependent nudging (if ``swnudge=1``)                              |
|                                 |          | | ``0``: Disabled                                                        |
|                                 |          | | ``1``: Enabled                                                         |
+---------------------------------+----------+--------------------------------------------------------------------------+
| ``timedeplist_nudge``           | *None*   | List of variables with time-dependent nudging                            |
+---------------------------------+----------+--------------------------------------------------------------------------+

----




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

----


Master ``[master]``
-------------------

The ``Master`` class contains the configuration settings for parallel runs.

+---------------------------------+--------------------+-------------------------------------------------+
| Name                            | Default            | Description and options                         |
+=================================+====================+=================================================+
| ``npx``                         | ``1``              | Numbers of processes in x (-)                   |
+---------------------------------+--------------------+-------------------------------------------------+
| ``npy``                         | ``1``              | Numbers of processes in y (-)                   |
+---------------------------------+--------------------+-------------------------------------------------+
| ``wallclocklimit``              | ``1.E8``           | Maximum run duration in wall clock time (h)     |
+---------------------------------+--------------------+-------------------------------------------------+

