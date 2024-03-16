
Events
======

The interaction between the BF2 engine and Python programs is largely `event-driven <https://en.wikipedia.org/wiki/Event-driven_programming>`_: when an “event” happens in a game, BF2 checks to see if any Python programs have registered to be notified of that particular event; if they have, they are called (a “callback”). One way to think about this: the events are “hooks” into the game engine to which you can attach your own Python code.

Multiple callbacks can be registered for any given event; all registered callbacks will be executed when the event occurs. For example, if three different programs have registered for the “PlayerConnect” event, then when a new player connects, all three of those programs will be run.

Types of Events
---------------

The BF2 engine supports five types of events

Standard Events
~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: These are events that occur during the normal course of gameplay

      host.registerHandler('EventName', pythonEventHandler[, parameter])

This registration will typically be done in the init() method of an object, but could be done anywhere in your code.

Game Status Events
~~~~~~~~~~~~~~~~~~

The BF2 engine generates these events when the status of the game changes.

.. code-block:: python
   :caption: You register to receive callbacks for these events

      host.registerGameStatusHandler(pythonEventHandler)

The possible states game status can be in (as enumerated in :py:class:`bf2.GameStatus`) are:

- NotConnected
- PreGame
- Playing
- Paused
- EndGame
- RestartServer

Game status events are usually used to kick off pre-game initialization or post-game clean-up processing.

Trigger Events
~~~~~~~~~~~~~~

“Trigger” events activate when a vehicle comes within a specified distance of an object.

.. code-block:: python
   :caption: Triggers are created and registered for by” bf2.triggerManager.

      createHemiSphericalTrigger(object, triggerEventHandler, objectName, radius[, data])

      bf2.triggerManager.createRadiusTrigger(object, triggerEventHandler, objectName, radius[, data])

In standard Battlefield 2, trigger events are used to track scoring for flag captures (triggers activate whenever a player enters or leaves a fixed radius around each control point), as well as effects such as birds (birds are triggered to take flight whenever a player enter their trigger radius).

.. _timer-events:

Timer Events
~~~~~~~~~~~~

.. py:currentmodule:: host

.. py:method:: bf2.Timer(timerEventHandler, delta, alwaysTrigger[, data])

   Timer events activate when a certain amount of time has elapsed.

   In standard Battlefield 2, timer events are used to cause periodic status checks related to scoring, ranking, punishing TKs, etc.

   See the description of the :py:class:`bf2.Timer` class for details.

Descriptions of Events
----------------------

EA/DICE have not published a list of events, but here is a list of events that have been discovered so far.

.. py:function:: EventName(handlerParameter1, handlerParameter2, ...)

   The ``EventName`` is the name of the event to register for with host. ``registerHandler``; the parameters are the parameters your handler should receive when called.

   :param playerObject: An instance of :py:class:`bf2.PlayerManager.Player`
   :param playerID: As players connect to the server they are assigned playerID numbers from “1” up
   :param int squadID: Squads for each side are independently numbered beginning at “1” and increasing thereafter. Players not on a squad, including team commanders, are assigned to squad “0”
   :param int teamID: 0 for US, 1 for China or MEC

Server Events
~~~~~~~~~~~~~

.. py:function:: ServerReady()

   TBD

.. py:function:: BeginRound()

   TBD

.. py:function:: EndRound()

   TBD

Player Events
~~~~~~~~~~~~~

.. py:function:: PlayerConnect(playerObject)

   Fires when a player connects to the game.

.. py:function:: PlayerSpawn(playerObject, soldierObject)

   Occurs when a player spawns, and associates a :py:class:`playerObject` “spirit” with a :py:class:`soldierObject` “body”.

.. py:function:: PlayerChangeTeams(playerObject, humanHasSpawned)

   :param humanHasSpawned: 1 if the player the event is firing for is a human (as opposed to an AI). Does not fire due to team change from “setTeam”!

.. py:function:: PlayerChangeWeapon(playerObject, oldWeaponObject, newWeaponObject)

   Player has changed which weapon they are holding.

.. py:function:: PlayerChangedSquad(playerObject, oldSquadID, newSquadID)

   ``SquadID`` is 0 for players who are not members of any squad (including the team commander).

.. py:function:: PlayerScore(playerObject, difference)

   Difference is change to player's score (positive or negative).

.. py:function:: PlayerHealPoint(givingPlayerObject, receivingSoldierObject)

   Occurs whenever a player heals another player; there is no indication of how much health was restored.

