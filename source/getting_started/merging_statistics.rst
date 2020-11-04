Merging statistics
==================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

In the design of MicroHH, we have decided to write a new statistics file after every restart, to ensure that in case of a crash of any kind the statistics do not get corrupted. This brings some inconvenience to the users that can easily be overcome by merging the files after the run. We suggest to use NCO's :code:`ncrcat` operator, which is available in most Linux distributions via the package manager:

.. code-block:: shell

    ncrcat drycblles.default.*.nc drycblles.default.nc

This creates a new file with the name drycblles.default.nc that contains the merged statistics.

In case you are viewing data with ncview during an active simulation, you can use :code:`ncview drycblles.default.*` to open all files at once. Ncview will concatenate them correctly.
