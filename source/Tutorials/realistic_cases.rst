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

.. admonition:: Task
    :class: tip

    1. install CDS and (LS) :sup:`2` D following the instructions at https://github.com/LS2D/LS2D
    2. run :code:`example_cams.py` and :code:`example_era5.py`

    Two files should have been created: :code:`ls2d_era5.nc` and :code:`ls2d_cams.nc`

.. note::

    1. When using CDS and ADS the :code:`$HOME/.cdsapirc` file must contain the url and key for CDS as :code:`url` and :code:`key` and for ADS as :code:`url_ads` and :code:`key_ads`.
    2. In :code:`example_cams.py` and :code:`example_era5.py` specify your own directories.
    3. Optionally, specify your own date, time and location in the settings dictionary in :code:`example_cams.py` and :code:`example_era5.py`.
    4. :code:`example_cams.py` and :code:`example_era5.py` stop after the download requests are submitted. Run them again once the data is downloaded to obtain the derived data.

The obtained files can now be used to generate a ``yourcase_input.nc`` file.
An example script to do this is available in ``/cases/cabauw/cabauw_input.py``

.. admonition:: Task
    :class: tip

    1. in :code:`cabauw_input.py` specify your own filenames for the ERA5 and CAMS data (or rename the output files from (LS) :sup:`2` D to :code:`ls2d_20160815.nc` (ERA5) and :code:`cams_20160815.nc` (CAMS))
    2. run cabauw_input.py

    Two files should have been created: :code:`cabauw_input.nc` and :code:`cabauw.ini`

..
    Should we add the images here that are created by these python scripts?

.. note::
    :code:`cabauw_input.py` is a very complete script that allows to set many options that are discussed below.
    Therefore, the script searches for some lookup tables in the microhh directory and links them to the working directory as required for the model run.
    Running :code:`cabauw_input.py` in a different directory will therefore likely result in some errors.
    To avoid these errors the linking functions (:code:`copy_xxxfiles`) can be commented out,
    but this means that the necessary files must be manually linked to the working directory before running MicroHH, as described under :ref:`Land surface` and :ref:`Radiation`.


.. admonition:: Task
    :class: tip

    Run a simulation using the created :code:`cabauw_input.nc` and :code:`cabauw.ini`.


Large scale forcings
-----------------------
Our Cabauw simulation includes large scale forcings based on ERA5.
This includes the following aspects:

| 1. A large scale pressure force, derived from the timedependent geostropic wind and the coriolis parameter.
|     This is specified in the ``.ini`` file by ``swlspres=geo``, ``swtimedep_geo=true`` and ``fc=0.000115``.
|     The ``_input.nc`` file contains the profiles of the geostropic wind (u and v) in the ``timedep`` group.
| 2. Timedependent large scale advection of thl, qt, u and v.
|     This is specified in the ``.ini`` file by ``swls=1``, ``swtimedep_ls=true``, ``lslist=thl,qt,u,v`` and ``timedeplist_ls=thl,qt,u,v``.
|     The ``_input.nc`` file contains the profiles of these variables (with ``_ls``) in the ``timedep`` group.
| 3. Timedepenent large scale subsidence based on the local field.
|     This is specified in the ``.ini`` file by ``swwls=local`` and ``swtimedep_wls=true``.
|     The ``_input.nc`` file contains the ``w_ls`` profile in the ``timedep`` group.
| 4. Nudging towards the timedependent ERA5 profiles of thl, qt, u and v.
|     This is specified in the ``.ini`` file by ``swnudge=true``, ``swtimedep_nudge=true`` and ``nudgelist=thl,qt,u,v``.
|     The ``_input.nc`` file contains the profiles of these variables (with ``_nudge``) in the ``timedep`` group and the profile of the nudging factor ``nudgefac`` in the ``init`` group.
| The ``_input.nc`` file also contains the time at which the timedependent variables are given.

..
    The requirements to include large scale forcings in general terms are listed below.

    | **Requirements**
    | In the force class in the ``.ini`` file:
    | 1. choose a method for the large scale pressure force ``swlspres`` (depending on your choice, specify ``fc``, ``dpdx``, ``uflux`` and/or ``swtimedep_geo``)
    | 2. set switch for large scale advection ``swls`` (if you enable large scale  advection, specify ``lslist``, ``swtimedep_ls`` and ``timedeplist_ls``)
    | 3. set switches for large scale subsidence ``swwls`` (scalars) and ``swwls_mom`` (momentum) (if you enable subsidence, specify ``timedep_wls``)
    | 4. set switch for nudging ``swnudge`` (if you enable nudging, specify ``scalenudgelist``, ``swtimedep_nudge`` and ``timedeplist_nudge``)
    | In the ``_input.nc`` file:
    | 1. if ``swlspres = geo``, ``u_geo`` and ``v_geo`` must be present in the ``init`` group if ``swtimedep_geo=false`` and in the ``timedep`` group if ``swtimedep_geo=true``
    | 2. if ``swls = true``, the variables listed in ``lslist`` must be present with ``_ls`` in the ``init`` group if ``swtimedep_ls=false`` and in the ``timedep`` group if ``swtimedep_ls=true`` and the variable is in ``timedeplist_ls``
    | 3. if ``swwls = true``, ``w_ls`` must be present in the ``init`` group if ``swtimedep_wls=false`` and in the ``timedep`` group if ``swtimedep_wls=true``
    | 4. if ``swnudge = true``, the variables listed in ``nudgelist`` must be present with ``_nudge`` in the ``init`` group if ``swtimedep_nudge=false`` and in the ``timedep`` group if ``swtimedep_nudge=true``. In addition, ``nudgefac`` should be present in the ``init`` group.


