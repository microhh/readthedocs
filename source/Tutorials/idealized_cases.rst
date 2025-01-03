Idealized simulations: beyond the drycblles
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Required files
---------------
To run a case, two files are always required: :code:`case_input.nc` and :code:`case.ini`.
:code:`case_input.nc` contains information about the vertical grid, the initial profiles for the prognostic variables,
and optionally input for the radiation scheme, (time varying) large-scale forcings, or time varying boundary conditions.
:code:`case.ini` is the namelist that contains the different model settings.

A dummy example of how to generate an input file for an idealized case is shown in :ref:`Example input NetCDF file`.
Many of the example cases available for MicroHH use such a script to generate the input file.
These scripts can be found in /cases/casename/casename_input.py and generate a file casename_input.nc.
Examples of cases that include only initial profiles are drycblles and Weisman Klemp.
The timedep group is e.g. included in the ARM example case and radiation group is e.g. included in the RCEMIP example case.

