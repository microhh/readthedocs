The ``yourcase_input.nc`` file
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Building the ``yourcase_input.nc``
----------------------------------

Each MicroHH experiment requires a NetCDF file with the initial vertical profiles, and optionally input for model components like e.g. large-scale forcings, boundary conditions, and/or radiation. The different input options are divided over different NetCDF groups.

Each input file should, as a bare minimum, specify the height of the full model levels:

+--------------+---------+------------+--------------------------------------------------------------+
| Variable     | Dims    | Unit       | Description                                                  |
+==============+=========+============+==============================================================+
| ``z``        | ``[z]`` | ``m``      | Height of the full model levels                              |
+--------------+---------+------------+--------------------------------------------------------------+

The tables below show an overview of the input options. If a wildcard ``*`` is used, variables (with units ``@``) can be filled in according to the description.

.. warning::

    If a variable required by the model is not present in the NetCDF file, the profile is filled with zero's, and a warning is printed.

``init`` group
--------------

The ``init`` group provides the initial vertical profiles of the prognostic variables, and optionally (non time dependent) large scale forcings like the geostrophic wind components, subsidence velocity, source terms, or nudging profiles. See :ref:`Large-scale forcings ``[force]``` for details on the different options.

+--------------+---------+------------+--------------------------------------------------------------+
| Variable     | Dims    | Unit       | Description                                                  |
+==============+=========+============+==============================================================+
| ``*``        | ``[z]`` | ``@``      | Initial profile of any prognostic variable                   |
+--------------+---------+------------+--------------------------------------------------------------+
| ``*_ls``     | ``[z]`` | ``@ s-1``  | | Source term of any prognostic variable                     |
|              |         |            | | (if ``swls=1`` and ``swtimedep_ls=0``)                     |
+--------------+---------+------------+--------------------------------------------------------------+
| ``*_nudge``  | ``[z]`` | ``@``      | | Nudging target of any prognostic variable                  |
|              |         |            | | (if ``swnudge=1`` and ``swtimedep_nudge=0``)               |
+--------------+---------+------------+--------------------------------------------------------------+
| ``u_geo``    | ``[z]`` | ``m s-1``  | | Zonal component geostrophic wind                           |
|              |         |            | | (if ``swlspres=geo`` and ``swtimedep_geo=0``)              |
+--------------+---------+------------+--------------------------------------------------------------+
| ``u_geo``    | ``[z]`` | ``m s-1)`` | | Meridional component geostrophic wind                      |
|              |         |            | | (if ``swlspres=geo`` and ``swtimedep_geo=0``)              |
+--------------+---------+------------+--------------------------------------------------------------+
| ``w_ls``     | ``[z]`` | ``m s-1``  | Subsidence velocity (if ``swwls=1`` and ``swtimedep_wls=0``) |
+--------------+---------+------------+--------------------------------------------------------------+
| ``nudgefac`` | ``[z]`` | ``s``      | Nudging time scale (if ``swnudge=1``)                        |
+--------------+---------+------------+--------------------------------------------------------------+


``timedep`` group
-----------------

The ``timedep`` group specifies the time dependent surface boundary conditions and/or large scale forcings.

+------------------+--------------------+-----------+------------------------------------------------------------+
| Variable         | Dims               | Unit      | Description                                                |
+==================+====================+===========+============================================================+
| ``time_surface`` | ``[time_surface]`` | ``s``     | Input time of surface boundary conditions                  |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``*_sbot``       | ``[time_surface]`` | note 1    | Surface boundary conditions of prognostic scalar variables |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``p_bot``        | ``[time_surface]`` | ``Pa``    | Surface pressure                                           |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``time_ls``      | ``[time_ls]``      | ``s``     | Input time of large scale forcings                         |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``*_ls``         | ``[time_ls, z]``   | ``@ s-1`` | | Source term of any prognostic variable                   |
|                  |                    |           | | (if ``swls=1`` and ``swtimedep_ls=1``)                   |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``*_nudge``      | ``[time_ls, z]``   | ``@``     | | Nudging target of any prognostic variable                |
|                  |                    |           | | (if ``swnudge=1`` and ``swtimedep_nudge=1``)             |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``u_geo``        | ``[time_ls, z]``   | ``m s-1`` | | Zonal component geostrophic wind                         |
|                  |                    |           | | (if ``swlspres=geo`` and ``swtimedep_geo=1``)            |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``u_geo``        | ``[time_ls, z]``   | ``m s-1`` | | Meridional component geostrophic wind                    |
|                  |                    |           | | (if ``swlspres=geo`` and ``swtimedep_geo=1``)            |
+------------------+--------------------+-----------+------------------------------------------------------------+
| ``w_ls``         | ``[time_ls, z]``   | ``m s-1`` | | Subsidence velocity                                      |
|                  |                    |           | | (if ``swwls=1`` and ``swtimedep_wls=1``)                 |
+------------------+--------------------+-----------+------------------------------------------------------------+

