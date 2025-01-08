Overview
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The decision tree below provides an overview of the available options in the model.
The tree touches upon all classes of the model the control the simulation, represented by the headers of the ``.ini`` file.
If you choose to include an aspect, we advice you to check out the complete list of the options in :ref:`ini-file-label`.

For any simulation, the grid and time settings have to be specified (:ref:`Grid ``[Grid]``` and :ref:`Timeloop ``[Time]```),
as well as the viscosity (:ref:`Fields ``[Fields]``` ``visc`` and ``svisc``).
Hence these are not included in the scheme below.

..
    grid and time are currently also not covered in the tutorials. Should something about that be added?

|

.. image:: flowchart.jpeg
    :width: 800

|

In addition to the classes in the decision tree there are classes that control the output settings.
These are:

1. domain average statistics: :ref:`Statistics ``[Stats]```

2. single column output: :ref:`Column ``[Column]```

3. cross sections: :ref:`Cross sections ``[Cross]```

4. 3D field dumps: :ref:`Dump of 3D fields ``[Dump]```

5. budgets of the second order moments: :ref:`Budget statistics ``[budget]```


Lastly, the :ref:`Master ``[Master]``` class controls the settings for parallel runs.


.. admonition:: Task
    :class: tip

    | To get familiar with the different output options, we can add some options to the drycblles.
      Here are some suggestions:
    | 1. Add output for a single column (:code:`swcolumn=true`).
      Note that you need to specify the x and y position of the column in meters (:code:`coordinates[x]` and :code:`coordinates[y]`) and the timeresolution (:code:`sampletime`)
    | 2. Add some cross sections (:code:`swcross=true`)
      Note that you need to specify the position of the cross-section (:code:`xy`, :code:`xz`, and/or :code:`yz`), the timeresolution (:code:`sampletime`),
      and the variable of which cross sections should be saved (:code:`crosslist`)

.. note::
    | How to convert cross-sections and 3D dump to netCDF is described in :ref:`Merging statistics`.
    | Options for masked statistics are described in :ref:`Masked statistics`.

..
    note: all classes are mentioned apart from the pressure class. (where) should this be included?
