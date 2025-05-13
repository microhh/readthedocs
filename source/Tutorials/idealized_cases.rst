Idealized simulations: beyond the drycblles
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


In :ref:`Running your first case` you ran an LES of a dry convective boundary layer.
In this tutorial we will explore the building bloks of such a simulation, such as advection and diffusion and the different options that are availabel (for LES).
As this tutorial will also cover the possible options for thermodynamics and microphysics, we will mainly show examples for a simle example case that includes moisture: the BOMEX case.
The :code:`bomex.ini` file and a python file to create the :code:`bomex_input.nc` are available in the case folder (:code:`cases/bomex`).

.. note::
Here we show examples of commonly used options and there impact, to help you choose suitable settings for your own simulations.
However, what the most suitable settings are depends on the case.
Apart from looking at the examples here, you can base your choises on the available example cases or test the sensitivity of your own case yourself.

.. note::
The BOMEX case that we use here for most examples is a realativelly simple case and runs on a small domain.
Hence, if you want to do some simulations to get familiar with the available options and the work flow, this case and the examples shown in this tutorial are very suitable .

.. note::
    For most of the available cases the case folder contains a :code:`case.ini` or :code:`case.ini.base` file as well as a python script to create the :code:`case_input.nc` file.
    With these files, you can run all of the example cases yourself.



Advection and Diffusion
--------------------------
Our BOMEX case (and also the drycblles) use a 2nd order advection scheme (``swadvec=2``).
Commonly used alternatives are the 2nd order scheme with 5th order interpolations (``swadvec=2i5``) and the 2nd order scheme with 6th order interpolations in the horizontal and 2nd order interpolations in the vertical (``swadvec=2i62``)
The advantage of the higher order schemes is a higher accuracy, but this comes at higher computational costs.

The odd ordered schemes have hyperdiffusion included and the ``2i5`` and ``2i62`` schemes have the possibility to provide a list of the scalars for which monotonic advection is guaranteed.
Both the hyperdiffusion and the flux limiters dampen the variance and smooth out sharp gradients.
In some cases, e.g. when using a coarse resolution, this can be advantagous.
However, in other cases, it can hamper the existence of small scale structures and result in overly smooth fields.

.. admonition:: Example
    :class: tip

    To get a feeling for the impact of the advection scheme, we show here the BOMEX case with three different advection schemes (:code:`swadvec=2`, :code:`swadvec=2i62`, and :code:`swadvec=2i5`).
    We ran the higher order advection schemes with and without flux limiters.
    The impact of the advection scheme can best be seen from the updraft structures, for example from the xz-cross sections of vertical wind.



All additional settings and alternative options are listed under :ref:`Advection ``[advec]```

Our BOMEX case (and also the drycblles) use a 2nd order Smagorinsky scheme for the diffusion.
This scheme (with the default values for the Smagorinsky constant (``cs``) and turbulent Prandtl number (``tPr``)) is used in most example LES cases, and is generally speeking a good choice.
All additional settings and alternative options are listed under :ref:`Diffusion ``[diff]```

.. note::
    By default, MicroHH uses an adaptive time step. In some cases when a simulation crashes, it can help to enforce a shorter timestep,
    which you can obtain by using stricter settings for the :code:`cflmax` in the :code:`advection` group and the :code:`dnmax` in the :code:`diffusion` group.

Thermodynamics
----------------
"MicroHH solves the conservation equations of mass, momentum, and energy under the anelastic approximation.
Under this approximation, the state variables density, pressure, and temperature are described as small fluctuations
from corresponding vertical reference profiles that are functions of height only." (`van Heerwaarden et al., 2017 <https://gmd.copernicus.org/articles/10/3145/2017/>`_)
These references profiles are also refered to as the base state.

Our BOMEX case uses this anelastic approximation (``swbasestate=anelastic``) and a base state that changes over time (``swupdatebasestate=true``).
The drycblles on other hand, uses the Boussinesq approximation (``swbasestate=boussinesq``), which is the same as the anelastic approximation with the additional assumption that the density is always 1.
Under this approximation the base state is always constant over time.
Furhermore, as mentioned in the beginning of this tutorial, the bomex case uses moist thermodynamics (``swthermo=moist``), hence clouds can be formed.
The dryccblles uses dry thermodynamics (``swthermo=dry``).

.. admonition:: Task
    :class: tip

    | To get a feeling for the impact of the switches in the thermodynamics scheme, we can play around with the BOMEX case.
      Here are some suggestions:
    | 1. Change the surface pressure (:code:`pbot`). The surface pressure determines the pressure and density profile, hence it influences cloud formation (higher pressure = less cloud formation).
    | 2. Use a constant base state (:code:`swupdatebasestate=false`)

Microphysics
-------------
Our BOMEX case does not include microphysics. Hence, there is no formation of rain or any frozen hydrometeors.
For the microphysics, two schemes are available.
One is a single moment scheme (``swmicro=nsw6``), which in short means that the scheme predics only the mixing ratios of the hydrometeors.
The other is a double moment scheme (``swmicro=2mom_warm``), which means that the scheme predics the mixing ratios and number concentrations of the hydrometeors.
Note that currently, our double moment scheme does not include ice and the cloud droplet number is fixed.

.. admonition:: Task
    :class: tip

    | To get a feeling for the impact of the switches in the microphysics scheme, we can play around with the BOMEX case.
      Here are some suggestions:
    | 1. Include single moment microphysics (:code:`swmicro=nsw6`).
      Note that the cloud droplet number (:code:`Nc0`) must be specified.
      The typical order of magnitude for :code:`Nc0` is 10-1000 cm\ :sup:`-3`, and the input value must be m\ :sup:`-3`.
    | 2. Include double moment microphysics (:code:`swmicro=nsw6`)
    | 3. Change the cloud droplet number concentration

.. note::
    Our BOMEX case has a limited domain size and small and shallow clouds, hence the amount of rain formed is very small.
    Some other cases are available with a bit larger domain that contain precipitating clouds, e.g. RICO.


Boundary conditions
---------------------
Our BOMEX case has a fixed ustar as bottom boundary condition and a freeslip top boundary condition for the momentum variables.
For the scalars, a neumann boudary conditions is used at the top, a flux boundary condition at the bottom, and the values used are provided.
The drycblles has the same boundary conditions apart from the momentum bottom boundary, where the drycblles uses a noslip condition.
Both cases use a surface model based on the Monin Obukhov Similary Theory (MOST).
The extended version of this scheme with an interactive land surface scheme is covered in :ref:`Land surface`.

.. admonition:: Task
    :class: tip

    | To get a feeling for the options for the boundary conditions, we can play around with the BOMEX case.
      Here are some suggestions:
    | 1. Use a noslip bottom boundary condition for the momentum variables (:code:`mbcbot=noslip`)
    | 2. Change the surface roughness (:code:`z0m` and :code:`z0h`)


Further aspects
-----------------
Apart from the aspects covered in this tutorial, the BOMEX and drycblles contain two more aspects for which settings are given in the ``.ini`` file.

1. A buffer layer, which is a layer at the top of the domain that prevents the reflection of gravity waves back into the domain.
The strength of this buffer layer and the height at which it starts are controlled by the settings in the ``.ini`` file.

2. Initial random perturbations. These are small perturbations that are necessary to trigger turbulent motions.
The strength of the perturbations and the height until which they are applied are controlled by the settings in the ``.ini`` file.
