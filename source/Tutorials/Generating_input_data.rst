Input files
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Required files
---------------
To run a case, two files are always required: :code:`case_input.nc` and :code:`case.ini`.
:code:`case_input.nc` contains information about the vertical grid, the initial profiles for the prognostic variables,
and optionally input for the radiation scheme, (time varying) large-scale forcings, or time varying boundary conditions.
:code:`case.ini` is the namelist that contains the different model settings.
Below we explain how to generate the :code:`case_input.nc` file.

Apart from the :code:`case_input.nc` and :code:`case.ini`, additional files might be required when different schemes are used.
Here you find an overview of potential additional files that should be present in the directory in which the model is run.

+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| File name                      | Required when                                               | Location of the file                                   |
+================================+=============================================================+========================================================+
| ``coefficients_lw.nc``         | ``[Radiation][swradiation]`` = ``rrtmgp`` or ``rrtmgp_rt``  || /rte-rrtmgp-cpp/rrtmgp-data/rrtmgp-gas-lw-g256.nc     |
|                                |                                                             || or /rte-rrtmgp-cpp/rrtmgp-data/rrtmgp-gas-lw-g128.nc  |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| ``coefficients_sw.nc``         | ``[Radiation][swradiation]`` = ``rrtmgp`` or ``rrtmgp_rt``  || /rte-rrtmgp-cpp/rrtmgp-data/rrtmgp-gas-sw-g224.nc     |
|                                |                                                             || or /rte-rrtmgp-cpp/rrtmgp-data/rrtmgp-gas-sw-g112.nc  |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| ``cloud_coefficients_lw.nc``   | ``[Radiation][swradiation]`` = ``rrtmgp`` or ``rrtmgp_rt``  | /rte-rrtmgp-cpp/rrtmgp-data/rrtmgp-clouds-lw.nc        |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| ``cloud_coefficients_sw.nc``   | ``[Radiation][swradiation]`` = ``rrtmgp`` or ``rrtmgp_rt``  | /rte-rrtmgp-cpp/rrtmgp-data/rrtmgp-clouds-sw.nc        |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| ``aerosol_optics.nc.nc``       || ``[Radiation][swradiation]`` = ``rrtmgp`` or ``rrtmgp_rt`` | /rte-rrtmgp-cpp/data/aerosol_optics.nc                 |
|                                || and ``[Aerosol][swaerosol]`` = ``true``                    |                                                        |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| ``van_genuchten_parameters.nc``| ``[boundary][swboundary]`` = ``surface_lsm``                | /misc/van_genuchten_parameters.nc                      |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+

For the lookup tables ``coefficients_lw.nc`` and ``coefficients_sw.nc`` there are two files available with different numbers of g-points.
Using less g-points is slightly less accurate, but requires less memory.

Idealized cases
----------------



Realistic cases (using LS2D)
----------------------------


