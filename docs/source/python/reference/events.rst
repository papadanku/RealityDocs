
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

The possible states game status can be in (as enumerated in :doc:`bf2.GameStatus <bf2>`) are:

-  NotConnected
-  PreGame
-  Playing
-  Paused
-  EndGame
-  RestartServer

Game status events are usually used to kick off pre-game initialization or post-game clean-up processing.

Trigger Events
~~~~~~~~~~~~~~

“Trigger” events activate when a vehicle comes within a specified distance of an object.

.. code-block:: python
   :caption: Triggers are created and registered for by” bf2.triggerManager.

      createHemiSphericalTrigger(object, triggerEventHandler, objectName, radius[, data])

      bf2.triggerManager.createRadiusTrigger(object, triggerEventHandler, objectName, radius[, data])

In standard Battlefield 2, trigger events are used to track scoring for flag captures (triggers activate whenever a player enters or leaves a fixed radius around each control point), as well as effects such as birds (birds are triggered to take flight whenever a player enter their trigger radius).

Timer Events
~~~~~~~~~~~~

.. code-block:: python
   :caption: Timer events activate when a certain amount of time has elapsed.

      bf2.Timer(timerEventHandler, delta, alwaysTrigger[, data])

In standard Battlefield 2, timer events are used to cause periodic status checks related to scoring, ranking, punishing TKs, etc.

   See the description of the :doc:`bf2.Timer <bf2>` class for details.

Descriptions of Events
----------------------

EA/DICE have not published a list of events, but here is a list of events that have been discovered so far.

.. ::code-block:: python
   :caption: Format for event descriptions.

      EventName(handlerParameter1, handlerParameter2, ...)

The ``EventName`` is the name of the event to register for with host. ``registerHandler``; the parameters are the parameters your handler should receive when called.

Some notes about some of the arguments used in these descriptions:

-  **playerObject (LINK)**: An instance of :doc:`bf2.PlayerManager.Player <bf2>`
-  **playerID (LINK)**: As players connect to the server they are assigned playerID numbers from “1” up.
-  ``squadID``: Squads for each side are independently numbered beginning at “1” and increasing thereafter. Players not on a squad, including team commanders, are assigned to squad “0”.
-  ``teamID``: “0” for US, “1” for China or MEC

Server Events
~~~~~~~~~~~~~

-  ``ServerReady``

   TBD

-  ``BeginRound``

   TBD

-  ``EndRound``

   TBD

Player Events
~~~~~~~~~~~~~

-  ``PlayerConnect(playerObject)``

   Fires when a player connects to the game.

-  ``PlayerSpawn(playerObject, soldierObject)``

   Occurs when a player spawns, and associates a ``playerObject`` “spirit” with a ``soldierObject`` “body”.

-  ``PlayerChangeTeams(playerObject, humanHasSpawned)``

   ``humanHasSpawned`` is 1 if the player the event is firing for is a human (as opposed to an AI). Does not fire due to team change from “setTeam”!

-  ``PlayerChangeWeapon(playerObject, oldWeaponObject, newWeaponObject)``

   Player has changed which weapon they are holding.

-  ``PlayerChangedSquad(playerObject, oldSquadID, newSquadID)``

   ``SquadID`` is 0 for players who are not members of any squad (including the team commander).

-  ``PlayerScore(playerObject, difference)``

   Difference is change to player's score (positive or negative).

-  ``PlayerHealPoint(givingPlayerObject, receivingSoldierObject)``

   Occurs whenever a player heals another player; there is no indication of how much health was restored.

-  ``PlayerRepairPoint(givingPlayerObject, receivingVehicleObject)``

   Occurs whenever a player repairs a vehicle; there is no indication of how much damage was repaired.

-  ``PlayerGiveAmmoPoint(givingPlayerObject, receivingPhysicalObject)``

   Occurs whenever a player replenishes the ammo in another player or vehicle. There is no indication of how much ammo was replenished.

