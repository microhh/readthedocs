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


