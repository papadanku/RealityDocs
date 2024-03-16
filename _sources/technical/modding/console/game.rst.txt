
Game
====

``game``
--------

``game.allowToggleFullscreen``
   bool -> bool

``game.lockFps``
   int -> int

   Sets a fps cap, makes it so that the fps can't go higher than the given number.

``game.radioMessage``
   TargetChannel std::string -> void

``game.sayAll``
   std::string -> void

``game.sayTeam``
   int std::string -> void

``game.simulationRate``
   int -> int

   - ``HudElementsDemoRecComm.con``
   - In Battlerecorder it sets the speed for the decrease speed and increase speed buttons.
   - Can be increased, though some users report no difference as it is dependent on the Demo FPS (Default is 30 settings must be recorded higher something like 60) and Game FPS

``game.toggleFullscreen``
   -> void

   - ~ Console
   - Toggles Full-Screen and Windowed mode
   - It will give you the nasty side-effect of seethrough terrain that would need the client to disconnect and reconnect to fix.

``game.unload``
   -> bool

``gameLogic``
-------------

``gameLogic.AddInvalidDropVehicleObject``
   std::string bool -> void

``gameLogic.becomeSquadLeader``
   bool -> bool

``gameLogic.createObject``
   std::string -> void

``gameLogic.damageForBeingOutSideWorld``
   float -> float

``gameLogic.defaultLevel``
   std::string -> std::string

``gameLogic.defaultTimeToNextAIWave``
   float -> float

``gameLogic.enableVoHelp``
   bool -> bool

   - Enables the Voice Over Tips feature from vBF2.
   - Uses ``prhelp.utxt`` in localization for std::strings/anything with HUD_HELP definitions
   - HudElementsHelp.con in Menu for the size, color, fade in time, create more messages and VoiceMessages_Help.con for voiceovers

``gameLogic.extraUAVVehicleFlightHeight``
   float -> float

``gameLogic.feslEnvironment``
   int -> int

``gameLogic.getBeforeSpawnCameraDirection``
   -> Vec3

``gameLogic.getBeforeSpawnCameraPosition``
   -> Vec3

``gameLogic.getDefaultNumberOfTickets``
   U32 -> U32

``gameLogic.getDefaultNumberOfTicketsEx``
   U32 U32 -> U32

``gameLogic.getNumberOfTickets``
   U32 -> U32

``gameLogic.getTeamDropVehicle``
   int -> std::string

``gameLogic.getTeamLanguage``
   int -> std::string

``gameLogic.getTeamName``
   int -> std::string

``gameLogic.getTicketLossAtEndPerMin``
   -> float

``gameLogic.getTicketLossPerMin``
   U32 -> float

``gameLogic.hitIndicationThreshold``
   float -> float

``gameLogic.maximumLevelViewDistance``
   float -> float

``gameLogic.messages.addHelpMessage``
   std::string std::string -> int

``gameLogic.messages.addMessage``
   std::string -> int

``gameLogic.messages.addRadioFilter``
   std::string std::string -> int

``gameLogic.messages.addRadioVoice``
   std::string std::string std::string -> int

``gameLogic.messages.playHelpMessage``
   std::string -> int

``gameLogic.messages.playRadioMessage``
   int std::string std::string -> int

``gameLogic.messages.setVolumes``
   float float -> void

``gameLogic.noVehiclesOmit``
   std::string -> void

``gameLogic.outputPlayerStats``
   bool -> bool

``gameLogic.printCameraCoordToConsole``
   -> void

``gameLogic.refreshTriggerables``
   -> void

``gameLogic.remoteCommand``
   int int int -> bool

``gameLogic.reset``
   -> void

``gameLogic.roundNr``
   int -> int

``gameLogic.setAirMouseInverted``
   bool -> void

``gameLogic.setAirMouseSensitivity``
   float -> float

``gameLogic.setBeforeSpawnCamera``
   Vec3 Vec3 -> void

``gameLogic.setDefaultNumberOfTickets``
   U32 U32 -> void

``gameLogic.setDefaultNumberOfTicketsEx``
   U32 U32 U32 -> void

``gameLogic.setDropVehicleDeviationRadius``
   int int -> void

``gameLogic.setKit``
   int KitType std::string -> void

``gameLogic.setNumberOfTickets``
   U32 U32 -> void

``gameLogic.setNumDropVehiclesForTeam``
   int int -> void

``gameLogic.setTeamDropVehicle``
   int std::string -> void

