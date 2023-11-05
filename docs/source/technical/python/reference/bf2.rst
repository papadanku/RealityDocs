
bf2
===

``bf2.GameStatus``
------------------

Just used as a container for the constant values returned by callbacks from the ``GameStatusChanged`` event:

-  ``bf2.GameStatus.Playing``
-  ``bf2.GameStatus.EndGame``
-  ``bf2.GameStatus.PreGame``
-  ``bf2.GameStatus.Paused``
-  ``bf2.GameStatus.RestartServer``
-  ``bf2.GameStatus.NotConnected``

You must ``import bf2`` to access these class attributes.

``bf2.GameLogic.GameLogic``
---------------------------

A wrapper around lots of BF2 engine stuff accessible through host, apparently to make it more Pythonic. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.gameLogic``.

You must ``import bf2`` to access the methods and attributes of this object.

Methods for the singleton object:

-  ``bf2.gameLogic.getModDir()``

-  ``bf2.gameLogic.getMapName()``

-  ``bf2.gameLogic.getWorldSize()``

   returns a tuple giving the north/south and east/west dimensions of the current map, more-or-less in meters.

-  ``bf2.gameLogic.getTeamName(team)``

-  ``bf2.gameLogic.isAIGame()``

-  ``bf2.gameLogic.sendClientCommand(playerId, command, args)``

   Appears to tell game engine to prompt a player for input; the player's response returns control to Python by generating a ```ClientCommand`` <../events.rst#command-events>`__ event; command is typically a numeric value, args can be anything, but is typically a tuple or list.

-  ``bf2.gameLogic.sendGameEvent(playerObject, event, data)``

   Tells the BF2 game engine to cause a [[GameEvent]] to occur.

-  ``bf2.gameLogic.sendMedalEvent(playerObject, type, value)``

-  ``bf2.gameLogic.sendRankEvent(playerObject, rank, score)``

-  ``bf2.gameLogic.sendHudEvent(playerObject, event, data)``

   Tells the BF2 game engine to cause a [[HudEvent]] to occur.

-  ``bf2.gameLogic.sendServerMessage(playerId, message)``

-  ``bf2.gameLogic.getTicketState(team)``

-  ``bf2.gameLogic.setTicketState(team, value)``

-  ``bf2.gameLogic.getTickets(team)``

-  ``bf2.gameLogic.setTickets(team, value)``

-  ``bf2.gameLogic.getDefaultTickets(team)``

-  ``bf2.gameLogic.getTicketChangePerSecond(team)``

-  ``bf2.gameLogic.setTicketChangePerSecond(team, value)``

-  ``bf2.gameLogic.getTicketLimit(team, id)``

-  ``bf2.gameLogic.setTicketLimit(team, id, value)``

-  ``bf2.gameLogic.getDefaultTicketLossPerMin(team)``

-  ``bf2.gameLogic.getDefaultTicketLossAtEndPerMin()``

-  ``bf2.gameLogic.getWinner()``

-  ``bf2.gameLogic.getVictoryType()``

-  ``bf2.gameLogic.setHealPointLimit(value)``

   Percentage heal required to trigger a ```PlayerHealPoint`` <../events.rst#player-events>`__ event.

-  ``bf2.gameLogic.setRepairPointLimit(value)``

   Percentage heal required to trigger a ```PlayerRepairPoint`` <../events.rst#player-events>`__ event.

-  ``bf2.gameLogic.setGiveAmmoPointLimit(value)``

   Percentage heal required to trigger a ```PlayerGiveAmmoPoint`` <../events.rst#player-events>`__ event.

-  ``bf2.gameLogic.setTeamDamagePointLimit(value)``

   Percentage heal required to trigger a ```PlayerTeamDamagePoint`` <../events.rst#player-events>`__ event.

-  ``bf2.gameLogic.setTeamVehicleDamagePointLimit(value)``

``bf2.GameLogic.ServerSettings``
--------------------------------

Another wrapper around more BF2 engine stuff that's accessible through host; this class makes it accessing these things cleaner and more Pythonic. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.serverSettings``.

You must ``import bf2`` to access the methods and attributes of this object.

