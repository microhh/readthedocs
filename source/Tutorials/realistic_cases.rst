Realistic simulations: the cabauw case
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Generating input data using (LS) :sup:`2` D
----------------------------------------------
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


Large scale forcings
-----------------------


Land surface
----------------------

The file ``van_genuchten_parameters.nc`` should be in the directory in which the model is run if ``[boundary][swboundary]`` = ``surface_lsm``.
This file can be found in ``/misc/van_genuchten_parameters.nc``.

Radiation
----------------------

Apart from the :code:`case_input.nc` and :code:`case.ini`, additional files might be required for the radiation computations.
Here you find an overview of available lookup tables that should be present in the directory in which the model is run.

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

For the lookup tables ``coefficients_lw.nc`` and ``coefficients_sw.nc`` there are two files available with different numbers of g-points.
Using less g-points is slightly less accurate, but requires less memory.


Raytracing
......................

Some basic instructions can be found on https://github.com/microhh/rte-rrtmgp-cpp.

Currently, raytracing is only available for shortwave radiation and requires an equidistant grid structure and runs only on GPU.

The raytracer uses a null-collision grid, which is a technique to divide the domain into smaller piece for efficient calculations.
For any simulation with the raytracer, the size of this grid in the three dimensions has to be specified in the ``.ini`` file.
In addition, the ``.ini`` file must contain the number of rays per pixel, which must always be a power of 2.
The most common values for rays per pixel are 64, 128 or 256, with the smaller numbers being faster but slightly less accurate.

The coupled raytracer
''''''''''''''''''''''''''
To use raytracing coupled to a MicroHH simulation, set ``swradiation`` to ``rrtmpg_rt`` in the ``.ini`` file.
Additional settings for the coupled raytracer are listed here: :ref:`Radiation ``[Radiation]```
Note: column statistics are not available when using the coupled raytracer.

The standalone raytracer
''''''''''''''''''''''''''

To run the standalone raytracer, the first step is to build the executables. Building the stand alone raytracer is similar to building MicroHH.
Several executables are created. For forward raytracing use ``test_rte_rrtmgp_rt`` and for backward raytracing use ``test_rte_rrtmgp_bw``.

Running the standalone raytracer requires 3D fields of absolute temperature and specific humidity and optionally 3D fields of cloud water and ice water content.
In addition, a 3D grid is required, vertical profiles of density and pressure, and values for the surface albedo, surface emissivity, solar zenith angle, zolar azimuth angle.
Optionally, profiles of other gasses and aerosols can be added. The necessary 3D fields can be obtained from a MicroHH simulation by adding the ``[dump]`` class to the ``.ini`` file.
To convert MicroHH output to input for the standalone raytracer, a python script is available in ``/python/microhh_to_raytracer_input.py``.

After creating the input file, the raytracer can be executed.
The available command line options for the backward raytracer can be found here: https://github.com/microhh/rte-rrtmgp-cpp/blob/a0f96acba099ba9d98d338a4f8f4c71fee0f987f/src_test/test_rte_rrtmgp_rt.cu#L226
For example, to run the raytracer for shortwave, including cloud-optics, aerosol-optics and 128 rays per pixel, use ``./test_rte_rrtmgp_rt --cloud-optics --aerosol-optics --raytrcing 128``
To use the option cloud-mie, an addition lookup table should be present in the working directory.
This table can be found here: https://github.com/microhh/rte-rrtmgp-cpp/blob/main/data/mie_lut_broadband.nc

The available command line options for the backward raytracer can be found here: https://github.com/microhh/rte-rrtmgp-cpp/blob/812c5fabdbdbe66787d343c7fae46d9302a9bd75/src_test/test_rte_rrtmgp_bw.cu#L235
The backward raytracer requires the same input as the foward raytracer, with additional information on the camera settings.
These can be added with a python script (https://github.com/microhh/rte-rrtmgp-cpp/blob/main/python/set_virtual_camera.py ).
To visualize the ouput of the backward raytracer, a python script is available here: https://github.com/microhh/rte-rrtmgp-cpp/blob/main/python/image_from_xyz.py
