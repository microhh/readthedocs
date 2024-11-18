Using the standalone raytracer
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Building the executables
-------------------------
Building the stand alone raytracer is similar to building MicroHH. Some instructions can be found on https://github.com/microhh/rte-rrtmgp-cpp.


Input files
---------------
Running the standalone raytracer requires 3D fields of absolute temperature and specific humidity and optionally 3D fields of cloud water and ice water content.
In addition, a 3D grid is required, vertical profiles of density and pressure, and values for the surface albedo, surface emissivity, solar zenith angle, zolar azimuth angle.
Optionally, profiles of other gasses and aerosols can be added.

The necessary 3D fields can be obtained from a MicroHH simulation by adding the ``[dump]`` class to the ``.ini`` file.
To convert MicroHH output to input for th standalone raytracer, a python script is available in ``/python/microhh_to_raytracer_input.py``.
This python script (with some example data) is also available as part of this documentation
