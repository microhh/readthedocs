The ``yourcase_input.nc`` file
==============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Building the ``yourcase_input.nc``
----------------------------------

Each MicroHH experiment requires a NetCDF file with the initial vertical profiles, and optionally input for model components like e.g. large-scale forcings, boundary conditions, and/or radiation. The different input options are divided over different NetCDF groups.

The tables below shows an overview of the input options. If a wildcard ``*`` is used, variables can be filled in according to the description.

``init`` group
--------------

The ``init`` group provides the initial vertical profiles of the prognostic variables, and optionally (non time dependent) large scale forcings like the geostrophic wind components, subsidence velocity, or nudging profiles. The optional input is only used if the corresponding switch is enabled in the ``force`` group of the ``.ini`` file, and the option for time dependent input (``swtimedep_*``) is disabled (see :ref:`Large-scale forcings ``[force]``` for details).

+----------------------------+---------------------------------------------------------------------------------+
| Variable                   | Description                                                                     |
+============================+=================================================================================+
| ``*``                      | Initial profile of any prognostic variable                                      |
+----------------------------+---------------------------------------------------------------------------------+
| ``*_ls``                   | Source term of any prognostic variable                                          |
+----------------------------+---------------------------------------------------------------------------------+
| ``*_nudge``                | Nudging target of any prognostic variable                                       |
+----------------------------+---------------------------------------------------------------------------------+
| ``u_geo``                  | Zonal component geostrophic wind (m/s)                                          |
+----------------------------+---------------------------------------------------------------------------------+
| ``v_geo``                  | Meridional component geostrophic wind (m/s)                                     |
+----------------------------+---------------------------------------------------------------------------------+
| ``w_ls``                   | Subsidence velocity (m/s)                                                       |
+----------------------------+---------------------------------------------------------------------------------+