.. py:function:: PlayerRepairPoint(givingPlayerObject, receivingVehicleObject)

   Occurs whenever a player repairs a vehicle; there is no indication of how much damage was repaired.

.. py:function:: PlayerGiveAmmoPoint(givingPlayerObject, receivingPhysicalObject)

   Occurs whenever a player replenishes the ammo in another player or vehicle. There is no indication of how much ammo was replenished.

.. py:function:: PlayerTeamDamagePoint(playerObject, victimSoldierObject)

   Occurs whenever a player damages another player on their own team. There is no indication of how much damage was done.

.. py:function:: PlayerKilled(victimPlayerObject, attackerPlayerObject, weaponObject, assists, victimSoldierObject)

   This event occurs when a player is “critically injured”, but still capable of being revived. If any players assisted in the kill, then “assists” will be a tuple of tuples: the top-level tuple will contain one lower-level tuple for each assisting player; the lower-level tuples will each have two elements: a :py:class:`playerObject` for one of the assisting players, and a number indicating the type of assist (1=targeting assist, 2=kill damage assist, 3=driver assist).

.. py:function:: PlayerRevived(revivedPlayerObject, medicPlayerObject)

   Player has been revived from a “critically injured” condition to full health by a medic using “shock paddles”. Players can only be revived in the interval between a :py:func:`PlayerKilled` event and a subsequent :py:func:`PlayerDeath` event.

.. py:function:: PlayerDeath(playerObject, soldierObject)

   This event occurs when a player is decisively dead, and cannot be revived; they will only return to the game by respawning. :py:class:`soldierObject` is the soldier “body” (which is now discarded) for the :py:class:`playerObject` “spirit” (which will persist through the next spawn).

.. py:function:: PlayerBanned(playerObject, time, type)

   TBD

.. py:function:: PlayerKicked(playerObject)

   Player has been kicked off the server.

.. py:function:: PlayerDisconnect(playerObject)

   Player has disconnected from the server.

Vehicle and Kit Events
~~~~~~~~~~~~~~~~~~~~~~

.. py:function:: EnterVehicle(playerObject, vehicleObject[, freeSoldier])

   Player represented by :py:class:`playerObject` has entered the vehicle represented by :py:class:`vehicleObject`. ``freeSoldier`` is 1 if the player is a passenger of the vehicle and is able to use weapons/objects of his kit. i.e. seat 4(+) of a black hawk.

.. py:function:: ExitVehicle(playerObject, vehicleObject)

   Player has exited a vehicle.

.. py:function:: VehicleDestroyed(vehicleObject, attackerObject)

   :py:class:`vehicleObject` has been destroyed by ``attackerObject``.

.. py:function:: PickupKit(playerObject, kitObject)

   Player has picked up a kit. This occurs both when a player physically picks up a kit, as well as when a player spawns.

.. py:function:: DropKit(playerObject, kitObject)

   Player has dropped a kit; can occur either because a player has died, or because a player has picked up a different kit.

Team Events
~~~~~~~~~~~

.. py:function:: Reset(data)

   TBD

.. py:function:: ChangedCommander(teamID, oldCommanderPlayerObject, newCommanderPlayerObject)

   Occurs when a team changes commanders; the old or new commander may be “None”.

.. py:function:: ChangedSquadLeader(squadID, oldLeaderPlayerObject, newLeaderPlayerObject)

   Occurs when a squad changes squad leaders; the old or new squad leader may be “None”.

.. _game-events:

Game Events
~~~~~~~~~~~

.. py:function:: ControlPointChangedOwner(controlPointObject, attackingTeamID)

   TBD

.. py:function:: TimeLimitReached(value)

   Event fires when the fixed time limit for a round expires (not sure what “value” is)

.. py:function:: TicketLimitReached(team, limitID)

   TBD

Command Events
~~~~~~~~~~~~~~