Methods for the singleton object:

-  ``bf2.serverSettings.getTicketRatio()``
-  ``bf2.serverSettings.getTeamRatioPercent()``
-  ``bf2.serverSettings.getMaxPlayers()``
-  ``bf2.serverSettings.getGameMode()``
-  ``bf2.serverSettings.getMapName()``
-  ``bf2.serverSettings.getTimeLimit()``
-  ``bf2.serverSettings.getScoreLimit()``
-  ``bf2.serverSettings.getAutoBalanceTeam()``
-  ``bf2.serverSettings.getTKPunishEnabled()``
-  ``bf2.serverSettings.getTKNumPunishToKick()``
-  ``bf2.serverSettings.getTKPunishByDefault()``
-  ``bf2.serverSettings.getUseGlobalRank()``
-  ``bf2.serverSettings.getUseGlobalUnlocks()``

You cannot find out server name, port and other similar information this way. Instead, use f.e. ``host.rcon_invoke('sv.serverName')`` to get the server name.

``bf2.ObjectManager.ObjectManager``
-----------------------------------

During its initialization the bf2 class instantiates this class as the singleton object ``bf2.objectManager``. This object can be used by Python to get access to internal game engine C++ objects. A list of the available object types can be found [[Game Engine Object Types|here]], and a list of available object templates can be found [[Game Engine Object Templates|here]].

You must ``import bf2`` to access the methods and attributes of this object.

Methods for the singleton object:

-  ``bf2.objectManager.getObjectsOfType('object type')``
-  ``bf2.objectManager.getObjectsOfTemplate('object template')``

``bf2.PlayerManager.PlayerScore``
---------------------------------

Objects of this class maintain a long list of player score attributes. They are used inside of objects of the ``Player`` class; for any ``Player`` object x, ``x.score`` is an object of class ``PlayerScore``.

You will not normally create objects of this class; they are created automatically as part of the ``Player`` class when ``Player`` objects are created. No special imports are necessary to access methods and attributes of these objects.

There is also a separate ``player.stats`` object, which tracks different information. You can use the following code fragment to see all of the variables in the ``player.stats`` object.

.. code-block:: python

   for s in vars(player.stats):
      print str(s)

Class Methods
~~~~~~~~~~~~~

-  ``reset()``

   Resets all score attributes stored within the object itself.

Class attributes stored in the ``PlayerScore`` object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``index``

-  ``heals``

-  ``ammos``

-  ``repairs``

-  ``damageAssists``

-  ``passengerAssists``

-  ``driverAssists``

-  ``targetAssists``

-  ``driverSpecials``

-  ``revives``

-  ``teamDamages``

-  ``teamVehicleDamages``

-  ``cpCaptures``

-  ``cpDefends``

-  ``cpAssists``

-  ``suicides``

-  ``cpNeutralizes``

-  ``cpNeutralizeAssists``

-  ``rplScore``

   This attribute may not be in all versions of BF2

-  ``skillScore``

-  ``cmdScore``

Class attributes stored in the BF2 engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``deaths``

-  ``kills``

-  ``TKs``

-  ``score``

-  ``skillScore``

-  ``rplScore``

-  ``cmdScore``

-  ``fracScore``

-  ``rank``

-  ``firstPlace``

-  ``secondPlace``

-  ``thirdPlace``

-  ``bulletsFired``

   Gives a tuple, each element of which is a 2-tuple consisting of the name of a weapon the player has fired, and the number of shots they fired from that weapon. As the player uses more weapons, more of the 2-tuples are added to the list. An example tuple returned:

   ``(("uspi-m16", 30), ("knife", 3))``

   Before the first weapon is fired, this may be ``None`` or an empty tuple. The first weapon fired will not always be the first 2-tuple on the list returned.

-  ``bulletsGivingDamage``

   Same as above, but only with bullets giving damage

-  ``bulletsFiredAndClear``

   The “AndClear” resets the engine counter. polling this will only give new bullets. However having more than one module polling them is not a good idea.

-  ``bulletsGivingDamageAndClear``

Class attributes computed from other attribute values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``dkRatio``

