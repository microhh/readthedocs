Masked statistics
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

MicroHH supports sampling and averaging of statistics over 2D or 3D masks. These masks can be defined dynamically (e.g. where :code:`ql>0`), or statically (user input). The dynamic masks are specified through the :code:`[stats]['masklist']` list (see :ref:`Statistics ``[stats]``` for the different options), the static masks through the :code:`[stats][xy_masklist]` list.

Static masks
------------

The static masks are currently limited to 2D (xy) masks, allowing the sampling of statistics over e.g. different land-use types. To enable the statistics, add an arbitrary number of mask names to:

.. code-block:: shell

    [stats]
    xy_masklist=dry,wet

Next, you need to create a binary file named :code:`dry.0000000` and :code:`wet.0000000`, defining the surface mask. In Python this is easy using Numpy, for example:

.. code-block:: python

    import numpy as np
   
    float_type = np.float32
    itot, jtot = 128, 128
    
    mask_dry = np.zeros((jtot, itot), dtype=float_type)
    mask_wet = np.zeros((jtot, itot), dtype=float_type)
    
    # Define mask for left and right side of domain:
    mask_dry[:,:itot//2] = 1
    mask_wet[:,itot//2:] = 1
    
    mask_dry.tofile('dry.0000000')
    mask_wet.tofile('wet.0000000')

After running this case, you get two additional statistics files named :code:`case_name.dry.0000000.nc` and :code:`case_name.wet.0000000.nc`.

Flux statistics and masks
-------------------------

The advective flux in the statistics file is the absolute flux (:math:`\langle ws \rangle`), and not the covariance of the fluctuations around the mean (:math:`\langle w's' \rangle`). For the domain averaged statistics where the mean vertical velocity (:math:`\langle w \rangle`) is zero, these two fluxes are identical:

.. math::

    w = \langle w \rangle + w' \\
    s = \langle s \rangle + s' \\

.. math::

    \langle w's' \rangle = \langle(w - \langle w \rangle)(s - \langle s \rangle) \rangle \\
    = \langle ws \rangle - \langle w \rangle \langle s \rangle

However, when using masked statistics, :math:`\langle w \rangle` calculated over the masked reqion is almost never zero, and as a result you need to correct the absolute flux to obtain :math:`\langle w's' \rangle`. As both :math:`\langle w \rangle` and :math:`\langle s \rangle` are available in the statistics files, this correction can be applied in the post-processing. 

The correction shown above is only valid for the even-ordered advection schemes (all except :code:`2i5`). For the :code:`2i5` scheme, the correction is more complex, as the advective flux contains an additional diffusive term.