Note 1: the units of the scalar boundary conditions (BCs) depend on the boundary conditions used: ``@`` for Dirichlet BCs, ``@ m s-1`` for flux BCs, and ``@ m-1`` for Neuman BCs.


``radiation`` group
-------------------

The ``radiation`` group defines background profiles, used by RRTMGP to calculate the radiation boundary conditions at the top of the LES domain. The input is specified at full (dimension ``lay``) and half (dimension ``lev``) pressure levels, and typically should extend to the top of the atmosphere (TOA).

+-----------+-----------+---------+------------------------------+
| Variable  | Dims      | Unit    | Description                  |
+===========+===========+=========+==============================+
| ``p_lay`` | ``[lay]`` | ``Pa``  | Pressure                     |
+-----------+-----------+---------+------------------------------+
| ``p_lev`` | ``[lev]`` | ``Pa``  | Pressure                     |
+-----------+-----------+---------+------------------------------+
| ``z_lay`` | ``[lay]`` | ``m``   | Height                       |
+-----------+-----------+---------+------------------------------+
| ``z_lev`` | ``[lev]`` | ``m``   | Height                       |
+-----------+-----------+---------+------------------------------+
| ``t_lay`` | ``[lay]`` | ``K``   | Absolute temperature         |
+-----------+-----------+---------+------------------------------+
| ``t_lev`` | ``[lev]`` | ``K``   | Absolute temperature         |
+-----------+-----------+---------+------------------------------+
| ``h2o``   | ``[lay]`` | ``??``  | Water vapour mixing ratio ?? |
+-----------+-----------+---------+------------------------------+
| ``co2``   | ``[lay]`` | ``ppm`` | Carbon dioxide mixing ratio  |
+-----------+-----------+---------+------------------------------+
| ``ch4``   | ``[lay]`` | ``ppb`` | Methane mixing ratio         |
+-----------+-----------+---------+------------------------------+
| ``n2o``   | ``[lay]`` | ``ppb`` | Nitrous oxide mixing ratio   |
+-----------+-----------+---------+------------------------------+
| ``n2``    | ``[lay]`` | ``??``  | Dinitrogen mixing ratio      |
+-----------+-----------+---------+------------------------------+
| ``o2``    | ``[lay]`` | ``??``  | Oxygen mixing ratio          |
+-----------+-----------+---------+------------------------------+
| ``o3``    | ``[lay]`` | ``??``  | Ozone mixing ratio           |
+-----------+-----------+---------+------------------------------+


Example input NetCDF file
-------------------------

The code snippet below illustrates how to create a NetCDF input file with Python.

.. code-block:: python

    import netCDF4 as nc4
    import numpy as np

    # Vertical dimension and coordinates
    ktot = 64
    dz = 40.
    z = np.arange(dz/2, ktot*dz, dz)

    # Initial profiles
    thl = 280. + 0.006*z
    u = np.ones(ktot)*5
    u_geo = np.ones(ktot)*5

    # Time dependent surface boundary condition
    time_surface = np.linspace(0, 43200, 128)

    # Surface potential temperature flux (cosine with max 0.2 K m s-1)
    thl_sbot = (1-np.cos(2*np.pi*time_surface/43200))/2*0.2

    # Save all the input data to NetCDF
    nc_file = nc4.Dataset('mycase_input.nc', mode='w', datamodel='NETCDF4', clobber=False)

    def add_variable(nc_group, name, dims, data):
        """ Help function for adding a new variable """
        var = nc_group.createVariable(name, 'f8', dims)
        var[:] = data

    # Create dimension and variable of vertical grid in main group:
    nc_file.createDimension('z', ktot)
    add_variable(nc_file, 'z', ('z'), z)

    # Create a group called `init` for the initial profiles:
    nc_group_init = nc_file.createGroup('init')
    add_variable(nc_group_init, 'thl', ('z'), thl)
    add_variable(nc_group_init, 'u', ('z'), u)
    add_variable(nc_group_init, 'u_geo', ('z'), u_geo)

    # Create a group called `timedep` for the time dependent variables:
    nc_group_timedep = nc_file.createGroup('timedep')
    nc_group_timedep.createDimension('time_surface', time_surface.size)
    add_variable(nc_group_timedep, 'time_surface', ('time_surface'), time_surface)
    add_variable(nc_group_timedep, 'thl_sbot', ('time_surface'), thl_sbot)

    nc_file.close()

This results in a NetCDF file ``mycase_input.nc``:

.. code-block:: shell

    netcdf mycase_input {
    dimensions:
            z = 64 ;
    variables:
            double z(z) ;

    group: init {
      variables:
            double thl(z) ;
            double u(z) ;
            double u_geo(z) ;
      } // group init

    group: timedep {
      dimensions:
            time_surface = 128 ;
      variables:
            double time_surface(time_surface) ;
            double thl_sbot(time_surface) ;
      } // group timedep
    }


