Code and compilation
====================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Requirements
------------

Before starting the tutorial, make sure that you meet the requirements of MicroHH. In order to compile MicroHH you need:

- C++ compiler (C++17)
- Fortran compiler (Fortran 2003)
- FFTW3
- Boost
- NetCDF4-C
- CMake
- MPI2/3 implementation `(optional for MPI support)`
- CUDA `(optional for GPU support)`
- Python + Numpy `(optional for running example cases)`
- Ipython + NetCDF4 + Matplotlib `(optional for plotting results example cases)`

.. note::

    The legacy netCDF C++ and NetCDF-CXX4 libraries are no longer supported (or required), as MicroHH has its own C++ wrapper for the NetCDF4-C library.

If you are running on OSX, please install also the GNU sed (:code:`gnu-sed` in Homebrew, or :code:`gsed` in MacPorts)

Obtaining the MicroHH code
--------------------------

.. note::

    If you want to contribute code to MicroHH, it is best not to clone the code from the main repository, but instead make a `fork` using the `fork` option at https://github.com/microhh/microhh. This will create a copy of MicroHH in https://github.com/your_username/microhh, which you can download using :code:`git clone https://github.com/your_username/microhh.git`. If you do not want to contribute, it is fine to `clone` the code from the main repository.

The MicroHH code is hosted at Github (https://github.com/microhh/microhh). The code can either be downloaded as a ZIP file (https://github.com/microhh/microhh/archive/main.zip), but if Git (version control system) is installed, the code can also be downloaded using:

Check out the code from GitHub using

.. code-block:: shell

    git clone --recurse-submodules https://github.com/microhh/microhh.git

In case you had already checked out the repository without checking out the submodules, use:

.. code-block:: shell

    git submodule update --init --recursive


The advantage of using Git is that the model can easily be updated at a later time by calling :code:`git pull` from anywhere in the MicroHH directory.

Compilation of the code
-----------------------

At the starting point of this tutorial, we assume that you are in the main directory of MicroHH. First, we will take care of the configuration file. Enter the config directory:

.. code-block:: shell

    cd config

Here, you find a potential series of settings with the extension `.cmake` for different systems. Check whether your system is there. If not, you can try the generic configuration (`generic.cmake`), or create a file with the correct compiler settings and the proper location for all libraries on your system. Then, copy your system file to default.cmake, for example:

.. code-block:: shell

    cp generic.cmake default.cmake

Then, go back to the main directory and create a subdirectory with an arbitrary name in which you will compile the code. Let us assume this directory is called :code:`build`:

.. code-block:: shell

    cd ..  
    mkdir build  
    cd build   


From this directory, run :code:`cmake` with the suffix :code:`..` to point to the parent directory where the CMakeLists.txt is found. This builds the model without Message Passing Interface (MPI) and CUDA support.

.. code-block:: shell

    cmake ..

Running :code:`cmake` without arguments gives you a serial build without GPU support in double precision. Parallel builds with MPI can be enabled by adding the :code:`-DUSEMPI=TRUE` flag. GPU support using NVIDIA CUDA can be enabled with the flag :code:`-DUSECUDA=TRUE`. Note that they cannot be combined at the moment in absence of multi-GPU support. The precision of the code can be reduced from double (64-bits) to single (32-bits) precision using the flag :code:`-DUSESP=TRUE`. Some examples are found below here:

.. code-block:: shell

    cmake .. -DUSEMPI=TRUE
    cmake .. -DUSECUDA=TRUE -DUSESP=TRUE
    cmake .. -DUSESP=TRUE

.. note::

    If you get an error :code:`add_subdirectory given source "rte-rrtmgp-cpp/src_kernels" which is not an existing directory`, you probably forgot to specify :code:`--recurse-submodules` in the :code:`git clone` command. You can fix this by running :code:`git submodule update --init --recursive` once.

.. warning::

    Once the build has been configured and you wish to change the :code:`USECUDA`, :code:`USEMPI`, or :code:`USESP` setting, you must delete the build directory or create an additional empty directory from which :code:`cmake` is run again.
    
With the previous command you have triggered the build system and created the :code:`Makefile`, if the :code:`default.cmake` file contains the correct settings. Now, you can start the compilation of the code and create the MicroHH executable with:

.. code-block:: shell

    make -j 4

Your directory should contain a file named :code:`microhh` now. This is the main executable.
