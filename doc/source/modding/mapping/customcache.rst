
Setting Custom Cache Amounts
============================

How-To
------

This is how to set custom cache amounts for your maps.

In your ``init.con`` for the layout you want to change set the amount of caches similar to how you set tickets on AAS.

.. code-block::

    gameLogic.setDefaultNumberOfTicketsEx <layer> <insurgent team> <caches>

The amount of caches can only be 10 as maximum. Every higher number will default back to the amount set in the realityconfig_public.py (at the moment 5).

Example
-------

Sbeneh is a real hard map for the MEC to win on insurgency. Let us compensate this by only having to destroy 3 caches on all layouts:

First we create a new ``init.con``. We call it ``init_ins.con`` and run it at the top of all out insurgency GamplayObjects (``gamemodes\gpm_insurgency``).

.. code-block::

    run ../../../Init_ins.con

Now we set the cache amount in this new init.con:

.. code-block::

    gameLogic.setDefaultNumberOfTicketsEx 32 1 3
    gameLogic.setDefaultNumberOfTicketsEx 64 1 3
    gameLogic.setDefaultNumberOfTicketsEx 128 1 3

If needed you can obviously change the BlueFor tickets just like you are used to from AAS. It's advisable for new maps and layers to keep the default of 5 caches and only change it after maptesting on public servers.

If you set it for any layer, I suggest to always set it for all even if the others are supposed to have the default amount. This prevents bugs when different layers are played after each other.
