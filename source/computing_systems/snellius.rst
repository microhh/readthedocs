Snellius @ SURFsara
====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

General information on the system and remote access (SSH) are available at: `<https://servicedesk.surfsara.nl/wiki/display/WIKI/Snellius>`_. Some additional notes are currently available at: `<https://github.com/microhh/microhh/issues/73>`_.

Modules
-------

Snellius uses a module system to load and/or switch between different compilers, libraries, etc. The following command unloads all modules (:code:`module purge`) and loads (:code:`module load`) the ones required to compile MicroHH, generate the input files with Python, merge the statistics with NCO, and visualise the results with Ncview:

.. code-block:: shell

    module purge
    module load 2021
    module load CMake/3.20.1-GCCcore-10.3.0

    # MicroHH + GCC:
    module load foss/2021a
    module load netCDF/4.8.0-gompi-2021a
    module load CUDA/11.3.1

    ## Python/plotting et al:
    module load ncview/2.1.8-gompi-2021a
    module load Python/3.9.5-GCCcore-10.3.0
    module load IPython/7.25.0-GCCcore-10.3.0
    module load NCO/5.0.1-foss-2021a

For compiling MicroHH with Intel (see https://github.com/microhh/microhh/issues/73 for notes on how to build NetCDF with Intel), replace the `MicroHH + GCC` part with:

.. code-block:: shell

    module load intel/2021a
    module load netCDF/4.8.0-iimpi-2021a
    module load FFTW/3.3.9-intel-2021a

To simplify switching between the two environments, it can be convenient to put the module commands in a shell script in your home directory (e.g. :code:`setup_env.sh`):

.. code-block:: shell

    if [ "$1" = "" ]; then
        echo "WARNING: You did not specify a build chain (gcc/intel), defaulting to GCC!"
        toolkit="gcc"
    else
        toolkit=$1
    fi

    module purge
    module load 2021
    module load CMake/3.20.1-GCCcore-10.3.0

    # Python/plotting et al:
    module load ncview/2.1.8-gompi-2021a
    module load Python/3.9.5-GCCcore-10.3.0
    module load IPython/7.25.0-GCCcore-10.3.0
    module load NCO/5.0.1-foss-2021a

    if [ "$toolkit" = "gcc" ]; then
        echo "Loading GCC build chain"
        module load foss/2021a
        module load netCDF/4.8.0-gompi-2021a
        module load CUDA/11.3.1
    elif [ "$toolkit" = "intel" ]; then
        echo "Loading Intel build chain"
        module load intel/2021a
        module load netCDF/4.8.0-iimpi-2021a
        module load FFTW/3.3.9-intel-2021a
    fi

    module list


After which you can simply switch using:

.. code-block:: shell

    source ~/setup_env.sh gcc
    # or:
    source ~/setup_env.sh intel

Slurm load balancer
-------------------

Like most supercomputers, Snellius uses a queuing system (Slurm) to schedule all the individual jobs from users. Instead of running the model directly from the login nodes, experiments have to be submitted to one or multiple compute nodes using a Slurm script.

The script below (also available in :code:`microhh_root/misc/runscripts/snellius_cpu.slurm`) shows an example for running the :code:`drycblles` case on 128 CPU cores (1 nodes) in the :code:`thin` partition:

.. code-block:: shell

    #!/bin/bash
    #SBATCH --job-name=drycblles

    # Log file `stdout` and `stderr` (%j is replaced with a unique job ID):
    #SBATCH --output=mhh-%j.out
    #SBATCH --error=mhh-%j.err

    # Thin CPU partition (https://servicedesk.surfsara.nl/wiki/display/WIKI/Snellius+usage+and+accounting):
    #SBATCH --partition=thin

    # Snellius has 128 cores/node. Slurm automatically determines the required number of nodes:
    #SBATCH -n 128
    #SBATCH --cpus-per-task=1
    #SBATCH --ntasks-per-core=1

    # Maximum wall clock time:
    #SBATCH -t 08:00:00

    # E-mail notifications, options are: {none, begin, end, fail, all}:
    #SBATCH --mail-type=end
    #SBATCH --mail-user=ceo@microhh.org

    # Load required modules:
    toolkit="gcc"     # Switch between gcc/intel builds

    module purge
    module load 2021
    module load CMake/3.20.1-GCCcore-10.3.0

    if [ "$toolkit" = "gcc" ]; then
        module load foss/2021a
        module load netCDF/4.8.0-gompi-2021a
    elif [ "$toolkit" = "intel" ]; then
        module load intel/2021a
        module load netCDF/4.8.0-iimpi-2021a
        module load FFTW/3.3.9-intel-2021a
    fi

    srun ./microhh init drycblles
    srun ./microhh run drycblles

For setting up and testing new cases, it can be convenient to run the case with a wall clock limit (:code:`#SBATCH -t`) of less than one hour. This automatically places your job in the `short` queue, for which the waiting time if typically very short.

New jobs can be submitted using the :code:`sbatch` command (:code:`sbatch my_slurm_script.slurm`), the status of existing jobs can be listed with the :code:`squeue` command, and running (or queued) jobs can be cancelled using :code:`scancel <jobid>`, where :code:`<jobid>` is the unique ID listed when running the :code:`squeue` command.

More information about the different Slurm options is available in the `Slurm documentation <https://slurm.schedmd.com/documentation.html>`_ or the `Snellius domentation <https://servicedesk.surfsara.nl/wiki/display/WIKI/Example+job+scripts>`_.

Best practices
--------------

#. You should always run your experiments on the GPFS :code:`scratch` (:code:`/scratch-shared/your_username/`) file system, which is designed for the storage of large volumes of data, and fast parallel I/O.
#. Files on the :code:`scratch` file system are automatically deleted after 14 days, so archive them in time to e.g. the SURFsara archive at :code:`/archive/your_username/`.
