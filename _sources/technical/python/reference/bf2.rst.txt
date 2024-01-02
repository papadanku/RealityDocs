
bf2
===

.. py:class:: bf2.GameStatus

   Just used as a container for the constant values returned by callbacks from the ``GameStatusChanged`` event

   .. py:attribute:: Playing
   .. py:attribute:: EndGame
   .. py:attribute:: PreGame
   .. py:attribute:: Paused
   .. py:attribute:: RestartServer
   .. py:attribute:: NotConnected

   You must ``import bf2`` to access these class attributes.

.. py:class:: bf2.GameLogic.GameLogic

   A wrapper around lots of BF2 engine stuff accessible through host, apparently to make it more Pythonic. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.gameLogic``.

   You must ``import bf2`` to access the methods and attributes of this object.

   .. py:method:: getModDir()
   .. py:method:: getMapName()
   .. py:method:: getWorldSize()

      :return: A tuple giving the north/south and east/west dimensions of the current map, more-or-less in meters.

   .. py:method:: getTeamName(team)
   .. py:method:: isAIGame()
   .. py:method:: sendClientCommand(playerId, command, args)

      Appears to tell game engine to prompt a player for input; the player's response returns control to Python by generating a ```ClientCommand`` <../events.rst#command-events>`_ event; command is typically a numeric value, args can be anything, but is typically a tuple or list.

   .. py:method:: sendGameEvent(playerObject, event, data)

      Tells the BF2 game engine to cause a :ref:`GameEvent <game-events>` to occur.

   .. py:method:: sendMedalEvent(playerObject, type, value)
   .. py:method:: sendRankEvent(playerObject, rank, score)
   .. py:method:: sendHudEvent(playerObject, event, data)

      Tells the BF2 game engine to cause a :doc:`HudEvent <hud>` to occur.

   .. py:method:: sendServerMessage(playerId, message)
   .. py:method:: getTicketState(team)
   .. py:method:: setTicketState(team, value)
   .. py:method:: getTickets(team)
   .. py:method:: setTickets(team, value)
   .. py:method:: getDefaultTickets(team)
   .. py:method:: getTicketChangePerSecond(team)
   .. py:method:: setTicketChangePerSecond(team, value)
   .. py:method:: getTicketLimit(team, id)
   .. py:method:: setTicketLimit(team, id, value)
   .. py:method:: getDefaultTicketLossPerMin(team)
   .. py:method:: getDefaultTicketLossAtEndPerMin()
   .. py:method:: getWinner()
   .. py:method:: getVictoryType()
   .. py:method:: setHealPointLimit(value)

      Percentage heal required to trigger a ```PlayerHealPoint`` <../events.rst#player-events>`_ event.

   .. py:method:: setRepairPointLimit(value)

      Percentage heal required to trigger a ```PlayerRepairPoint`` <../events.rst#player-events>`_ event.

   .. py:method:: setGiveAmmoPointLimit(value)

      Percentage heal required to trigger a ```PlayerGiveAmmoPoint`` <../events.rst#player-events>`_ event.

   .. py:method:: setTeamDamagePointLimit(value)

      Percentage heal required to trigger a ```PlayerTeamDamagePoint`` <../events.rst#player-events>`_ event.

   .. py:method:: setTeamVehicleDamagePointLimit(value)

.. py:class:: bf2.GameLogic.ServerSettings

   Another wrapper around more BF2 engine stuff that's accessible through host; this class makes it accessing these things cleaner and more Pythonic. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.serverSettings``.

   You must ``import bf2`` to access the methods and attributes of this object.

   .. py:method:: getTicketRatio()
   .. py:method:: getTeamRatioPercent()
   .. py:method:: getMaxPlayers()
   .. py:method:: getGameMode()
   .. py:method:: getMapName()
   .. py:method:: getTimeLimit()
   .. py:method:: getScoreLimit()
   .. py:method:: getAutoBalanceTeam()
   .. py:method:: getTKPunishEnabled()
   .. py:method:: getTKNumPunishToKick()
   .. py:method:: getTKPunishByDefault()
   .. py:method:: getUseGlobalRank()
   .. py:method:: getUseGlobalUnlocks()

   You cannot find out server name, port and other similar information this way. Instead, use f.e. ``host.rcon_invoke('sv.serverName')`` to get the server name.

.. py:class:: bf2.ObjectManager.ObjectManager

   During its initialization the bf2 class instantiates this class as the singleton object ``bf2.objectManager``. This object can be used by Python to get access to internal game engine C++ objects. A list of the available object types can be found :doc:`here <../../engine/objecttemplates>`.

   You must ``import bf2`` to access the methods and attributes of this object.

   .. py:method:: getObjectsOfType(object type)
   .. py:method:: getObjectsOfTemplate(object template)

