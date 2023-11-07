
Player Identity
===============

There are several ways a player's identity can be represented in Battlefield 2; this page discusses them, explains some of their different uses, and shows how to access them and convert one to another.

Player ID (index)
-----------------

``Player ID`` ("playerID", also known as "index") is the simplist and most basic way of identifying players, and is the most commonly used throughout the game. The first player to connect to the server is given a Player ID of "0"; the second gets a Player ID of "1", and so on. At the beginning of the next round the server goes through and re-assigns Player IDs for each player, again beginning at 0, so as to fill in any "holes" in the numbering system created by players who have disconnected.

Most :doc:`console commands <../modding/consolecommands>` that refer to players use Player ID: for example, ``admin.kickPlayer`` is followed by a Player ID number. The easiest way to find out which player has which Player ID from the console is to use the ``admin.listplayers`` command.

From Python, several methods are available access information about a player based on Player ID, for example :py:meth:`bf2.playerManager.getPlayerByIndex` will take a playerID and return the associated playerObject.

Player Name
-----------

This is the name that shows up in the colored "name tag" above each player's head in the BF2 game world, and is also the same as the "account name" that players log into BF2 with. Because players must create an account in order to log in for multiplayer internet play, EA's account management system insures that each Player Name is unique. On the other hand, there is nothing to stop a single player from signing up with many different Player Names.

.. code-block:: python
   :caption: How to find a player's name from their Player Object

      playerObject.getName()

As of BF2 version 1.03, this will return the player's name AND their 'prefix', which is an arbitrary tag, 6 letters in length. RegEx ``\S{0,6}\s`` will match the entire prefix of a playername for stripping or whatnot. Less precise, but just as effective: ``\S.*?\s``

Player Object
-------------

Player Objects ("playerObjects") are instances of the :py:class:`bf2.PlayerManager.Player` class, and each of them encapsulate and provide access to much of the information about a specific connected player. PlayerObjects exist from the time a player first connects to a running BF2 server until that server shuts down-even if a player disconnects, BF2 retains his or her Player Object, and if the same player later reconnects to the server, BF2 attempts to reassociate the player with the same Player Object.

If you want to know the name, score, ping, or other properties of a player, you use methods of the their Player Object.

Soldier Object
--------------

Player Objects are abstractions in the BF2 world-they can be thought of as corresponding to the "spirit" or "ghost" of a player. Soldier Objects ("soldierObjects"), on the other hand, are instances of the :py:class:`soldierObject` class, and correspond to "physical" objects in the BF2 world, complete with geographic coordinates, orientation, the ability to contain, and be contained by, other physical objects, etc. When a player spawns into a game, a new Soldier Object is created, and their Player Object becomes associated with it. When a player dies, the Soldier Object is destroyed, but the Player Object continues to exist, until the player spawns into the game again.

If you want to know the location of a player, their current kit and weapon (contained "child" objects), or what vehicle their are riding in (a containing "parent" object), you look at the player's Soldier Object.

.. code-block:: python
   :caption: How find which Soldier Object corresponds to a specific spawned-in player from their Player Object

      playerObject.getVehicle()

Other than searching through all possible players, there is no known way to go directly from a Soldier Object to it's corresponding Player Object. Instead, most of the :doc:`game events <../python/reference/events>` for which you would want to do this send **both** the relevent Player Object and Soldier Object in their callbacks.

PlayerID (Hash)
---------------

PlayerID, formerly and known as CDKey and hash, not to be confused with index PlayerID.

This number uniquely identifies players to the master server. Each Steam login is associated with a 32 digit 128-bit hexidecimal number. On logging into the PR server, the MSProxy_ contacts the master server and authenticates the users account, and will pass back a verified or unverified value to the proxy. The PlayerID is entered into logs in the connection, banlog and banlist, and is used to identify accounts with multiple usernames. The commands !banid, !timebanid and !unbanid take a PlayerID to manually ban or unban a player.

.. _MSProxy: https://gitlab.com/realitymod/public/prserverproxy/

In Python, PlayerId is available through realityserver.getPlayerHash(player), and is primarily used in the bansystem.

Example hash: ``ec74c4b5dcc40a1962cfd61e1d062ea3``

IP Address
----------

The `IP address <https://en.wikipedia.org/wiki/IP_address>`__ is the address of a particular computer on a network, such as ``192.168.100.1``. Generally speaking, a player's IP address can be used as a way to identify their computer (similar to how CD key hash can be used), as well as to tell something about their location-which country they are in, for example. In practice, care must be used in these applications because many internet service providers use `NAT <https://en.wikipedia.org/wiki/Network_address_translation>`__ to dynamically change their customers' IP addresses from day to day; AOL is the worst, changing addresses from one connection to the next! If you ban or kick a player based on their IP address, they may well reconnect to your server a few minutes later with a different IP address.

.. code-block:: python
   :caption: How to access the IP address a player is using from their Player Object

      playerObject.getAddress()
