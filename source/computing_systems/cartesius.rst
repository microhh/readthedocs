Cartesius @ SURFsara
====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

General information on the system and remote access (SSH) are available at: `userinfo.surfsara.nl <https://userinfo.surfsara.nl/systems/cartesius>`_.

Modules
-------

Cartesius uses a module system to load and/or switch between different compilers, libraries, etc. The following command unloads all modules (:code:`module purge`) and loads (:code:`module load`) the ones required to compile MicroHH:

.. code-block:: shell

    module purge
    module load surfsara
    module load compilerwrappers
    module load 2019
    module load CMake
    module load intel/2018b
    module load netCDF/4.6.1-intel-2018b
    module load netCDF-Fortran/4.4.4-intel-2018b
    module load FFTW/3.3.8-intel-2018b

To use Python, for example to generate the NetCDF input files for MicroHH, the following modules work:

.. code-block:: shell

    module purge
    module load 2019
    module load Python/3.7.5-foss-2018b
    module load netCDF/4.6.1-foss-2018b

Slurm load balancer
-------------------

Like most supercomputers, Cartesius uses a queuing system (Slurm) to schedule all the individual jobs from users. Instead of running the model directly from the login nodes, experiments have to be submitted to one or multiple compute nodes using a Slurm script.

The script below (also available in :code:`misc/runscripts/cartesius.slurm`) shows an example for running the :code:`drycblles` case on 48 CPU cores (2 nodes) in the :code:`normal` queue:

.. code-block:: shell

    #!/bin/bash
    #SBATCH --job-name=my_job

    # Log file `stdout` and `stderr` (%j is replaced with a unique job ID):
    #SBATCH --output=mhh-%j.out
    #SBATCH --error=mhh-%j.err

    # Total number of CPU cores:
    #SBATCH -n 48

    # Normal queue for long runs:
    #SBATCH -p normal
    #SBATCH -t 24:00:00

    # Nodes with Haswell cores are fastest:
    #SBATCH --constraint=haswell

    # E-mail notifications, options are: {none, begin, end, fail, all}
    #SBATCH --mail-type=end
    #SBATCH --mail-user=abc@def.de

    # Init and run MicroHH
    srun ./microhh init drycblles
    srun ./microhh run drycblles

For setting up and testing new cases, it is often convenient to use the :code:`short` queue. This queue has a wallclock limit of only one hour, but the time spent waiting in the queue is typically much shorter (often less than a few minutes):

.. code-block:: shell

    # Short queue for quick tests:
    #SBATCH -p short
    #SBATCH -t 01:00:00

New jobs can be submitted using the :code:`sbatch` command (:code:`sbatch my_slurm_script.slurm`), the status of existing jobs can be listed with the :code:`squeue` command, and running (or queued) jobs can be cancelled using :code:`scancel <jobid>`, where :code:`<jobid>` is the unique ID listed when running the :code:`squeue` command.

More information about the different Slurm options is available in the `Slurm documentation <https://slurm.schedmd.com/documentation.html>`_ or the `Cartesius domentation <https://userinfo.surfsara.nl/systems/cartesius/usage/batch-usage>`_.

Best practices
--------------

#. Compute nodes on Cartesius have 24 CPU cores per node, and the system does not support shared node usage. As a result, a job requesting e.g. 32 CPU cores will run on two nodes, on which 16 CPU cores are unused. In terms of costs, you are still accounted for all 48 cores, so it is always best to design your experiment (grid configuration) around a multiple of 24 CPU cores.

#. You should always run your experiments on the Lustre :code:`scratch` (:code:`/scratch-shared/your_username/`) file system, which is designed for the storage of large volumes of data, and fast parallel I/O. To speedup the writing of large files with MPI-I/O, always configure the Lustre file striping using e.g. :code:`lfs setstripe -c 50 /scratch-shared/your_username/your_dir`. Note that you need to set the file striping for a directory before copying any files into that directory.

#. Files on the :code:`scratch` file system are automatically deleted after 14 days, so archive them in time to e.g. the SURFsara archive at :code:`/archive/you_username/`.