.. py:class:: bf2.PlayerManager.PlayerScore

   Objects of this class maintain a long list of player score attributes. They are used inside of objects of the ``Player`` class; for any ``Player`` object x, ``x.score`` is an object of class ``PlayerScore``.

   You will not normally create objects of this class; they are created automatically as part of the ``Player`` class when ``Player`` objects are created. No special imports are necessary to access methods and attributes of these objects.

   There is also a separate ``player.stats`` object, which tracks different information. You can use the following code fragment to see all of the variables in the ``player.stats`` object.

   .. code-block:: python

      for s in vars(player.stats):
         print str(s)

   .. py:method:: reset()

      Resets all score attributes stored within the object itself.

   .. py:attribute:: index
   .. py:attribute:: heals
   .. py:attribute:: ammos
   .. py:attribute:: repairs
   .. py:attribute:: damageAssists
   .. py:attribute:: passengerAssists
   .. py:attribute:: driverAssists
   .. py:attribute:: targetAssists
   .. py:attribute:: driverSpecials
   .. py:attribute:: revives
   .. py:attribute:: teamDamages
   .. py:attribute:: teamVehicleDamages
   .. py:attribute:: cpCaptures
   .. py:attribute:: cpDefends
   .. py:attribute:: cpAssists
   .. py:attribute:: suicides
   .. py:attribute:: cpNeutralizes
   .. py:attribute:: cpNeutralizeAssists
   .. py:attribute:: rplScore

      This attribute may not be in all versions of BF2

   .. py:attribute:: skillScore
   .. py:attribute:: cmdScore

Class attributes stored in the BF2 engine

- ``deaths``
- ``kills``
- ``TKs``
- ``score``
- ``skillScore``
- ``rplScore``
- ``cmdScore``
- ``fracScore``
- ``rank``
- ``firstPlace``
- ``secondPlace``
- ``thirdPlace``
- ``bulletsFired``

   Gives a tuple, each element of which is a 2-tuple consisting of the name of a weapon the player has fired, and the number of shots they fired from that weapon. As the player uses more weapons, more of the 2-tuples are added to the list. An example tuple returned:

   ``(("uspi-m16", 30), ("knife", 3))``

   Before the first weapon is fired, this may be ``None`` or an empty tuple. The first weapon fired will not always be the first 2-tuple on the list returned.

- ``bulletsGivingDamage``

   Same as above, but only with bullets giving damage

- ``bulletsFiredAndClear``

   The “AndClear” resets the engine counter. polling this will only give new bullets. However having more than one module polling them is not a good idea.

- ``bulletsGivingDamageAndClear``
- ``dkRatio``

.. py:class:: bf2.PlayerManager.Player

   An object of this class is created for each player in the game. When they are initialized, ``Player`` objects automatically instantiate a ``PlayerScore`` object and assign it to their score attribute.

   You must ``import bf2.PlayerManager`` if you wish to create objects of this class; normally, however, you will just access methods and attributes of already existing ``Player`` objects that are returned to you by other calls, which requires no special import statement.

   .. code-block:: python
      :caption: Instance creation

      x = bf2.PlayerManager.Player(index)

   .. py:attribute:: index

      ``playerID`` for this player.

   .. py:attribute:: score

      Current score for this player.

   .. py:method:: isValid()
   .. py:method:: isRemote()
   .. py:method:: isAIPlayer()
   .. py:method:: isAlive()
   .. py:method:: isManDown()
   .. py:method:: isConnected()
   .. py:method:: getProfileId()
   .. py:method:: isFlagHolder()
   .. py:method:: getTeam()
   .. py:method:: setTeam(t)
   .. py:method:: getPing()

      :return: The player's ping (network transit time from player to server and back) in milliseconds

   .. py:method:: getSuicide()

      :return: `1` if the player suicided. Resets once the player spawns.

   .. py:method:: setSuicide(t)
   .. py:method:: getTimeToSpawn()

      :return: `0` when a player is spawned in; when a player is waiting to spawn, it returns the number of seconds until they are allowed to spawn.

   .. py:method:: setTimeToSpawn(t)

      Appears to generate an exception if used on a player that is already spawned in; if used on a player that that is waiting to spawn it changes the time until they are allowed to spawn.

   .. py:method:: getSquadId()

      :return: The player's squad ID. Squads for each team are independently numbered beginning at 1 and increasing thereafter. Players not on a squad, including team commanders, are assigned to squad 0.

   .. py:method:: isSquadLeader()

      :return: `1` if player is a squad leader.

   .. py:method:: isCommander()

      :return: `1` if player is currently the commander.

   .. py:method:: getName()

      :return: Player's name

   .. py:method:: setName(name)

      Sets a player's name (at least, it changes what ``getName()`` returns), but the change doesn't show up in-game–everything in the game still shows the player's old name.

      It is working, but only sees that player who connected after the name change.

   .. py:method:: getSpawnGroup()
   .. py:method:: setSpawnGroup(t)
   .. py:method:: getKit()

      :return: The current player's kit object.

   .. py:method:: getVehicle()

      :return: The current player's vehicle object. If the player is not in a vehicle at the time this returns the player's soldier object.

   .. py:method:: getDefaultVehicle()

      :return: The player's soldier object, no matter what vehicle they are in.

   .. py:method:: getPrimaryWeapon()

      :return: The weapon object for the player's currently selected weapon.

   .. py:method:: getAddress()

      :return: The player's IP address.

   .. py:method:: setIsInsideCP(val)
   .. py:method:: getIsInsideCP()

