The ``.ini`` file
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


TODO DIFF FORCE  IB Limiter radiation source thermo 

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

+--------------------+--------------------+--------------------------------------------------------+
| Name               | Default            | Description and options                                |
+====================+====================+========================================================+
| ``swadvec``        | ``swspatialorder`` | | Advection scheme                                     |
|                    |                    | | ``0``: Disabled                                      |
|                    |                    | | ``2``: 2nd-order                                     |
|                    |                    | | ``2i4``: 2nd-order with 4th-order interpolations     |
|                    |                    | | ``2i5``: 2nd-order with 5th-order interpolations     |
|                    |                    | | ``2i62``: 2nd-order with 6th/2nd-order interpolation |
|                    |                    | | ``4``: 4th-order (DNS, high accuracy)                |
|                    |                    | | ``4m``: 2nd-order (DNS, energy conserving)           |
+--------------------+--------------------+--------------------------------------------------------+
| ``cflmax``         | ``1.0``            | Max. CFL for adaptive time stepping                    |
+--------------------+--------------------+--------------------------------------------------------+
| ``fluxlimit_list`` | ``Empty list``     | Use flux limiter for scalars (2i5 and 2i62 only)       |
+--------------------+--------------------+--------------------------------------------------------+

----

Aerosol ``[aerosol]``
---------------------

Description: TO-DO Mirjam.

+-----------------------+---------------+--------------------------------------------+
| Name                  | Default       | Description and options                    |
+=======================+===============+============================================+
| ``swaerosol``         | ``false``     | Switch for aerosols in radiation           |
+-----------------------+---------------+--------------------------------------------+
| ``swtimedep``         | ``false``     | Switch for time dependent aerosols         |
+-----------------------+---------------+--------------------------------------------+
| ``tdep_aermr{01-11}`` | ``swtimedep`` | Aerosol individual time depenence switches |
+-----------------------+---------------+--------------------------------------------+

----

Boundary conditions ``[boundary]``
----------------------------------

The ``Boundary`` class computes the boundary conditions.
It has a derived class ``Boundary_surface`` that extends the base class in case the surface model is enabled, and ``Boundary_surface_lsm`` which further extends ``Boundary_surface`` with an interactive land surface scheme (HTESSEL based).

