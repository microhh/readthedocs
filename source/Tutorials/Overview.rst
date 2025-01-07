Overview
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The decision tree below provides an overview of the available options in the model.
The tree touches upon all classes of the model the control the simulation, represented by the headers of the ``.ini`` file.
If you choose to include an aspect, we advice you to check out the complete list of the options in :ref:`ini-file-label`.

For any simulation, the grid and time settings have to be specified (:ref:`Grid ``[Grid]``` and :ref:`Timeloop ``[Time]```), as well as the viscosity (:ref:`Fields ``[Fields]``` ``visc`` and ``svisc``). Hence these are not included in the scheme below.

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

..
    NOTE: all classes are mentioned apart from the pressure class. (where) should this be included?