.. py:class:: bf2.PlayerManager

   This class is a wrapper around some player management functions in the BF2 engine, and also adds some simple calculations and logic to those functions. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.playerManager``.

   You must ``import bf2`` to access the methods and attributes of this object.

   .. py:method:: getNumberOfPlayers()
   .. py:method:: getCommander(team)
   .. py:method:: getPlayers()
   .. py:method:: getPlayerByIndex(index)
   .. py:method:: getNextPlayer(index)
   .. py:method:: getNumberOfPlayersInTeam(team)
   .. py:method:: getNumberOfAlivePlayersInTeam(team)
   .. py:method:: enableScoreEvents()

      Enables PlayerScore events

   .. py:method:: disableScoreEvents()

      Disables PlayerScore events

.. py:class:: bf2.Timer

   (Not available in PR, use the ``realitytimer`` below.)

   Objects in this class are timers that can cause :ref:`timer events <timer-events>` to be generated when a fixed amount of time has elapsed.

   .. py:method:: bf2.Timer(timerEventHandler, delta, alwaysTrigger, data)

      - Note that even though ``data`` is optional when establishing a timer, the timerEventHandler must specify it as a parameter, or the handler won't work.
      - You must ``import bf2.Timer`` to create timer objects.

      :param timerEventHandler: Handler to be called when ``delta`` seconds have elapsed since the creation of the timer.
      :param alwaysTrigger: Should be 1 *(not sure what the alternative is)*
      :param data: Optional item (typically a tuple) that will be passed to ``timerEventHandler``.

   .. py:method:: destroy()

      Destroys the associated game engine timer (but not the Python instance.)

   .. py:method:: getTime()

      :return: The :doc:`wall time <../../engine/time>` at which this timer will fire.

   .. py:method:: setTime(time)

      Changes the :doc:`wall time <../../engine/time>` at which this timer will fire.

   .. py:method:: setRecurring(interval)

      Specifies this this timer should fire repeatedly, every interval seconds.

   .. py:method:: onTrigger()

      For internal use only; calls ``timerEventHandler``.

.. py:class:: realitytimer.py

   Project Reality timer (``realitytimer.py``) expands the default interface with the following:

   - Exception catching with a debug message when an exception is not caught in the handler

      No need to worry about bad code crashing the server.

   - Internal check to make sure timers don't fire after :py:meth:`bf2.Timer.destroy` was called

      Can happen when :py:meth:`bf2.Timer.destroy` is called on the same tick

   .. py:method:: fireOnce(targetFunc, delay, data=None)

      Class that can fire an event once after delay and then destroy itself. No need to store reference.

   .. py:method:: fireNextTick(targetFunc, data=None)

      Class that will fire the event at the next game tick and then destroy itself. No need to store reference

.. py:class:: bf2.TriggerManager.TriggerManager

   This class is a wraper around some player management functions in the BF2 engine. During its initialization the bf2 class instantiates this class as the singleton object ``bf2.triggerManager``. This object is used to manage “triggers”, which are events that are fired when a PCO enters a defined spherical or hemispherical volume surrounding an object.

   You must ``import bf2`` to access the methods and attributes of this object.

   .. py:method:: createRadiusTrigger(object, callback, objName, radius, data=None)

      Creates a trigger that causes ``callback`` to be called if a player enters a spherical region of radius ``radius`` centered on ``object``, passing ``data`` as an argument.

   .. py:method:: createHemiSphericalTrigger(object, callback, objName, radius, data=None)

      Same as :py:meth:`createRadiusTrigger`, except that instead of a spherical trigger region, the trigger region is a flat circle lying along the ground (yes, it's badly named).

   .. py:method:: destroyAllTriggers()

      Destroys all registered triggers.

   .. py:method:: destroy(trig_id)

      Destroys a specific trigger.

   .. py:method:: getObjects(trig_id)

      :return: A tuple containing all objects currently within the specified trigger region.

.. py:class:: bf2.stats.constants

   This module appears intended to be imported with something like...

   .. code-block:: python

      from bf2.stats.constants import *

   ... so that everything in it is loaded into the local namespace, rather than being a part of any object. The module includes a lot of constants and dictionaries, as well as some utility functions.

   .. py:method:: getVehicleType(templateName)
   .. py:method:: getWeaponType(templateName)
   .. py:method:: getKitType(templateName)
   .. py:method:: getArmy(templateName)
   .. py:method:: getMapId(mapName)
   .. py:method:: getGameModeId(gameMode)
   .. py:method:: getRootParent(physicalObject)

      Traverses the containment for physicalObject all the way to the top

      For example, ``getWeaponType("usrif_m16a2")`` looks up an M16 rifle in a dictionary called ``weaponTypeMap`` (also defined in :py:class:`bf2.stats.constants`) and returns the constant ``WEAPON_TYPE_ASSAULT``\ … which, too, is defined in :py:class:`bf2.stats.constants`, as having a numeric value of “0”. A list of template names used in some of these functions can be found in the :doc:`Game Engine Object Templates <../../engine/objecttemplates>` page.

      :return: The outermost (topmost?) containing object.