+-----------------------+----------------+-------------------------------------------------------------------------+
| Name                  | Default        | Description and options                                                 |
+=======================+================+=========================================================================+
| ``swboundary``        | ``None``       | | Boundary discretization                                               |
|                       |                | | ``default``: Resolved boundaries                                      |
|                       |                | | ``surface``: MOST-based surface model                                 |
|                       |                | | ``surface_lsm``: MOST-based surface model with HTESSEL LSM            |
|                       |                | | ``surface_bulk``: Surface model with prescribed drag coefficients     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``mbcbot``            | ``None``       | | Bottom boundary type for momentum variables                           |
|                       |                | | ``no-slip``: Dirichlet BC with ``u = v = 0``                          |
|                       |                | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``                    |
|                       |                | | ``ustar``: Fixed ustar at bottom                                      |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``mbctop``            | ``None``       | | Top boundary type for momentum variables                              |
|                       |                | | ``no-slip``: Dirichlet BC with ``u = v = 0``                          |
|                       |                | | ``free-slip``: Neumann BC with ``dudz = dvdz = 0``                    |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``sbcbot``            | ``None``       | | Bottom boundary type for scalar variables.                            |
|                       |                | | Types can be specified per scalar (``sbot[thl]=flux``)                |
|                       |                | | ``dirichlet``: Dirichlet BC                                           |
|                       |                | | ``neumann``: Neumann BC                                               |
|                       |                | | ``flux``: Flux BC                                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``sbctop``            | ``None``       | | Top boundary type for scalar variables.                               |
|                       |                | | Types can be specified per scalar (``stop[qt]=neumann``)              |
|                       |                | | ``dirichlet``: Dirichlet BC                                           |
|                       |                | | ``neumann``: Neumann BC                                               |
|                       |                | | ``flux``: Flux BC                                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``ubot``              | ``0``          | Bottom boundary value for east-west velocity (m s-1)                    |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``utop``              | ``0``          | Top boundary value for east-west velocity (m s-1)                       |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``vbot``              | ``0``          | Bottom boundary value for north-south velocity (m s-1)                  |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``vtop``              | ``0``          | Top boundary value for north-south velocity (m s-1)                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``sbot``              | ``None``       | | Bottom boundary value for scalar variables                            |
|                       |                | | Values can be specified per scalar: ``sbot[thl]=0.1``.                |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``stop``              | ``None``       | | Top boundary value for scalar variables                               |
|                       |                | | Values can be specified per scalar: ``stop[qt]=0``.                   |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``sbot_2d_list``      | ``Empty list`` | | Comma-separate list of scalars that provide a binary                  |
|                       |                | | file (``sbot_thl_in.0000000``) with 2D slice                          |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``z0m``               | ``None``       | Roughness length of momentum (m)                                        |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``z0h``               | ``None``       | Roughness length of heat (m)                                            |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``swconstantz0``      | ``true``       | | Switch for spatially homogeneous z0m/z0h                              |
|                       |                | | ``true``: Homogeneous z0m/z0h, from ``.ini`` file                     |
|                       |                | | ``false``: Heterogeneous z0m/z0h from ``z0m.0000000``/``z0h.0000000`` |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``swcharnock``        | ``false``      | Switch for Charnock parameterization (``boundary_surface`` only)        |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``alpha_m``           | ``None``       | Parameter Charnock parameterization                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``alpha_ch``          | ``None``       | Parameter Charnock parameterization                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``alpha_h``           | ``None``       | Parameter Charnock parameterization                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``ustar``             | ``None``       | Value of the fixed friction velocity (m s-1)                            |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``bulk_cm``           | ``None``       | Drag coefficient for momentum (-)                                       |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``bulk_cs``           | ``None``       | Drag coefficient for scalar (-)                                         |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``swtimedep``         | ``false``      | Switch for time varying surface BCs                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``timedeplist``       | ``Empty list`` | List of scalars with time varying BCs                                   |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``swtimedep_sbot_2d`` | ``false``      | Switch for time varying 2D surface BCs                                  |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``sbot_2d_loadtime``  | ``None``       | Frequency of 2D surface BC input                                        |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``scalar_outflow``    | ``Empty list`` | List of scalars with non-periodic lateral BCs                           |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``flow_direction``    | ``None``       | | Flow direction used for ``scalar_outflow`` at each lateral edge       |
|                       |                | | ``inflow``: Inflow (Dirichlet BC)                                     |
|                       |                | | ``outflow``: Outflow (Neumann BC)                                     |
+-----------------------+----------------+-------------------------------------------------------------------------+
| ``swtimedep_outflow`` | ``false``      | Switch for time varying scalar outflow                                  |
+-----------------------+----------------+-------------------------------------------------------------------------+

For ``swboundary=surface_lsm``, the ``[land_surface]`` group contains some additional settings:

+------------------------+-----------+---------------------------------------------------+
| Name                   | Default   | Description and options                           |
+========================+===========+===================================================+
| ``swhomogeneous``      | ``true``  | Use spatially homogeneous land-surface properties |
+------------------------+-----------+---------------------------------------------------+
| ``swfreedrainage``     | ``true``  | Free drainage BC at bottom of soil column         |
+------------------------+-----------+---------------------------------------------------+
| ``swwater``            | ``false`` | Switch for allowing open water                    |
+------------------------+-----------+---------------------------------------------------+
| ``swtilestats``        | ``false`` | Output individual tile statistics                 |
+------------------------+-----------+---------------------------------------------------+
| ``swtilestats_column`` | ``false`` | Output individual tile column statistics          |
+------------------------+-----------+---------------------------------------------------+
| ``emis_sfc``           | ``None``  | Surface emissivity                                |
+------------------------+-----------+---------------------------------------------------+

For ``swhomogeneous=true``, the following surface and vegetation properties need to be specified in the ``[land_surface]`` group:

+---------------------+----------+-------------------------------------------------------+
| Name                | Default  | Description and options                               |
+=====================+==========+=======================================================+
| ``gD``              | ``None`` | gD coefficient in VDP reduction canopy resistance (?) |
+---------------------+----------+-------------------------------------------------------+
| ``c_veg``           | ``None`` | Sub-grid vegetation fraction (0-1)                    |
+---------------------+----------+-------------------------------------------------------+
| ``lai``             | ``None`` | Leaf area index (m2 m-2)                              |
+---------------------+----------+-------------------------------------------------------+
| ``rs_veg_min``      | ``None`` | Minium canopy resistance (s m-1)                      |
+---------------------+----------+-------------------------------------------------------+
| ``rs_soil_min``     | ``None`` | Minium soil resistance (s m-1)                        |
+---------------------+----------+-------------------------------------------------------+
| ``lambda_stable``   | ``None`` | Skin conductivity stable conditions (W m-2 K-1)       |
+---------------------+----------+-------------------------------------------------------+
| ``lambda_unstable`` | ``None`` | Skin conductivity unstable conditions (W m-2 K-1)     |
+---------------------+----------+-------------------------------------------------------+
| ``cs_veg``          | ``None`` | Heat capacity skin layer (J K-1)                      |
+---------------------+----------+-------------------------------------------------------+

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
-------------------------

The ``Buffer`` class contains the implementation of the buffer layer in the top of the domain that prevents the reflection of gravity waves back into the domain.
The strength of the buffering is defined per layer as
:math:`\sigma ( (z - z_\textrm{start}) / ( z_\textrm{size} - z_\textrm{start}) )^\beta`.
A logical choice for ``sigma`` is :math:`(2 \pi) / N`, where :math:`N` is the Brunt-Vaisala frequency in the sponge layer.

+--------------+-----------+---------------------------------------------------------------+
| Name         | Default   | Description and options                                       |
+==============+===========+===============================================================+
| ``swbuffer`` | ``false`` | Switch for the buffer layer                                   |
+--------------+-----------+---------------------------------------------------------------+
| ``swupdate`` | ``false`` | Switch whether to update the buffer with actual mean profiles |
+--------------+-----------+---------------------------------------------------------------+
| ``zstart``   | ``None``  | Height in domain at which the buffer layer starts (m)         |
+--------------+-----------+---------------------------------------------------------------+
| ``sigma``    | ``None``  | Damping frequency of buffer layer (rad s-1)                   |
+--------------+-----------+---------------------------------------------------------------+
| ``beta``     | ``2``     | Exponent of strength reduction function (-)                   |
+--------------+-----------+---------------------------------------------------------------+

----

Column ``[column]``
-------------------

The ``Column`` class contains the settings for single column output.

+--------------------+----------------+--------------------------------------+
| Name               | Default        | Description and options              |
+====================+================+======================================+
| ``swcolumn``       | ``false``      | Switch for column statistics         |
+--------------------+----------------+--------------------------------------+
| ``sampletime``     | ``None``       | Time between consecutive samples (s) |
+--------------------+----------------+--------------------------------------+
| ``coordinates[x]`` | ``Empty list`` | List with x-coordinates column (m)   |
+--------------------+----------------+--------------------------------------+
| ``coordinates[y]`` | ``Empty list`` | List with y-coordinates column (m)   |
+--------------------+----------------+--------------------------------------+

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

Always available: 

+---------------+-----------------------------------------------------------------------------+
| Name          | Description and options                                                     |
+===============+=============================================================================+
| ``*_path``    | Density-weighted vertical integral of any prognostic or diagnostic variable |
+---------------+-----------------------------------------------------------------------------+
| ``*_bot``     | Bottom boundary value of any prognostic variable                            |
+---------------+-----------------------------------------------------------------------------+
| ``*_top``     | Top boundary value of any prognostic variable                               |
+---------------+-----------------------------------------------------------------------------+
| ``*_fluxbot`` | Bottom boundary flux of any prognostic variable                             |
+---------------+-----------------------------------------------------------------------------+
| ``*_fluxtop`` | Top boundary flux of any prognostic variable                                |
+---------------+-----------------------------------------------------------------------------+
| ``*_lngrad``  | Logarithm of the length of the gradient vector for any prognostic variable  |
+---------------+-----------------------------------------------------------------------------+