``gameLogic.setTeamFlag``
   int std::string -> void

``gameLogic.setTeamLanguage``
   int std::string -> void

``gameLogic.setTeamName``
   int std::string -> void

``gameLogic.setTicketLossAtEndPerMin``
   float -> void

``gameLogic.setTicketLossPerMin``
   U32 float -> void

``gameLogic.spawnAtCameraPosition``
   bool -> bool

``gameLogic.spawnObjectSpeed``
   float -> float

``gameLogic.spawnPlayers``
   bool -> bool

``gameLogic.supplyDropHeight``
   float -> float

``gameLogic.supplyDropNumSecsToLive``
   float -> float

``gameLogic.teleport``
   -> void

``gameLogic.teleportCameraTo``
   Vec3 -> void

``gameLogic.teleportTo``
   Vec3 -> void

``gameLogic.timeAllowedOutSideWorld``
   float -> float

``gameLogic.timeToNextAIWave``
   float -> float

``gameLogic.togglePause``
   -> void

   Console ~ Command

   Pauses the game. Pressing :kbd:`P` in COOP and Local does the same thing.

``gameLogic.vehicleDropHeight``
   float -> float

``gameServerSettings``
----------------------

``gameServerSettings.setAdminScript``
   std::string -> void

``gameServerSettings.setAllowNATNegotation``
   bool -> void

``gameServerSettings.setAutoBalanceTeam``
   bool -> void

``gameServerSettings.setAutoRecord``
   bool -> void

``gameServerSettings.setAutoRecordRounds``
   int -> void

``gameServerSettings.setCommunityLogoURL``
   std::string -> void

``gameServerSettings.setCoopBotCount``
   int -> void

``gameServerSettings.setCoopBotDifficulty``
   float -> void

``gameServerSettings.setCoopBotRatio``
   float -> void

``gameServerSettings.setDemoDownloadURL``
   std::string -> void

``gameServerSettings.setDemoHook``
   std::string -> void

``gameServerSettings.setDemoIndexURL``
   std::string -> void

``gameServerSettings.setEndDelay``
   int -> void

``gameServerSettings.setFriendlyFireWithMines``
   bool -> void

``gameServerSettings.setGameMode``
   std::string -> void

``gameServerSettings.setGameSpyPort``
   int -> void

``gameServerSettings.setInterfaceIP``
   std::string -> void

``gameServerSettings.setInternet``
   bool -> void

``gameServerSettings.setManDownTime``
   float -> void

``gameServerSettings.setMaxPlayers``
   int -> void

``gameServerSettings.setMinPlayersForVoting``
   int -> void

``gameServerSettings.setNoVehicles``
   float -> void

``gameServerSettings.setPassword``
   std::string -> void

``gameServerSettings.setPunishTeamKills``
   bool -> void

``gameServerSettings.setRoundsPerMap``
   int -> void

``gameServerSettings.setScoreLimit``
   int -> void

``gameServerSettings.setServerName``
   std::string -> void

``gameServerSettings.setSoldierFF``
   int -> void

``gameServerSettings.setSoldierSplashFF``
   int -> void

``gameServerSettings.setSpawnTime``
   float -> void

``gameServerSettings.setSponsorLogoURL``
   std::string -> void

``gameServerSettings.setSponsorText``
   std::string -> void

``gameServerSettings.setStartDelay``
   int -> void

``gameServerSettings.setSvPunkBuster``
   bool -> void

``gameServerSettings.setTeamRatio``
   float -> void

``gameServerSettings.setTeamVoteOnly``
   bool -> void

``gameServerSettings.setTicketRatio``
   int -> void

``gameServerSettings.setTimeBeforeRestartMap``
   float -> void

``gameServerSettings.setTimeLimit``
   int -> void

``gameServerSettings.setVehicleFF``
   int -> void

``gameServerSettings.setVehicleSplashFF``
   int -> void

``gameServerSettings.setVoipBFClientPort``
   int -> void

``gameServerSettings.setVoipBFServerPort``
   int -> void

``gameServerSettings.setVoipEnabled``
   bool -> void

``gameServerSettings.setVoipQuality``
   int -> void

``gameServerSettings.setVoipServerPort``
   int -> void

``gameServerSettings.setVoipServerRemote``
   bool -> void

``gameServerSettings.setVoipServerRemoteIP``
   std::string -> void

``gameServerSettings.setVoipSharedPassword``
   std::string -> void

``gameServerSettings.setVoteTime``
   int -> void
