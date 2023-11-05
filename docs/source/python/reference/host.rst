
host
========

The ``host`` object encapsulates the interfaces between the main BF2 engine (written in C++) and Python modules. Most ``host`` methods will generally not need to be used directly from within Python modules, as standard BF2 Python modules (like ``bf2.GameLogic``, for example) provide object-oriented wrappers around most of the raw BF2 engine functions.

You must ``import host`` to access the methods and attributes shown here.

Event Handler Methods
---------------------

-  ``host.registerHandler('EventName', eventHandler[, alwaysCall])``

   Registers a function to handle an event. If ``alwaysCall`` is not specified the handler will only be called when the game is in the “Playing” state–not in the “Pregame” and “Postgame” states. If you would like it to run in Pregame and Postgame as well, ``alwaysCall`` must be specified and evaluate as true (e.g. “1”).

-  ``host.registerGameStatusHandler(gameStatusEventHandler)``

   Registers a function to handle a game status event.

-  ``host.unregisterGameStatusHandler(gameStatusEventHandler)``

   Unregisters a game status event-handling function.

Trigger Methods
---------------

-  ``host.trig_create(object, callback, objName, radius, unknownBool, data)``
-  ``host.trig_getObjects(trig_id)``
-  ``host.trig_destroyAll()``
-  ``host.trig_destroy(trig_id)``

Global Stats Methods
--------------------

-  ``host.pers_gamespyStatsNewGame()``

-  ``host.pers_gamespyStatsEndGame()``

-  ``host.pers_gamespyStatsSendSnapshotFinal(snapShot)``

-  ``host.pers_gamespyStatsSendSnapshotUpdate``

-  ``host.pers_getStatsKeyVal(key)``

-  ``host.pers_plrRequestAwards(playerIndex, unknown, unknown)``

-  ``host.pers_plrRequestStats(playerIndex, unknown, urlToStatType)``

   Presumably returns the specified stat of the specified player.

-  ``host.pers_plrRequestUnlocks(playerIndex, unknown)``

   Presumably returns the specified player’s unlocks.

-  ``host.pers_plrSetUnlocks(playerIndex, unknown, unknown)``

-  ``host.pers_plrAwardMedal``

``sh`` Methods (SwiffHost?)
---------------------------

-  ``host.sh_setEnableCommander(bool)``

   Enables or disables the commander position.

``gl`` Methods (GameLogic?)
---------------------------

-  ``host.gl_sendEndOfRoundData(dataString)``

   Presumably sends stats-related information to clients when a round ends.

``sgl`` Methods (ServerGameLogic?)
----------------------------------

-  ``host.sgl_getSettingsBool``

-  ``host.sgl_sendTextMessage(playerId, 10, 1, message)``

   Send a server message to one player. Working Status Unknown

-  ``host.sgl_sendRankEvent(playerIndex, rank, score)``

-  ``host.sgl_sendMedalEvent(playerIndex, type, value)``

-  ``host.sgl_sendPythonEvent``

-  ``host.sgl_sendGameLogicEvent(playerID, event, data)``

-  ``host.sgl_sendHudEvent(playerID, event, data)``

-  ``host.sgl_getIsAIGame()``

   Presumably returns whether or not the current game has AI.

-  ``host.sgl_getControlPointsInGroup``

-  ``host.sgl_endGame(winner, victoryType)``

   Presumably ends a current game, awarding victory of victoryType to winner.

-  ``host.sgl_getParam(name, unknown, unknown)``

-  ``host.sgl_setParam(name, unknown, unknown, unknown)``

-  ``host.sgl_getWorldSize()``

   returns a tuple giving the north/south and east/west dimensions of the current map, more-or-less in meters.

-  ``host.sgl_getMapName()``

   Returns the current map name.

-  ``host.sgl_getModDirectory()``

   Returns the directory containing the currently active mod.

``ss`` Methods (Server Settings?)
---------------------------------

-  ``host.ss_getParam(parameter)``

   Returns value of specified setting.

   Settings include:

   -  ``ticketRatio``
   -  ``teamRatioPct``
   -  ``maxPlayers``
   -  ``gameMode``
   -  ``mapName``
   -  ``timeLimit``
   -  ``scoreLimit``
   -  ``autoBalance``
   -  ``tkpEnabled``
   -  ``tkpNeeded``
   -  ``tkpDefault``
   -  ``globRank``
   -  ``globUnlocks``

   You cannot find out server name, port and other similar information this way. Instead, use f.e. host.rcon_invoke(‘sv.serverName’) to get the server name.

Object Manager Methods
----------------------

-  ``host.omgr_getObjectsOfTemplate(template)``
-  ``host.omgr_getObjectsOfType(type)``

Timer Methods
-------------

-  ``host.timer_created(timer)``

-  ``host.timer_getTimers``

   **Do not use, unfinished DICE code.**

   Creates a Tuple and only fills one slot. Trying to access the other slots will crash the server.

-  ``host.timer_destroy(timer)``

-  ``host.timer_getWallTime()``

   Return the number of seconds since server started -  see :doc:`BF2 Time <../../engine/time>`

Player Manager Methods
----------------------

-  ``host.pmgr_enableScoreEvents``

-  ``host.pmgr_getScore(playerIndex, name)``

   Gets value of score name of specified player.

-  ``host.pmgr_setScore(playerIndex, name, value)``

   Sets value of score name of specified player.

-  ``host.pmgr_p_get(name, playerIndex)``

-  ``host.pmgr_p_set(name, playerIndex, value)``

-  ``host.pmgr_isIndexValid(index)``

   Checks the validity of specified player index.

-  ``host.pmgr_getCommander()``

   Presumably returns Player object for the current commander.

-  ``host.pmgr_getPlayers()``

   Returns current player objects.

-  ``host.pmgr_getNumberOfPlayers()``

   Returns number of players.

``RCon`` Methods
----------------

-  ``host.rcon_invoke(command)``

   Executes a server console command.

-  ``host.rcon_feedback(playerid, message)``

   Send a message to an in-game player ``RCon`` client.

Logging Methods
---------------

-  ``host.log(message)``

   Send a message to the log.