Available if ``swboundary`` != ``default``:

+-----------+---------------------------+
| Name      | Description and options   |
+===========+===========================+
| ``ustar`` | Friction velocity (m s-1) |
+-----------+---------------------------+
| ``obuk``  | Obukhov length (m)        |
+-----------+---------------------------+

Availabe if ``[ib]`` has ``swib=1``:

+------------------+----------------------------------------------------------------+
| Name             | Description and options                                        |
+==================+================================================================+
| ``*_fluxbot_ib`` | Bottom boundary flux of any prognostic variable at DEM surface |
+------------------+----------------------------------------------------------------+

Availabe if ``swmicro`` in (``nsw6``, ``2mom_warm``):

+------------+-----------------------------+
| Name       | Description and options     |
+============+=============================+
| ``rr_bot`` | Surface rain rate (kg s-1)  |
+------------+-----------------------------+

Availabe if ``swmicro==nsw6``:

+------------+--------------------------------+
| Name       | Description and options        |
+============+================================+
| ``rg_bot`` | Surface graupel rate (kg s-1)  |
+------------+--------------------------------+
| ``rs_bot`` | Surface snow rate (kg s-1)     |
+------------+--------------------------------+

Availabe if ``swradiation`` in (``rrtmgp``, ``rrtmgp_rt``): 

+--------------------+-----------------------------------------------------+
| Name               | Description and options                             |
+====================+=====================================================+
| ``sw_flux_dn``     | Downwelling shortwave radiation flux (W m-2)        |
+--------------------+-----------------------------------------------------+
| ``sw_flux_up``     | Upwelling shortwave radiation flux (W m-2)          |
+--------------------+-----------------------------------------------------+
| ``sw_flux_dn_dir`` | Downwelling direct shortwave radiation flux (W m-2) |
+--------------------+-----------------------------------------------------+
| ``lw_flux_dn``     | Downwelling longwave radiation flux (W m-2)         |
+--------------------+-----------------------------------------------------+
| ``lw_flux_up``     | Upwelling longwave radiation flux (W m-2)           |
+--------------------+-----------------------------------------------------+

Available if ``swradiation == rrtmgp_rt``:

+------------------------+---------------------------------------------------------------+
| Name                   | Description and options                                       |
+========================+===============================================================+
| ``sw_flux_sfc_dir_rt`` | Surface downwellling direct shortwave radiation flux (W m-2)  |
+------------------------+---------------------------------------------------------------+
| ``sw_flux_sfc_dif_rt`` | Surface downwellling diffuse shortwave radiation flux (W m-2) |
+------------------------+---------------------------------------------------------------+
| ``sw_flux_sfc_up_rt``  | Surface upwelling shortwave radiation flux (W m-2)            |
+------------------------+---------------------------------------------------------------+
| ``sw_flux_tod_dn_rt``  | Top of domain downwellling shortwave radiation flux (W m-2)   |
+------------------------+---------------------------------------------------------------+
| ``sw_flux_tod_up_rt``  | Top of domain upwelling shortwave radiation flux (W m-2)      |
+------------------------+---------------------------------------------------------------+

Available if ``swradiation`` in (``rrtmgp``, ``rrtmgp_rt``) and ``swclearskystats=true``:

+--------------------------+---------------------------------------------------------------+
| Name                     | Description and options                                       |
+==========================+===============================================================+
| ``sw_flux_dn_clear``     | Clear-sky downwelling shortwave radiation flux (W m-2)        |
+--------------------------+---------------------------------------------------------------+
| ``sw_flux_up_clear``     | Clear-sky upwelling shortwave radiation flux (W m-2)          |
+--------------------------+---------------------------------------------------------------+
| ``sw_flux_dn_dir_clear`` | Clear-sky downwelling direct shortwave radiation flux (W m-2) |
+--------------------------+---------------------------------------------------------------+
| ``lw_flux_dn_clear``     | Clear-sky downwelling longwave radiation flux (W m-2)         |
+--------------------------+---------------------------------------------------------------+
| ``lw_flux_up_clear``     | Clear-sky upwelling longwave radiation flux (W m-2)           |
+--------------------------+---------------------------------------------------------------+

Availabe if ``swthermo == thermo_moist``:

+---------------+----------------------------------------------------------------------------+
| Name          | Description and options                                                    |
+===============+============================================================================+
| ``ql``        | Cloud liquid water (kg kg-1)                                               |
+---------------+----------------------------------------------------------------------------+
| ``qi``        | Cloud ice (kg kg-1)                                                        |
+---------------+----------------------------------------------------------------------------+
| ``qlqi``      | Cloud liquid water + ice (kg kg-1)                                         |
+---------------+----------------------------------------------------------------------------+
| ``ql_base``   | Cloud base height (m)                                                      |
+---------------+----------------------------------------------------------------------------+
| ``ql_top``    | Cloud top height (m)                                                       |
+---------------+----------------------------------------------------------------------------+
| ``ql_path``   | Density-weighted vertical integral of cloud liquid water (kg m-2)          |
+---------------+----------------------------------------------------------------------------+
| ``qi_path``   | Density-weighted vertical integral of cloud ice (kg m-2)                   |
+---------------+----------------------------------------------------------------------------+
| ``qlqi_base`` | Cloud (water+ice) base height (m)                                          |
+---------------+----------------------------------------------------------------------------+
| ``qlqi_top``  | Cloud (water+ice) top height (m)                                           |
+---------------+----------------------------------------------------------------------------+
| ``qlqi_path`` | Density-weighted vertical integral of cloud water+ice (kg m-2)             |
+---------------+----------------------------------------------------------------------------+
| ``qsat_path`` | Density-weighted vertical integral of saturated specific humidity (kg m-2) |
+---------------+----------------------------------------------------------------------------+
| ``w500hpa``   | Vertical velocity at the 500 hPa level (m s-1)                             |
+---------------+----------------------------------------------------------------------------+

----

Decay ``[decay]``
-----------------

Imposes an expontial decay on prognostic variables of choice. It also defines a statistical mask for areas where a decaying field is a certain number of standard deviations above the mean.

+-------------------+----------+----------------------------------------------------------------------------------+
| Name              | Default  | Description and options                                                          |
+===================+==========+==================================================================================+
| ``swdecay``       | ``0``    | | Decay type:                                                                    |
|                   |          | | ``0``: No decay                                                                |
|                   |          | | ``exponential``: Exponential decay                                             |
|                   |          | | Set per scalar, e.g. ``decay[s1]=0``, ``decay[s2]=exponential``                |
+-------------------+----------+----------------------------------------------------------------------------------+
| ``timescale``     | ``None`` | Exponential decay rate (s)                                                       |
+-------------------+----------+----------------------------------------------------------------------------------+
| ``nstd_couvreux`` | ``1``    | Number of standard deviations above the horizontal mean for conditional sampling |
+-------------------+----------+----------------------------------------------------------------------------------+

----


Diffusion ``[diff]``
--------------------

The ``Diff`` class computes the tendencies related to molecular, and in case of LES, of eddy diffusion. The order of the diffusion scheme has to match the order of the spatial discretization, as set by ``[grid] swspatialorder``.

+------------+---------+----------------------------------------------------+
| Name       | Default | Description and options                            |
+============+=========+====================================================+
| ``swdiff`` | ``0``   | | Switch for diffusion type                        |
|            |         | | ``0``: Disabled                                  |
|            |         | | ``2``: 2nd-order DNS                             |
|            |         | | ``4``: 4th-order DNS                             |
|            |         | | ``smag2``: 2nd-order Smagorinsky for LES         |
|            |         | | ``tke2``: 2nd-order Deardorff TKE scheme for LES |
+------------+---------+----------------------------------------------------+
| ``dnmax``  | ``0.4`` | Max. diffusion number for adaptive time stepping   |
+------------+---------+----------------------------------------------------+

