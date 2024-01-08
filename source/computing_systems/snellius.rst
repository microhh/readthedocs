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
    module load 2022
    module load CMake/3.23.1-GCCcore-11.3.0

    # MicroHH + GCC
    module load foss/2022a
    module load netCDF/4.9.0-gompi-2022a
    module load CUDA/11.8.0
    module load Clang/13.0.1-GCCcore-11.3.0

    # Python et al.
    module load Python/3.10.4-GCCcore-11.3.0
    module load NCO/5.1.0-foss-2022a

To simplify setting up the environment, it can be convenient to put the module commands in a shell script in your home directory (e.g. :code:`setup_env.sh`), after which you can setup the environment using:

.. code-block:: shell

    source ~/setup_env.sh

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

    module purge
    module load 2022
    module load CMake/3.23.1-GCCcore-11.3.0
    module load foss/2022a
    module load netCDF/4.9.0-gompi-2022a
    module load CUDA/11.8.0
    module load Clang/13.0.1-GCCcore-11.3.0

    export OMPI_MCA_fcoll="two_phase"
    export OMPI_MCA_io_ompio_bytes_per_agg="512MB"

    srun ./microhh init drycblles
    srun ./microhh run drycblles

For setting up and testing new cases, it can be convenient to run the case with a wall clock limit (:code:`#SBATCH -t`) of less than one hour. This automatically places your job in the `short` queue, for which the waiting time if typically very short.

New jobs can be submitted using the :code:`sbatch` command (:code:`sbatch my_slurm_script.slurm`), the status of existing jobs can be listed with the :code:`squeue` command, and running (or queued) jobs can be cancelled using :code:`scancel <jobid>`, where :code:`<jobid>` is the unique ID listed when running the :code:`squeue` command.

More information about the different Slurm options is available in the `Slurm documentation <https://slurm.schedmd.com/documentation.html>`_ or the `Snellius domentation <https://servicedesk.surfsara.nl/wiki/display/WIKI/Example+job+scripts>`_.

Best practices
--------------

#. You should always run your experiments on the GPFS :code:`scratch` (:code:`/scratch-shared/your_username/`) file system, which is designed for the storage of large volumes of data, and fast parallel I/O.
#. Files on the :code:`scratch` file system are automatically deleted after 14 days, so archive them in time to e.g. the SURFsara archive at :code:`/archive/your_username/`.
#. Always specify the following two OpenMPI parameters before :code:`srun ./microhh init case_name` (see run script above), otherwise I/O becomes a bottleneck:

.. code-block:: shell

    export OMPI_MCA_fcoll="two_phase"
    export OMPI_MCA_io_ompio_bytes_per_agg="512MB"
