Running cases
=============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Running your first case
-----------------------

To start one of the included test cases, go to the main directory and open the directory :code:`cases`. Here, a collection of test cases has been included. In this example, we start the drycblles case, a simple large-eddy simulation of a dry convective boundary layer.

.. code-block:: shell

    cd cases/drycblles

First, we have to create the input for LES:

.. code-block:: shell

    python drycblles_input.py

This creates a file called :code:`case_input.nc` (in this case: :code:`drycblles_input.nc`), which contains information about the vertical grid, the initial profiles for the prognostic variables, and optionally input for the radiation scheme, (time varying) large-scale forcings, or time varying boundary conditions. Next, we have to copy or link the :code:`microhh` executable to the current directory. Here we assume the executable is in the :code:`build` directory.

.. code-block:: shell

    cp ../../build/microhh .

Now, we can start MicroHH in initialization mode to create the initial fields:

.. code-block:: shell

    ./microhh init drycblles

If everything works out properly, a series of files has been created. The model can be started now following:

.. code-block:: shell

    ./microhh run drycblles

This will take some time. Now, a NetCDF statistics file called :code:`drycblles.default.0000000.nc` has been created. You can open this file with your favorite plotting tool (e.g. ncview or Panoply), or run some example plots using the provided plotting script that uses Python and Matplotlib. This is most easily done in interactive Python:

.. code-block:: shell

    ipython
    run drycblles_stats.py

This should show you a set of basic plots. Congratulations, you have just completed your first run of MicroHH.

Running cases with MPI
----------------------

To run cases in parallel with MPI, first of all, the code has to be compiled with MPI enabled. Second, the domain decomposition needs to be specified in the :code:`.ini` file:

.. code-block:: shell

    [master]
    npx=2       # number of processes in the x-direction
    npy=2       # number of processes in the y-direction

.. note::

    There are a few constraints on the domain decomposition and grid: The number of grid points in the x and y-directions (:code:`itot` and :code:`jtot`) both need to be dividable by both :code:`npx` and :code:`npy`, and the number of grid points in the vertical (:code:`ktot`) needs to be dividable by :code:`npx`.

For a correctly configured grid and domain decomposition, your parallel run can be started as usual, for example:

.. code-block:: shell

    mpiexec -n 4 ./microhh init drycblles
    mpiexec -n 4 ./microhh run drycblles