For ``swdiff=smag2``, the following settings are available:

+-------------+----------+-------------------------------+
| Name        | Default  | Description and options       |
+=============+==========+===============================+
| ``cs``      | ``0.23`` | Smagorinsky constant          |
+-------------+----------+-------------------------------+
| ``tPr``     | ``1/3``  | Turbulent Prandtl number      |
+-------------+----------+-------------------------------+
| ``swmason`` | ``true`` | Switch for Mason wall damping |
+-------------+----------+-------------------------------+

For ``swdiff=tke2``, the following settings are available:

+-------------+----------+-------------------------------+
| Name        | Default  | Description and options       |
+=============+==========+===============================+
| ``ap``      | ``0.4``  | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``cf``      | ``2.5``  | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``ce1``     | ``0.19`` | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``ce2``     | ``0.51`` | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``cm``      | ``0.12`` | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``ch1``     | ``1``    | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``ch2``     | ``2``    | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``cn``      | ``0.76`` | Contant TKE scheme (TO-DO)    |
+-------------+----------+-------------------------------+
| ``swmason`` | ``true`` | Switch for Mason wall damping |
+-------------+----------+-------------------------------+

----


Dump of 3D fields ``[dump]``
----------------------------

The ``Dump`` class contains the settings for 3D field dumps.

+------------------+----------------+-----------------------------------------------------+
| Name             | Default        | Description and options                             |
+==================+================+=====================================================+
| ``swdump``       | ``false``      | Switch for 3D field dumps                           |
+------------------+----------------+-----------------------------------------------------+
| ``swdoubledump`` | ``false``      | Switch for dump at two consecutive model iterations |
+------------------+----------------+-----------------------------------------------------+
| ``sampletime``   | ``None``       | Time between consecutive samples (s)                |
+------------------+----------------+-----------------------------------------------------+
| ``dumplist``     | ``Empty list`` | List of 3D dumps to be made                         |
+------------------+----------------+-----------------------------------------------------+

``dumplist`` can contain any prognostic or diagnostic field. In addition, ``swthermo=thermo_moist`` can provide:

+--------+------------------------------+
| Name   | Description and options      |
+========+==============================+
| ``ql`` | Cloud liquid water (kg kg-1) |
+--------+------------------------------+
| ``qi`` | Cloud ice (kg kg-1)          |
+--------+------------------------------+
| ``T``  | Absolute temperature (K)     |
+--------+------------------------------+

----


Fields ``[fields]``
-------------------

The ``Fields`` class initializes and contains the 3D fields that are passed around in the model.
This class generates passive scalars, which are prognostic variables that are not initialized by other classes.
It is also responsible for the generation of the random perturbation in the init.

+-----------------+----------------+----------------------------------------------------------+
| Name            | Default        | Description and options                                  |
+=================+================+==========================================================+
| ``slist``       | ``Empty list`` | List of passive scalars to be initialized                |
+-----------------+----------------+----------------------------------------------------------+
| ``visc``        | ``None``       | Kinematic viscosity (m2 s-1)                             |
+-----------------+----------------+----------------------------------------------------------+
| ``svisc``       | ``None``       | Diffusivity of scalars (m2 s-1)                          |
+-----------------+----------------+----------------------------------------------------------+
| ``rndseed``     | ``0``          | Seed of random number generator (-)                      |
+-----------------+----------------+----------------------------------------------------------+
| ``rndamp``      | ``0``          | | Amplitude of perturbations. Value can be specified per |
|                 |                | | prognostic variable, for instance ``rndamp[s] = 0.1``  |
+-----------------+----------------+----------------------------------------------------------+
| ``rndz``        | ``0``          | Height until which perturbations applied (m)             |
+-----------------+----------------+----------------------------------------------------------+
| ``rndexp``      | ``0``          | Decay of perturbation amplitude with height              |
+-----------------+----------------+----------------------------------------------------------+
| ``vortexnpair`` | ``0``          | Number of pairs of counter rotating vortices (-)         |
+-----------------+----------------+----------------------------------------------------------+
| ``vortexamp``   | ``0``          | Maximum vortex velocity (m s-1)                          |
+-----------------+----------------+----------------------------------------------------------+
| ``vortexaxis``  | ``y``          | | Orientation of axis vortices                           |
|                 |                | | ``x``: Rotation of vortices in xz-plane                |
|                 |                | | ``y``: Rotation of vortices in yz-plane                |
+-----------------+----------------+----------------------------------------------------------+

