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
| ``aerosol_optics.nc``          || ``[Radiation][swradiation]`` = ``rrtmgp`` or ``rrtmgp_rt`` | /rte-rrtmgp-cpp/data/aerosol_optics.nc                 |
|                                || and ``[Aerosol][swaerosol]`` = ``true``                    |                                                        |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+
| ``van_genuchten_parameters.nc``| ``[boundary][swboundary]`` = ``surface_lsm``                | /misc/van_genuchten_parameters.nc                      |
+--------------------------------+-------------------------------------------------------------+--------------------------------------------------------+

For the lookup tables ``coefficients_lw.nc`` and ``coefficients_sw.nc`` there are two files available with different numbers of g-points.
Using less g-points is slightly less accurate, but requires less memory.

Idealized cases
----------------
A dummy example of how to generate an input file for an idealized case is shown in :ref:`Example input NetCDF file`.
Many of the example cases available for MicroHH use such a script to generate the input file.
These scripts can be found in /cases/casename/casename_input.py and generate a file casename_input.nc.
Examples of cases that include only initial profiles are drycblles and Weisman Klemp.
The timedep group is e.g. included in the ARM example case and radiation group is e.g. included in the RCEMIP example case.


Realistic cases (using (LS) :sup:`2` D)
---------------------------------------
To run simulations with a more realistic setup, MicroHH can use initial conditions and large scale forcings from ERA5 (and if desired, CAMS).
To generate input based on ERA5, the (LS) :sup:`2` D python package can be used. General instructions on (LS) :sup:`2` D can be found here: https://github.com/LS2D/LS2D.
Here we shortly describe the steps to take and where to find the relevant scripts and functions.

1. Download the ERA5 (and CAMS) data.
This is done with the ``download_era5`` function from /ls2d/ecmwf/download_era5.py (and the ``download_cams`` function from /ls2d/ecmwf/download_cams.py).
If the requested data is not done before, these functions submit a request to the ECMWF system and close after submitting the request.
Hence, you have to call this function a second time once the request is completed to download the data.

2. Read the data.
This is done with the ``Read_era5`` class from /ls2d/ecmwf/read_era5.py (and the ``Read_cams`` class from /ls2d/ecmwf/read_cams.py).
For the ERA5 data, this class also calculates some derived quantities such as thl.

3. Calculate large scale forcings.
This is done with the ``calculate_forcings`` function from Read_era5 class that was called under step 2.

4. Interpolate the ERA5 and CAMS data to the MicroHH grid
This can be done with the ``get_les_input`` function from Read_era5 class that was called under step 2 (and the ``get_les_input`` function from the Read_cams class).

5. Save the input variables to NetCDF.

Examples of python scripts that follow these steps are available.
For ERA5: https://github.com/LS2D/LS2D/blob/main/examples/example_era5.py
For CAMS: https://github.com/LS2D/LS2D/blob/main/examples/example_cams.py

An example of of a scipts that combines downloaded ERA5 and CAMS data to MicroHH input can be found here:
https://github.com/microhh/microhh/blob/main/cases/cabauw/cabauw_input.py
In terms of the steps above, steps 1, 2 and 3 were perfomed to obtain the datsets ``ls2d_20160815.nc`` and ``cams_20160815.nc``.
Steps 4 and 5 are done in the cabauw_input.py script.