.. admonition:: Task
    :class: tip

    | To get a feeling for the impact of large scale forcings, we can play around with the Cabauw case. Here are some suggestions:
    | 1. Disable all large scale forcings by putting :code:`swlspres=false`, :code:`swls=false` and :code:`swwls=false`
    | 2. Exclude the nudging to ERA5 by putting :code:`swnudge=false`.
    | 3. Make the large scale forcings constant by putting :code:`swtimedep_geo=false`, :code:`swtimedep_ls=false`, :code:`swtimedep_wls=false`.
      Note that this also requires a new :code:`_input.nc` file where the necessary profiles are in :code:`init` group instead of the :code:`timedep`.
      This should be one profile for each variable, so take e.g. the profile at t=0 or a time-averaged profile.

.. note::
    The default day (15 August 2016) is mostly locally driven, so the impact of the large scale forcings and nudging to ERA5 might seems small, but can be very different (larger) in other cases.


Land surface
----------------------
Our Cabauw simulation includes a surface model with an interactive land-surface scheme.
This is specified in the ``.ini`` file by ``swboundary=surface_lsm`` and the settings in the ``[land_surface]`` group.

Using the interactive land surface-scheme requires (in the ``.ini`` file) the surface and vegetation properties as listed in :ref:`boundary conditions ``[boundary]```, as well as the number of vertical soil grid points ``ktot`` and the surface emissitivity in the ``radiation`` group.
The ``_input.nc`` file must contain a ``soil`` group with profiles (of size ``ktot``) of the soil temperature, soil water content, soil type, root fraction and depth of the soil layers (``t_soil``, ``theta_soil``, ``index_soil``, ``root_frac``, and ``z``)

.. note::
    The interactive land-surface scheme can only be used in combination with :code:`swthermo=moist` and :code:`swradiation = prescribed, rrtmgp or rrtmgp_rt`

.. note::
    The file ``van_genuchten_parameters.nc`` should be in the directory in which the model is run if ``[boundary][swboundary]`` = ``surface_lsm``.
    This file can be found in ``/misc/van_genuchten_parameters.nc``.

.. admonition:: Task
    :class: tip

    | To get a feeling for the impact of the land surface, we can play around with the Cabauw case. Here are some suggestions:
    | 1. Exclude the interactive land-surface scheme by putting :code:`swboundary=surface`
    | 2. Make the soil wetter or drier by increasing or decreasing the soil water content in the ``_input.nc`` file

..
    Does suggestion 1 work or should I remake the input to have thl_sbot and qt_sbot

Radiation
----------------------
Our Cabauw case includes radiation calculated with RTE+RRTMGP. This is specified in the ``.ini`` file by ``swradiation=rrtmgp``.

Using RRTMGP requires (in the ``radiation`` group of ``.ini`` file) at least surface albedos for the direct and diffuse radiation (``sfc_alb_dir``, ``sfc_alb_dif``), the surface emissivity (``emis_sfc``) and the radiation time interval (``dt_rad``).
In addition, apart from the default settings, the Cabauw case uses a variable solar zenith angle, hence ``swfixedsza=false`` and therefore the latitude and longitude need to be specified in the ``grid`` group.

The ``_input.nc`` file must contain a ``radiation`` group with profiles of height, temperature and pressure (all at model layers and model levels).
Furthermore, concentration of a number of gasses must be provided, either as profile or a a constant.
These gasses are at least H\ :sub:`2`\ O, O\ :sub:`3`, N\ :sub:`2`\ O, O\ :sub:`2`, CO\ :sub:`2`, CH\ :sub:`4`,
and optionally also CO, N\ :sub:`2`, CCl\ :sub:`4`, CFC-11, CFC-12, CFC-22, HFC-143a, HFC-125, HFC-23, HFC-32, HFC-134a, CF\ :sub:`4`, NO\ :sub:`2`)
These profiles are used for calculating radiation in a background column. This is one column in which radiation is calculated to determine the incoming radiation at the top of the domain.
This is necessary as the domain top is generally far below the top of the atmopshere, hence we need to account for the attenuation of radiation.

The ``_input.nc`` file must also contain concentrations of gasses, either as a profile or as a constant value to use in the model domain.
In our case, the concentrations of H\ :sub:`2`\ O and O\ :sub:`3` are given as profiles, the others essential gasses and N\ :sub:`2` as constants.

Apart from the :code:`_input.nc` and :code:`.ini`, additional files are required when using rrtmgp.
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

