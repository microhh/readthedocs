Converting binaries
===================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Some MicroHH output -- like restart files, 3D field dumps, and cross-sections -- are written in binary format. For the conversion to NetCDF, several Python scripts are available in the :code:`python` directory.

Cross-sections
--------------

For the conversion of cross-sections, copy both the :code:`microhh_tools.py` and :code:`cross_to_nc.py` scripts to your working directory. If :code:`cross_to_nc.py` is executed without any arguments, the script will automatically try to deduce the correct settings from the :code:`case.ini` file, and convert all cross-sections. More fine grained control is possible by specifying arguments to the :code:`cross_to_nc.py` script, for example:

.. code-block:: shell

   python cross_to_nc.py -m xy -v thl -t0 3600 -t1 7200 -tstep 300 -p single -c

will convert only the horizontal (:code:`-m xy`) cross-sections of potential temperature (:code:`-v thl`) of the second hour of the experiment (:code:`-t0 3600 -t1 7200`) at a 300s frequency (:code:`-tstep 300`), saving the resulting NetCDF file using single precision (4 byte) floats (:code:`-p single`), without NetCDF compression (:code:`-c`).

For an overview of all options, see the help function:

.. code-block:: shell

   python cross_to_nc.py -h


Restart files and field dumps
-----------------------------

The conversion of restart files and field dumps works the same as the conversion of cross-sections, only using the :code:`3d_to_nc.py` script. Many of the possible command line arguments are the same as in the :code:`cross_to_nc.py` script. For an overview, see the help function:

.. code-block:: shell

   python 3d_to_nc.py -h