.. _bf2-PlayerManager-Player:

``bf2.PlayerManager.Player``
----------------------------

An object of this class is created for each player in the game. When they are initialized, ``Player`` objects automatically instantiate a ``PlayerScore`` object and assign it to their score attribute.

You must ``import bf2.PlayerManager`` if you wish to create objects of this class; normally, however, you will just access methods and attributes of already existing ``Player`` objects that are returned to you by other calls, which requires no special import statement.

.. code-block:: python
   :caption: Instance creation

   x = bf2.PlayerManager.Player(index)

Class Attributes
~~~~~~~~~~~~~~~~

-  ``index``

   ``playerID`` for this player.

-  ``score``

   Current score for this player.

Class Methods
~~~~~~~~~~~~~

-  ``isValid()``

-  ``isRemote()``

-  ``isAIPlayer()``

-  ``isAlive()``

-  ``isManDown()``

-  ``isConnected()``

-  ``getProfileId()``

-  ``isFlagHolder()``

-  ``getTeam()``

-  ``setTeam(t)``

-  ``getPing()``

   Returns the player's ping (network transit time from player to server and back) in milliseconds

-  ``getSuicide()``

   Returns 1 if the player suicided. Resets once the player spawns.

-  ``setSuicide(t)``

-  ``getTimeToSpawn()``

   Returns 0 when a player is spawned in; when a player is waiting to spawn, it returns the number of seconds until they are allowed to spawn.

-  ``setTimeToSpawn(t)``

   Appears to generate an exception if used on a player that is already spawned in; if used on a player that that is waiting to spawn it changes the time until they are allowed to spawn.

-  ``getSquadId()``

   Returns the player's squad ID. Squads for each team are independently numbered beginning at 1 and increasing thereafter. Players not on a squad, including team commanders, are assigned to squad 0.

-  ``isSquadLeader()``

   Returns 1 if player is a squad leader.

-  ``isCommander()``

   Returns 1 if player is currently the commander.

-  ``getName()``

   Return's player's name

-  ``setName(name)``

   Sets a player's name (at least, it changes what ``getName()`` returns), but the change doesn't show up in-game–everything in the game still shows the player's old name.

   It is working, but only sees that player who connected after the name change.

-  ``getSpawnGroup()``

-  ``setSpawnGroup(t)``

-  ``getKit()``

   Returns the current player's kit object.

-  ``getVehicle()``

   Returns the current player's vehicle object. If the player is not in a vehicle at the time this returns the player's soldier object.

-  ``getDefaultVehicle()``

   Returns the player's soldier object, no matter what vehicle they are in.

-  ``getPrimaryWeapon()``

   Returns the weapon object for the player's currently selected weapon.

-  ``getAddress()``

   Returns player's IP address.

-  ``setIsInsideCP(val)``

-  ``getIsInsideCP()``

.. _bf2-playerManager-PlayerManager:

``bf2.PlayerManager.PlayerManager``
-----------------------------------

This class is a wraper around some player management functions in the BF2 engine, and also adds some simple calculations and logic to those functions. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.playerManager``.

You must ``import bf2`` to access the methods and attributes of this object.

Methods for the singleton object:

-  ``bf2.playerManager.getNumberOfPlayers()``

-  ``bf2.playerManager.getCommander(team)``

-  ``bf2.playerManager.getPlayers()``

-  ``bf2.playerManager.getPlayerByIndex(index)``

-  ``bf2.playerManager.getNextPlayer(index)``

-  ``bf2.playerManager.getNumberOfPlayersInTeam(team)``

-  ``bf2.playerManager.getNumberOfAlivePlayersInTeam(team)``

-  ``bf2.playerManager.enableScoreEvents()``

   Enables PlayerScore events

-  ``bf2.playerManager.disableScoreEvents()``

   Disables PlayerScore events

``bf2.Timer``
-------------

(Not available in PR, use the ``realitytimer`` below.)