----


Large-scale forcings ``[force]``
--------------------------------

The ``Force`` class provides the tendencies for all forms of large-scale forcings.

+-----------------------+----------------+--------------------------------------------------------------+
| Name                  | Default        | Description and options                                      |
+=======================+================+==============================================================+
| ``swlspres``          | ``0``          | | Switch for large-scale pressure force                      |
|                       |                | | ``geo``: Fixed pressure gradient in x-direction            |
|                       |                | | ``dpdx``: Rotation of vortices in yz-plane                 |
|                       |                | | ``uflux``: ixed volume flux through domain                 |
+-----------------------+----------------+--------------------------------------------------------------+
| ``fc``                | ``None``       | Coriolis parameter (s-1) (if ``swlspres=geo``)               |
+-----------------------+----------------+--------------------------------------------------------------+
| ``dpdx``              | ``None``       | Fixed pressure gradient in x (Pa m-1) (if ``swlspres=dpdx``) |
+-----------------------+----------------+--------------------------------------------------------------+
| ``uflux``             | ``None``       | Fixed volume-mean velocity (m s-1) (if ``swlspres=uflux``)   |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swtimedep_geo``     | ``false``      | Switch for time dependent geostrophic wind                   |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swls``              | ``false``      | Switch for large-scale advective tendencies                  |
+-----------------------+----------------+--------------------------------------------------------------+
| ``lslist``            | ``Empty list`` | List of variables for which advective tendencies are given   |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swtimedep_ls``      | ``false``      | Switch for time-dependent advective tendencies               |
+-----------------------+----------------+--------------------------------------------------------------+
| ``timedeplist_ls``    | ``Empty list`` | List of scalars with time-dependent advective tendencies     |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swwls``             | ``false``      | Switch for large-scale subsidence (scalars)                  |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swwls_mom``         | ``false``      | Switch for large-scale subsidence (momentum)                 |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swtimedep_wls``     | ``false``      | Switch for time dependent subsidence                         |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swnudge``           | ``false``      | Switch for nudging                                           |
+-----------------------+----------------+--------------------------------------------------------------+
| ``nudgelist``         | ``Empty list`` | List of variables to which nudging is applied                |
+-----------------------+----------------+--------------------------------------------------------------+
| ``scalednudgelist``   | ``Empty list`` | List of variables to which a nudging scale is applied        |
+-----------------------+----------------+--------------------------------------------------------------+
| ``swtimedep_nudge``   | ``false``      | Switch for time-dependent nudging                            |
+-----------------------+----------------+--------------------------------------------------------------+
| ``timedeplist_nudge`` | ``Empty list`` | List of variables with time-dependent nudging                |
+-----------------------+----------------+--------------------------------------------------------------+

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
--------------------------

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
------------------------

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
-------------------

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
-------------------------

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
-------------------

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
----------------------
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
---------------------------

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
-------------------

+------------------+------------+---------------------------------------------------------------------------------+
|       Name       |  Default   |                             Description and options                             |
+==================+============+=================================================================================+
| ``starttime``    | *None*     | Start time of the simulation (s)                                                |
+------------------+------------+---------------------------------------------------------------------------------+
| ``endtime``      | *None*     | End time of the simulation (s)                                                  |
+------------------+------------+---------------------------------------------------------------------------------+
| ``savetime``     | *None*     | Interval at which a restart file will be saved (s)                              |
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


