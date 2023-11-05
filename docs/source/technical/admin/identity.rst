
Player Identity
===============

There are several ways a player's identity can be represented in Battlefield 2; this page discusses them, explains some of their different uses, and shows how to access them and convert one to another.

Player ID
---------

``Player ID`` ("playerID", also known as "index") is the simplist and most basic way of identifying players, and is the most commonly used throughout the game. The first player to connect to the server is given a Player ID of "0"; the second gets a Player ID of "1", and so on. At the beginning of the next round the server goes through and re-assigns Player IDs for each player, again beginning at 0, so as to fill in any "holes" in the numbering system created by players who have disconnected.

Most :doc:`console commands <../modding/consolecommands>` that refer to players use Player ID: for example, ``admin.kickPlayer`` is followed by a Player ID number. The easiest way to find out which player has which Player ID from the console is to use the ``admin.listplayers`` command.

From Python, several methods are available access information about a player based on Player ID, for example :ref:`bf2.playerManager.getPlayerByIndex <bf2-playerManager-PlayerManager>` will take a playerID and return the associated playerObject.

Player Name
-----------

This is the name that shows up in the colored "name tag" above each player's head in the BF2 game world, and is also the same as the "account name" that players log into BF2 with. Because players must create an account in order to log in for multiplayer internet play, EA's account management system insures that each Player Name is unique. On the other hand, there is nothing to stop a single player from signing up with many different Player Names.

.. code-block:: python
   :caption: How to find a player's name from their Player Object

      playerObject.getName()

As of BF2 version 1.03, this will return the player's name AND their 'prefix', which is an arbitrary tag, 6 letters in length. RegEx ``\S{0,6}\s`` will match the entire prefix of a playername for stripping or whatnot. Less precise, but just as effective: ``\S.*?\s``

Player Object
-------------

Player Objects ("playerObjects") are instances of the :ref:`bf2.PlayerManager.Player <bf2-PlayerManager-Player>` class, and each of them encapsulate and provide access to much of the information about a specific connected player. PlayerObjects exist from the time a player first connects to a running BF2 server until that server shuts down-even if a player disconnects, BF2 retains his or her Player Object, and if the same player later reconnects to the server, BF2 attempts to reassociate the player with the same Player Object.

If you want to know the name, score, ping, or other properties of a player, you use methods of the their Player Object.

Soldier Object
--------------

Player Objects are abstractions in the BF2 world-they can be thought of as corresponding to the "spirit" or "ghost" of a player. Soldier Objects ("soldierObjects"), on the other hand, are instances of the :ref:`SoldierObject` class, and correspond to "physical" objects in the BF2 world, complete with geographic coordinates, orientation, the ability to contain, and be contained by, other physical objects, etc. When a player spawns into a game, a new Soldier Object is created, and their Player Object becomes associated with it. When a player dies, the Soldier Object is destroyed, but the Player Object continues to exist, until the player spawns into the game again.

If you want to know the location of a player, their current kit and weapon (contained "child" objects), or what vehicle their are riding in (a containing "parent" object), you look at the player's Soldier Object.

.. code-block:: python
   :caption: How find which Soldier Object corresponds to a specific spawned-in player from their Player Object

      playerObject.getVehicle()

Other than searching through all possible players, there is no known way to go directly from a Soldier Object to it's corresponding Player Object. Instead, most of the :doc:`game events <../python/reference/events>` for which you would want to do this send **both** the relevent Player Object and Soldier Object in their callbacks.

Profile ID
----------

Profile ID is a `GameSpy <https://www.gamespy.net/>`__ ID number that is unique to a specific BF2 player login; no matter what computer, no matter what CD key, no matter what server that player uses, if they login with the same name and password, they will be assigned the same Profile ID. Profile ID can therefore be used to uniquely identify particular players, and is the basis for the EA ranking system: player statistics are tracked by Profile ID.

.. code-block:: python
   :caption: How to retrieve the Profile ID for a player

      playerObj.getProfileId()