.. py:function:: ConsoleSendCommand(command, args)

   This event is triggered by someone using the ``pythonHost.sendCommand`` console command. Unfortunately, this command/event mechanism appears to be disabled in non-ranked servers. (As a workaround, you can achieve a similar effect :doc:`creating and registering your own custom RCon commands <../../cookbook/new_rcon>`.

.. py:function:: RemoteCommand(playerId, cmd)

   Event fires when a game client gives an ``RCon`` (remote console) command. ``cmd`` is the command the player gave. This event is used by the admin module to receive and process ``RCon`` commands from players; ``RCon`` commands from TCP connections are received by the admin module directly, and do not fire this event.

.. py:function:: ClientCommand(command, issuerPlayerObject, args)

   This event occurs when a game client issues certain in-game commands. The only such commands identified so far are: command=100 means player wants to punish teammate for teamkill; command=101 means player wants to forgive. In both cases, args=1. This response is generated by the player responding to an on-screen prompt caused by a call to the :py:meth:`bf2.gameLogic.sendClientCommand <bf2.GameLogic.GameLogic.sendClientCommand>` method.

Miscellaneous Events
~~~~~~~~~~~~~~~~~~~~

.. py:function:: PlayerUnlocksResponse(succeeded, player, unlocks)

   Unlocks are requested and received asynchronously. This event is triggered when the response for player (which is an object of type Player) are received. If the ranking server did not successfully find the player in question, ``succeeded`` is set to false, else true. unlocks is a list of kit ids, which are 11, 22, 33 .. 77.

.. py:function:: PlayerAwardsResponse()

   TBD

.. py:function:: ChatMessage(playerId, text, channel, flags)

   ``channel`` is ``Squad``, ``Team``, ``Global``, ``ServerTeamMessage`` or ``ServerMessage``. Text is the text of the message sent, prefixed by ``HUD_TEXT_CHAT_TEAM`` or ``HUD_TEXT_CHAT_SQUAD`` if the message is sent to the Team or Squad channel; there is no prefix if it is sent to the Global channel. ``playerId`` is -1 for all server messages. If the player sending the message is dead, their message is also prefixed by ``HUD_CHAT_DEADPREFIX``. (Strings such as ``HUD_TEXT_CHAT_TEAM``, ``HUD_CHAT_DEADPREFIX``, and so on, are used as keys by the game engine to match and replace with localized text.)

.. py:function:: PlayerStatsResponse(succeeded, player, response)

   TBD

.. py:function:: Update(data)

   TBD

Non-Standard Events
~~~~~~~~~~~~~~~~~~~

.. py:function:: GameStatusChangedEvent(status)

   This type of event is registered for with :py:meth:`host.registerGameStatusHandler`. ``status`` is an integer status code enumerated by :py:class:`bf2.GameStatus`.

.. py:function:: TriggerEvent(triggerID, object, vehicle, enter, userData)

   This type of event is registered for with :py:meth:`bf2.triggerManager.createHemiSphericalTrigger <bf2.TriggerManager.TriggerManager.createHemiSphericalTrigger>` or :py:meth:`bf2.triggerManager.createRadiusTrigger <bf2.TriggerManager.TriggerManager.createHemiSphericalTrigger>`; trigger ``triggerID`` is activated when ``vehicle`` comes within the preset radius of ``object``.

.. py:function:: TimerEvent(data)

   This type of event fires when a timer established with :py:class:`bf2.Timer` expires. “data” is an optional piece of information (of any type) that can be set when the timer is established.

Mysterious Events
-----------------

These strings were found in the server executable, and appear to be internal game engine events. They seem to not be accessible from Python, except in a few cases, where there is a correspondence between these “events” and Python events (e.g. “BeginRoundEvent” may be the same as “BeginRound”). For more information, see :doc:`BF2 Internals <../../engine/internals>`.

.. py:function:: RemoveSpawnGroupEvent
.. py:function:: CreateSpawnGroupEvent
.. py:function:: ContentCheckEvent
.. py:function:: UAVEvent
.. py:function:: MissileInitEvent
.. py:function:: UnlockEvent
.. py:function:: MedalEvent
.. py:function:: ToggleFreeCameraEvent
.. py:function:: VoipSessionEvent
.. py:function:: RequestEvent
.. py:function:: PythonCommandEvent
.. py:function:: EndOfRoundEvent

   → EndRound

.. py:function:: BeginRoundEvent

   → BeginRound

.. py:function:: TargetDirectionEvent
.. py:function:: VoteEvent
.. py:function:: VoipPlayerMuteEvent
.. py:function:: SupplyDropEvent
.. py:function:: CommanderCamEvent
.. py:function:: VoipOnOffEvent
.. py:function:: AmbientEffectAreaEvent
.. py:function:: StickyProjectileEvent
.. py:function:: ArtilleryEvent
.. py:function:: SpottedEvent
.. py:function:: SetSquadLeaderEvent
.. py:function:: SetAcceptOrderEvent
.. py:function:: KickBanEvent
.. py:function:: RankEvent
.. py:function:: InviteEvent
.. py:function:: IssueSquadOrderEvent
.. py:function:: SetPrivateSquadEvent
.. py:function:: ChangeSquadNameEvent
.. py:function:: KilledByEvent
.. py:function:: RadioMessageEvent
.. py:function:: CommanderEvent
.. py:function:: LeaveSquadEvent
.. py:function:: JoinSquadEvent
.. py:function:: StringBlockEvent
.. py:function:: HandleDropEvent
.. py:function:: HandlePickupEvent
.. py:function:: ChangePlayerNameEvent
.. py:function:: PostRemoteEvent
.. py:function:: ExitVehicleEvent

   → ExitVehicle

.. py:function:: EnterVehicleEvent

   → EnterVehicle
   
.. py:function:: DestroyPlayerEvent
.. py:function:: DestroyObjectEvent
.. py:function:: CreateKitEvent
.. py:function:: CreateObjectEvent
.. py:function:: CreatePlayerEvent
.. py:function:: DataBlockEvent
.. py:function:: ConnectionTypeEvent
.. py:function:: ChallengeResponseEvent
.. py:function:: ChallengeEvent

Event Patterns
--------------

While each event documented here corresponds to a discrete change of game state, there are certain actions that happen in the game that cause a fixed sequence of events to happen every time-a PlayerSpawn event, for example, is always followed by a :py:func:`PlayerChangeWeapon` event and a PickupKit event. This section documents some of these recurring patterns.

Player Spawn
~~~~~~~~~~~~

#. :py:func:`PlayerConnect`
#. :py:func:`PlayerSpawn`

   Player becomes associated with a :py:class:`soldierObject`.

#. :py:func:`PlayerChangeWeapon`

   From ``None`` to a :py:class:`weaponObject`.

#. :py:func:`PickupKit`

Player Killed
~~~~~~~~~~~~~

#. :py:func:`PlayerKilled`
#. :py:func:`PlayerScore`
#. :py:func:`DropKit`

   The victim drops their kit.

#. :py:func:`ExitVehicle`

   If player is inside a vehicle.

#. :py:func:`PlayerDeath`

Player Revived
~~~~~~~~~~~~~~

#. :py:func:`PlayerKilled`
#. :py:func:`PlayerScore`

   For attacker.

#. :py:func:`DropKit`

   Victim drops their kit.

#. :py:func:`PlayerRevived`
#. :py:func:`PickupKit`

   Revived player picks up the nearest kit [hopefully, but not necessarily, their old one]; if there is no kit nearby, they default to picking up an “assault” kit.

#. :py:func:`PlayerScore`

   For medic who did the revive.

Flag Change
~~~~~~~~~~~

#. :py:func:`ControlPointChangedOwner`

   When neutralized.

#. :py:func:`PlayerScoreEvent`

   Score for having neutralized flag, repeated for each attacker in CP radius.

#. :py:func:`ControlPointChangedOwner`

   When capture complete.

#. :py:func:`PlayerScoreEvent`

   Score for having completed capture, repeated for each attacker in CP radius.

Player Kicked
~~~~~~~~~~~~~

#. :py:func:`PlayerKicked`
#. :py:func:`DropKit`
#. :py:func:`PlayerDeath`
#. :py:func:`PlayerDisconnect`

Player Banned
~~~~~~~~~~~~~

#. :py:func:`PlayerBanned`
#. :py:func:`PlayerKicked`
#. :py:func:`DropKit`
#. :py:func:`PlayerDeath`
#. :py:func:`PlayerDisconnect`

Overall Game State Change
~~~~~~~~~~~~~~~~~~~~~~~~~

#. :py:func:`StatusChange`

   To ``PreGame``.

#. :py:func:`Reset`

   This event doesn't happen in the first round after a server starts.

#. :py:func:`StatusChange`

   To ``Playing``; stay here until enough players connect.

#. :py:func:`StatusChange`

   To ``PreGame``, once enough players have connected.

#. :py:func:`Reset`
#. :py:func:`StatusChange`

   To ``Playing``-the real game round now begins.

#. Play game, beginning with players spawning in.

#. :py:func:`StatusChange`

   To ``EndGame``.

#. :py:func:`DropKit`

   For each player still in game at end.