-  ``PlayerTeamDamagePoint(playerObject, victimSoldierObject)``

   Occurs whenever a player damages another player on their own team. There is no indication of how much damage was done.

-  ``PlayerKilled(victimPlayerObject, attackerPlayerObject, weaponObject, assists, victimSoldierObject)``

   This event occurs when a player is “critically injured”, but still capable of being revived. If any players assisted in the kill, then “assists” will be a tuple of tuples: the top-level tuple will contain one lower-level tuple for each assisting player; the lower-level tuples will each have two elements: a ``playerObject`` for one of the assisting players, and a number indicating the type of assist (1=targeting assist, 2=kill damage assist, 3=driver assist).

-  ``PlayerRevived(revivedPlayerObject, medicPlayerObject)``

   Player has been revived from a “critically injured” condition to full health by a medic using “shock paddles”. Players can only be revived in the interval between a ``PlayerKilled`` event and a subsequent ``PlayerDeath`` event.

-  ``PlayerDeath(playerObject, soldierObject)``

   This event occurs when a player is decisively dead, and cannot be revived; they will only return to the game by respawning. ``soldierObject`` is the soldier “body” (which is now discarded) for the ``playerObject`` “spirit” (which will persist through the next spawn).

-  ``PlayerBanned(playerObject, time, type)``

   TBD

-  ``PlayerKicked(playerObject)``

   Player has been kicked off the server.

-  ``PlayerDisconnect(playerObject)``

   Player has disconnected from the server.

Vehicle and Kit Events
~~~~~~~~~~~~~~~~~~~~~~

-  ``EnterVehicle(playerObject, vehicleObject[, freeSoldier])``

   Player represented by ``playerObject`` has entered the vehicle represented by ``vehicleObject``. ``freeSoldier`` is 1 if the player is a passenger of the vehicle and is able to use weapons/objects of his kit. i.e. seat 4(+) of a black hawk.

-  ``ExitVehicle(playerObject, vehicleObject)``

   Player has exited a vehicle.

-  ``VehicleDestroyed(vehicleObject, attackerObject)``

   ``vehicleObject`` has been destroyed by ``attackerObject``.

-  ``PickupKit(playerObject, kitObject)``

   Player has picked up a kit. This occurs both when a player physically picks up a kit, as well as when a player spawns.

-  ``DropKit(playerObject, kitObject)``

   Player has dropped a kit; can occur either because a player has died, or because a player has picked up a different kit.

Team Events
~~~~~~~~~~~

-  ``Reset(data)``

   TBD

-  ``ChangedCommander(teamID, oldCommanderPlayerObject, newCommanderPlayerObject)``

   Occurs when a team changes commanders; the old or new commander may be “None”.

-  ``ChangedSquadLeader(squadID, oldLeaderPlayerObject, newLeaderPlayerObject)``

   Occurs when a squad changes squad leaders; the old or new squad leader may be “None”.

Game Events
~~~~~~~~~~~

-  ``ControlPointChangedOwner(controlPointObject, attackingTeamID)``

   TBD

-  ``TimeLimitReached(value)``

   Event fires when the fixed time limit for a round expires (not sure what “value” is)

-  ``TicketLimitReached(team, limitID)``

   TBD

Command Events
~~~~~~~~~~~~~~

-  ``ConsoleSendCommand(command, args)``

   This event is triggered by someone using the ``pythonHost.sendCommand`` console command. Unfortunately, this command/event mechanism appears to be disabled in non-ranked servers. (As a workaround, you can achieve a similar effect by [[Cookbook:Adding New RCon Commands|creating and registering your own custom RCon commands]]).

-  ``RemoteCommand(playerId, cmd)``

   Event fires when a game client gives an ``RCon`` (remote console) command. ``cmd`` is the command the player gave. This event is used by the admin module to receive and process ``RCon`` commands from players; ``RCon`` commands from TCP connections are received by the admin module directly, and do not fire this event.

