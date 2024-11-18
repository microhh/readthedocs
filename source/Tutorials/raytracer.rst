Using the raytracer
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

General information
--------------------
Some basic instructions can be found on https://github.com/microhh/rte-rrtmgp-cpp.

Currently, raytracing is only available for shortwave radiation and requires an equidistant grid structure and runs only on GPU.

The raytracer uses a null-collision grid, which is a technique to divide the domain into smaller piece for efficient calculations.
For any simulation with the raytracer, the size of this grid in the three dimensions has to be specified in the ``.ini`` file.
In addition, the ``.ini`` file must contain the number of rays per pixel, which must always be a power of 2.
The most common values for rays per pixel are 64, 128 or 256, with the smaller numbers being faster but slightly less accurate.

The standalone raytracer
-------------------------
To run the standalone raytracer, the first step is to build the executables. Building the stand alone raytracer is similar to building MicroHH.
Several executables are created. For forward raytracing use ``test_rte_rrtmgp_rt`` and for backward raytracing use ``test_rte_rrtmgp_bw``.

Running the standalone raytracer requires 3D fields of absolute temperature and specific humidity and optionally 3D fields of cloud water and ice water content.
In addition, a 3D grid is required, vertical profiles of density and pressure, and values for the surface albedo, surface emissivity, solar zenith angle, zolar azimuth angle.
Optionally, profiles of other gasses and aerosols can be added.

The necessary 3D fields can be obtained from a MicroHH simulation by adding the ``[dump]`` class to the ``.ini`` file.
To convert MicroHH output to input for the standalone raytracer, a python script is available in ``/python/microhh_to_raytracer_input.py``.
This python script (with some example data) is also available as part of this documentation (:ref:`/Tutorials/MicroHH_to_raytracer_input.ipynb`).

After creating the input file, the raytracer can be executed.
For the forward raytracer the following command line options are available:

+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| option            | default   | description                                                                                           |
+===================+===========+=======================================================================================================+
| shortwave         | true      | Enable computation of shortwave radiation.                                                            |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| longwave          | false     | Enable computation of longwave radiation.                                                             |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| fluxes            | true      | Enable computation of fluxes.                                                                         |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| raytracing        | true      | Use raytracing for flux computation. '--raytracing 256': use 256 rays per pixel"                      |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| cloud-optics      | false     | Enable cloud optics.                                                                                  |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| cloud-mie         | true      | Use Mie tables for cloud scattering in ray tracer.                                                    |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| aerosol-optics    | false     | Enable aerosol optics.                                                                                |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| single-gpt        | false     | Output optical properties and fluxes for a single g-point. '--single-gpt 100': output 100th g-point   |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| delta-cloud       | false     | delta-scaling of cloud optical properties.                                                            |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| delta-aerosol     | false     | delta-scaling of aerosol optical properties                                                           |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| raytracing        | 32        | Number of rays initialised at TOD per pixel per quadraute.                                            |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+
| single-gpt        | 1         | g-point to store optical properties and fluxes of                                                     |
+-------------------+-----------+-------------------------------------------------------------------------------------------------------+


For example, to run the raytracer for shortwave, including cloud-optics, aerosol-optics and 128 rays per pixel, use ``./test_rte_rrtmgp_rt --cloud-optics --aerosol-optics --raytrcing 128``
To use the option cloud-mie, an addition lookup table should be present in the working directory.
This table can be found here: https://github.com/microhh/rte-rrtmgp-cpp/blob/main/data/mie_lut_broadband.nc

The available command line options for the backward raytracer can be found here: https://github.com/microhh/rte-rrtmgp-cpp/blob/812c5fabdbdbe66787d343c7fae46d9302a9bd75/src_test/test_rte_rrtmgp_bw.cu#L235
The backward raytracer requires the same input as the foward raytracer, with additional information on the camera settings.
These can be added with a python script (https://github.com/microhh/rte-rrtmgp-cpp/blob/main/python/set_virtual_camera.py ).
To visualize the ouput of the backward raytracer, a python script is available here: https://github.com/microhh/rte-rrtmgp-cpp/blob/main/python/image_from_xyz.py

The coupled raytracer
----------------------
To use raytracing coupled to a MicroHH simulation, set ``swradiation`` to ``rrtmpg_rt`` in the ``.ini`` file.
Additional settings for the coupled raytracer are listed here: :ref:`Radiation ``[Radiation]```
Note: column statistics are not available when using the coupled raytracer.


