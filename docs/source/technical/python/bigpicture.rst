
How Battlefield 2 Hooks Python
==============================

Here's a description of how the BF2 engine interacts with Python code:

1.  When BF2 engine starts up it fires up its embedded Python interpreter, with it's sys.path set to include

    -  The Python standard library (which is contained in the file ``Battlefield 2 Server/pylib-2.3.4.zip``).
    -  The ``Battlefield 2 Server/python directory``
    -  The Python directory of the current mod (e.g. ``Battlefield 2 Server/mods/bf2/python``)

       -  If the server switches mods, this will be changed, too. (It appears that the current BF2 game engine doesn't have the ability to switch mods automatically between rounds-that once a mod is loaded, it stays loaded and running until the server is manually stopped, reconfigured, and restarted).

    -  The ``Battlefield 2 Server/admin`` directory.

2.  The BF2 engine imports the ``bf2`` package (the code for this package is located in the directory ``Battlefield 2 Server/python``).
3.  When Python imports a package, it executes the ``_init_.py`` module in that package. In the case of the ``bf2``, the ``_init_`` module imports and instantiates the basic code and objects needed for the game, including ``game.scoringCommon`` from the active mod's python directory (this appears to be the only place any mod-specific Python code gets pulled in).
4.  The BF2 engine calls ``bf2.init_module()``

    -  That method imports the stats modules
    -  Not clear why it's done this way, instead of just putting everything in the ``_init_`` module.

5.  The BF2 engine processes the ``Battlefield 2 Server/mods/bf2/settings/ServerSettings.con`` configuration file. In it's default, out-of-the-box configuration, that file has a directive that causes more Python activity: ``sv.adminScript "default"`` causes the ``default`` module in the directory ``Battlefield 2 Server/admin`` to be imported. This module primarily handles the ``RCon`` interface, but contains an ``init()`` function that, when called later by the game engine, causes the ``admin.standard_admin`` package to be imported. This package presently handles team autobalancing and punishing team killing (“TK”). See the :doc:`Admin Module <../admin/module>` for more details.
6.  Throughout the start-up process, as packages and modules are imported into the embedded Python interpreter they are registering themselves to receive callbacks when various :doc:`events <reference/events>` occur in the BF2 engine.
7.  Some modules need to carry out initialization activities before each round can begin; they arrange for their initialization code to be called by registering to receive callbacks for ``GameStatusChangedEvents``. When they receive such a callback and see that the game status is “``PreGame``”, they execute their initialization code.
8.  When set-up is complete and the game is running, the Python code that was initialized during start-up then runs in event-driven mode, with the game engine dispatching execution to Python handlers when the events they registered for occur. When a player is killed in the game, for example, a ``PlayerKilled`` event fires, and any modules that registered to receive a callback for this event (for example, a module related to keeping score) will be called.
9.  When a game round ends, it is important to know the game engine **does not** restart, and neither does the embedded Python interpreter - the ``bf2`` packages are **not** reimported or reinitialized. Instead, during start-up, modules that need to do end-of-round cleanup registered to receive callbacks for ``GameStatusChangedEvents``, and when they see the game status change to “``EndGame``” they carry out their cleanup activities.
10.  The game engine now jumps back a few steps in this process, to the point where game status changes to “``PreGame``”, and pre-game initialization callback handlers are called to begin the cycle again.

Note that there is another directory of Python code in the ``Battlefield 2 Server`` directory that does **not** get pulled in by the game engine: ``adminutils`` contains source code and executables for the ``rotate_demo`` and ``remoteconsole`` stand-alone applications, as examples of how to write software that will interact with BF2. The fact that these are written in Python is coincidental. (The BF2 engine handles ``RCon`` and demo recording functionality internally, without using the embedded Python interpreter, although there are events connected with these functions that can be used to hook your own Python code to them).