The profile ID is also stored between the square brackets on the 2nd line of the "gp.info" file, which resides in the root of the BF2 client folder. Note that the file is cumulative so it may contain the info for all the players that have been using the client computer; if so then each player info block is separated by a blank line. \-\-- Dimmer (2005-07-29)

CD Key Hash
-----------

As part of the BF2 client installation process, the user must enter a "CD key" that was provided along with their copy of the game, along with their CDs or DVD. The CD key is supposed to be unique to one specific copy of the game; more than one game can be installed with the same CD key, but EA has various anti-piracy safeguards that will block game copies with duplicate CD keys from functioning in most cases.

Because the CD key uniquely (for the most part) identifies a particular computer and not any particular player, it can be a useful tool-for example, as a way to ban jerks (*smaktards*, in technical language) from a server, so that they will be blocked regardless of what login (Profile ID) they use.

For security reasons, a player's CD key is never accessible within BF2, but for virtually all purposes, their "CD key hash", which is available, serves just as well. This "hash" uses the obsolete `MD5 <https://en.wikipedia.org/wiki/MD5>`__ algorithm to create a `crytographic hash <https://en.wikipedia.org/wiki/Cryptographic_hash_function>`__ of the player's CD key (after removing any dashes, and converting it to upper-case). CD key hashes in BF2 are 128-bit numbers, which are typically represented in `hexadecimal <https://en.wikipedia.org/wiki/Hexadecimal>`_; for example: ``5e851bd2ce31a2b885266537a9c704aa``

There is no built-in means of determining a player's CD key hash, but the [playerData](Cookbook:Accessing_CD_Key_Hash "wikilink") function provides a quick and easy way to get at it. Conversely, the [keyHash](Cookbook:Computing_CD_Key_Hashes "wikilink") function provides an easy way to convert a CD key into it's corresponding hash; if you just want to find out what your own key hash is, the fastest way to do that is to use this standalone [key-hashing program](BF2_Key_Hasher "wikilink").

IP Address
----------

[IP address](wikipedia:IP_Address "wikilink") is the address of a particular computer on a network, such as "``192.168.100.1``". Generally speaking, a player's IP address can be used as a way to identify their computer (similar to how CD key hash can be used), as well as to tell something about their location-which country they are in, for example. In practice, care must be used in these applications because many internet service providers use `NAT <https://en.wikipedia.org/wiki/Network_address_translation>`__ to dynamically change their customers' IP addresses from day to day; AOL is the worst, changing addresses from one connection to the next! If you ban or kick a player based on their IP address, they may well reconnect to your server a few minutes later with a different IP address.

.. code-block:: python
   :caption: How to access the IP address a player is using from their Player Object

      playerObject.getAddress()

You can also use the [playerData](Scripts:playerData "wikilink") function to retrieve the same information, along with [CD key hashes](Player_Identity#CD_Key_Hash "wikilink").

PunkBuster GUID 
---------------

The `PunkBuster <http://www.evenbalance.com/index.php?page=support-bf2.php>`__ anti-cheating system is built into Battlefield 2. PunkBuster assigns a "Globally Unique ID", or GUID, to each user, and uses this for the purpose of tracking and banning players that it detects cheating. In principle, GUIDs are pretty much the same thing as BF2's [CD key hashes](Player_Identity#CD_Key_Hash "wikilink"), but appear to initialize the MD5 algorithm differently. For all practical purposes, you can think of a player's GUID as just being a second (and different) CD key hash. Just like CD key hashes, they uniquely identify installed copies of BF2, and so can be used for all the same purposes as CD key hashes.

PunkBuster GUIDs for players on a server can easily be determined by using the ``pb_sv_plist`` command from the console. Unfortunately, the "wiring" between BF2 and PunkBuster is such that RCon clients and Python scripts trying to run this command cannot receive any data back; there is therefore no way at present to access GUID information from within a script or from RCon.
