
The Administrative Module
=========================

Battlefield 2 provides for a Python “administrative” module; this module can do pretty much anything, but the Python code that ships with BF2 serves two basic roles:

-  It implements the BF2 RCon (“Remote Console”) interface
-  It implements several in-game automatic administration functions; the standard module automatically balances the number of players on each team, and handles punishment of players for killing teammates (“TK”ing).

The ``sv.adminScript`` server configuration directive tells the BF2 game engine which administrative module should be loaded as the engine is starting up; this directive gives the name of the Python module to load in the ``Battlefield 2 Server/admin`` directory; the default administrative module that ships with BF2 is called, appropriately, ``default``:

.. code-block:: python

   sv.adminScript "default"

You can create your own administrative modules; just put them in the ``Battlefield 2 Server/admin`` directory and change the setting for ``sv.adminScript`` in the ``ServerSettings.con`` file. One example of a custom administrative module can be found [[Scripts:Modified_admin_script|here]] (in this case, it's an expansion of the ``default`` module that adds more features).

Module Methods
--------------

Any administrative module, including ``default``, has three methods which are called by the game engine itsef:

-  ``init()``

   The game engine calls this method while it is :doc:`starting up <../python/bigpicture>`; in the ``default`` module, this method reads the admin configuration file (``default.cfg``), initializes the admin system, registers to receive :doc:`RemoteCommand events <../python/reference/events>`, etc.

-  ``shutdown()``

   The game engine calls this method when the server is shutting down (shutting down completely-not just after each game round). In the ``default`` module this method just closes the TCP socket used for receiving RCon commands from the network.

-  ``update()``

   The game engine calls this method roughly every 30ms; in the ``default`` module, this method checks for any new input arriving over the network TCP RCon socket.

``RCon``
--------

BF2 includes an ``RCon`` (Remote Console) function that allows many administrative functions that can be done from the regular console (the black-and-white curses interface on the machine running the BF2 server) to be done from a “remote console”-either from within a BF2 game client (accessed by a player pressing the ``~`` key), or via a TCP network interface.

The ``RCon`` interface is implemented completely in Python, with the code in the ``Battlefield 2 Server/admin`` directory. The game engine provides five facilities that this Python code uses:

-  As part of it's :doc:`start-up procedure <../python/bigpicture>`, the server imports the Python module in the ``admin`` directory specified by the ``sv.adminScript`` directive. This is normally the ``default`` module, but the fact that it's imported based on a configuration directive means that it could easily be changed to a custom module.
-  The game engine provides an event, :doc:`RemoteCommand <../python/reference/events>`, that fires whenever an in-game player accesses their console and types any line beginning with “rcon”. The event passes any registered callback handlers the actual command typed by the player. This is how the ``default`` module receives ``RCon`` commands from players (but it can be used by other Python code, as well).
-  The game engine provides a method, ``host.rcon_feedback``, that can be used to send messages to a player's in-game console. This is what the ``default`` module uses to send responses to players' ``RCon`` commands back to them (but it can be used by other Python code, also).
-  The game engine calls the ``update`` method of the ``default`` module (or whatever module has been specified by ``sv.adminScript``) repeatedly, generally about every 30 milliseconds (roughly 30 times per second). The ``default`` module uses this to run a fast check for input on a TCP port (normally port 4711) for ``RCon`` commands-this is how the network ``RCon`` interface receives commands. More information about the ``RCon`` protocol the ``default`` module implements can be found in the :doc:`RCon Protocol Specification <../networking/protocols_rcon>`.
-  When the ``default`` module decides to execute a console command from a remote user, it passes it on to the game engine for execution using the ``host.rcon_invoke`` method. This method isn't specific to ``RCon`` commands-in fact, it doesn't execute ``RCon`` commands at all-it executes server console commands, and can be used to good effect by any Python code. Note, however, that there is presently a bug in BF2 that prevents any feedback from PunkBuster commands from being sent back to the caller of ``host.rcon_invoke``; since this is the only way remote console commands are executed, it means that ``RCon`` users can never see any feedback from PunkBuster commands they send via ``RCon``.

The ``default`` module implements just three RCon commands (but could easily be extended to add others):

-  ``login``

   ``default`` won't accept any other RCon commands until this command is given with the valid password, as specified in the ``default.cfg`` file.

-  ``users``

   Lists players connected to the server, along with their :doc:`IP Addresses and CD key hashes <identity>`.

-  ``exec``

   Executes any server command.

(Note that from a player's in-game console window, each of these commands must be preceeded by the word “rcon” to cause the game engine to send it to the ``default`` module; from a TCP RCon connection, these commands are typed exactly as shown).

Other Administrative Functions
------------------------------

When the game engine imports the ``default`` administrative module, one of the things the module does is to import the ``standard_admin`` module. When ``standard_admin`` is imported, it in turn imports and initializes two other modules:

-  ``standard_admin.autobalance``
-  ``standard_admin.tk_punish``