-  ``ClientCommand(command, issuerPlayerObject, args)``

   This event occurs when a game client issues certain in-game commands. The only such commands identified so far are: command=100 means player wants to punish teammate for teamkill; command=101 means player wants to forgive. In both cases, args=1. This response is generated by the player responding to an on-screen prompt caused by a call to the ``bf2.gameLogic.sendClientCommand`` method.

Misc. Events
~~~~~~~~~~~~

-  ``PlayerUnlocksResponse(succeeded, player, unlocks)``

   Unlocks are requested and received asynchronously. This event is triggered when the response for player (which is an object of type Player) are received. If the ranking server did not successfully find the player in question, ``succeeded`` is set to false, else true. unlocks is a list of kit ids, which are 11, 22, 33 .. 77.

-  ``PlayerAwardsResponse``

   TBD

-  ``ChatMessage(playerId, text, channel, flags)``

   ``channel`` is ``Squad``, ``Team``, ``Global``, ``ServerTeamMessage`` or ``ServerMessage``. Text is the text of the message sent, prefixed by ``HUD_TEXT_CHAT_TEAM`` or ``HUD_TEXT_CHAT_SQUAD`` if the message is sent to the Team or Squad channel; there is no prefix if it is sent to the Global channel. ``playerId`` is -1 for all server messages. If the player sending the message is dead, their message is also prefixed by ``HUD_CHAT_DEADPREFIX``. (Strings such as ``HUD_TEXT_CHAT_TEAM``, ``HUD_CHAT_DEADPREFIX``, and so on, are used as keys by the game engine to match and replace with localized text.)

-  ``PlayerStatsResponse(succeeded, player, response)``

   TBD

-  ``Update(data)``

   TBD

Non-Standard Events
~~~~~~~~~~~~~~~~~~~

-  ``GameStatusChangedEvent(status)``

   This type of event is registered for with host.\ ``registerGameStatusHandler``. ``status`` is an integer status code enumerated by :doc:`bf2.GameStatus <bf2>`.

-  ``TriggerEvent(triggerID, object, vehicle, enter, userData)``

   This type of event is registered for with ``bf2.triggerManager.createHemiSphericalTrigger`` or ``bf2.triggerManager.createRadiusTrigger``; trigger ``triggerID`` is activated when ``vehicle`` comes within the preset radius of ``object``.

-  ``TimerEvent(data)``

   This type of event fires when a timer established with :doc:`bf2.Timer <bf2>` expires. “data” is an optional piece of information (of any type) that can be set when the timer is established.

Mysterious Events
-----------------

