The ``yourcase_input.nc`` file
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Building the ``yourcase_input.nc``
----------------------------------

Each MicroHH experiment requires a NetCDF file with the initial vertical profiles, and optionally input for model components like e.g. large-scale forcings, boundary conditions, and/or radiation. The different input options are divided over different NetCDF groups.

Each input file should, as a bare minimum, specify the vertical coordinates of the

The tables below shows an overview of the input options. If a wildcard ``*`` is used, variables can be filled in according to the description.

``init`` group
--------------

The ``init`` group provides the initial vertical profiles of the prognostic variables, and optionally (non time dependent) large scale forcings like the geostrophic wind components, subsidence velocity, source terms, or nudging profiles. See :ref:`Large-scale forcings ``[force]``` for details on the different options.

+-------------+---------+--------------------------------------------------------------+
| Variable    | Dims    | Description                                                  |
+=============+=========+==============================================================+
| ``*``       | ``[z]`` | Initial profile of any prognostic variable                   |
+-------------+---------+--------------------------------------------------------------+
| ``*_ls``    | ``[z]`` | | Source term of any prognostic variable                     |
|             |         | | (if ``swls=1`` and ``swtimedep_ls=0``)                     |
+-------------+---------+--------------------------------------------------------------+
| ``*_nudge`` | ``[z]`` | | Nudging target of any prognostic variable                  |
|             |         | | (if ``swnudge=1`` and ``swtimedep_nudge=0``)               |
+-------------+---------+--------------------------------------------------------------+
| ``u_geo``   | ``[z]`` | | Zonal component geostrophic wind                           |
|             |         | | (if ``swlspres=geo`` and ``swtimedep_geo=0``)              |
+-------------+---------+--------------------------------------------------------------+
| ``u_geo``   | ``[z]`` | | Meridional component geostrophic wind                      |
|             |         | | (if ``swlspres=geo`` and ``swtimedep_geo=0``)              |
+-------------+---------+--------------------------------------------------------------+
| ``w_ls``    | ``[z]`` | Subsidence velocity (if ``swwls=1`` and ``swtimedep_wls=0``) |
+-------------+---------+--------------------------------------------------------------+

``timedep`` group
-----------------

The ``timedep`` group specifies the time dependent surface boundary conditions and/or large scale forcings....

+------------------+--------------------+--------------------------------------------------------------+
| Variable         | Dims               | Description                                                  |
+==================+====================+==============================================================+
| ``time_surface`` | ``[time_surface]`` | Input time of surface boundary conditions                    |
+------------------+--------------------+--------------------------------------------------------------+
| ``*_sbot``       | ``[time_surface]`` | Surface boundary conditions of any prognostic variable       |
+------------------+--------------------+--------------------------------------------------------------+
| ``p_bot``        | ``[time_surface]`` | Surface pressure                                             |
+------------------+--------------------+--------------------------------------------------------------+
| ``time_ls``      | ``[time_ls]``      | Input time of large scale forcings                           |
+------------------+--------------------+--------------------------------------------------------------+
| ``*_ls``         | ``[time_ls, z]``   | | Source term of any prognostic variable                     |
|                  |                    | | (if ``swls=1`` and ``swtimedep_ls=1```)                    |
+------------------+--------------------+--------------------------------------------------------------+
| ``*_nudge``      | ``[time_ls, z]``   | | Nudging target of any prognostic variable                  |
|                  |                    | | (if ``swnudge=1`` and ``swtimedep_nudge=1```)              |
+------------------+--------------------+--------------------------------------------------------------+
| ``u_geo``        | ``[time_ls, z]``   | | Zonal component geostrophic wind                           |
|                  |                    | | (if ``swlspres=geo`` and ``swtimedep_geo=1``)              |
+------------------+--------------------+--------------------------------------------------------------+
| ``u_geo``        | ``[time_ls, z]``   | | Meridional component geostrophic wind                      |
|                  |                    | | (if ``swlspres=geo`` and ``swtimedep_geo=1``)              |
+------------------+--------------------+--------------------------------------------------------------+
| ``w_ls``         | ``[time_ls, z]``   | Subsidence velocity (if ``swwls=1`` and ``swtimedep_wls=1``) |
+------------------+--------------------+--------------------------------------------------------------+


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