Objects in this class are timers that can cause [[Event Reference#Timer Events|timer events]] to be generated when a fixed amount of time has elapsed.

.. code-block:: python
   :caption: Instance creation

   timer = bf2.Timer(timerEventHandler, delta, alwaysTrigger, data)

``timerEventHandler`` is the handler to be called when ``delta`` seconds have elapsed since the creation of the timer; ``alwaysTrigger`` should be ``1`` *(not sure what the alternative is)*. ``data`` is an optional item (typically a tuple) that will be passed to ``timerEventHandler``. (Note that even though ``data`` is optional when establishing a timer, the timerEventHandler must specify it as a parameter, or the handler won't work).

You must ``import bf2.Timer`` to create timer objects.

Class Methods
~~~~~~~~~~~~~

-  ``destroy()``

   Destroys the associated game engine timer (but not the Python instance.)

-  ``getTime()``

   Returns the :doc:`wall time <../../engine/time>` at which this timer will fire.

-  ``setTime(time)``

   Changes the :doc:`wall time <../../engine/time>` at which this timer will fire.

-  ``setRecurring(interval)``

   Specifies this this timer should fire repeatedly, every interval seconds.

-  ``onTrigger()``

   For internal use only; calls ``timerEventHandler``.

Project Reality Timer interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project Reality timer (``realitytimer.py``) expands the default interface and adds:

-  Exception catching with a debug message when an exception is not caught in the handler

   No need to worry about bad code crashing the server.

-  Internal check to make sure timers don't fire after destroy() was called

   Can happen when ``Destroy()`` is called on the same tick

-  ``realitytimer.fireOnce(targetFunc, delay, data=None)`` class that can fire an event once after delay and then destroy itself

   No need to store reference

-  ``realitytimer.fireNextTick(targetFunc, data=None)`` class that will fire the event at the next game tick and then destroy itself

   Also no need to store

``bf2.TriggerManager.TriggerManager``
-------------------------------------

This class is a wraper around some player management functions in the BF2 engine. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.triggerManager``. This object is used to manage “triggers”, which are events that are fired when a PCO enters a defined spherical or hemispherical volume surrounding an object.

You must ``import bf2`` to access the methods and attributes of this object.

Methods for the singleton object:

-  ``bf2.triggerManager.createRadiusTrigger(object, callback, objName, radius, data=None)``

   Creates a trigger that causes ``callback`` to be called if a player enters a spherical region of radius ``radius`` centered on ``object``, passing ``data`` as an argument.

-  ``bf2.triggerManager.createHemiSphericalTrigger(object, callback, objName, radius, data=None)``

   Same as ``bf2.triggerManager.createRadiusTrigger``, except that instead of a spherical trigger region, the trigger region is a flat circle lying along the ground (yes, it's badly named).

-  ``bf2.triggerManager.destroyAllTriggers()``

   Destroys all registered triggers.

-  ``bf2.triggerManager.destroy(trig_id)``

   Destroys a specific trigger.

-  ``getObjects(trig_id)``

   Returns a tuple containing all objects currently within the specified trigger region.

``bf2.stats.constants``
-----------------------

This module appears intended to be imported with something like

.. code-block:: python

   from bf2.stats.constants import *

so that everything in it is loaded into the local namespace, rather than being a part of any object. The module includes a lot of constants and dictionaries, as well as some utility functions.

Functions
~~~~~~~~~

-  ``getVehicleType(templateName)``

-  ``getWeaponType(templateName)``

-  ``getKitType(templateName)``

-  ``getArmy(templateName)``

-  ``getMapId(mapName)``

-  ``getGameModeId(gameMode)``

-  ``getRootParent(physicalObject)``

   Traverses the containment for physicalObject all the way to the top; returns the outermost (topmost?) containing object.

For example, ``getWeaponType("usrif_m16a2")`` looks up an M16 rifle in a dictionary called ``weaponTypeMap`` (also defined in ``bf2.stats.constants``) and returns the constant ``WEAPON_TYPE_ASSAULT``\ … which, too, is defined in ``bf2.stats.constants``, as having a numeric value of “0”. A list of template names used in some of these functions can be found in the [[Game Engine Object Templates]] page.

These constant values appear to be the same as those used in the [[BF2Stats|statistics server]], specifically the [[BF2Stats_LookUp_Values|look up values]].
