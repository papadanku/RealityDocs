
host
====

.. py:module:: host

The ``host`` object encapsulates the interfaces between the main BF2 engine (written in C++) and Python modules. Most ``host`` methods will generally not need to be used directly from within Python modules, as standard BF2 Python modules (like ``bf2.GameLogic``, for example) provide object-oriented wrappers around most of the raw BF2 engine functions.

You must ``import host`` to access the methods and attributes shown here.

Event Handler Methods
---------------------

.. py:method:: registerHandler('EventName', eventHandler[, alwaysCall])

   Registers a function to handle an event. If ``alwaysCall`` is not specified the handler will only be called when the game is in the “Playing” state--not in the “Pregame” and “Postgame” states. If you would like it to run in Pregame and Postgame as well, ``alwaysCall`` must be specified and evaluate as true (e.g. “1”).

.. py:method:: registerGameStatusHandler(gameStatusEventHandler)

   Registers a function to handle a game status event.

.. py:method:: unregisterGameStatusHandler(gameStatusEventHandler)

   Unregisters a game status event-handling function.

Trigger Methods
---------------

.. py:method:: trig_create(object, callback, objName, radius, unknownBool, data)
.. py:method:: trig_getObjects(trig_id)
.. py:method:: trig_destroyAll()
.. py:method:: trig_destroy(trig_id)

Global Stats Methods
--------------------

.. py:method:: pers_gamespyStatsNewGame()

.. py:method:: pers_gamespyStatsEndGame()

.. py:method:: pers_gamespyStatsSendSnapshotFinal(snapShot)

.. py:method:: pers_gamespyStatsSendSnapshotUpdate

.. py:method:: pers_getStatsKeyVal(key)

.. py:method:: pers_plrRequestAwards(playerIndex, unknown1, unknown2)

.. py:method:: pers_plrRequestStats(playerIndex, unknown, urlToStatType)

   :return: Specified stat of the specified player.

.. py:method:: pers_plrRequestUnlocks(playerIndex, unknown)

   :return: Specified player's unlocks.

.. py:method:: pers_plrSetUnlocks(playerIndex, unknown1, unknown2)

.. py:method:: pers_plrAwardMedal

``sh`` Methods (SwiffHost?)
---------------------------

.. py:method:: sh_setEnableCommander(bool)

   Enables or disables the commander position.

``gl`` Methods (GameLogic?)
---------------------------

.. py:method:: gl_sendEndOfRoundData(dataString)

   Presumably sends stats-related information to clients when a round ends.

``sgl`` Methods (ServerGameLogic?)
----------------------------------

.. py:method:: sgl_getSettingsBool

.. py:method:: sgl_sendTextMessage(playerId, 10, 1, message)

   Send a server message to one player. Working Status Unknown.

.. py:method:: sgl_sendRankEvent(playerIndex, rank, score)

.. py:method:: sgl_sendMedalEvent(playerIndex, type, value)

.. py:method:: sgl_sendPythonEvent

.. py:method:: sgl_sendGameLogicEvent(playerID, event, data)

.. py:method:: sgl_sendHudEvent(playerID, event, data)

.. py:method:: sgl_getIsAIGame()

   :return: Whether or not the current game has AI.

.. py:method:: sgl_getControlPointsInGroup

.. py:method:: sgl_endGame(winner, victoryType)

   Presumably ends a current game, awarding victory of victoryType to winner.

.. py:method:: sgl_getParam(name, unknown1, unknown2)

.. py:method:: sgl_setParam(name, unknown1, unknown2, unknown3)

.. py:method:: sgl_getWorldSize()

   :return: Tuple giving the north/south and east/west dimensions of the current map, more-or-less in meters.

.. py:method:: sgl_getMapName()

   :return: Current map name.

.. py:method:: sgl_getModDirectory()

   :return: Directory containing the currently active mod.

``ss`` Methods (Server Settings?)
---------------------------------

.. py:method:: ss_getParam(parameter)

   You cannot find out server name, port and other similar information this way. Instead, use f.e. :py:meth:`host.rcon_invoke` to get the server name.

   :return: Value of specified setting

   Settings include:

   - ``ticketRatio``
   - ``teamRatioPct``
   - ``maxPlayers``
   - ``gameMode``
   - ``mapName``
   - ``timeLimit``
   - ``scoreLimit``
   - ``autoBalance``
   - ``tkpEnabled``
   - ``tkpNeeded``
   - ``tkpDefault``
   - ``globRank``
   - ``globUnlocks``

Object Manager Methods
----------------------

.. py:method:: omgr_getObjectsOfTemplate(template)
.. py:method:: omgr_getObjectsOfType(type)

Timer Methods
-------------

.. py:method:: timer_created(timer)

.. py:method:: timer_getTimers()

   **Do not use, unfinished DICE code.**

   :return: Creates a Tuple and only fills one slot. Trying to access the other slots will crash the server.

.. py:method:: timer_destroy(timer)

.. py:method:: timer_getWallTime()

   See :doc:`BF2 Time <../../engine/time>`

   :return: The number of seconds since server started.

Player Manager Methods
----------------------

.. py:method:: pmgr_enableScoreEvents
.. py:method:: pmgr_getScore(playerIndex, name)

   :return: Score name of specified player.

.. py:method:: pmgr_setScore(playerIndex, name, value)

   :return: Score name of specified player.

.. py:method:: pmgr_p_get(name, playerIndex)
.. py:method:: pmgr_p_set(name, playerIndex, value)
.. py:method:: pmgr_isIndexValid(index)

   :return: Validity of specified player index.

.. py:method:: pmgr_getCommander()

   :return: Player object for the current commander.

.. py:method:: pmgr_getPlayers()

   :return: Current player objects.

.. py:method:: pmgr_getNumberOfPlayers()

   :return: Number of players.

``RCon`` Methods
----------------

.. py:method:: rcon_invoke(command)

   Executes a server console command.

.. py:method:: rcon_feedback(playerid, message)

   Send a message to an in-game player ``RCon`` client.

Logging Methods
---------------

.. py:method:: log(message)

   Send a message to the log.