.. admonition:: Task
    :class: tip

    | To get a feeling for the possibilities of the radiation code, we can play around with the Cabauw case. Here are some suggestions:
    | 1. use different values for the surface albedo (:code:`sfc_alb_dir`, :code:`sfc_alb_dif`)
    | 2. use horizontally homogeneous surface radiation for the shortwave radiation (:code:`swhomogenizesfc_sw`)
    | 3. make the background column time-dependent (:code:`swtimedep_background=true`).
      Note that this requires a new :code:`_input.nc` file where the necessary profiles are in :code:`timedep` group.
    | 4a. add aerososols (:code:`swaerosol=true` in :ref:`aerosol ``[aerosol]```)
      Note that this requires a new :code:`_input.nc` file where the necessary profiles are in :code:`init` and :code:`radiation` group.
    | 4b. make the aerosols time-dependent (:code:`swtimedep=true` in :ref:`aerosol ``[aerosol]```)
      Note that this requires a new :code:`_input.nc` file where the necessary profiles are in :code:`timedep`.


Ray tracing
......................
Instead of the commonly used 2D radiative transfer calculations, MicroHH can also be ran with a coupled ray tracer.
The code, as well as some basic instructions can be found on https://github.com/microhh/rte-rrtmgp-cpp.

Using ray tracing coupled to a MicroHH simulation requires ``swradiation=rrtmgp_rt`` in the ``.ini`` file as well as some additional settings in :ref:`Radiation ``[Radiation]```.
The ray tracer uses a null-collision grid, which is a technique to divide the domain into smaller piece for efficient calculations.
For any simulation with the ray tracer, the size of this grid in the three dimensions has to be specified in the ``.ini`` file (``kngrid_i``, ``kngrid_j``, ``kngrid_k``).
In addition, the ``.ini`` file must contain the number of rays per pixel (``rays_per_pixel``), which must always be a power of 2.
The most common values for rays per pixel are 64, 128 or 256, with the smaller numbers being faster but slightly less accurate.

.. note::
    1. Currently, ray tracing is only available for shortwave radiation, requires an equidistant grid structure, and runs only on GPU.
    2. column statistics are not available when using the coupled ray tracer.

.. admonition:: Task
    :class: tip

    Adapt the ``cabauw.ini`` file and run a simulation with the coupled ray tracer



**The standalone ray tracer**

It is also possible to run the ray tracer offline. In other words, to apply 3D radiative transfer calculations to a cloud field from a simulation with simpler radiation.
This can be done in two ways: forward and backward. Forward ray tracing follows rays from the sun to compute radiative fluxes. Backward ray tracing traces rays back from the surface upwards to compute radiances.

Running the standalone ray tracer requires 3D fields of absolute temperature, specific humidity, cloud water content, ice water content and the essential gasses as listed above.
In addition, a 3D grid is required, vertical profiles of density and pressure, and values for the surface albedo, surface emissivity, solar zenith angle, zolar azimuth angle.
Optionally, other gasses and aerosols can be added. The backward ray tracer requires additional information on the camera settings.

The standalone ray tracer has the option to use Mie phase functions, instead of the default Heyey-Greenstein functions.
To use the option cloud-mie, an addition lookup table should be present in the working directory. This table is located in ``rte-rrtmgp-cpp/data/mie_lut_broadband.nc``

.. admonition:: Task
    :class: tip

    | 1. Build the executables. This can be done in the rte-rrtmgp-cpp subdirectory of MicroHH, or you can clone rte-rrtmgp-cpp in a seperate direcotry and compile the code there.
      Building the stand alone ray tracer is similar to building MicroHH. Several executables are created. For forward ray tracing use :code:`test_rte_rrtmgp_rt` and for backward ray tracing use :code:`test_rte_rrtmgp_bw`.
    | 2. Obtain input for the ray tracer. The necessary 3D fields can be obtained from a MicroHH simulation by adding the :code:`[dump]` class to the :code:`.ini` file.
      To convert MicroHH output to input for the standalone ray tracer, a python script is available :code:`/python/microhh_to_raytracer_input.py`.
      To add the camera settings for the backward ray tracer, a python script is available :code:`/rte-rrtmgp-cpp/python/set_virtual_camera.py`
    | 3. Execute the ray tracer. For example, to run the ray tracer including cloud-optics, aerosol-optics and 128 rays per pixel, use :code:`./test_rte_rrtmgp_rt --cloud-optics --aerosol-optics --raytrcing 128`.
      All available command line options are listed in the code for the `forward ray tracer <https://github.com/microhh/rte-rrtmgp-cpp/blob/a0f96acba099ba9d98d338a4f8f4c71fee0f987f/src_test/test_rte_rrtmgp_rt.cu#L226>`_
      and `backward ray tracer <https://github.com/microhh/rte-rrtmgp-cpp/blob/812c5fabdbdbe66787d343c7fae46d9302a9bd75/src_test/test_rte_rrtmgp_bw.cu#L235>`_.
    | (4. To visualize the output of the backward ray tracer, a python script is available :code:`/rte-rrtmgp-cpp/python/image_from_xyz.py`)

