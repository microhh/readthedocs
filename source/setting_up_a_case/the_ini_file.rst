The ``.ini`` file
=================
TODO DIFF FORCE  IB Limiter radiation source thermo 
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
Note that the odd ordered schemes (e.g. ``2i5``) have hyperdiffusion included that results in a smooth solution.
For ```2i62``, the interpolations are 6th order accurate in the horizontal, and 2nd order in the vertical.

Variables on the ``fluxlimit_list`` are guaranteed to be monotonically advected.

The order of the advection scheme has to match the order of the spatial discretization, as set by ``[grid] swspatialorder``.

For more details about the 2nd order accurate schemes, see: `<dx.doi.org/10.1175/1520-0493(2002)130%3C2088:TSMFEM%3E2.0.CO;2>`_.

+-------------+--------------------+-----------------------------------------------------+
| Name        | Default            | Description and options                             |
+=============+====================+=====================================================+
| ``swadvec`` | ``swspatialorder`` | | Advection scheme                                  |
|             |                    | | ``0``: Disabled                                   |
|             |                    | | ``2``: 2nd-order                                  |
|             |                    | | ``2i4``: 2nd-order (4th-order interpolation)      |
|             |                    | | ``2i4``: 2nd-order (4th-order interpolation)      |
|             |                    | | ``2i5``: 2nd-order (5th-order interpolation)      |
|             |                    | | ``2i62``: 2nd-order (6th/2nd-order interpolation) |
|             |                    | | ``4``: 4th-order (DNS, high accuracy)             |
|             |                    | | ``4m``: 2nd-order (DNS, energy conserving)        |
+-------------+--------------------+-----------------------------------------------------+
| ``fluxlimit_list``  | ````       | List of variables that are flux-limited             |
+-------------+--------------------+-----------------------------------------------------+
| ``cflmax``  | ``1.0``            | Max. CFL for adaptive time stepping                 |
+-------------+--------------------+-----------------------------------------------------+
TODO fluxlimit_list
----

Aerosol ``[aerosol]``
---------------------

+-----------------+--------------------+-----------------------------------------------------+
| Name            | Default            | Description and options                             |
+=================+====================+=====================================================+
| ``swaerosol``   | ``0``              | | Aerosol scheme                                    |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
| ``swtimedep``   | ``0``              | | Time-dependent aerosol                            |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+

----


Boundary conditions ``[boundary]``
----------------------------------

The ``Boundary`` class computes the boundary conditions.
It has a derived class ``Boundary_surface`` that extends the base class in case the surface model is enabled, and ``Boundary_surface_lsm`` which further extends ``Boundary_surface`` with an interactive land surface scheme (HTESSEL based).
Setting ``swboundary=surface`` requires ``z0m`` and ``z0h`` to be set.
Setting ``swboundary=surface_bulk`` requires ``bulk_cm`` and ``bulk_cs`` to be set.

+-----------------------+----------------+---------------------------------------------------------------------+
| Name                  | Default        | Description and options                                             |
+=======================+================+=====================================================================+
| ``swboundary``        | ``None``       | | Boundary discretization                                           |
|                       |                | | ``default``: resolved boundaries                                  |
|                       |                | | ``surface``: MOST-based surface model                             |
|                       |                | | ``surface_lsm``: MOST-based surface model with HTESSEL LSM        |
|                       |                | | ``surface_bulk``: Surface model with prescribed drag coefficients |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``mbcbot``            | ``None``       | | Bottom boundary type for momentum variables                       |
|                       |                | | ``no-slip``: Dirichlet BC with ``u = v = 0``                      |
|                       |                | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``                |
|                       |                | | ``ustar``: Fixed ustar at bottom                                  |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``mbctop``            | ``None``       | | Top boundary type for momentum variables                          |
|                       |                | | ``no-slip``: Dirichlet BC with ``u = v = 0``                      |
|                       |                | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``                |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``sbcbot``            | ``None``       | | Bottom boundary type for scalar variables.                        |
|                       |                | | Types can be specified per scalar (``sbot[thl]=flux``)            |
|                       |                | | ``dirichlet``: Dirichlet BC                                       |
|                       |                | | ``neumann``: Neumann BC                                           |
|                       |                | | ``flux``: Flux BC                                                 |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``sbctop``            | ``None``       | | Top boundary type for scalar variables.                           |
|                       |                | | Types can be specified per scalar (``stop[qt]=neumann``)          |
|                       |                | | ``dirichlet``: Dirichlet BC                                       |
|                       |                | | ``neumann``: Neumann BC                                           |
|                       |                | | ``flux``: Flux BC                                                 |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``ubot``              | ``0``          | Bottom boundary value for east-west velocity (m s-1)                |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``utop``              | ``0``          | Top boundary value for east-west velocity (m s-1)                   |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``vbot``              | ``0``          | Bottom boundary value for north-south velocity (m s-1)              |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``vtop``              | ``0``          | Top boundary value for north-south velocity (m s-1)                 |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``sbot``              | ``None``       | | Bottom boundary value for scalar variables                        |
|                       |                | | Values can be specified per scalar: ``sbot[thl]=0.1``.            |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``stop``              | ``None``       | | Top boundary value for scalar variables                           |
|                       |                | | Values can be specified per scalar: ``stop[qt]=0``.               |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``sbot_2d_list``      | ``Empty list`` | | Comma-separate list of scalars that provide a binary              |
|                       |                | | file (``sbot_thl.0000000``) with 2D slice                         |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``swtimedep_sbot_2d`` | ``0``          | Enable time varying 2D surface fields                               |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``sbot_2d_loadtime``  | ``None``       | Frequency of 2D surface input                                       |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``z0m``               | ``None``       | Roughness length of momentum (m)                                    |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``z0h``               | ``None``       | Roughness length of heat (m)                                        |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``ustar``             | ``None``       | Value of the fixed friction velocity (m s-1)                        |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``bulk_cm``           | ``None``       | Drag coefficient for momentum (-)                                   |
+-----------------------+----------------+---------------------------------------------------------------------+
| ``bulk_cs``           | ``None``       | Drag coefficient for scalar (-)                                     |
+-----------------------+----------------+---------------------------------------------------------------------+
TODO swtimedep swtimedep_outflow swconstantz0 swcharnock alpha_m alpha_ch alpha_h swhomogeneous swfreedrainage swwater swhomegenizesfsc swtilestats swtilestats_column emis_sfc flow_direction scalar_outflow
----


Budget statistics ``[budget]``
------------------------------

The ``Budget`` class contains the computation of the statistics of the budgets of the second order moments.
It contains the entire Reynolds-stress tensor, the variances of the buoyancy variable, and the budget of the buoyancy flux.
The switch ``swbudget`` can only be set to ``4`` if ``[grid]`` has ``swspatialorder=4``.

+--------------+---------+-------------------------------------------------------+
| Name         | Default | Description and options                               |
+==============+=========+=======================================================+
| ``swbudget`` | ``0``   | | Switch for the budget statistics                    |
|              |         | | ``2``: Budget statistics with second-order accuracy |
|              |         | | ``4``: Budget statistics with fourth-order accuracy |
+--------------+---------+-------------------------------------------------------+

----


Buffer layer ``[buffer]``
------------------------------

The ``Buffer`` class contains the implementation of the buffer layer in the top of the domain that prevents the reflection of gravity waves back into the domain.
The strength of the buffering is defined per layer as
:math:`\sigma ( (z - z_\textrm{start}) / ( z_\textrm{size} - z_\textrm{start}) )^\beta`.
A logical choice for ``sigma`` is :math:`(2 \pi) / N`, where :math:`N` is the Brunt-Vaisala frequency in the sponge layer.

+--------------+----------+-----------------------------------------------------------------+
| Name         | Default  | Description and options                                         |
+==============+==========+=================================================================+
| ``swbuffer`` | ``0``    | | Switch for the buffer layer                                   |
|              |          | | ``0``: Buffer layer disabled                                  |
|              |          | | ``1``: Buffer layer enabled                                   |
+--------------+----------+-----------------------------------------------------------------+
| ``swupdate`` | ``0``    | | Switch whether to update the buffer with actual mean profiles |
|              |          | | ``0``: Updating disabled                                      |
|              |          | | ``1``: Updating enabled                                       |
+--------------+----------+-----------------------------------------------------------------+
| ``zstart``   | ``None`` | Height in domain at which the buffer layer starts (m)           |
+--------------+----------+-----------------------------------------------------------------+
| ``sigma``    | ``None`` | Damping frequency of buffer layer (rad s-1)                     |
+--------------+----------+-----------------------------------------------------------------+
| ``beta``     | ``2``    | Exponent of strength reduction function (-)                     |
+--------------+----------+-----------------------------------------------------------------+

----

Column ``[column]``
---------------------
The ``Column`` class contains the settings for single column output.
+------------------+--------------------+-----------------------------------------------------+
| Name             | Default            | Description and options                             |
+==================+====================+=====================================================+
| ``swcolumn``     | ``0``              | | Column output                                     |
|                  |                    | | ``0``: Disabled                                   |
|                  |                    | | ``1``: Enabled                                    |
+------------------+--------------------+-----------------------------------------------------+
| ``sampletime``   | *None*             | Time between consecutive samples (s)                |
+------------------+--------------------+-----------------------------------------------------+
|``coordinates[x]``| *None*             | List of locations of the vertical columns (m)       |
|``coordinates[y]``|                    |                                                     |
+------------------+--------------------+-----------------------------------------------------+
| ``swtimedep``    | ``0``              | | Time-dependent aerosol                            |
|                  |                    | | ``0``: Disabled                                   |
|                  |                    | | ``1``: Enabled                                    |
+------------------+--------------------+-----------------------------------------------------+
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

Decay ``[decay]``
---------------------
Imposes an expontial decay on prognostic variables of choice. It also defines a statistical mask for areas where a decaying field is a certain number of standard deviations above the mean.
+-------------------+---------+----------------------------------------------------------------------------------+
|       Name        | Default |                             Description and options                              |
+===================+=========+==================================================================================+
| ``swdecay``       | ``0``   | Decay scheme                                                                     |
|                   |         | ``0``: Disabled                                                                  |
|                   |         | ``1``: Enabled                                                                   |
+-------------------+---------+----------------------------------------------------------------------------------+
| ``timescale``     | *None*  | Exponential timescale                                                            |
|                   |         | of the decay rate (s)                                                            |
|                   |         | ``1``: Enabled                                                                   |
+-------------------+---------+----------------------------------------------------------------------------------+
| ``nstd_couvreux`` | ``1``   | Number of standard deviations above the horizontal mean for conditional sampling |
+-------------------+---------+----------------------------------------------------------------------------------+
----


Diffusion ``[diff]``
--------------------

The ``Diff`` class computes the tendencies related to molecular, and in case of LES, of eddy diffusion.
If ``swdiff=smag2``, LES mode is enabled and the user can choose ``cs`` and/or ``tPr``.

The order of the diffusion scheme has to match the order of the spatial discretization, as set by ``[grid] swspatialorder``.

+---------------------------------+--------------------+------------------------------------------------------------+
| Name                            | Default            | Description and options                                    |
+=================================+====================+============================================================+
| ``swdiff``                      | ``0``              | | Switch for diffusion type                                |
|                                 |                    | | ``0``: Disabled                                          |
|                                 |                    | | ``2``: 2nd-order                                         |
|                                 |                    | | ``4``: 4th-order                                         |
|                                 |                    | | ``smag2``: 2nd-order Smagorinsky for LES                 |
|                                 |                    | | ``tke2``: 2th-order Deardorff for LES                    |
+---------------------------------+--------------------+------------------------------------------------------------+
| ``dnmax``                       | ``0.4``            | Max. diffusion number for adaptive time stepping           |
+---------------------------------+--------------------+------------------------------------------------------------+
| ``cs``                          | ``0.23``           | Smagorinsky constant                                       |
+---------------------------------+--------------------+------------------------------------------------------------+
| ``tPr``                         | ``1./3.``          | Turbulent Prandtl number                                   |
+---------------------------------+--------------------+------------------------------------------------------------+
TODO swmason, ap, cf ce1 ce2 cm ch1 ch2 cn
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
TODO swwls_mom
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
| ``lat``                         | ``0.``             | Latitude of the domain center (degrees)         |
+---------------------------------+--------------------+-------------------------------------------------+
| ``lon``                         | ``0.``             | Longitude of the domain center (degrees)        |
+---------------------------------+--------------------+-------------------------------------------------+
| ``utrans``                      | ``0.``             | Galilean translation velocity in x (m s-1)      |
+---------------------------------+--------------------+-------------------------------------------------+
| ``vtrans``                      | ``0.``             | Galilean translation velocity in y (m s-1)      |
+---------------------------------+--------------------+-------------------------------------------------+

----

Immersed boundary ``[ib]``
-------------------

+-----------------+--------------------+-----------------------------------------------------+
| Name            | Default            | Description and options                             |
+=================+====================+=====================================================+
| ``swaerosol``   | ``0``              | | Aerosol scheme                                    |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
| ``swtimedep``   | ``0``              | | Time-dependent aerosol                            |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
TODO sbot_spatial sbot sbcbot
----

Limiter ``[limiter]``
+-----------------+--------------------+-----------------------------------------------------+
| Name            | Default            | Description and options                             |
+=================+====================+=====================================================+
| ``swaerosol``   | ``0``              | | Aerosol scheme                                    |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
| ``swtimedep``   | ``0``              | | Time-dependent aerosol                            |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
TODO limitlist

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

----
Microphysics ``[micro]``
---------------------

+-------------+---------+-----------------------------------------------------+
|    Name     | Default |               Description and options               |
+=============+=========+=====================================================+
| ``swmicro`` | ``0``   | Microphysics scheme                                 |
|             |         | ``0``: Disabled                                     |
|             |         | ``2mom_warm``: Use 2 moment warm Seifert and Beheng |
|             |         | ``nsw6``: Use Tomita Ice microphyics                |
+-------------+---------+-----------------------------------------------------+
| ``Nc0``     | *None*  | The cloud droplet number concentration (m-3)        |
+-------------+---------+-----------------------------------------------------+
| ``cflmax``  | ``2``   | The CFL criterion limiter for the sedimentation     |
+-------------+---------+-----------------------------------------------------+

----


Pressure ``[pres]``
---------------------

+----------------------+---------+------------------------------------------+
|         Name         | Default |         Description and options          |
+======================+=========+==========================================+
| ``swpres``           | ``0``   | Pressure force                           |
|                      |         | ``0``: Disabled                          |
|                      |         | ``1``: Enabled                           |
+----------------------+---------+------------------------------------------+
| ``sw_fft_per_slice`` | ``0``   | Do not allow the FFT to be handled in 3D |
|                      |         | ``0``: Disabled                          |
|                      |         | ``1``: Enabled                           |
+----------------------+---------+------------------------------------------+
----

Radiation ``[radiation]``
---------------------

+-----------------+--------------------+-----------------------------------------------------+
| Name            | Default            | Description and options                             |
+=================+====================+=====================================================+
| ``swaerosol``   | ``0``              | | Aerosol scheme                                    |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
| ``swtimedep``   | ``0``              | | Time-dependent aerosol                            |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
TODO
swradiation
radiation_gcss: xka, fr0, fr1, div
radiation_prescribed: swtimedep_prescribed, lw/sw_flux_dn/up
radiation_rrrtmgp and _rt:swshort/longwave, swfixedsza, swupdatecolumn, swdeltacloud, swdeltaaer, swalawysrt, swclearskystats, swhomogenizesfc_sw/lw, swhomogenizehr_sw/lw, dt_rad, t_sfc, tsi_scaling, emis_sfcm sfc_alb_dir, sfc_alb_dif timedeplist_bg
radiation_rrtmgp alone: swfilterdiffuse, sigma_filter
radiation_rrtmgp_rt alone: rays_per_pixel, kngrid_i/j/k, sza


----


Source ``[source]``
---------------------

+-----------------+--------------------+-----------------------------------------------------+
| Name            | Default            | Description and options                             |
+=================+====================+=====================================================+
| ``swsource``    | ``0``              | | Aerosol scheme                                    |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
| ``swtimedep``   | ``0``              | | Time-dependent aerosol                            |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
TODO swtimedep_location _strength, sw_profile, sourcelist, source x/y/z0, sigma_x/y/z strength line_x/y/z swvmr profile_index
----

Statistics ``[stats]``
---------------------
The statistics class contains the settings for the statistics output, in particular the time series and the profiles. All statistics can be masked, meaning that only grid points that satisfy a certain condition are included in the statistics.
The statistics over the entire domain are written out in a file named ``<casename>.default.<restarttime>.nc``. Conditional statistics are written out in files named ``<casename>.<maskname>.<restarttime>.nc``.
+----------------+---------+-------------------------------------------------------------------------------------------------+
|      Name      | Default |                                     Description and options                                     |
+================+=========+=================================================================================================+
| ``swstats``    | ``0``   | Enable/Disable the statistics                                                                   |
|                |         | ``0``: Disabled                                                                                 |
|                |         | ``1``: Enabled                                                                                  |
+----------------+---------+-------------------------------------------------------------------------------------------------+
| ``sampletime`` | *None*  | Time between two samples (s)                                                                    |
+----------------+---------+-------------------------------------------------------------------------------------------------+
| ``swtendency`` | ``0``   | Enable/Disable budget terms of all prognostic variables                                         |
|                |         | ``0``: Disabled                                                                                 |
|                |         | ``1``: Enabled                                                                                  |
+----------------+---------+-------------------------------------------------------------------------------------------------+
| ``blacklist``  | *None*  | List of variables that should not be included in the statistics                                 |
|                |         | Can be a regular expression                                                                     |
+----------------+---------+-------------------------------------------------------------------------------------------------+
| ``whitelist``  | *None*  | List of variables that should be included in the statistics                                     |
|                |         | Can be a regular expression                                                                     |
+----------------+---------+-------------------------------------------------------------------------------------------------+
| ``masklist``   | *None*  | List of masks that should be applied to the statistics                                          |
|                |         | ``ql``: Where ``ql>0``                                                                          |
|                |         | ``bplus``: Where buoyancy ``bu>0``                                                              |
|                |         | ``bmin``: Where buoyancy``bu<0``                                                                |
|                |         | ``qlcore``: Where ``ql>0`` and ``bu>0``                                                         |
|                |         | ``qr`` : (2mom microphyics) Where ``qr>1e-6``                                                   |
|                |         | ``wplus``: Where ``w>0``                                                                        |
|                |         | ``wmin``: Where ``w<0``                                                                         |
|                |         | ``couvreux``: Where the couvreux scalar is `nstd` standard deviations above the horizontal mean |
|                |         | ``ib``:????                                                                                     |
+----------------+---------+-------------------------------------------------------------------------------------------------+
| ``xymasklist`` | *None*  | ????                                                                                            |
+----------------+---------+-------------------------------------------------------------------------------------------------+





----


Thermodynamics ``[thermo]``
---------------------

+-----------------+--------------------+-----------------------------------------------------+
| Name            | Default            | Description and options                             |
+=================+====================+=====================================================+
| ``swaerosol``   | ``0``              | | Aerosol scheme                                    |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+
| ``swtimedep``   | ``0``              | | Time-dependent aerosol                            |
|                 |                    | | ``0``: Disabled                                   |
|                 |                    | | ``1``: Enabled                                    |
+-----------------+--------------------+-----------------------------------------------------+

Thermo_buoy: Alpha, N2, swbaroclinic, dbdy_ls
Thermo_dry: swbasestate, swbaroclinic, dthetady_ls, swtimedep_pbot pbot, thref0
Thermo_moist: swbasestate, swupdatebasestat,  swtimedep_pbot pbot, thref0

----


Timeloop ``[time]``
---------------------

+------------------+------------+---------------------------------------------------------------------------------+
|       Name       |  Default   |                             Description and options                             |
+==================+============+=================================================================================+
| ``starttime``    | *None*     | Start time of the simulation (s)                                                |
+------------------+------------+---------------------------------------------------------------------------------+
| ``endtime``      | *None*     | End time of the simulation (s)                                                  |
+------------------+------------+---------------------------------------------------------------------------------+
| ``savetime``     | *None      | Interval at which a restart file will be saved (s)                              |
+------------------+------------+---------------------------------------------------------------------------------+
| ``adaptivestep`` | ``1``      | Adaptive time stepping, based on CFL, Diffusion Number, and other limitations   |
|                  |            | ``0``: Disabled                                                                 |
|                  |            | ``1``: Enabled                                                                  |
+------------------+------------+---------------------------------------------------------------------------------+
| ``dtmax``        | ``\infty`` | Maximum time step (s)                                                           |
+------------------+------------+---------------------------------------------------------------------------------+
| ``dt``           | ``dtmax``  | Initial time step (s)                                                           |
+------------------+------------+---------------------------------------------------------------------------------+
| ``rkorder``      | ``3``      | Order of the Runge-Kutta scheme                                                 |
|                  |            | ``3``: Third Order                                                              |
|                  |            | ``4``: Fourth Order                                                             |
+------------------+------------+---------------------------------------------------------------------------------+
| ``outputiter``   | ``20``     | Number of iterations between diagnostic output is written to ``<casename>.out`` |
+------------------+------------+---------------------------------------------------------------------------------+
| ``iotimeprec``   | ``0``      | Precision of the file timestamp, in ``10**iotimeprec`` s                        |
+------------------+------------+---------------------------------------------------------------------------------+
| ``datetime_utc`` | ``0``      | Calendar start time of the simulation. Must be of the format YY-MM-DD HH:MM::SS |
+------------------+------------+---------------------------------------------------------------------------------+
| ``postrpoctime`` | ``0``      | Timestamp to use in postprocessing mode                                         |
+------------------+------------+---------------------------------------------------------------------------------+