These strings were found in the server executable, and appear to be internal game engine events. They seem to not be accessible from Python, except in a few cases, where there is a correspondence between these “events” and Python events (e.g. “BeginRoundEvent” may be the same as “BeginRound”). For more information, see [[BF2_Internals#GameEvent|BF2 Internals]].

-  ``RemoveSpawnGroupEvent``
-  ``CreateSpawnGroupEvent``
-  ``ContentCheckEvent``
-  ``UAVEvent``
-  ``MissileInitEvent``
-  ``UnlockEvent``
-  ``MedalEvent``
-  ``ToggleFreeCameraEvent``
-  ``VoipSessionEvent``
-  ``RequestEvent``
-  ``PythonCommandEvent``
-  ``EndOfRoundEvent`` → ``EndRound``
-  ``BeginRoundEvent`` → ``BeginRound``
-  ``TargetDirectionEvent``
-  ``VoteEvent``
-  ``VoipPlayerMuteEvent``
-  ``SupplyDropEvent``
-  ``CommanderCamEvent``
-  ``VoipOnOffEvent``
-  ``AmbientEffectAreaEvent``
-  ``StickyProjectileEvent``
-  ``ArtilleryEvent``
-  ``SpottedEvent``
-  ``SetSquadLeaderEvent``
-  ``SetAcceptOrderEvent``
-  ``KickBanEvent``
-  ``RankEvent``
-  ``InviteEvent``
-  ``IssueSquadOrderEvent``
-  ``SetPrivateSquadEvent``
-  ``ChangeSquadNameEvent``
-  ``KilledByEvent``
-  ``RadioMessageEvent``
-  ``CommanderEvent``
-  ``LeaveSquadEvent``
-  ``JoinSquadEvent``
-  ``StringBlockEvent``
-  ``HandleDropEvent``
-  ``HandlePickupEvent``
-  ``ChangePlayerNameEvent``
-  ``PostRemoteEvent``
-  ``ExitVehicleEvent`` → ``ExitVehicle``
-  ``EnterVehicleEvent`` → ``EnterVehicle``
-  ``DestroyPlayerEvent``
-  ``DestroyObjectEvent``
-  ``CreateKitEvent``
-  ``CreateObjectEvent``
-  ``CreatePlayerEvent``
-  ``DataBlockEvent``
-  ``ConnectionTypeEvent``
-  ``ChallengeResponseEvent``
-  ``ChallengeEvent``

Event Patterns
--------------

While each event documented here corresponds to a discrete change of game state, there are certain actions that happen in the game that cause a fixed sequence of events to happen every time-a PlayerSpawn event, for example, is always followed by a PlayerChangeWeapon event and a PickupKit event. This section documents some of these recurring patterns.

Player Spawn
~~~~~~~~~~~~

1. ``PlayerConnect``

2. ``PlayerSpawn``

   Player becomes associated with a ``SoldierObject``.

3. ``PlayerChangeWeapon``

   From ``None`` to a ``WeaponObject``.

4. ``PickupKit``

Player Killed
~~~~~~~~~~~~~

1. ``PlayerKilled``

2. ``PlayerScore``

3. ``DropKit``

   The victim drops their kit.

4. ``ExitVehicle``

   If player is inside a vehicle.

5. ``PlayerDeath``

Player Revived
~~~~~~~~~~~~~~

1. ``PlayerKilled``

2. ``PlayerScore``

   For attacker.

3. ``DropKit``

   Victim drops their kit.

4. ``PlayerRevived``

5. ``PickupKit``

   Revived player picks up the nearest kit [hopefully, but not necessarily, their old one]; if there is no kit nearby, they default to picking up an “assault” kit.

6. ``PlayerScore``

   For medic who did the revive.

Flag Change
~~~~~~~~~~~

1. ``ControlPointChangedOwner``

   When neutralized.

2. ``PlayerScoreEvent``

   Score for having neutralized flag, repeated for each attacker in CP radius.

3. ``ControlPointChangedOwner``

   When capture complete.

4. ``PlayerScoreEvent``

   Score for having completed capture, repeated for each attacker in CP radius.

Player Kicked
~~~~~~~~~~~~~

1. ``PlayerKicked``
2. ``DropKit``
3. ``PlayerDeath``
4. ``PlayerDisconnect``

Player Banned
~~~~~~~~~~~~~

1. ``PlayerBanned``
2. ``PlayerKicked``
3. ``DropKit``
4. ``PlayerDeath``
5. ``PlayerDisconnect``

Overall Game State Change
~~~~~~~~~~~~~~~~~~~~~~~~~

1. ``StatusChange``

   To ``PreGame``.

2. ``Reset``

   This event doesn't happen in the first round after a server starts.

3. ``StatusChange``

   To ``Playing``; stay here until enough players connect.

4. ``StatusChange``

   To ``PreGame``, once enough players have connected.

5. ``Reset``

6. ``StatusChange``

   To ``Playing``-the real game round now begins.

7. Play game, beginning with players spawning in.

8. ``StatusChange``

   To ``EndGame``.

9. ``DropKit``

   For each player still in game at end.
