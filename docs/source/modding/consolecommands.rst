
.. role:: raw-latex(raw)
   :format: latex
..

BF2 Console Commands
====================

``AnimationBundle``
-------------------

-  ``animationBundle.abruptPlayback`` bool -> bool
-  ``animationBundle.addAnimation`` std::string -> void
-  ``animationBundle.addEvent`` std::string -> void
-  ``animationBundle.fadeInTime`` float -> float

   -  Used in AnimationSystem1p and 3p .inc files
   -  Fade in: Animation Start. Allows a smooth transition between animations.

      -  The lower it is, the quicker it is.
      -  A high value makes the transition slower and longer.
      -  Fade in 0.01.

   -  Example: Idle/Walking to Sprinting”

-  ``animationBundle.fadeOutTime`` float -> float

   -  Used in AnimationSystem1p and 3p .inc files
   -  Fade out: Animation End.

      -  Same as above, Fadeout 0.1.
      -  Fadeout 0.4 would make it take 0.4 seconds to finish an animation

   -  Example: From Sprinting to Walk/Idle”

-  ``animationBundle.getAnimationLength`` std::string -> float
-  ``animationBundle.getAnimationStartTime`` std::string -> float
-  ``animationBundle.getEventStartTime`` std::string -> float
-  ``animationBundle.isLooping`` bool -> bool
-  ``animationBundle.jumpToLastAnimationAtStop`` bool -> bool
-  ``animationBundle.length`` float -> float
-  ``animationBundle.listAnimations`` -> std::string
-  ``animationBundle.listEvents`` -> std::string
-  ``animationBundle.playBackward`` bool -> bool
-  ``animationBundle.playForever`` bool -> bool
-  ``animationBundle.removeAnimation`` std::string -> void
-  ``animationBundle.removeEvent`` std::string -> void
-  ``animationBundle.setAnimationLength`` std::string float -> void
-  ``animationBundle.setAnimationStartTime`` std::string float -> void
-  ``animationBundle.setEventStartTime`` std::string float -> void
-  ``animationBundle.useSpeedAsTime`` bool -> bool

``AnimationManager``
--------------------

-  ``animationManager.fadeInTime`` float -> float
-  ``animationManager.ignoreMotherOrientation`` int -> int
-  ``animationManager.length`` float -> float

   -  “AnimationSystem1p, AnimationSystem3p.inc”
   -  The length of the animation. Must match up with ObjectTemplate.ammo.reloadTime to sync.

      -  If it’s a lower value, animation will be sped up.
      -  If it’s a higher value, animation will be slowed down.

-  ``animationManager.looping`` bool -> bool

   -  “AnimationSystem1p, AnimationSystem3p.inc”

-  ``animationManager.noiceAmplitude`` float -> float
-  ``animationManager.noiceFreq`` int -> int
-  ``animationManager.originalLength`` -> float

``AnimationSystem``
-------------------

-  ``animationSystem.activestd::string`` -> std::string
-  ``animationSystem.activeAnimation`` std::string -> std::string
-  ``animationSystem.activeBundle`` std::string -> std::string
-  ``animationSystem.activeTrigger`` std::string -> std::string
-  ``animationSystem.activeValueHolder`` std::string -> std::string
-  ``animationSystem.cameraSpring.amplitude`` Vec3 -> Vec3
-  ``animationSystem.cameraSpring.fire`` Vec3 -> Vec3
-  ``animationSystem.cameraSpring.hit`` Vec3 -> Vec3
-  ``animationSystem.cameraSpring.look`` Vec2 -> Vec2
-  ``animationSystem.cameraSpring.move`` Vec3 -> Vec3
-  ``animationSystem.cameraSpring.stiffness`` Vec3 -> Vec3
-  ``animationSystem.cameraSpring.use`` bool -> bool
-  ``animationSystem.cameraSpring.zoomDamping`` Vec3 -> Vec3
-  ``animationSystem.create`` std::string -> void
-  ``animationSystem.createAnimation`` std::string -> anim.BoneAnimation\*
-  ``animationSystem.createBundle`` std::string -> anim.Bundle\*
-  ``animationSystem.createTrigger`` std::string std::string -> anim.Trigger\*
-  ``animationSystem.createValueHolder`` std::string -> void
-  ``animationSystem.deleteActiveBundle`` -> void
-  ``animationSystem.deleteActiveTrigger`` -> void
-  ``animationSystem.hide`` -> void
-  ``animationSystem.list`` -> std::string
-  ``animationSystem.listAnimations`` -> std::string
-  ``animationSystem.listBundles`` -> std::string
-  ``animationSystem.listTriggers`` -> std::string
-  ``AnimationSystem.listTriggerTypes`` -> std::string
-  ``animationSystem.listValueHolders`` -> std::string
-  ``animationSystem.playbackModifier`` float -> float
-  ``animationSystem.reloadScript`` -> void
-  ``animationSystem.save`` std::string -> void
-  ``animationSystem.saveActive`` -> void
-  ``animationSystem.saveValueHolders`` -> void

``animationTrigger``
--------------------

-  ``animationTrigger.addBundle`` std::string -> void
-  ``animationTrigger.addChild`` std::string -> void
-  ``animationTrigger.clearValueHolder`` -> void
-  ``animationTrigger.fadeInTime`` float -> float
-  ``animationTrigger.getTypeName`` -> std::string
-  ``animationTrigger.idleTime`` Vec2 -> Vec2
-  ``animationTrigger.listBundles`` -> std::string
-  ``animationTrigger.message`` int -> int
-  ``animationTrigger.removeBundle`` std::string -> void
-  ``animationTrigger.removeChild`` std::string -> void
-  ``animationTrigger.triggerOnAcceleration`` bool -> bool
-  ``animationTrigger.useDirection`` bool -> bool
-  ``animationTrigger.valueHolder`` std::string -> std::string

``animationValueHolder``
------------------------

-  ``animationValueHolder.getFilename`` -> std::string
-  ``animationValueHolder.max`` float -> float
-  ``animationValueHolder.min`` float -> float
-  ``animationValueHolder.normal`` float -> float
-  ``animationValueHolder.passOnMessage`` unsigned int -> unsigned int
-  ``animationValueHolder.stopOnMessage`` unsigned int -> unsigned int
-  ``animationValueHolder.values`` float float float -> void

``audioSettings``
-----------------

-  ``audioSettings.alwaysAllowSystemOpenAL`` bool -> bool
-  ``audioSettings.effectsVolume`` float -> float
-  ``audioSettings.enableEAX`` bool -> bool
-  ``audioSettings.englishOnlyVoices`` bool -> bool
-  ``audioSettings.forceNumberOfVoices`` int -> int
-  ``audioSettings.helpVoiceVolume`` float -> float
-  ``audioSettings.musicVolume`` float -> float
-  ``audioSettings.provider`` std::string -> std::string
-  ``audioSettings.soundQuality`` std::string -> std::string
-  ``audioSettings.voipBoostEnabled`` bool -> bool
-  ``audioSettings.voipCaptureThreshold`` float -> float
-  ``audioSettings.voipCaptureVolume`` float -> float
-  ``audioSettings.voipEnabled`` bool -> bool
-  ``audioSettings.voipPlaybackVolume`` float -> float
-  ``audioSettings.voipUsePushToTalk`` bool -> bool
-  ``bf2Engine.playMovie`` std::string int -> void
-  ``chat.sayAll`` std::string -> void

   -  Menu (Hud Elements Chat.con)
   -  All Chat. Used in ``HudElementsChat.con``

-  ``chat.sayTeam`` std::string -> void

   -  Menu (Hud Elements Chat.con)
   -  Team Chat. Used in ``HudElementsChat.con``

-  ``CollisionCheck.checkStaticCollisionMeshes`` int -> void

``collisionManager``
--------------------

-  ``collisionManager.buildDebugCollisionMeshes`` -> void
-  ``collisionManager.create`` std::string -> void
-  ``collisionManager.createTemplate`` std::string -> void

   -  Used in .con files for collision meshes
   -  Creates a Collision Mesh template from the collision mesh name so it can be used in other files without creating a duplicate mesh

-  ``collisionManager.drawBoundingBoxes`` bool -> void
-  ``collisionManager.drawForces`` bool -> void
-  ``collisionManager.drawIntersectFaces`` bool -> void
-  ``collisionManager.drawMeshes`` bool -> void
-  ``collisionManager.drawNormals`` bool -> void
-  ``collisionManager.drawOnlyRoot`` float -> void
-  ``collisionManager.drawPivots`` bool -> void
-  ``collisionManager.drawPrimitives`` bool -> void
-  ``collisionManager.drawSoldierMesh`` bool -> void
-  ``collisionManager.drawTestedFaces`` bool -> void
-  ``collisionManager.getNameOfObjectInFocus`` -> void
-  ``collisionManager.identityRotateObjectInFocus`` -> void
-  ``collisionManager.rotateObjectInFocusAroundAxis`` uint float -> void
-  ``collisionManager.rotateObjectInFocusAroundVector`` Vec3 float -> void
-  ``collisionManager.setActiveLod`` int -> void
-  ``collisionManager.setDrawDistance`` float -> void
-  ``collisionManager.setGeometry`` bool -> void
-  ``collisionManager.setSleepinessOfObjectInFocus`` int -> void

   -  ``.con`` presumably
   -  Effect Unknown. Causes a game crash during loading when using collisionManager.setSleepinessOfObjectInFocus 0 in a ``.con`` of a GenericFirearm

-  ``collisionManager.updateFlagsOfObjectInFocus`` U32 U32 -> void
-  ``collisionManager.useDeferredLoading`` bool -> bool

``combatArea``
--------------

-  ``combatArea.active`` std::string -> void

-  ``combatArea.addAreaPoint`` Vec2 -> void

-  ``combatArea.create`` std::string -> void

-  ``combatArea.deleteActiveCombatArea`` -> void

-  ``combatArea.getActiveCombatAreaName`` -> std::string

-  ``combatArea.inverted`` bool -> bool

-  ``combatArea.layer`` int -> int

-  ``combatAreaManager.addVehicleDamage`` world::VehicleCategory float -> void

-  ``combatAreaManager.addVehicleTimer`` world::VehicleCategory float -> void

-  ``combatAreaManager.damage`` float -> float

-  ``combatAreaManager.timeAllowedOutside`` float -> float

-  ``combatAreaManager.use`` bool -> void

-  ``combatArea.max`` Vec2 -> Vec2

-  ``combatArea.min`` Vec2 -> Vec2

-  ``combatArea.team`` int -> int

-  ``combatArea.usedByPathFinding`` bool -> bool

-  ``combatArea.vehicles`` int -> int

   Controls what kind of vehicle is effected by the combat zone. This can be used for crating an extra large, separate combat zone around the base combat zone only for jets, to give them a much larger area to fly in and when you hop into a jet, you can still see the base combat zone, but the area between the base and the jet combat zone will be 1/2 transparent. When hand coding this the values are:

   -  VehicleType “0” - Land
   -  VehicleType “1” - Sea
   -  VehicleType “2” - Planes
   -  VehicleType “3” - Choppers
   -  VehicleType “4” - All
   -  VehicleType “5” - Planes & Choppers

``commander``
-------------

-  ``commander.accept`` bool -> void
-  ``commander.artillery`` -> void
-  ``commander.commanderApply`` -> void
-  ``commander.commanderMutiny`` -> void
-  ``commander.commanderResign`` -> void
-  ``commander.satellite`` -> bool
-  ``commander.sendOrder`` int bool -> void
-  ``commander.supplies`` -> bool
-  ``commander.toggleArtilleryState`` -> void
-  ``commander.toggleSupplyState`` -> void
-  ``commander.toggleUAVState`` -> void
-  ``commander.toggleVehicleDropState`` -> void
-  ``commander.uav`` -> bool
-  ``commander.vehicleDrop`` -> bool
-  ``commander.zoomCommander`` -> bool

``commanderInterface``
----------------------

-  ``commanderInterface.selectOrder`` std::string -> bool
-  ``commanderInterface.setstd::stringMap`` std::string std::string std::string -> void

``commanderMenu``
-----------------

-  ``commanderMenu.deselect`` -> void
-  ``commanderMenu.doubleClick`` -> void
-  ``commanderMenu.rightClick`` -> void
-  ``commanderMenu.sendRadioMessage`` std::string TargetChannel -> void
-  ``commanderMenu.singleClick`` -> void
-  ``commanderMenu.vehicleDropReloadTime`` float -> float

``Console``
-----------

-  ``Console.allowMultipleFileLoad`` bool -> bool
-  ``Console.bindKeyToConsoleScript`` int std::string -> bool
-  ``Console.echo`` bool -> bool
-  ``Console.echoErrors`` bool -> bool
-  ``Console.getActiveMethods`` std::string -> std::string
-  ``Console.getArgumentTypes`` std::string std::string -> std::string
-  ``Console.getCategory`` std::string std::string -> std::string
-  ``Console.getDelta`` std::string std::string -> std::string
-  ``Console.getEnumName`` std::string std::string int -> std::string
-  ``Console.getRange`` std::string std::string -> std::string
-  ``Console.getReturnType`` std::string std::string -> std::string
-  ``Console.getTypeDescription`` std::string std::string -> std::string
-  ``Console.hasBundledType`` std::string std::string -> std::string
-  ``Console.hasRange`` std::string std::string -> std::string
-  ``Console.isDynamic`` std::string std::string -> std::string
-  ``Console.isSetGet`` std::string std::string -> std::string
-  ``Console.listConstants`` std::string -> std::string
-  ``Console.listVariables`` std::string -> std::string
-  ``Console.maxCommandHistorySize`` int -> int
-  ``Console.maxHistorySize`` int -> int
-  ``Console.maxLineSize`` int -> int
-  ``Console.run`` std::string std::string std::string -> std::string
-  ``Console.useRelativePaths`` bool -> bool
-  ``Console.workingPath`` std::string -> std::string

``controlMap``
--------------

-  ``controlMap.addAxisToAxisMapping`` int InputDeviceFlags InputDeviceAxes -> void
-  ``controlMap.addAxisToTriggerMapping`` int int InputDeviceFlags -> void
-  ``controlMap.addButtonAndKeyToAxisMapping`` int InputDeviceFlags InputDeviceButtons -> void
-  ``controlMap.addButtonsToAxisMapping`` int InputDeviceFlags InputDeviceButtons -> void
-  ``controlMap.addButtonToTriggerMapping`` int InputDeviceFlags InputDeviceButtons -> void
-  ``controlMap.addKeyAndButtonToAxisMapping`` int InputDeviceFlags InputDeviceKeys -> void
-  ``controlMap.addKeysToAxisMapping`` int InputDeviceFlags InputDeviceKeys -> void
-  ``controlMap.AddKeyToTriggerMapping`` int InputDeviceFlags InputDeviceKeys -> void
-  ``controlMap.create`` std::string -> void
-  ``controlMap.deleteControlMap`` std::string -> void
-  ``controlMap.dump`` -> void
-  ``controlMap.InvertMouse`` bool -> bool
-  ``controlMap.keyboardSensitivity`` float -> float
-  ``controlMap.mouseSensitivity`` float -> float
-  ``controlMap.setActive`` std::string -> void
-  ``controlMap.setAxisScale`` io::InputDeviceAxes float -> void
-  ``controlMap.setButtonFallTime`` float -> void
-  ``controlMap.setButtonRiseTime`` float -> void
-  ``controlMap.setDoubleTapTime`` float -> void
-  ``controlMap.setPitchFactor`` float -> void
-  ``controlMap.setYawFactor`` float -> void

``DecalManager``
----------------

-  ``decalManager.decalGeomClipAngle`` float -> float

-  ``decalManager.decalNormalOffset`` float -> float

-  ``decalManager.drawStats`` bool -> bool

-  ``decalManager.fadeDistance`` float -> float

   Set the View Distance of the Decals to start to fade. Works in level .con files

-  ``decalManager.fadeOutAtPercentageOfTimeToLive`` float -> float

-  ``decalManager.generateTexture`` -> bool

-  ``decalManager.startFadePercentageOfFadeDistancel`` float -> float

-  ``decalManager.timeToLive`` float -> float

   Time in seconds of how long will a vehicle, effect or projectile will last. For vehicles, if it has been exited for a time, it will blow up. Uses CRD Arguments.

   `More info <http://bfmods.com/mdt/scripting/ObjectTemplate/Properties/TimeToLive.html>`__

-  ``demo.recordDemo`` std::string -> void

   Starts the Battlerecorder Recording. Needs to specify a name. File is saved in mods/(mod)/Demos. In My Documents/Project Reality/Profile/001 (i.e 002, 003, default) create a demos folder and place both files there.

``demo``
--------

-  ``demo.restartDemo`` -> void

-  ``demo.shutdownDemo`` -> void

-  ``demo.stopRecording`` -> void

   Console ~ Command

   Stops the Battlerecorder Recording. File is saved in mods/(mod)/Demos. In My Documents/Battlefield 2/Profile/001 etc create a demos folder and place both files there.

-  ``demo.toggleCameraDemo`` -> void

-  ``demo.toggleDemoPauseOrPlay`` -> void

-  ``demo.togglePlayerDemo`` bool -> void

``Editor``
----------

-  ``Editor.createNewLayer`` std::string -> void
-  ``Editor.deleteAllLayers`` -> void
-  ``Editor.deleteAllObjects`` -> std::string
-  ``Editor.deleteObject`` world::IObject_ptrproxy -> void
-  ``Editor.deleteTemplate`` world::IObjectTemplate_ptrproxy -> void
-  ``Editor.getActiveLayer`` -> std::string
-  ``Editor.getActiveLayerId`` -> int
-  ``Editor.getActiveObject`` -> world::IObject_ptrproxy
-  ``Editor.getActiveObjectTemplate`` -> world::IObjectTemplate_ptrproxy
-  ``Editor.hideLayer`` std::string -> void
-  ``Editor.listAllVehicles`` -> std::string
-  ``Editor.listLayers`` -> std::string
-  ``Editor.listMeshes`` -> std::string
-  ``Editor.listObjects`` -> std::string
-  ``Editor.listObjectsOfTemplate`` world::IObjectTemplate_ptrproxy -> std::string
-  ``Editor.listTemplates`` std::string -> std::string
-  ``Editor.listTextures`` -> std::string
-  ``Editor.loadAllObjects`` std::string -> bool
-  ``Editor.loadAllTemplatesAndObjects`` -> bool
-  ``Editor.printObjectCreationScript`` world::IObject_ptrproxy -> std::string
-  ``Editor.printTemplateCreationScript`` world::IObjectTemplate_ptrproxy -> std::string
-  ``Editor.quickReloadActiveTemplate`` -> void
-  ``Editor.quickReloadTemplate`` world::IObjectTemplate_ptrproxy -> void
-  ``Editor.removeLayer`` std::string -> void
-  ``Editor.renameLayer`` std::string std::string -> void
-  ``Editor.saveAllEffects`` -> void
-  ``Editor.saveAllObjects`` std::string -> bool
-  ``Editor.saveAllSpawners`` -> bool
-  ``Editor.saveAllTemplates`` -> bool
-  ``Editor.saveAllTemplatesAndObjects`` -> bool
-  ``Editor.saveAllUsedTemplates`` std::string -> bool
-  ``Editor.saveFolderToArchive`` std::string bool bool -> int
-  ``Editor.saveSpawners`` bool bool bool -> void
-  ``Editor.saveTemplateToFile`` std::string std::string -> bool
-  ``Editor.saveTemplateTreeStructure`` std::string std::string -> int
-  ``Editor.saveVehicles`` bool -> bool
-  ``Editor.setActiveLayer`` std::string -> void
-  ``Editor.setActiveLayerId`` int -> void
-  ``Editor.setActiveObject`` world::IObject_ptrproxy -> world::IObject_ptrproxy
-  ``Editor.setActiveObjectTemplate`` world::IObjectTemplate_ptrproxy -> world::IObjectTemplate_ptrproxy
-  ``Editor.ShowEntryPoints`` bool -> bool
-  ``Editor.showLayer`` std::string -> void
-  ``Editor.start`` world::IObject_ptrproxy -> void
-  ``Editor.stop`` world::IObject_ptrproxy -> void
-  ``Editor.updateAllTemplates`` -> void
-  ``Editor.updateTemplate`` world::IObjectTemplate_ptrproxy -> void

``effectTweak``
---------------

-  ``effectTweak.setAgeScaleFactorForAllEffects`` float -> void

-  ``effectTweak.setAlphaIntensityForAllEffects`` float -> void

-  ``effectTweak.setEmitScaleFactorForAllEffects`` float -> void

-  ``effectTweak.setEmitSpeedScaleFactorForAllEffects`` float -> void

-  ``effectTweak.setSoundIntensity`` float -> void

-  ``effectTweak.setStartAgeForAllEffects`` float -> void

-  ``envmapManager.generateEnvMaps`` -> void

-  ``envmapManager.loadEMIFile`` std::string -> void

-  ``envmapManager.perPixelEnvironmentMappingEnabled`` bool -> bool

-  ``envmapManager.save`` -> void

-  ``fileManager.addPath`` std::string -> void

-  ``fileManager.copyFile`` std::string std::string -> bool

-  ``fileManager.deleteFile`` std::string -> bool

-  ``fileManager.fileExists`` std::string -> bool

-  ``fileManager.mountArchive`` std::string std::string bool -> void

-  ``fileManager.moveFile`` std::string std::string -> bool

-  ``game.allowToggleFullscreen`` bool -> bool

-  ``game.lockFps`` int -> int

   Sets a fps cap, makes it so that the fps can’t go higher than the given number.

``gameLogic``
-------------

-  ``gameLogic.AddInvalidDropVehicleObject`` std::string bool -> void

-  ``gameLogic.becomeSquadLeader`` bool -> bool

-  ``gameLogic.createObject`` std::string -> void

-  ``gameLogic.damageForBeingOutSideWorld`` float -> float

-  ``gameLogic.defaultLevel`` std::string -> std::string

-  ``gameLogic.defaultTimeToNextAIWave`` float -> float

-  ``gameLogic.enableVoHelp`` bool -> bool

   -  Enables the Voice Over Tips feature from vBF2.
   -  Uses ``prhelp.utxt`` in localization for std::strings/anything with HUD_HELP definitions
   -  HudElementsHelp.con in Menu for the size, color, fade in time, create more messages and VoiceMessages_Help.con for voiceovers

-  ``gameLogic.extraUAVVehicleFlightHeight`` float -> float

-  ``gameLogic.feslEnvironment`` int -> int

-  ``gameLogic.getBeforeSpawnCameraDirection`` -> Vec3

-  ``gameLogic.getBeforeSpawnCameraPosition`` -> Vec3

-  ``gameLogic.getDefaultNumberOfTickets`` U32 -> U32

-  ``gameLogic.getDefaultNumberOfTicketsEx`` U32 U32 -> U32

-  ``gameLogic.getNumberOfTickets`` U32 -> U32

-  ``gameLogic.getTeamDropVehicle`` int -> std::string

-  ``gameLogic.getTeamLanguage`` int -> std::string

-  ``gameLogic.getTeamName`` int -> std::string

-  ``gameLogic.getTicketLossAtEndPerMin`` -> float

-  ``gameLogic.getTicketLossPerMin`` U32 -> float

-  ``gameLogic.hitIndicationThreshold`` float -> float

-  ``gameLogic.maximumLevelViewDistance`` float -> float

-  ``gameLogic.messages.addHelpMessage`` std::string std::string -> int

-  ``gameLogic.messages.addMessage`` std::string -> int

-  ``gameLogic.messages.addRadioFilter`` std::string std::string -> int

-  ``gameLogic.messages.addRadioVoice`` std::string std::string std::string -> int

-  ``gameLogic.messages.playHelpMessage`` std::string -> int

-  ``gameLogic.messages.playRadioMessage`` int std::string std::string -> int

-  ``gameLogic.messages.setVolumes`` float float -> void

-  ``gameLogic.noVehiclesOmit`` std::string -> void

-  ``gameLogic.outputPlayerStats`` bool -> bool

-  ``gameLogic.printCameraCoordToConsole`` -> void

-  ``gameLogic.refreshTriggerables`` -> void

-  ``gameLogic.remoteCommand`` int int int -> bool

-  ``gameLogic.reset`` -> void

-  ``gameLogic.roundNr`` int -> int

-  ``gameLogic.setAirMouseInverted`` bool -> void

-  ``gameLogic.setAirMouseSensitivity`` float -> float

-  ``gameLogic.setBeforeSpawnCamera`` Vec3 Vec3 -> void

-  ``gameLogic.setDefaultNumberOfTickets`` U32 U32 -> void

-  ``gameLogic.setDefaultNumberOfTicketsEx`` U32 U32 U32 -> void

-  ``gameLogic.setDropVehicleDeviationRadius`` int int -> void

-  ``gameLogic.setKit`` int KitType std::string -> void

-  ``gameLogic.setNumberOfTickets`` U32 U32 -> void

-  ``gameLogic.setNumDropVehiclesForTeam`` int int -> void

-  ``gameLogic.setTeamDropVehicle`` int std::string -> void

-  ``gameLogic.setTeamFlag`` int std::string -> void

-  ``gameLogic.setTeamLanguage`` int std::string -> void

-  ``gameLogic.setTeamName`` int std::string -> void

-  ``gameLogic.setTicketLossAtEndPerMin`` float -> void

-  ``gameLogic.setTicketLossPerMin`` U32 float -> void

-  ``gameLogic.spawnAtCameraPosition`` bool -> bool

-  ``gameLogic.spawnObjectSpeed`` float -> float

-  ``gameLogic.spawnPlayers`` bool -> bool

-  ``gameLogic.supplyDropHeight`` float -> float

-  ``gameLogic.supplyDropNumSecsToLive`` float -> float

-  ``gameLogic.teleport`` -> void

-  ``gameLogic.teleportCameraTo`` Vec3 -> void

-  ``gameLogic.teleportTo`` Vec3 -> void

-  ``gameLogic.timeAllowedOutSideWorld`` float -> float

-  ``gameLogic.timeToNextAIWave`` float -> float

-  ``gameLogic.togglePause`` -> void

   Console ~ Command

   Pauses the game. Pressing ‘P’ in COOP and Local does the same thing.

-  ``gameLogic.vehicleDropHeight`` float -> float

-  ``Game.radioMessage`` TargetChannel std::string -> void

-  ``game.sayAll`` std::string -> void

-  ``game.sayTeam`` int std::string -> void

``gameServerSettings``
----------------------

-  ``gameServerSettings.setAdminScript`` std::string -> void
-  ``gameServerSettings.setAllowNATNegotation`` bool -> void
-  ``gameServerSettings.setAutoBalanceTeam`` bool -> void
-  ``gameServerSettings.setAutoRecord`` bool -> void
-  ``gameServerSettings.setAutoRecordRounds`` int -> void
-  ``gameServerSettings.setCommunityLogoURL`` std::string -> void
-  ``gameServerSettings.setCoopBotCount`` int -> void
-  ``gameServerSettings.setCoopBotDifficulty`` float -> void
-  ``gameServerSettings.setCoopBotRatio`` float -> void
-  ``gameServerSettings.setDemoDownloadURL`` std::string -> void
-  ``gameServerSettings.setDemoHook`` std::string -> void
-  ``gameServerSettings.setDemoIndexURL`` std::string -> void
-  ``gameServerSettings.setEndDelay`` int -> void
-  ``gameServerSettings.setFriendlyFireWithMines`` bool -> void
-  ``gameServerSettings.setGameMode`` std::string -> void
-  ``gameServerSettings.setGameSpyPort`` int -> void
-  ``gameServerSettings.setInterfaceIP`` std::string -> void
-  ``gameServerSettings.setInternet`` bool -> void
-  ``gameServerSettings.setManDownTime`` float -> void
-  ``gameServerSettings.setMaxPlayers`` int -> void
-  ``gameServerSettings.setMinPlayersForVoting`` int -> void
-  ``gameServerSettings.setNoVehicles`` float -> void
-  ``gameServerSettings.setPassword`` std::string -> void
-  ``gameServerSettings.setPunishTeamKills`` bool -> void
-  ``gameServerSettings.setRoundsPerMap`` int -> void
-  ``gameServerSettings.setScoreLimit`` int -> void
-  ``gameServerSettings.setServerName`` std::string -> void
-  ``gameServerSettings.setSoldierFF`` int -> void
-  ``gameServerSettings.setSoldierSplashFF`` int -> void
-  ``gameServerSettings.setSpawnTime`` float -> void
-  ``gameServerSettings.setSponsorLogoURL`` std::string -> void
-  ``gameServerSettings.setSponsorText`` std::string -> void
-  ``gameServerSettings.setStartDelay`` int -> void
-  ``gameServerSettings.setSvPunkBuster`` bool -> void
-  ``gameServerSettings.setTeamRatio`` float -> void
-  ``gameServerSettings.setTeamVoteOnly`` bool -> void
-  ``gameServerSettings.setTicketRatio`` int -> void
-  ``gameServerSettings.setTimeBeforeRestartMap`` float -> void
-  ``gameServerSettings.setTimeLimit`` int -> void
-  ``gameServerSettings.setVehicleFF`` int -> void
-  ``gameServerSettings.setVehicleSplashFF`` int -> void
-  ``gameServerSettings.setVoipBFClientPort`` int -> void
-  ``gameServerSettings.setVoipBFServerPort`` int -> void
-  ``gameServerSettings.setVoipEnabled`` bool -> void
-  ``gameServerSettings.setVoipQuality`` int -> void
-  ``gameServerSettings.setVoipServerPort`` int -> void
-  ``gameServerSettings.setVoipServerRemote`` bool -> void
-  ``gameServerSettings.setVoipServerRemoteIP`` std::string -> void
-  ``gameServerSettings.setVoipSharedPassword`` std::string -> void
-  ``gameServerSettings.setVoteTime`` int -> void
-  ``game.simulationRate`` int -> int

   -  ``HudElementsDemoRecComm.con``
   -  In Battlerecorder it sets the speed for the decrease speed and increase speed buttons.
   -  Can be increased, though some users report no difference as it is dependent on the Demo FPS (Default is 30 settings must be recorded higher something like 60) and Game FPS

-  ``game.toggleFullscreen`` -> void

   -  ~ Console
   -  Toggles Full-Screen and Windowed mode
   -  It will give you the nasty side-effect of seethrough terrain that would need the client to disconnect and reconnect to fix.

-  ``game.unload`` -> bool

``generalSettings``
-------------------

-  ``generalSettings.addFavouriteServer`` std::string int std::string -> void
-  ``generalSettings.addServerHistory`` std::string int std::string -> void
-  ``generalSettings.setAllowPunkBuster`` bool -> void
-  ``generalSettings.setAutoReady`` bool -> void
-  ``generalSettings.setAutoReload`` bool -> void
-  ``generalSettings.setBFTVSaveDirectory`` std::string -> void
-  ``generalSettings.setBotSkill`` float -> void
-  ``generalSettings.setBuddytagColor`` int int int -> void
-  ``generalSettings.setConfirmQuit`` bool -> void
-  ``generalSettings.setConnectionType`` int -> void
-  ``generalSettings.setCrosshairColor`` int int int -> void
-  ``generalSettings.setHUDTransparency`` float -> void
-  ``generalSettings.setItemSelectionReverseItems`` bool -> void
-  ``generalSettings.setLCDDisplayModes`` bool -> void
-  ``generalSettings.setMapIconAlphaTransparency`` float -> void
-  ``generalSettings.setMaxBots`` int -> void
-  ``generalSettings.setMaxBotsIncludeHumans`` bool -> void
-  ``generalSettings.setMinimapRotate`` bool -> void
-  ``generalSettings.setMinimapTransparency`` float -> void
-  ``generalSettings.setNumRoundsPlayed`` int -> void
-  ``generalSettings.setOutOfVoting`` bool -> void
-  ``generalSettings.setPlayedVOHelp`` std::string -> void
-  ``generalSettings.setServerFilter`` std::string -> void
-  ``generalSettings.setSortKey`` std::string -> void
-  ``generalSettings.setSortOrder`` int -> void
-  ``generalSettings.setSquadtagColor`` int int int -> void
-  ``generalSettings.setToggleFilters`` int -> void
-  ``generalSettings.setUseAdvancedServerBrowser`` bool -> void
-  ``generalSettings.setUseBots`` bool -> void
-  ``generalSettings.setViewIntroMovie`` bool -> void

``geometryTemplate``
--------------------

-  ``geometryTemplate.active`` IGeometryTemplate\* -> IGeometryTemplate\*
-  ``geometryTemplate.color`` Vec3 -> Vec3
-  ``geometryTemplate.compressVertexData`` bool -> bool
-  ``GeometryTemplate.create`` std::string std::string -> IGeometryTemplate\*

   -  Used in ``.con`` files
   -  Creates a Geometry Mesh template from the geometry mesh name so it can be used in other files without creating a duplicate mesh

-  ``geometryTemplate.depth`` float -> float
-  ``geometryTemplate.doNotGenerateLightmaps`` bool -> bool
-  ``geometryTemplate.dumpInstances`` -> void
-  ``geometryTemplate.glowFadeOutDistEnd`` float -> float
-  ``geometryTemplate.glowFadeOutDistStart`` float -> float
-  ``geometryTemplate.glowing`` bool -> bool
-  ``geometryTemplate.height`` float -> float
-  ``geometryTemplate.ignoreLeafLighting`` bool -> bool
-  ``geometryTemplate.innerRadius`` float -> float
-  ``geometryTemplate.lenght`` float -> float
-  ``geometryTemplate.length`` float -> float
-  ``geometryTemplate.lightmapOverride`` bool -> bool
-  ``geometryTemplate.maxSkip3pLods`` uint -> uint
-  ``geometryTemplate.maxSkipWreckLods`` uint -> uint
-  ``geometryTemplate.maxTextureRepeat`` int -> int
-  ``geometryTemplate.meshDetailLevel`` int -> int
-  ``geometryTemplate.name`` -> std::string
-  ``geometryTemplate.noLighting`` bool -> bool
-  ``geometryTemplate.nrOfAnimatedUVMatrix`` int -> int
-  ``geometryTemplate.outerRadius`` float -> float
-  ``GeometryTemplate.printInfo`` bool -> std::string
-  ``geometryTemplate.radius1`` float -> float
-  ``geometryTemplate.radius2`` float -> float
-  ``geometryTemplate.rings`` uint -> uint
-  ``geometryTemplate.setLightmapSizeAll`` int int int -> void
-  ``geometryTemplate.setMaterialParallaxHeightScale`` int int int -> void
-  ``geometryTemplate.setMaterialReflectionScale`` int int int -> void
-  ``geometryTemplate.setSpecularStaticGloss`` int int int -> void
-  ``geometryTemplate.setSubGeometryLodDistance`` int int float -> void
-  ``geometryTemplate.shader`` std::string -> std::string
-  ``geometryTemplate.shadowDetailLevel`` int -> int
-  ``geometryTemplate.sides`` uint -> uint
-  ``geometryTemplate.slices`` uint -> uint
-  ``geometryTemplate.stacks`` uint -> uint
-  ``geometryTemplate.tesselation`` BaseVector2 -> BaseVector2
-  ``geometryTemplate.texture`` std::string -> std::string
-  ``geometryTemplate.useRadiusForShadowDepth`` bool -> bool
-  ``geometryTemplate.useRadiusForShadowSpatial`` bool -> bool
-  ``geometryTemplate.width`` float -> float

``globalSettings``
------------------

-  ``globalSettings.setDefaultUser`` std::string -> void
-  ``globalSettings.setNamePrefix`` std::string -> void

``hapticSettings``
------------------

-  ``hapticSettings.addWeaponClassMap`` std::string int -> void
-  ``hapticSettings.load`` -> bool
-  ``hapticSettings.setAimSensitivity`` float float float -> void
-  ``hapticSettings.setAimSensitivityAIR`` float float float -> void
-  ``hapticSettings.setAimSensitivityHELI`` float float float -> void
-  ``hapticSettings.setAimSensitivityLAND`` float float float -> void
-  ``hapticSettings.setAimSensitivityLength`` float float float -> void
-  ``hapticSettings.setAimSensitivityLengthAIR`` float float float -> void
-  ``hapticSettings.setAimSensitivityLengthHELI`` float float float -> void
-  ``hapticSettings.setAimSensitivityLengthLAND`` float float float -> void
-  ``hapticSettings.setAimSensitivityLengthSEA`` float float float -> void
-  ``hapticSettings.setAimSensitivityLengthSOLDIER`` float float float -> void
-  ``hapticSettings.setAimSensitivitySEA`` float float float -> void
-  ``hapticSettings.setAimSensitivitySOLDIER`` float float float -> void
-  ``hapticSettings.setControlBoxLength`` float float float -> void
-  ``hapticSettings.setControlBoxLengthAIR`` float float float -> void
-  ``hapticSettings.setControlBoxLengthHELI`` float float float -> void
-  ``hapticSettings.setControlBoxLengthLAND`` float float float -> void
-  ``hapticSettings.setControlBoxLengthSEA`` float float float -> void
-  ``hapticSettings.setControlBoxLengthSOLDIER`` float float float -> void
-  ``hapticSettings.setControlBoxStiffness`` float float float -> void
-  ``hapticSettings.setControlBoxStiffnessAIR`` float float float -> void
-  ``hapticSettings.setControlBoxStiffnessHELI`` float float float -> void
-  ``hapticSettings.setControlBoxStiffnessLAND`` float float float -> void
-  ``hapticSettings.setControlBoxStiffnessSEA`` float float float -> void
-  ``hapticSettings.setControlBoxStiffnessSOLDIER`` float float float -> void
-  ``hapticSettings.setDamageScale`` float -> void
-  ``hapticSettings.setExplosionShakeScale`` float -> void
-  ``hapticSettings.setForceCapX`` float -> void
-  ``hapticSettings.setForceCapY`` float -> void
-  ``hapticSettings.setForceCapZ`` float -> void
-  ``hapticSettings.setGeneralShakeScale`` float -> void
-  ``hapticSettings.setPhysicsAIRScale`` float float float -> void
-  ``hapticSettings.setPhysicsAIRScaleXHigh`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleXLow`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleXMed`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleYHigh`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleYLow`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleYMed`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleZHigh`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleZLow`` float -> void
-  ``hapticSettings.setPhysicsAIRScaleZMed`` float -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeXHigh`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeXLow`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeXMed`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeYHigh`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeYLow`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeYMed`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeZHigh`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeZLow`` int -> void
-  ``hapticSettings.setPhysicsAIRSmoothTimeZMed`` int -> void
-  ``hapticSettings.setPhysicsAIRTransitionValueHigh`` float -> void
-  ``hapticSettings.setPhysicsAIRTransitionValueMed`` float -> void
-  ``hapticSettings.setPhysicsHELIScale`` float float float -> void
-  ``hapticSettings.setPhysicsHELIScaleXHigh`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleXLow`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleXMed`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleYHigh`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleYLow`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleYMed`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleZHigh`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleZLow`` float -> void
-  ``hapticSettings.setPhysicsHELIScaleZMed`` float -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeXHigh`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeXLow`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeXMed`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeYHigh`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeYLow`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeYMed`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeZHigh`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeZLow`` int -> void
-  ``hapticSettings.setPhysicsHELISmoothTimeZMed`` int -> void
-  ``hapticSettings.setPhysicsHELITransitionValueHigh`` float -> void
-  ``hapticSettings.setPhysicsHELITransitionValueMed`` float -> void
-  ``hapticSettings.setPhysicsLANDScale`` float float float -> void
-  ``hapticSettings.setPhysicsLANDScaleXHigh`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleXLow`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleXMed`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleYHigh`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleYLow`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleYMed`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleZHigh`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleZLow`` float -> void
-  ``hapticSettings.setPhysicsLANDScaleZMed`` float -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeXHigh`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeXLow`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeXMed`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeYHigh`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeYLow`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeYMed`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeZHigh`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeZLow`` int -> void
-  ``hapticSettings.setPhysicsLANDSmoothTimeZMed`` int -> void
-  ``hapticSettings.setPhysicsLANDTransitionValueHigh`` float -> void
-  ``hapticSettings.setPhysicsLANDTransitionValueMed`` float -> void
-  ``hapticSettings.setPhysicsSEAScale`` float float float -> void
-  ``hapticSettings.setPhysicsSEAScaleXHigh`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleXLow`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleXMed`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleYHigh`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleYLow`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleYMed`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleZHigh`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleZLow`` float -> void
-  ``hapticSettings.setPhysicsSEAScaleZMed`` float -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeXHigh`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeXLow`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeXMed`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeYHigh`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeYLow`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeYMed`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeZHigh`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeZLow`` int -> void
-  ``hapticSettings.setPhysicsSEASmoothTimeZMed`` int -> void
-  ``hapticSettings.setPhysicsSEATransitionValueHigh`` float -> void
-  ``hapticSettings.setPhysicsSEATransitionValueMed`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScale`` float float float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleXHigh`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleXLow`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleXMed`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleYHigh`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleYLow`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleYMed`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleZHigh`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleZLow`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERScaleZMed`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeXHigh`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeXLow`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeXMed`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeYHigh`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeYLow`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeYMed`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeZHigh`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeZLow`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERSmoothTimeZMed`` int -> void
-  ``hapticSettings.setPhysicsSOLDIERTransitionValueHigh`` float -> void
-  ``hapticSettings.setPhysicsSOLDIERTransitionValueMed`` float -> void
-  ``hapticSettings.setRecoilPitchScaleCARBINE`` float -> void
-  ``hapticSettings.setRecoilPitchScaleDEFIB`` float -> void
-  ``hapticSettings.setRecoilPitchScaleDROP`` float -> void
-  ``hapticSettings.setRecoilPitchScaleKNIFE`` float -> void
-  ``hapticSettings.setRecoilPitchScaleLAUNCHER`` float -> void
-  ``hapticSettings.setRecoilPitchScaleLMG`` float -> void
-  ``hapticSettings.setRecoilPitchScalePISTOL`` float -> void
-  ``hapticSettings.setRecoilPitchScaleRIFLE`` float -> void
-  ``hapticSettings.setRecoilPitchScaleRIFLELAUNCHER`` float -> void
-  ``hapticSettings.setRecoilPitchScaleSHOTGUN`` float -> void
-  ``hapticSettings.setRecoilPitchScaleSMG`` float -> void
-  ``hapticSettings.setRecoilPitchScaleSNIPER`` float -> void
-  ``hapticSettings.setRecoilPitchScaleTHROWN`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_AIRGUN`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_ARMORCANNON`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_COAXIALGUN`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_HELIGUN`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_HMG`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_LMG`` float -> void
-  ``hapticSettings.setRecoilPitchScaleV_MISSILE`` float -> void
-  ``hapticSettings.setRecoilPunchScaleCARBINE`` float -> void
-  ``hapticSettings.setRecoilPunchScaleDEFIB`` float -> void
-  ``hapticSettings.setRecoilPunchScaleDROP`` float -> void
-  ``hapticSettings.setRecoilPunchScaleKNIFE`` float -> void
-  ``hapticSettings.setRecoilPunchScaleLAUNCHER`` float -> void
-  ``hapticSettings.setRecoilPunchScaleLMG`` float -> void
-  ``hapticSettings.setRecoilPunchScalePISTOL`` float -> void
-  ``hapticSettings.setRecoilPunchScaleRIFLE`` float -> void
-  ``hapticSettings.setRecoilPunchScaleRIFLELAUNCHER`` float -> void
-  ``hapticSettings.setRecoilPunchScaleSHOTGUN`` float -> void
-  ``hapticSettings.setRecoilPunchScaleSMG`` float -> void
-  ``hapticSettings.setRecoilPunchScaleSNIPER`` float -> void
-  ``hapticSettings.setRecoilPunchScaleTHROWN`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_AIRGUN`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_ARMORCANNON`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_COAXIALGUN`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_HELIGUN`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_HMG`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_LMG`` float -> void
-  ``hapticSettings.setRecoilPunchScaleV_MISSILE`` float -> void
-  ``hapticSettings.setRecoilPunchTimeCARBINE`` float -> void
-  ``hapticSettings.setRecoilPunchTimeDEFIB`` float -> void
-  ``hapticSettings.setRecoilPunchTimeDROP`` float -> void
-  ``hapticSettings.setRecoilPunchTimeKNIFE`` float -> void
-  ``hapticSettings.setRecoilPunchTimeLAUNCHER`` float -> void
-  ``hapticSettings.setRecoilPunchTimeLMG`` float -> void
-  ``hapticSettings.setRecoilPunchTimePISTOL`` float -> void
-  ``hapticSettings.setRecoilPunchTimeRIFLE`` float -> void
-  ``hapticSettings.setRecoilPunchTimeRIFLELAUNCHER`` float -> void
-  ``hapticSettings.setRecoilPunchTimeSHOTGUN`` float -> void
-  ``hapticSettings.setRecoilPunchTimeSMG`` float -> void
-  ``hapticSettings.setRecoilPunchTimeSNIPER`` float -> void
-  ``hapticSettings.setRecoilPunchTimeTHROWN`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_AIRGUN`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_ARMORCANNON`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_COAXIALGUN`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_HELIGUN`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_HMG`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_LMG`` float -> void
-  ``hapticSettings.setRecoilPunchTimeV_MISSILE`` float -> void
-  ``hapticSettings.setRecoilYawScaleCARBINE`` float -> void
-  ``hapticSettings.setRecoilYawScaleDEFIB`` float -> void
-  ``hapticSettings.setRecoilYawScaleDROP`` float -> void
-  ``hapticSettings.setRecoilYawScaleKNIFE`` float -> void
-  ``hapticSettings.setRecoilYawScaleLAUNCHER`` float -> void
-  ``hapticSettings.setRecoilYawScaleLMG`` float -> void
-  ``hapticSettings.setRecoilYawScalePISTOL`` float -> void
-  ``hapticSettings.setRecoilYawScaleRIFLE`` float -> void
-  ``hapticSettings.setRecoilYawScaleRIFLELAUNCHER`` float -> void
-  ``hapticSettings.setRecoilYawScaleSHOTGUN`` float -> void
-  ``hapticSettings.setRecoilYawScaleSMG`` float -> void
-  ``hapticSettings.setRecoilYawScaleSNIPER`` float -> void
-  ``hapticSettings.setRecoilYawScaleTHROWN`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_AIRGUN`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_ARMORCANNON`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_COAXIALGUN`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_HELIGUN`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_HMG`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_LMG`` float -> void
-  ``hapticSettings.setRecoilYawScaleV_MISSILE`` float -> void
-  ``hapticSettings.setSpeedShakeScale`` float -> void
-  ``hapticSettings.setTurnSensitivity`` float float float -> void
-  ``hapticSettings.setTurnSensitivityAIR`` float float float -> void
-  ``hapticSettings.setTurnSensitivityHELI`` float float float -> void
-  ``hapticSettings.setTurnSensitivityLAND`` float float float -> void
-  ``hapticSettings.setTurnSensitivitySEA`` float float float -> void
-  ``hapticSettings.setTurnSensitivitySOLDIER`` float float float -> void

``heightmapcluster``
--------------------

-  ``heightmapcluster.addHeightmap`` std::string int int -> void
-  ``heightmapcluster.compileWaterMeshesIntoHeightmap`` -> void
-  ``heightmapcluster.create`` std::string -> void
-  ``heightmapcluster.importSurroundingRawHeightMap`` std::string -> bool
-  ``heightmapcluster.intersectCameraRay`` -> void
-  ``heightmapcluster.setClusterSize`` int -> void
-  ``heightmapcluster.setHeightmapSize`` int -> void
-  ``heightmapcluster.setSeaWaterLevel`` float -> void
-  ``heightmapcluster.smoothEdges`` int float float -> void
-  ``heightmapcluster.stitchEdges`` -> void
-  ``heightmap.loadHeightData`` std::string -> void
-  ``heightmap.loadMaterialData`` std::string -> void
-  ``heightmap.setBitResolution`` int -> void
-  ``heightmap.setMaterialScale`` int -> void
-  ``heightmap.setModified`` bool -> void
-  ``heightmap.setScale`` Vec3 -> void
-  ``heightmap.setSize`` int int -> void
-  ``hemiMapManager.hemiLerpBias`` float -> float
-  ``hemiMapManager.makeHemiMap`` unsigned long std::string Vec3 -> bool
-  ``hemiMapManager.setBaseHemiMap`` std::string Vec3 float -> bool

``hudBuilder``
--------------

-  ``hudBuilder.addNodeAlphaShowEffect`` -> bool
-  ``hudBuilder.addNodeBlendEffect`` int int -> bool
-  ``hudBuilder.addNodeMoveShowEffect`` float int -> bool
-  ``hudBuilder.addNodeVariableMoveShowEffect`` std::string std::string -> bool
-  ``hudBuilder.addObjectMarkerNodeLockTextNode`` std::string -> bool
-  ``hudBuilder.addTransformListNode`` std::string -> bool
-  ``hudBuilder.createBarNode`` std::string std::string int -> bool
-  ``hudBuilder.createButtonNode`` std::string std::string int -> bool
-  ``hudBuilder.createCompassNode`` std::string std::string int -> bool
-  ``hudBuilder.createEditNode`` std::string std::string int -> bool
-  ``hudBuilder.createHoverNode`` std::string std::string int -> bool
-  ``hudBuilder.createListNode`` std::string std::string int -> bool
-  ``hudBuilder.createMapNode`` std::string std::string -> bool
-  ``hudBuilder.createMiniMapNode`` std::string std::string int -> bool
-  ``hudBuilder.createObjectMarkerNode`` std::string std::string int -> bool
-  ``hudBuilder.createObjectSelectionNode`` std::string std::string int -> bool
-  ``hudBuilder.createOccupiedNode`` std::string std::string int -> bool
-  ``hudBuilder.createPictureNode`` std::string std::string int -> bool
-  ``hudBuilder.createSliderNode`` std::string std::string float -> bool
-  ``hudBuilder.createSplitNode`` std::string std::string -> bool
-  ``hudBuilder.createTextNode`` std::string std::string int -> bool
-  ``hudBuilder.createTileNode`` std::string std::string int -> bool
-  ``hudBuilder.createTransformListNode`` std::string std::string int -> bool
-  ``hudBuilder.createTransformNode`` std::string std::string int -> int
-  ``hudBuilder.deleteNode`` -> bool
-  ``hudBuilder.newLayer`` -> bool
-  ``hudBuilder.searchNodes`` std::string std::string -> meme::Node\*
-  ``hudBuilder.setActiveObject`` std::string std::string -> bool
-  ``hudBuilder.setBarNodeBorder`` int int int -> bool
-  ``hudBuilder.setBarNodeSnap`` int -> bool
-  ``hudBuilder.setBarNodeSnapDir`` bool -> bool
-  ``hudBuilder.setBarNodeTexture`` int std::string -> bool
-  ``hudBuilder.setBarNodeValueVariable`` std::string -> bool
-  ``hudBuilder.setBarNodeVariableTexture`` int std::string -> bool
-  ``hudBuilder.setButtonNodeAltConCmd`` std::string int -> bool
-  ``hudBuilder.setButtonNodeConCmd`` std::string int -> bool
-  ``hudBuilder.setButtonNodeDebug`` bool -> bool
-  ``hudBuilder.setButtonNodeFunction`` std::string int -> bool
-  ``hudBuilder.setButtonNodeMouseArea`` int int int -> bool
-  ``hudBuilder.setButtonNodeMouseOverColor`` float float float -> bool
-  ``hudBuilder.setButtonNodeTexture`` int std::string -> bool
-  ``hudBuilder.setCommanderPos`` Vec2 -> bool
-  ``hudBuilder.setCommanderSize`` Vec2 -> bool
-  ``hudBuilder.setCompassNodeBorder`` int int int -> bool
-  ``hudBuilder.setCompassNodeOffset`` int -> bool
-  ``hudBuilder.setCompassNodeSnapOffset`` int int int -> bool
-  ``hudBuilder.setCompassNodeSnapTexture`` bool std::string -> bool
-  ``hudBuilder.setCompassNodeTexture`` int std::string -> bool
-  ``hudBuilder.setCompassNodeTextureSize`` int int -> bool
-  ``hudBuilder.setCompassNodeValueVariable`` std::string -> bool
-  ``hudBuilder.setCompassNodeVariableTexture`` int std::string -> bool
-  ``hudBuilder.setCPFont`` std::string -> void
-  ``hudBuilder.setCPFontColor`` float float float -> void
-  ``hudBuilder.setEditNodeColor`` float float float -> bool
-  ``hudBuilder.setEditNodeData`` int -> bool
-  ``hudBuilder.setEditNodeFont`` std::string bool -> bool
-  ``hudBuilder.setEditNodeMaxLength`` int -> bool
-  ``hudBuilder.setEditNodestd::string`` int -> bool
-  ``hudBuilder.setHoverInMiddlePos`` int int -> bool
-  ``hudBuilder.setHoverMaxValue`` float -> bool
-  ``hudBuilder.setHoverWidthLength`` float float -> bool
-  ``hudBuilder.setListNodeBackgroundColor`` float float float -> bool
-  ``hudBuilder.setListNodeBorder`` int int int -> bool
-  ``hudBuilder.setListNodeBorderColor`` float float float -> bool
-  ``hudBuilder.setListNodeConCmd`` int std::string -> bool
-  ``hudBuilder.setListNodeData`` int -> bool
-  ``hudBuilder.setListNodeFont`` std::string int -> bool
-  ``hudBuilder.setListNodeOutline`` bool -> bool
-  ``hudBuilder.setListNodeRowSpacing`` int -> bool
-  ``hudBuilder.setListNodeScrollbar`` int int -> bool
-  ``hudBuilder.setListNodeScrollbarBackgroundColor`` float float float -> bool
-  ``hudBuilder.setListNodeScrollbarColor`` float float float -> bool
-  ``hudBuilder.setListNodeSelectColor`` float float float -> bool
-  ``hudBuilder.setMaxiPos`` Vec2 -> bool
-  ``hudBuilder.setMaxiSize`` Vec2 -> bool
-  ``hudBuilder.setMiniPos`` Vec2 -> bool
-  ``hudBuilder.setMiniSize`` Vec2 -> bool
-  ``hudBuilder.setModifyer`` float -> void
-  ``hudBuilder.setNodeAlphaVariable`` std::string -> bool
-  ``hudBuilder.setNodeColor`` float float float -> bool
-  ``hudBuilder.setNodeInTime`` float -> bool
-  ``hudBuilder.setNodeLogicShowVariable`` std::string std::string int -> bool
-  ``hudBuilder.setNodeOffset`` int int -> bool
-  ``hudBuilder.setNodeOutTime`` float -> bool
-  ``hudBuilder.setNodePos`` int int -> bool
-  ``hudBuilder.setNodePosVariable`` int std::string -> bool
-  ``hudBuilder.setNodeRGBVariables`` std::string std::string std::string -> bool
-  ``hudBuilder.setNodeShowVariable`` std::string -> bool
-  ``hudBuilder.setNodeSize`` int int -> bool
-  ``hudBuilder.setObjectMarkerNodeLockOnType`` int -> bool
-  ``hudBuilder.setObjectMarkerNodeLockText`` bool std::string -> bool
-  ``hudBuilder.setObjectMarkerNodeLockTextOffset`` int int -> bool
-  ``hudBuilder.setObjectMarkerNodeObjects`` int -> bool
-  ``hudBuilder.setObjectMarkerNodeTexture`` int std::string -> bool
-  ``hudBuilder.setObjectMarkerNodeTextureSize`` int int int -> bool
-  ``hudBuilder.setObjectMarkerNodeWeapon`` int -> bool
-  ``hudBuilder.setObjectSelectionNodePointerSize`` int int -> bool
-  ``hudBuilder.setOccupiedNodeData`` int -> bool
-  ``hudBuilder.setOccupiedNodePosVariable`` int std::string -> bool
-  ``hudBuilder.setPictureNodeAlphaMask`` std::string -> bool
-  ``hudBuilder.setPictureNodeBorder`` int int int -> bool
-  ``hudBuilder.setPictureNodeBorderColor`` float float float -> bool
-  ``hudBuilder.setPictureNodeCenterPoint`` int int -> bool
-  ``hudBuilder.setPictureNodeRotateVariable`` std::string -> bool
-  ``hudBuilder.setPictureNodeRotation`` int -> bool
-  ``hudBuilder.setPictureNodeTexture`` std::string -> bool
-  ``hudBuilder.setPictureNodeVariableTexture`` std::string -> bool
-  ``hudBuilder.setSliderNodeChild`` std::string -> bool
-  ``hudBuilder.setSliderNodeData`` std::string -> bool
-  ``hudBuilder.setTextNodeOutLine`` std::string -> bool
-  ``hudBuilder.setTextNodeOutLineOffset`` float float -> bool
-  ``hudBuilder.setTextNodestd::string`` std::string -> bool
-  ``hudBuilder.setTextNodestd::stringVariable`` std::string -> bool
-  ``hudBuilder.setTextNodeStyle`` std::string int -> bool
-  ``hudBuilder.setTileNodeOptions`` int int int -> bool
-  ``hudBuilder.setTranformListNodeOffset`` int int -> bool
-  ``hudBuilder.setTranformListNodePosVariable`` int std::string -> bool
-  ``hudBuilder.setZoomIcons`` bool -> bool
-  ``hudItems.setBool`` std::string bool -> void
-  ``hudItems.setFloat`` std::string float -> void
-  ``hudItems.setstd::string`` std::string std::string -> void
-  ``hudManager.addFavouriteServer`` bool -> void
-  ``hudManager.addTextureAtlas`` std::string -> void
-  ``hudManager.enableSayAllChatBox`` bool -> void
-  ``hudManager.enableSaySquadChatBox`` bool -> void
-  ``hudManager.enableSayTeamChatBox`` bool -> void
-  ``hudManager.refresh`` -> bool
-  ``hudManager.setCommMousePos`` int int -> bool
-  ``hudManager.setCommMouseSensitivity`` int -> bool
-  ``hudManager.setCommPos`` int int -> bool
-  ``hudManager.setCommSize`` int int -> bool
-  ``hudManager.setDisplayControlpoints`` bool -> void
-  ``hudManager.setDisplayTickets`` bool -> void
-  ``hudManager.setDone`` bool -> void
-  ``hudManager.setMapStatic`` bool -> void
-  ``hudManager.setMaximumNrOfCPs`` int -> void
-  ``hudManager.setMouseTextureArtillery`` std::string -> bool
-  ``hudManager.setMouseTextureCancel`` std::string -> bool
-  ``hudManager.setMouseTextureEmpty`` std::string -> bool
-  ``hudManager.setMouseTextureFull`` std::string -> bool
-  ``hudManager.setMouseTextureSupply`` std::string -> bool
-  ``hudManager.setMouseTextureUAV`` std::string -> bool
-  ``hudManager.setPaint`` bool -> void
-  ``hudManager.setPointerMouseSensitivity`` int -> bool
-  ``hudManager.setPointerSize`` int int -> bool
-  ``hudManager.setSpottedAngle`` float -> void
-  ``hudManager.setSpottedMenuPos`` int int -> bool
-  ``hudManager.setSpottedMenuSize`` int int -> bool
-  ``hudManager.setSpottedMousePos`` int int -> bool
-  ``hudManager.setTargetTop`` float -> void
-  ``hudManager.setUpdate`` bool -> void
-  ``ingameHelp.showIngameHelp`` std::string float -> void
-  ``InputDevices.setAxisScale`` InputDeviceFlags InputDeviceAxes float -> bool
-  ``InputDevices.setInvertAxis`` InputDeviceFlags InputDeviceAxes bool -> bool
-  ``itemSelection.setReverseItems`` bool -> void
-  ``levelsList.setVoteMapShow`` int -> void
-  ``levelsList.singleClick`` int -> void
-  ``lightManager.ambientColor`` Vec3 -> Vec3

``lightManager``
----------------

-  ``lightManager.defaultEffectLightAffectionFactor`` float -> float
-  ``lightManager.dynamicPointColor`` Vec3 -> Vec3
-  ``lightManager.dynamicPointColorHigh`` Vec3 -> Vec3
-  ``lightManager.dynamicPointColorLow`` Vec3 -> Vec3
-  ``lightManager.dynamicPointScale`` float -> float
-  ``lightManager.effectShadowColor`` Vec3 -> Vec3
-  ``lightManager.effectSunColor`` Vec3 -> Vec3
-  ``lightManager.enableStencilCullerReset`` bool -> bool
-  ``lightManager.enableSun`` bool -> bool
-  ``lightManager.groundHemi`` std::string -> std::string
-  ``lightManager.hemiLerpBias`` float -> float
-  ``lightManager.init`` -> void
-  ``lightManager.lightCullDistance`` float -> float

   -  Used in sky.con
   -  Raises the default limit of the culling of lightsources from a distance.
   -  Example: lightManager.lightCullDistance 2000 which extends the rendering of the lightsource.

-  ``lightManager.lightMapAmbientAlphaCutoffRange`` Vec2 -> Vec2
-  ``lightManager.maxLightsPerBundledMesh`` int -> int
-  ``lightManager.maxLightsPerSkinnedMesh`` int -> int
-  ``lightManager.maxLightsPerStaticMesh`` int -> int
-  ``lightManager.maxLightsPerTerrainPatch`` int -> int
-  ``lightManager.maxLodForMaterialBatching`` int -> int
-  ``lightManager.singlePointColor`` Vec3 -> Vec3
-  ``lightManager.singlePointColorHigh`` Vec3 -> Vec3
-  ``lightManager.singlePointColorLow`` Vec3 -> Vec3
-  ``lightManager.skinnedMeshShaderLodDistance`` float -> float
-  ``lightManager.skyColor`` Vec3 -> Vec3
-  ``lightManager.skyColorHigh`` Vec3 -> Vec3
-  ``lightManager.skyColorLow`` Vec3 -> Vec3
-  ``lightManager.staticLightBlendingTime`` double -> double
-  ``lightManager.staticSkyColor`` Vec3 -> Vec3
-  ``lightManager.staticSkyColorHigh`` Vec3 -> Vec3
-  ``lightManager.staticSkyColorLow`` Vec3 -> Vec3
-  ``lightManager.staticSpecularColor`` Vec3 -> Vec3
-  ``lightManager.staticSunColor`` Vec3 -> Vec3
-  ``lightManager.sunColor`` Vec3 -> Vec3
-  ``lightManager.sunColorHigh`` Vec3 -> Vec3
-  ``lightManager.sunColorLow`` Vec3 -> Vec3
-  ``lightManager.sunDirection`` Vec3 -> Vec3
-  ``lightManager.sunSpecColor`` Vec3 -> Vec3
-  ``lightManager.sunSpecColorHigh`` Vec3 -> Vec3
-  ``lightManager.sunSpecColorLow`` Vec3 -> Vec3
-  ``lightManager.treeAmbientColor`` Vec3 -> Vec3
-  ``lightManager.treeSkyColor`` Vec3 -> Vec3
-  ``lightManager.treeSunColor`` Vec3 -> Vec3

``localPlayer``
---------------

-  ``localPlayer.commanderSelectDelay`` float -> float
-  ``localPlayer.firstCommanderSelectDelay`` float -> float

``localProfile``
----------------

-  ``localProfile.addDemoBookmark`` std::string std::string std::string -> void

   Adds a bookmark to a battlerecorder demo

-  ``localProfile.save`` -> bool

-  ``localProfile.setEmail`` std::string -> std::string

   Sets or shows the email adress of the current profile

-  ``localProfile.setGamespyNick`` std::string -> std::string

   Sets or shows the gamespy login name of the current profile

-  ``localProfile.setName`` std::string -> std::string

   Sets or shows the name for the current profile

-  ``localProfile.setNick`` std::string -> std::string

   Sets or shows the nickname for the current profile

-  ``localProfile.setNumTimesLoggedIn`` int -> int

-  ``localProfile.setPassword`` std::string -> std::string

   Sets or shows the password for the current profile

-  ``localProfile.setTotalPlayedTime`` float -> void

``maplist``
-----------

-  ``maplist.append`` std::string std::string int -> bool
-  ``maplist.clear`` -> bool
-  ``maplist.configFile`` std::string -> std::string
-  ``maplist.currentMap`` -> int
-  ``maplist.insert`` int std::string std::string -> bool
-  ``maplist.list`` -> std::string
-  ``maplist.load`` -> bool
-  ``maplist.mapCount`` -> int
-  ``maplist.remove`` int -> int
-  ``maplist.save`` -> bool

``material``
------------

-  ``material.active`` unsigned int -> unsigned int
-  ``material.damageLoss`` float -> float
-  ``material.elasticity`` float -> float
-  ``material.friction`` float -> float
-  ``material.hasWaterPhysics`` bool -> bool
-  ``material.isBarbwire`` bool -> bool
-  ``material.isOneSided`` bool -> bool
-  ``material.isSeeThrough`` bool -> bool
-  ``materialManager.attMaterial`` unsigned int -> void
-  ``materialManager.createCell`` unsigned int unsigned int -> void
-  ``materialManager.damageMod`` float -> float
-  ``materialManager.defMaterial`` unsigned int -> void
-  ``materialManager.setDecalTemplate`` unsigned int IObjectTemplate_ptrproxy -> void
-  ``materialManager.setEffectTemplate`` unsigned int IObjectTemplate_ptrproxy -> void
-  ``materialManager.setSoundTemplate`` unsigned int IObjectTemplate_ptrproxy -> void
-  ``material.maxDamageLoss`` float -> float
-  ``material.minDamageLoss`` float -> float
-  ``material.name`` std::string -> std::string
-  ``material.overrideNeverPenetrate`` bool -> bool
-  ``material.penetrationDeviation`` float -> float
-  ``material.projectileCollisionHardness`` float -> float
-  ``material.resistance`` float -> float
-  ``material.type`` int -> int

``menuTeamManager``
-------------------

-  ``menuTeamManager.addKit`` std::string -> void
-  ``menuTeamManager.addTeam`` std::string std::string -> void
-  ``menuTeamManager.addWeapon`` std::string int int -> void
-  ``menuTeamManager.setTeamId`` int -> void

``minimap``
-----------

-  ``minimap.setCommanderOffset`` Vec2 -> void
-  ``minimap.setCurrOrderList`` int -> void
-  ``minimap.setDestinationBlend`` int -> void
-  ``minimap.setFilterColor`` float float float -> void
-  ``minimap.setFullScreenZoom`` int -> void
-  ``minimap.setPaintAllKits`` -> void
-  ``minimap.setPaintAllVehicles`` -> void
-  ``minimap.setPaintKit`` int -> void
-  ``minimap.setPaintVehicle`` int -> void
-  ``minimap.setSourceBlend`` int -> void
-  ``minimap.setZoom`` -> void
-  ``minimap.toggleShowKits`` -> void

``nametags``
------------

-  ``nametags.createBar`` NametagItemIDs int int -> void
-  ``nametags.createIcon`` NametagItemIDs -> void
-  ``nametags.deathFadeOutTime`` float -> float
-  ``nametags.deployableDistance`` double -> double
-  ``nametags.enemyDotLimit`` float -> float
-  ``nametags.enemyTagDelayTime`` double -> double
-  ``nametags.enemyTagFadeInTime`` double -> double
-  ``nametags.enemyTagFadeOutTime`` double -> double
-  ``nametags.getCullDistance`` TagType -> Vec2
-  ``nametags.manDownFadeOutTime`` float -> float
-  ``nametags.maxCallDistance`` float -> float
-  ``nametags.maxFriendlyDistance`` float -> float
-  ``nametags.setCullDistance`` TagType Vec2 -> void
-  ``nametags.setTexture`` int std::string int -> void
-  ``nametags.vehicleNametagOffset`` float -> float
-  ``nametags.vehicleNametagOffsetFactor`` float -> float

``networkableInfo``
-------------------

-  ``networkableInfo.createNewInfo`` std::string -> void

   -  Used in objects:raw-latex:`\common`:raw-latex:`\Networkables`.con
   -  Creates a custom ``NetworkableInfo``.
   -  Use with ``NetworkableInfo.setPredictionMode`` etc

-  ``networkableInfo.deleteInfo`` std::string -> void

-  ``networkableInfo.setBasePriority`` float -> void

-  ``networkableInfo.setForceNetworkableId`` bool -> void

-  ``networkableInfo.setIsUnique`` bool -> void

-  ``networkableInfo.setPredictionMode`` PredictionMode -> void

   NetworkableInfo.setPredictionMode

-  ``network.globalPredictionMode`` PredictionMode -> PredictionMode

``object``
----------

-  ``object.absolutePosition`` Vec3 -> Vec3
-  ``object.absolutePositionSecondary`` Vec3 -> Vec3
-  ``object.absoluteTransformation`` Mat4 -> Mat4
-  ``Object.active`` world::IObject_ptrproxy -> world::IObject_ptrproxy
-  ``object.addAbsolutePoint`` -> void
-  ``object.attenuationRange1`` float -> float
-  ``object.attenuationRange2`` float -> float
-  ``object.color`` Vec3 -> Vec3
-  ``object.coneAngle1`` float -> float
-  ``object.coneAngle2`` float -> float
-  ``Object.create`` world::IObjectTemplate_ptrproxy Vec3 Vec3 -> world::IObject_ptrproxy
-  ``Object.delete`` world::IObject_ptrproxy -> void
-  ``Object.deleteAll`` -> std::string
-  ``object.direction`` Vec3 -> Vec3
-  ``object.disableChildren`` bool -> bool
-  ``objectDrawer.collectPlanesDistance`` float -> float
-  ``objectDrawer.drawDebugPlanes`` bool -> bool
-  ``objectDrawer.faceForwardThreshold`` float -> float
-  ``objectDrawer.showCullStats`` bool -> bool
-  ``objectDrawer.useExactTest`` bool -> bool
-  ``objectDrawer.useOcclusion`` bool -> bool
-  ``Object.forceStart`` world::IObject_ptrproxy -> void
-  ``Object.forceStop`` world::IObject_ptrproxy -> void
-  ``object.fov`` float -> float
-  ``object.geometry.color`` Vec4 -> Vec4
-  ``object.geometry.GenerateLightmapForThisInstance`` bool -> bool
-  ``object.geometry.loadMesh`` std::string -> void
-  ``object.geometry.subGeometry`` int -> int
-  ``object.geometry.subGeometryCount`` -> int
-  ``object.geometry.technique`` std::string -> std::string
-  ``object.geometry.template`` -> IGeometryTemplate\*
-  ``object.getControlPointId`` -> int
-  ``Object.getGroundPos`` Vec3 -> Vec3
-  ``object.getLightSourceMask`` -> int
-  ``object.getVisibleTeam`` -> int
-  ``object.group`` int -> int
-  ``object.hasCollision`` bool -> bool
-  ``object.hasUpdate`` bool -> bool
-  ``object.HDRIntensity`` float -> float
-  ``Object.info`` world::IObject_ptrproxy -> std::string
-  ``object.initGrid`` Vec2 Vec2 int -> void
-  ``object.isInGrid`` bool -> bool
-  ``object.isOvergrowth`` bool -> bool
-  ``object.isSaveable`` bool -> bool
-  ``object.isVisible`` bool -> bool
-  ``object.layer`` int -> int
-  ``Object.list`` -> std::string
-  ``Object.listObjectsOfTemplate`` world::IObjectTemplate_ptrproxy -> std::string
-  ``Object.loadAll`` std::string -> bool
-  ``objectManager.drawStats`` int -> int
-  ``object.name`` std::string -> std::string
-  ``object.notInAI`` bool -> bool
-  ``Object.printScript`` world::IObject_ptrproxy -> std::string
-  ``object.rotation`` Vec3 -> Vec3
-  ``object.rotationSecondary`` Vec3 -> Vec3
-  ``Object.saveAll`` std::string -> bool
-  ``object.scale`` Vec3 -> Vec3
-  ``object.setActive`` bool -> void
-  ``object.setAsSkyLight`` -> void
-  ``object.setControlPointId`` int -> void
-  ``object.setIsDisabledRecursive`` bool -> void
-  ``object.setIsInTweakModeRecursive`` bool -> void
-  ``object.setIsSaveableRecursive`` bool -> void
-  ``object.setIsVisibleRecursive`` bool -> void
-  ``object.setLightSourceMask`` int -> void
-  ``Object.setObjectToGround`` world::IObject_ptrproxy -> Vec3
-  ``object.setTeam`` int -> void
-  ``object.setVisibleTeam`` int -> void
-  ``object.spawnOffset`` Vec3 -> Vec3
-  ``Object.start`` world::IObject_ptrproxy -> void
-  ``Object.stop`` world::IObject_ptrproxy -> void
-  ``object.team`` int -> int
-  ``object.template`` -> const IObjectTemplate\*

``objectTemplate``
------------------

-  ``objectTemplate.3dMapIcon`` int -> int

   -  Used in GenericFirearms (Mine etc) .tweak
   -  The image number sequence referenced in :raw-latex:`\menu`:raw-latex:`\nametag`:raw-latex:`\Objects`.dds.
   -  Use the vBF2 file and count the images. 9 is the mine icon.
   -  Using this system, you could have custom 3D Mine Icons, as long as they are the same size as the original.

-  ``objectTemplate.ability.hasAmmoAbility`` bool -> bool

-  ``objectTemplate.ability.hasHealingAbility`` bool -> bool

-  ``objectTemplate.ability.hasRepairingAbility`` bool -> bool

-  ``objectTemplate.ability.radarRadius`` int -> int

-  ``objectTemplate.abilityHud.ammoSound`` std::string -> std::string

-  ``objectTemplate.abilityHud.healingSound`` std::string -> std::string

-  ``objectTemplate.abilityHud.repairingSound`` std::string -> std::string

-  ``objectTemplate.abilityInVehicleMaterial`` int -> int

-  ``objectTemplate.abilityInVehicleRadius`` float -> float

-  ``objectTemplate.abilityInVehicleStrength`` float -> float

-  ``objectTemplate.abilityRestoreRate`` float -> float

-  ``objectTemplate.acceleration`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.acceleration`` float -> float

-  ``objectTemplate.accumulate`` bool -> bool

-  ``ObjectTemplate.active`` world::IObjectTemplate_ptrproxy -> world::IObjectTemplate_ptrproxy

-  ``ObjectTemplate.activeSafe`` std::string world::IObjectTemplate_ptrproxy -> void

-  ``objectTemplate.addAmmoType`` int int float -> void

-  ``objectTemplate.addChild`` bool -> bool

-  ``objectTemplate.addEmitterSpeed`` bool -> bool

-  ``objectTemplate.addKitVehicleMod`` std::string int -> void

-  ``objectTemplate.addLinePoint`` Vec2 -> void

-  ``objectTemplate.addPcoPosId`` int -> void

-  ``objectTemplate.addTargetObjectTypeToWatch`` int -> void

-  ``objectTemplate.addTemplate`` std::string -> void

-  ``objectTemplate.addToCollisionGroup`` U32 -> void

-  ``objectTemplate.addToProjectileList`` bool -> bool

-  ``objectTemplate.addTriggerableTarget`` std::string -> void

-  ``objectTemplate.addVehicleType`` std::string int float -> void

-  ``objectTemplate.addVehicleType`` VehicleCategory -> void

-  ``objectTemplate.addWorkOnMaterial`` int -> void

-  ``objectTemplate.affectingType`` int -> int

-  ``objectTemplate.affectLightmappedObjects`` bool -> bool

-  ``objectTemplate.AgeScaleFactorFromAcceleration`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorFromAltitude`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorFromEngine`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorFromRotationalSpeed`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorFromSpeed`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorFromSpeedInDof`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorRange`` Vec2 -> Vec2

-  ``objectTemplate.AgeScaleFactorUsed`` bool -> bool

-  ``objectTemplate.airFlowAffect`` float -> float

-  ``objectTemplate.airFriction`` float -> float

-  ``objectTemplate.airResistance`` float -> float

-  ``objectTemplate.airResistanceGraph`` Vec4 -> Vec4

-  ``objectTemplate.aiTemplate`` std::string -> std::string

-  ``objectTemplate.alignEffectTransformation`` bool -> bool

-  ``objectTemplate.alignRotationToSpeed`` bool -> bool

-  ``objectTemplate.allowDucking`` bool -> bool

-  ``objectTemplate.allowInsideDynamicLights`` bool -> bool

-  ``objectTemplate.allowInsideStaticSun`` bool -> bool

-  ``objectTemplate.alphaCull`` float -> float

-  ``objectTemplate.alphaIntensityFromAcceleration`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityFromAltitude`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityFromEngine`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityFromRotationalSpeed`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityFromSpeed`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityFromSpeedInDof`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityRange`` Vec2 -> Vec2

-  ``objectTemplate.alphaIntensityUsed`` bool -> bool

-  ``objectTemplate.alphaOverTime`` OverTimeDistribution -> OverTimeDistribution

-  ``objectTemplate.alternateTemplate0`` std::string -> std::string

-  ``objectTemplate.alternateTemplate1`` std::string -> std::string

-  ``objectTemplate.alternateTemplate2`` std::string -> std::string

-  ``objectTemplate.alternateTemplate3`` std::string -> std::string

-  ``objectTemplate.alternateTemplate4`` std::string -> std::string

-  ``objectTemplate.altSoldierExitPosition`` Vec3 -> Vec3

-  ``objectTemplate.ammo.abilityCost`` float -> float

-  ``objectTemplate.ammo.abilityDrain`` float -> float

-  ``objectTemplate.ammo.abilityMaterial`` int -> int

-  ``objectTemplate.ammo.abilityRadius`` float -> float

-  ``objectTemplate.ammo.abilityStrength`` float -> float

-  ``objectTemplate.ammo.ammoType`` int -> int

-  ``objectTemplate.ammo.autoReload`` bool -> bool

-  ``objectTemplate.ammo.changeMagAt`` float -> float

-  ``objectTemplate.ammo.firstShotExtraTime`` float -> float

-  ``objectTemplate.ammo.instantReloadOnEnable`` bool -> bool

-  ``objectTemplate.ammo.lastShotExtraTime`` float -> float

-  ``objectTemplate.ammo.magLinkWeapon`` std::string -> std::string

   -  Weapons, Vehicles ``.tweak``
   -  Allows two weapons to share the same amount of bullets and magazines.
   -  Enter the weapon name to maglink.
   -  The weapon that’s referenced must also have the same code.
   -  Weapons with fire selector code causes it to not work properly (citation needed)

-  ``objectTemplate.ammo.magSize`` int -> int

   -  Weapons ``.tweak``
   -  Number of bullets in a magazine.

      -  -1 for Infinity
      -  Maximum non-infinity allowed is 1023
      -  Any more will cause a crash

   -  Bug: In the Battlerecorder, it doesn’t pickup a gun that fires for 10 seconds on with 1000 bullets for some reason. Tested with the L4Bren on Auto.

-  ``objectTemplate.ammo.minimumTimeUntilReload`` float -> float

-  ``objectTemplate.ammo.nrOfMags`` int -> int

   Number of magazines allowed for a weapon.

-  ``objectTemplate.ammo.onlyActiveWhileFiring`` bool -> bool

   Prevents the Medibag and Ammo Bag from being thrown when firing. Used in PR’s Medikit and Repair Bag

-  ``objectTemplate.ammo.reloadAmount`` int -> int

-  ``objectTemplate.ammo.reloadTime`` float -> float

   -  Time in seconds of how long it takes to reload.
   -  Must be the same number as the reload animation time from AnimationSystem1p.inc to sync properly.

-  ``objectTemplate.ammo.reloadWithoutPlayer`` bool -> bool

   -  If enabled, weapon will autoreload regardless client settings for autoreload.
   -  1 - Enabled
   -  0 - Disabled

-  ``objectTemplate.ammo.replenishingType`` ReplenishingType -> ReplenishingType

-  ``objectTemplate.ammo.toggleWhenNoAmmo`` bool -> bool

   -  Weapons ``.tweak``
   -  When no ammo, switch to previous selected weapon.

-  ``objectTemplate.ammoStorageSize`` float -> float

-  ``objectTemplate.anchor`` Vec3 -> Vec3

-  ``objectTemplate.anchorOffset`` Vec3 -> Vec3

-  ``objectTemplate.animatedUVRotation`` int -> int

-  ``objectTemplate.animatedUVRotationIndex`` int -> int

-  ``objectTemplate.animatedUVRotationRadius`` float -> float

-  ``objectTemplate.animatedUVRotationReverse`` bool -> bool

-  ``objectTemplate.animatedUVRotationScale`` Vec2 -> Vec2

-  ``objectTemplate.animatedUVTranslation`` bool -> bool

-  ``objectTemplate.animatedUVTranslationIndex`` int -> int

-  ``objectTemplate.animatedUVTranslationMax`` Vec2 -> Vec2

-  ``objectTemplate.animatedUVTranslationReverse`` bool -> bool

-  ``objectTemplate.animatedUVTranslationSize`` Vec2 -> Vec2

-  ``objectTemplate.animatedUVTranslationSpeed`` Vec2 -> Vec2

-  ``objectTemplate.animation.animateOnZoom`` bool -> bool

-  ``objectTemplate.animation.loopingFire`` float -> float

-  ``objectTemplate.animation.shiftDelay`` float -> float

-  ``objectTemplate.animation.useShiftAnimation`` bool -> bool

-  ``objectTemplate.animationEnable`` bool -> bool

-  ``objectTemplate.animationFrameCount`` int -> int

-  ``objectTemplate.animationFrameCountX`` int -> int

-  ``objectTemplate.animationFrameHeight`` int -> int

-  ``objectTemplate.animationFrameWidth`` int -> int

-  ``objectTemplate.animationPlayOnce`` bool -> bool

-  ``objectTemplate.animationRandomizedStartFrame`` bool -> bool

-  ``objectTemplate.animationSpeed`` float -> float

-  ``objectTemplate.animationSystem1P`` std::string -> void

-  ``objectTemplate.animationSystem3P`` std::string -> void

-  ``objectTemplate.antenna.accelerationFactor`` float -> float

-  ``objectTemplate.antenna.damping`` float -> float

-  ``objectTemplate.antenna.maxSwayAngle`` Vec2 -> Vec2

-  ``objectTemplate.antenna.skeleton`` std::string -> std::string

-  ``objectTemplate.antenna.speedFactor`` float -> float

-  ``objectTemplate.antenna.stiffness`` float -> float

-  ``objectTemplate.areaValueTeam1`` U32 -> U32

-  ``objectTemplate.areaValueTeam2`` U32 -> U32

-  ``objectTemplate.armingDelay`` float -> float

   -  Weapons ``.tweak``
   -  Delay in seconds until the collision event is active.
   -  Used in the tripflares, which has a 15 second delay before passing through it will trigger the collision.

      -  Also could just be the seconds before the grenade explodes though not sure

-  ``objectTemplate.armor.addArmorEffect`` int std::string Vec3 -> void

-  ``objectTemplate.armor.addArmorEffectSpectacular`` int std::string Vec3 -> void

-  ``objectTemplate.armor.addWreckArmorEffect`` int std::string Vec3 -> void

-  ``objectTemplate.armor.alignLastEffectToHitDirection`` bool -> bool

-  ``objectTemplate.armor.angleMod`` float -> float

-  ``objectTemplate.armor.attackDamage`` float -> float

-  ``objectTemplate.armor.canBeDestroyed`` bool -> bool

-  ``objectTemplate.armor.canBeRepairedWhenWreck`` bool -> bool

   -  Vehicles .tweak, Weapons ``.tweak``
   -  Used in the AA Ship Boats.
   -  Basically, when it’s a wreck, it can be repaired back to life.

-  ``objectTemplate.armor.criticalDamage`` float -> float

-  ``objectTemplate.armor.deepWaterDamageDelay`` float -> float

-  ``objectTemplate.armor.deepWaterLevel`` float -> float

-  ``objectTemplate.armor.defaultMaterial`` int -> int

-  ``objectTemplate.armor.destroyOnSpectacularDeath`` bool -> bool

-  ``objectTemplate.armor.explosionDamage`` float -> float

-  ``objectTemplate.armor.explosionForce`` float -> float

-  ``objectTemplate.armor.explosionForceMax`` float -> float

-  ``objectTemplate.armor.explosionForceMod`` float -> float

-  ``objectTemplate.armor.explosionMaterial`` int -> int

-  ``objectTemplate.armor.explosionRadius`` float -> float

-  ``objectTemplate.armor.hideChildrenOnSpectacularDeath`` bool -> bool

-  ``objectTemplate.armor.hitPoints`` float -> float

   -  Vehicles ``.tweak``
   -  The health of the vehicle.
   -  0 - Dead.

-  ``objectTemplate.armor.hpLostWhileCriticalDamage`` float -> float

-  ``objectTemplate.armor.hpLostWhileInDeepWater`` float -> float

-  ``objectTemplate.armor.hpLostWhileInWater`` float -> float

-  ``objectTemplate.armor.hpLostWhileUpSideDown`` float -> float

-  ``objectTemplate.armor.maxHitPoints`` float -> float

-  ``objectTemplate.armor.showDamageAsDirt`` float -> float

-  ``objectTemplate.armor.speedMod`` float -> float

-  ``objectTemplate.armor.timeToStayAfterDestroyed`` float -> float

   -  Vehicles ``.tweak``
   -  Interesting code. If set to PR’s Jets and Helis, when they explode from wreck, the non-flaming wreck model stays though it shows in the minimap as an occupied vehicle.

-  ``objectTemplate.armor.timeToStayAsWreck`` float -> float

-  ``objectTemplate.armor.useMMOnDeath`` bool -> bool

   -  Use the Material Manager on Death. Not too sure about this one

-  ``objectTemplate.armor.waterDamageDelay`` float -> float

-  ``objectTemplate.armor.waterLevel`` float -> float

-  ``objectTemplate.armor.wreckDelay`` float -> float

-  ``objectTemplate.armor.wreckExplosionDamage`` float -> float

-  ``objectTemplate.armor.wreckExplosionForce`` float -> float

-  ``objectTemplate.armor.wreckExplosionForceMax`` float -> float

-  ``objectTemplate.armor.wreckExplosionForceMod`` float -> float

-  ``objectTemplate.armor.wreckExplosionMaterial`` int -> int

-  ``objectTemplate.armor.wreckExplosionRadius`` float -> float

-  ``objectTemplate.armor.wreckHitPoints`` float -> float

-  ``objectTemplate.artPos`` bool -> bool

-  ``objectTemplate.attachClimberRadius`` float -> float

-  ``objectTemplate.attachToEventObject`` bool -> bool

-  ``objectTemplate.attackSpeed`` float -> float

-  ``objectTemplate.attenuationRange1`` float -> float

   -  Used in ``.tweak`` Effect Files for Lightsource Templates
   -  How wide you want the lightsource effect to be, used with ``ObjectTemplate.isDynamic 1``.
   -  Range1 - X, which is the horizontal range.
   -  Max is 100, more than that will trigger an error message

-  ``objectTemplate.attenuationRange2`` float -> float

   -  Used in ``.tweak`` Effect Files for Lightsource Templates
   -  The height at which the lightsource will begin to drop.
   -  Range2 - Y, which is the vertical range.
   -  Max is 100, like above.

      -  To know the difference, set one to 50 and one to 100 and count the number of seconds the lightsource effect will last and compare.

-  ``objectTemplate.audio.newStyleAudio`` bool -> bool

-  ``objectTemplate.audio.transformationRelativeRoot`` bool -> bool

-  ``objectTemplate.audioReset`` -> void

-  ``objectTemplate.automaticPitchStabilization`` bool -> bool

-  ``objectTemplate.automaticReset`` bool -> bool

-  ``objectTemplate.automaticYawStabilization`` bool -> bool

-  ``objectTemplate.autoUseAbility`` int -> int

-  ``objectTemplate.averageTimeBetweenTests`` float -> float

-  ``objectTemplate.awakeTime`` float -> float

-  ``objectTemplate.blendMode`` std::string -> std::string

-  ``objectTemplate.blockInputOnRotBundle`` std::string -> std::string

-  ``objectTemplate.blurryVisionHoldTime`` float -> float

-  ``objectTemplate.blurryVisionTime`` float -> float

-  ``objectTemplate.boneName`` std::string -> std::string

-  ``objectTemplate.bounceDamping`` float -> float

-  ``objectTemplate.bounceLength`` float -> float

-  ``objectTemplate.bounceSensitivity`` float -> float

-  ``objectTemplate.bounceStrength`` float -> float

-  ``objectTemplate.boundingRadiusModifierWhenOccupied`` float -> float

-  ``objectTemplate.cameraId`` int -> int

-  ``objectTemplate.cameraShakeMaxSpeed`` float -> float

-  ``objectTemplate.cameraShakeSensitivity`` float -> float

-  ``objectTemplate.cameraShakeStartSpeed`` float -> float

-  ``objectTemplate.cameraSwayDofMax`` float -> float

-  ``objectTemplate.cameraSwayDofMin`` float -> float

-  ``objectTemplate.cameraSwayRightMax`` float -> float

-  ``objectTemplate.cameraSwayRightMin`` float -> float

-  ``objectTemplate.cameraSwayRodLength`` float -> float

-  ``objectTemplate.cameraSwaySensitivity`` float -> float

-  ``objectTemplate.cameraSwaySpringDamping`` float -> float

-  ``objectTemplate.cameraSwaySpringStrength`` float -> float

-  ``objectTemplate.canFireGuiIndex`` int -> int

-  ``objectTemplate.cannotFireGuiIndex`` int -> int

-  ``objectTemplate.cannotFireTimer`` float -> float

-  ``objectTemplate.canPickup`` bool -> bool

   -  Weapons
   -  Allows explosives to be picked up using the wrench/repair object
   -  Example: ``at_mine``

-  ``objectTemplate.canReverse`` bool -> bool

-  ``objectTemplate.capMaxSpeed`` bool -> bool

-  ``objectTemplate.castsDynamicShadow`` bool -> bool

   -  Vehicles, Weapons, and Soldiers
   -  Enables the rendering of shadows.

-  ``objectTemplate.castsStaticShadow`` bool -> bool

-  ``objectTemplate.centerOfCollisionOffset`` Vec3 -> Vec3

-  ``objectTemplate.centerOfMassOffset`` Vec3 -> Vec3

   To offset the center of mass using 0/0/0 - ``X/Y/Z.`` Setting it to X/0.5/Z will make a Logistics Truck survive a direct ram to a Van while setting to 0 makes the truck crash. Tested while holding shift.

-  ``objectTemplate.chance`` float -> float

   -  ``AmbientObjects.con``
   -  Chance that the triggerable effect may play when the player steps inside the radius.

      -  1 means it will always play
      -  0 means it will never play

-  ``objectTemplate.changeLodAt`` float -> float

-  ``objectTemplate.chaseAngle`` float -> float

-  ``objectTemplate.chaseDistance`` float -> float

-  ``objectTemplate.chaseOffset`` Vec3 -> Vec3

-  ``objectTemplate.clearTemplateList`` -> void

-  ``objectTemplate.clientHitDetection`` bool -> bool

-  ``objectTemplate.climbableAngle`` float -> float

-  ``objectTemplate.climbersAttachForce`` float -> float

-  ``objectTemplate.climbingSpeed`` float -> float

-  ``objectTemplate.clockwise`` bool -> bool

-  ``objectTemplate.cockpitLod`` int -> int

-  ``objectTemplate.cockpitLod`` U32 -> U32

-  ``objectTemplate.cockpitSubGeom`` int -> int

-  ``objectTemplate.cockpitSubGeom`` U32 -> U32

-  ``objectTemplate.collision.bouncing`` bool -> bool

-  ``objectTemplate.collision.hasCollisionEffect`` bool -> bool

-  ``objectTemplate.collision.maxStickAngle`` float -> float

-  ``objectTemplate.collision.replenishingStrength`` float -> float

-  ``objectTemplate.collision.replenishingType`` ReplenishingType -> ReplenishingType

-  ``objectTemplate.collision.restoreHP`` float -> float

-  ``objectTemplate.collision.resurrectDamage`` float -> float

-  ``objectTemplate.collision.stickToStaticObjects`` bool -> bool

-  ``objectTemplate.collision.stickToTerrain`` bool -> bool

-  ``objectTemplate.collision.stickToVehicles`` bool -> bool

-  ``objectTemplate.collisionEffectName`` std::string -> std::string

-  ``objectTemplate.collisionEnable`` bool -> bool

-  ``objectTemplate.collisionGroups`` U32 -> U32

-  ``objectTemplate.collisionMesh`` std::string -> void

-  ``objectTemplate.collisionMesh`` std::string -> std::string

-  ``objectTemplate.collisionPart`` int -> int

-  ``objectTemplate.collisionSpeedAlongNormal`` float -> float

-  ``objectTemplate.collisionSpeedAlongPlane`` float -> float

-  ``objectTemplate.collisionStartRadius`` float -> float

-  ``objectTemplate.color`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.color`` Vec3ColorFloat -> Vec3ColorFloat

-  ``objectTemplate.color1`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.color2`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.colorBlendGraph`` Vec4 -> Vec4

-  ``objectTemplate.coneAngle1`` float -> float

-  ``objectTemplate.coneAngle2`` float -> float

-  ``objectTemplate.coneDirection`` Vec3 -> Vec3

-  ``objectTemplate.coneInnerAngle`` float -> float

-  ``objectTemplate.coneOuterAngle`` float -> float

-  ``objectTemplate.coneOuterVolume`` float -> float

-  ``objectTemplate.constantForce`` float -> float

-  ``objectTemplate.constantRpm`` bool -> bool

-  ``objectTemplate.continousRotationSpeed`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.controlPointId`` int -> int

-  ``objectTemplate.ControlPointId`` U32 -> U32

-  ``objectTemplate.controlPointName`` std::string -> std::string

-  ``objectTemplate.controlsCategory`` dice::hfe::world::VehicleCategory -> dice::hfe::world::VehicleCategory

-  ``objectTemplate.coolDownPerSec`` float -> float

-  ``objectTemplate.coolingFactor`` float -> float

-  ``objectTemplate.copyLinksCount`` int -> int

-  ``ObjectTemplate.create`` std::string std::string -> IObjectTemplate\*

-  ``objectTemplate.createComponent`` std::string -> void

-  ``objectTemplate.createdInEditor`` bool -> bool

-  ``objectTemplate.createInvisible`` bool -> bool

   -  Creates the object as invisible.
   -  Collisions and Functions still work.
   -  Tested on the ``at_mine``

-  ``objectTemplate.createNotInGrid`` bool -> bool

-  ``objectTemplate.createVisibleInEditor`` bool -> bool

-  ``objectTemplate.crewKitIndex`` int -> int

   -  ``kits.con`` (example: ``gb82_pilot.con``)
   -  Defines what Geom to use for the kit.
   -  Looks up the Geom1 etc in the ``.skinnedmesh``, which is located in the Meshes folder. For example, arg82/Meshes/arg82_kits1.skinnedmeshes.
   -  Open with BfMeshViewer to know what each number looks like.

-  ``objectTemplate.crosshairFireTime`` float -> float

-  ``objectTemplate.cullRadiusScale`` float -> float

   Used in Weapons, Vehicle, Statics etc.

-  ``objectTemplate.CVMChase`` bool -> bool

   -  Vehicle ``.tweak`` files
   -  Used to set at what distance the object is culled from display.
   -  Each number represents a distance of 25m.
   -  For example: ``ObjectTemplate.cullRadiusScale 6`` - VD of 150m

-  ``objectTemplate.CVMExternTrace`` bool -> bool

   Vehicle ``.tweak`` files

-  ``objectTemplate.CVMFlyBy`` bool -> bool

   Vehicle ``.tweak`` files

-  ``objectTemplate.CVMFrontChase`` bool -> bool

   Vehicle ``.tweak`` files

-  ``objectTemplate.CVMInside`` bool -> bool

   Vehicle ``.tweak`` files

-  ``objectTemplate.CVMNose`` bool -> bool

   Vehicle ``.tweak`` files

-  ``objectTemplate.CVMTrace`` bool -> bool

   Vehicles ``.tweak`` files

-  ``objectTemplate.cycles`` int -> int

-  ``objectTemplate.damage`` float -> float

-  ``objectTemplate.damagedAmbientSoundLimit`` float -> float

-  ``objectTemplate.damageForBeingOutSideWorld`` float -> float

-  ``objectTemplate.damageMandownSoldiers`` bool -> bool

-  ``objectTemplate.damageOwner`` bool -> bool

-  ``objectTemplate.damageSpeed`` float -> float

-  ``objectTemplate.damageWhenLost`` float -> float

-  ``objectTemplate.dampenSprintRotationalForceInAirMod`` float -> float

-  ``objectTemplate.dampHorizontalVel`` float -> float

-  ``objectTemplate.dampHorizontalVelFactor`` float -> float

-  ``objectTemplate.damping`` float -> float

-  ``objectTemplate.deAcceleration`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.debugAutoRotate`` bool -> bool

-  ``objectTemplate.debugForceGearUp`` bool -> bool

-  ``objectTemplate.decalTextureName`` std::string -> std::string

-  ``objectTemplate.decreaseAngleToZero`` bool -> bool

-  ``objectTemplate.decreaseAngleToZeroSpeed`` float -> float

-  ``objectTemplate.decreaseAngleToZeroVerticalVel`` float -> float

-  ``objectTemplate.defaultAngleOfAttack`` float -> float

-  ``objectTemplate.defaultWeaponIndex`` int -> int

-  ``objectTemplate.degradeDropStrength`` float -> float

-  ``objectTemplate.degradeThrowStrength`` float -> float

-  ``objectTemplate.degradeThrowStrength2`` float -> float

-  ``objectTemplate.delay`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.delayBeforeCycle`` float -> float

-  ``objectTemplate.delayBeforeEnd`` float -> float

-  ``objectTemplate.delayBeforeStart`` float -> float

-  ``objectTemplate.delayToUse`` float -> float

-  ``ObjectTemplate.delete`` world::IObjectTemplate_ptrproxy -> void

-  ``objectTemplate.deleteComponent`` std::string -> void

-  ``objectTemplate.deployAnimationTime`` float -> float

-  ``objectTemplate.destroyableWindowsTemplate`` std::string -> std::string

-  ``objectTemplate.destroyOnExit`` bool -> bool

-  ``objectTemplate.destroyWhenEmptyStorage`` bool -> bool

-  ``objectTemplate.detonateAfterProjectileStopped`` bool -> bool

-  ``objectTemplate.detonateAfterProjectileStoppedMinSpeed`` float -> float

-  ``objectTemplate.detonation.allowFriendlyFireDetonation`` bool -> bool

-  ``objectTemplate.detonation.detectionRadius`` float -> float

-  ``objectTemplate.detonation.detonateDistanceToTarget`` float -> float

-  ``objectTemplate.detonation.detonateOnWaterCollision`` bool -> bool

-  ``objectTemplate.detonation.effectRotation`` Vec3 -> Vec3

-  ``objectTemplate.detonation.endEffectTemplate`` std::string -> std::string

-  ``objectTemplate.detonation.explosionConeAngle`` float -> float

-  ``objectTemplate.detonation.explosionDamage`` float -> float

-  ``objectTemplate.detonation.explosionForce`` float -> float

-  ``objectTemplate.detonation.explosionInnerConeRadius`` float -> float

-  ``objectTemplate.detonation.explosionLineOfSightMinimumDamage`` float -> float

-  ``objectTemplate.detonation.explosionMaterial`` int -> int

-  ``objectTemplate.detonation.explosionRadius`` float -> float

-  ``objectTemplate.detonation.explosionSoldierLineOfSight`` float -> float

-  ``objectTemplate.detonation.explosionSoldierLineOfSightHealRate`` float -> float

-  ``objectTemplate.detonation.explosionSoldierLineOfSightTimer`` float -> float

-  ``objectTemplate.detonation.explosionYMod`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMaxAlpha`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMaxHealTime`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMaxHoldTime`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMaxRampTime`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMinAlpha`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMinHealTime`` float -> float

-  ``objectTemplate.detonation.flashbangAdditiveGlowMinHoldTime`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMaxAlpha`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMaxHealTime`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMaxHoldTime`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMaxRampTime`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMinAlpha`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMinHealTime`` float -> float

-  ``objectTemplate.detonation.flashbangBillboardMinHoldTime`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMaxAlpha`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMaxHealTime`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMaxHoldTime`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMaxRampTime`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMinAlpha`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMinHealTime`` float -> float

-  ``objectTemplate.detonation.flashbangMotionBlurMinHoldTime`` float -> float

-  ``objectTemplate.detonation.flashbangRadiusWithNightVision`` float -> float

-  ``objectTemplate.detonation.invisibleAtEndEffect`` bool -> bool

-  ``objectTemplate.detonation.maxDepthForExplosion`` float -> float

-  ``objectTemplate.detonation.minDetonationSpeed`` float -> float

-  ``objectTemplate.detonation.playMaterialEffectAtSurface`` bool -> bool

-  ``objectTemplate.detonation.radiusDetonateWithAirVehicles`` bool -> bool

-  ``objectTemplate.detonation.replenishingStrength`` float -> float

-  ``objectTemplate.detonation.replenishingType`` ReplenishingType -> ReplenishingType

-  ``objectTemplate.detonation.showMineIndicationIcon`` bool -> bool

-  ``objectTemplate.detonation.stopAtEndEffect`` bool -> bool

-  ``objectTemplate.detonation.timeUntilCanDetonate`` float -> float

-  ``objectTemplate.detonation.triggerAngle`` float -> float

-  ``objectTemplate.detonation.triggerRadius`` float -> float

-  ``objectTemplate.detonation.triggerTime`` float -> float

-  ``objectTemplate.detonation.triggerType`` RadiusTriggerType -> RadiusTriggerType

-  ``objectTemplate.detonation.triggerVictimMinSpeed`` float -> float

-  ``objectTemplate.detonation.useCollisionNormal`` bool -> bool

-  ``objectTemplate.detonation.useMMOnEndEffect`` bool -> bool

-  ``objectTemplate.deviation.devModCrouch`` float -> float

-  ``objectTemplate.deviation.devModLie`` float -> float

-  ``objectTemplate.deviation.devModStand`` float -> float

-  ``objectTemplate.deviation.devModZoom`` float -> float

-  ``objectTemplate.deviation.fireDevAdd`` float -> float

-  ``objectTemplate.deviation.fireDevMax`` float -> float

-  ``objectTemplate.deviation.fireDevSub`` float -> float

-  ``objectTemplate.deviation.minDev`` float -> float

-  ``objectTemplate.deviation.miscDevAddJump`` float -> float

-  ``objectTemplate.deviation.miscDevMax`` float -> float

-  ``objectTemplate.deviation.miscDevSub`` float -> float

-  ``objectTemplate.deviation.radius`` float -> float

-  ``objectTemplate.deviation.setFireDev`` float float float -> void

-  ``objectTemplate.deviation.setMiscDev`` float float float -> void

-  ``objectTemplate.deviation.setSpeedDev`` float float float -> void

-  ``objectTemplate.deviation.setTurnDev`` float float float -> void

-  ``objectTemplate.deviation.speedDevAddForward`` float -> float

-  ``objectTemplate.deviation.speedDevAddStrafe`` float -> float

-  ``objectTemplate.deviation.speedDevMax`` float -> float

-  ``objectTemplate.deviation.speedDevSub`` float -> float

-  ``objectTemplate.deviation.subProjectileDev`` float -> float

-  ``objectTemplate.deviation.turnDevAddPitch`` float -> float

-  ``objectTemplate.deviation.turnDevAddYaw`` float -> float

-  ``objectTemplate.deviation.turnDevMax`` float -> float

-  ``objectTemplate.deviation.turnDevSub`` float -> float

-  ``objectTemplate.differential`` float -> float

-  ``objectTemplate.direction`` Vec3 -> Vec3

-  ``objectTemplate.directionalScale`` float -> float

-  ``objectTemplate.disableIfEnemyInsideRadius`` bool -> bool

-  ``objectTemplate.disableInputWhileDucking`` bool -> bool

-  ``objectTemplate.disableSpawnPointsOnEnter`` bool -> bool

-  ``objectTemplate.disableWhenEmptyVehicle`` bool -> bool

-  ``objectTemplate.disableWhenEmptyVehicleDelay`` float -> float

-  ``objectTemplate.disableWhenLosingControl`` bool -> bool

-  ``objectTemplate.disableWhenWreck`` bool -> bool

-  ``objectTemplate.dismountAngle`` float -> float

-  ``objectTemplate.dismountCheckOffset`` float -> float

-  ``objectTemplate.distance`` float -> float

-  ``objectTemplate.distanceCannotEnter`` float -> float

-  ``objectTemplate.distToMinDamage`` float -> float

-  ``objectTemplate.distToStartLoseDamage`` float -> float

-  ``objectTemplate.dontAllowExit`` bool -> bool

-  ``objectTemplate.dontClearTeamOnExit`` bool -> bool

-  ``objectTemplate.drag`` float -> float

   -  How much the drag from the body of a vehicle affects its speed.
   -  Without it, a vehicle will have an infinite top speed.

-  ``objectTemplate.drag`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.dragModifier`` Vec3 -> Vec3

-  ``objectTemplate.dragModifier`` float -> float

-  ``objectTemplate.dragOffset`` Vec3 -> Vec3

   To offset the drag using 0/0/0 - ``X/Y/Z``

-  ``objectTemplate.dragOverTime`` OverTimeDistribution -> OverTimeDistribution

-  ``objectTemplate.drawOrder`` std::string -> std::string

-  ``objectTemplate.dropHeadwear`` std::string -> std::string

-  ``objectTemplate.dropStrength`` float -> float

-  ``objectTemplate.effectChangeWaterHeight`` float -> float

-  ``objectTemplate.effectOnSpawn`` std::string -> std::string

-  ``objectTemplate.effectTemplateBaseName`` std::string -> std::string

-  ``objectTemplate.elasticity`` float -> float

-  ``objectTemplate.emitDelay`` float -> float

-  ``objectTemplate.emitDirection`` Vec3 -> Vec3

-  ``objectTemplate.emitDirectionZFromSpeedDof`` bool -> bool

-  ``objectTemplate.emitFrequency`` float -> float

-  ``objectTemplate.emitFrequencyScaleFactorLowerBound`` float -> float

-  ``objectTemplate.emitPrio`` std::string -> std::string

-  ``objectTemplate.emitRadius`` Vec3 -> Vec3

-  ``objectTemplate.emitRangeX`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.emitRangeY`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.emitRangeZ`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.emitScaleFactorFromAcceleration`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorFromAltitude`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorFromEngine`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorFromRotationalSpeed`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorFromSpeed`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorFromSpeedInDof`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorRange`` Vec2 -> Vec2

-  ``objectTemplate.emitScaleFactorUsed`` bool -> bool

-  ``objectTemplate.emitSpeed`` float -> float

-  ``objectTemplate.emitSpeedGraph`` Vec4 -> Vec4

-  ``objectTemplate.emitSpeedScaleFromAcceleration`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleFromAltitude`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleFromEngine`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleFromRotationalSpeed`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleFromSpeed`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleFromSpeedInDof`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleRange`` Vec2 -> Vec2

-  ``objectTemplate.emitSpeedScaleUsed`` bool -> bool

-  ``objectTemplate.emitterSpeedScale`` float -> float

-  ``objectTemplate.emitterType`` std::string -> std::string

-  ``objectTemplate.emitTime`` float -> float

-  ``objectTemplate.enabled`` bool -> bool

-  ``objectTemplate.enemyTicketLossWhenCaptured`` int -> int

-  ``objectTemplate.engineInfluence`` float -> float

-  ``objectTemplate.engineName`` std::string -> std::string

-  ``objectTemplate.engineType`` int -> int

   -  What kind of vehicle the engine is for.
   -  Car, tank, plane, ship, or helicopter.

-  ``objectTemplate.entryRadius`` float -> float

-  ``objectTemplate.events`` int -> int

-  ``objectTemplate.exitSpeedMod`` float -> float

-  ``objectTemplate.fadeInFactor`` float -> float

-  ``objectTemplate.fadeOutFactor`` float -> float

-  ``objectTemplate.fire.addBarrelName`` std::string -> void

-  ``objectTemplate.fire.addFireRate`` int -> void

   -  Used in Weapons and Vehicle ``.tweak``
   -  “Defines the fire mode selector. You can add three lines max of each one.

      -  0 - Single
      -  1 - Burst
      -  2 - Auto”

-  ``objectTemplate.fire.addTimeEvent`` WeaponTrigger WeaponAction float -> void

-  ``objectTemplate.fire.altFireInput`` io::PlayerInputMap -> io::PlayerInputMap

   Which PlayerInput map to use for the right-click function. Usually PIAlt

-  ``objectTemplate.fire.batchSize`` int -> int

-  ``objectTemplate.fire.burstSize`` int -> int

-  ``objectTemplate.fire.busyUntilButtonRelease`` bool -> bool

-  ``objectTemplate.fire.detonatorObject`` std::string -> std::string

-  ``objectTemplate.fire.dropLod`` int -> int

-  ``objectTemplate.fire.dropWeaponAfterFiringDelay`` float -> float

-  ``objectTemplate.fire.dropWeaponAfterReloadDelay`` float -> float

-  ``objectTemplate.fire.fireInCameraDof`` bool -> bool

-  ``objectTemplate.fire.fireInCameraDofLocked`` bool -> bool

-  ``objectTemplate.fire.fireInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.fire.fireLaunchDelay`` float -> float

-  ``objectTemplate.fire.fireLaunchDelaySoft`` float -> float

-  ``objectTemplate.fire.fireStartDelay`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.fire.hideLod`` int -> int

-  ``objectTemplate.fire.hideWeaponAfterFiringDelay`` float -> float

-  ``objectTemplate.fire.hideWeaponAfterReloadDelay`` float -> float

-  ``objectTemplate.fire.ignoreFireButton`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.fire.isBarrel`` std::string -> bool

-  ``objectTemplate.fire.maxProjectilesInWorld`` int -> int

   -  The max amount of projectiles in the weapon that can be set before the engine cleans up each one.
   -  If the limit is 10, deploying one any further will delete an existing projectile.
   -  Used for explosives, mines, and maybe bullets.

-  ``objectTemplate.fire.onlyFireWhenProne`` bool -> bool

   Restricts the weapon to fire only when prone. Though when firing during prone, a player can then stand and run to deploy an explosive for example. FH2 uses these for the machine gunner kits

-  ``objectTemplate.fire.projectileStartPosition`` Vec3 -> Vec3

   Position in X/Y/Z from the crosshair or PCO from where the projectile will launch.

-  ``objectTemplate.fire.projectileStartRotation`` Vec3 -> Vec3

-  ``objectTemplate.fire.pullbackTime`` float -> float

-  ``objectTemplate.fire.radioMessageDelay`` float -> float

-  ``objectTemplate.fire.randomRotationSpeed`` float -> float

-  ``objectTemplate.fire.removeBarrelName`` std::string -> void

-  ``objectTemplate.fire.roundsPerMinute`` int -> int

   -  Used in GenericFirearms (Weapons, Projectiles)
   -  The rate of fire, measured in Rounds Per Minute (RPM).
   -  Must be dividable by 1800.
   -  Check: http://researchmaniacs.com/Math/Divisible-By/What-is-1800-divisible-by.html

-  ``objectTemplate.fire.showWeaponAfterReloadDelay`` float -> float

-  ``objectTemplate.fire.timeToReachMaxStrengthSlow`` float -> float

-  ``objectTemplate.fire.toggleWeaponTime`` float -> float

-  ``objectTemplate.fire.triggerChargesTime`` float -> float

-  ``objectTemplate.fire.useDummyProjectiles`` bool -> bool

-  ``objectTemplate.fixAxisSpring`` bool -> bool

-  ``objectTemplate.flagTemplateTeam0`` std::string -> std::string

-  ``objectTemplate.flagTemplateTeam1`` std::string -> std::string

-  ``objectTemplate.flagTemplateTeam2`` std::string -> std::string

-  ``objectTemplate.flapLift`` float -> float

-  ``objectTemplate.flicker`` float -> float

-  ``objectTemplate.floaterMod`` float -> float

-  ``objectTemplate.floatMaxLift`` float -> float

-  ``objectTemplate.floatMinLift`` float -> float

-  ``objectTemplate.follow.changePitch`` float -> float

-  ``objectTemplate.follow.changeYaw`` float -> float

-  ``objectTemplate.follow.maxPitch`` float -> float

-  ``objectTemplate.follow.maxYaw`` float -> float

-  ``objectTemplate.follow.minDist`` float -> float

-  ``objectTemplate.followStiffness`` float -> float

-  ``objectTemplate.force`` float -> float

-  ``objectTemplate.forceSustainedFire`` bool -> bool

-  ``objectTemplate.forceToWaterSurface`` bool -> bool

-  ``objectTemplate.ForSoldierOnly`` bool -> bool

-  ``objectTemplate.fov`` float -> float

-  ``objectTemplate.gasCloudDamage`` float -> float

-  ``objectTemplate.gasCloudRadiusTime`` float -> float

-  ``objectTemplate.gasCloudType`` geom::GasCloudType -> geom::GasCloudType

-  ``objectTemplate.gasMaskSprintFactor`` float -> float

-  ``objectTemplate.gearChangeTime`` float -> float

-  ``objectTemplate.gearDown`` float -> float

-  ``objectTemplate.gearDownDelay`` float -> float

-  ``objectTemplate.gearDownHeight`` float -> float

-  ``objectTemplate.gearDownSpeed`` float -> float

-  ``objectTemplate.gearUp`` float -> float

-  ``objectTemplate.gearUpDelay`` float -> float

-  ``objectTemplate.gearUpHeight`` float -> float

-  ``objectTemplate.gearUpSpeed`` float -> float

-  ``objectTemplate.geometry`` std::string -> std::string

-  ``objectTemplate.geometry.dropGeom`` int -> int

-  ``objectTemplate.geometry.kit`` int -> int

-  ``objectTemplate.geometry1P`` std::string -> void

-  ``objectTemplate.geometry3P`` std::string -> void

-  ``objectTemplate.geometryPart`` int -> int

-  ``objectTemplate.getHeatBarType`` -> int

-  ``objectTemplate.getPosition`` int -> Math::Vec3

-  ``objectTemplate.getRotation`` int -> Math::Vec3

-  ``objectTemplate.getTemplate`` int -> std::string

-  ``objectTemplate.globalEffectLevel`` float -> float

-  ``objectTemplate.gravity`` float -> float

   Sets the gravity for the map. Can use minus values as well

-  ``objectTemplate.gravityGraph`` Vec4 -> Vec4

-  ``objectTemplate.gravityModifier`` float -> float

   -  Sets the gravity for the vehicle.
   -  Can use minus values as well which makes the projectile go upwards

-  ``objectTemplate.gravityModifier`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.gravityModifierOverTime`` OverTimeDistribution -> OverTimeDistribution

-  ``objectTemplate.grip`` PhysicsGripFlags -> PhysicsGripFlags

   -  “Set only for wheels.
   -  Roll grip for wheels that are not powered.
   -  Engine grip for wheels that are powered.
   -  Engine dummy grip for wheel you want to make looking like they are powered, but actually aren’t.

-  ``objectTemplate.groundContactVolume`` float -> float

-  ``objectTemplate.group`` U32 -> U32

-  ``objectTemplate.halfVolumeDistance`` float -> float

-  ``objectTemplate.handleCollisionSpeed`` float -> float

-  ``objectTemplate.hasAltEffect`` bool -> bool

-  ``objectTemplate.hasCollisionPhysics`` bool -> bool

   -  Check for all objects that has a collision mesh.
   -  Allows it to be hit by both bullets, players, and vehicles

-  ``objectTemplate.HasGreyCapturingState`` bool -> bool

-  ``objectTemplate.hasMobilePhysics`` bool -> bool

   Check for objects and parts that can move.

-  ``objectTemplate.hasOnTimeEffect`` bool -> bool

-  ``objectTemplate.hasOverDamage`` bool -> bool

-  ``objectTemplate.hasPartner`` bool -> bool

-  ``objectTemplate.hasPointPhysics`` bool -> void

-  ``objectTemplate.hasRelativeOffset`` bool -> bool

-  ``objectTemplate.hasResponsePhysics`` bool -> void

-  ``objectTemplate.hasRestrictedExit`` bool -> bool

-  ``objectTemplate.hasRotationalPointPhysics`` bool -> void

-  ``objectTemplate.HDRIntensity`` float -> float

-  ``objectTemplate.healSpeed`` float -> float

-  ``objectTemplate.healStorageSize`` float -> float

-  ``objectTemplate.heatAddWhenFire`` float -> float

-  ``objectTemplate.heatIncrement`` float -> float

-  ``objectTemplate.height`` float -> float

-  ``objectTemplate.heightOffset`` float -> float

-  ``objectTemplate.helpHud.altHelpSoundKey`` std::string -> std::string

-  ``objectTemplate.helpHud.altHelpstd::stringKey`` std::string -> std::string

-  ``objectTemplate.helpHud.closeToDistance`` int -> int

-  ``objectTemplate.helpHud.closeToHelpSoundKeyEnemy`` std::string -> std::string

-  ``objectTemplate.helpHud.closeToHelpSoundKeyFriendly`` std::string -> std::string

-  ``objectTemplate.helpHud.closeToHelpSoundKeyNeutral`` std::string -> std::string

-  ``objectTemplate.helpHud.closeToHelpstd::stringKeyEnemy`` std::string -> std::string

-  ``objectTemplate.helpHud.closeToHelpstd::stringKeyFriendly`` std::string -> std::string

-  ``objectTemplate.helpHud.closeToHelpstd::stringKeyNeutral`` std::string -> std::string

-  ``objectTemplate.helpHud.helpSoundKey`` std::string -> std::string

-  ``objectTemplate.helpHud.helpstd::stringKey`` std::string -> std::string

-  ``objectTemplate.helpHud.lowAmmoHelpSoundKey`` std::string -> std::string

-  ``objectTemplate.helpHud.lowAmmoHelpstd::stringKey`` std::string -> std::string

-  ``objectTemplate.helpHud.lowArmorHelpSoundKey`` std::string -> std::string

-  ``objectTemplate.helpHud.lowArmorHelpstd::stringKey`` std::string -> std::string

-  ``objectTemplate.hideFirstPerson`` bool -> bool

-  ``objectTemplate.hoistFlag`` bool -> bool

-  ``objectTemplate.hoistMinMax`` Vec2 -> Vec2

-  ``objectTemplate.holdObject`` bool -> bool

-  ``objectTemplate.horizontalDampAngle`` float -> float

-  ``objectTemplate.horizontalDampAngleFactor`` float -> float

-  ``objectTemplate.horizontalSpeedMagnifier`` float -> float

-  ``objectTemplate.hullHeight`` float -> float

-  ``objectTemplate.ik.poleVectorLeft`` Vec3 -> Vec3

-  ``objectTemplate.ik.poleVectorRight`` Vec3 -> Vec3

-  ``objectTemplate.ik.positionLeft`` Vec3 -> Vec3

-  ``objectTemplate.ik.positionRight`` Vec3 -> Vec3

-  ``objectTemplate.ik.rotationLeft`` Vec3 -> Vec3

-  ``objectTemplate.ik.rotationRight`` Vec3 -> Vec3

-  ``objectTemplate.inertiaModifier`` Vec3 -> Vec3

-  ``ObjectTemplate.info`` world::IObjectTemplate_ptrproxy -> std::string

-  ``objectTemplate.inheritHeatFromPrimary`` bool -> bool

-  ``objectTemplate.initiallyWalkable`` bool -> bool

-  ``objectTemplate.input`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.inputToPitch`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.inputToRoll`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.inputToYaw`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.insideDamageFrequency`` float -> float

-  ``objectTemplate.insideDamageThreshold`` float -> float

-  ``objectTemplate.insideFOV`` float -> float

-  ``objectTemplate.insideStaticSunAmbientColor`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.insideStaticSunColor`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.insideStaticSunDamageColor`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.insideStaticSunDirection`` Vec3 -> Vec3

-  ``objectTemplate.intensity`` float -> float

-  ``objectTemplate.intensity`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.intensityAtSpeed`` float -> float

-  ``objectTemplate.intensityOverTime`` OverTimeDistribution -> OverTimeDistribution

-  ``objectTemplate.inventorySize`` U32 -> U32

-  ``objectTemplate.inverseHeatBar`` bool -> bool

-  ``objectTemplate.invertGear`` bool -> bool

-  ``objectTemplate.invisible`` bool -> bool

-  ``objectTemplate.is3dSound`` bool -> bool

   If the .wav file is Mono, setting it to 1 will tell the engine to play it on both channels. If applied to a .wav that is Stereo, it will play on the entire map. Same with .ogg files though it’s usually experimentation.

-  ``objectTemplate.isCounterForce`` bool -> bool

-  ``objectTemplate.isDestructable`` bool -> bool

   Check only if object is a destroyable static object.

-  ``objectTemplate.isDynamic`` bool -> bool

-  ``objectTemplate.isGasMask`` bool -> bool

-  ``objectTemplate.isHemisphere`` bool -> bool

-  ``objectTemplate.isLocalSystem`` bool -> bool

   -  Makes the effect follow the projectile and allows it to arch.
   -  Used for the M67 *Zippo* Tank Flamethrower Effect.
   -  Without it, the flame effect just shoots straight but not following the projectile

-  ``objectTemplate.isLooping`` bool -> bool

-  ``objectTemplate.isNightVision`` bool -> bool

-  ``objectTemplate.isNotSaveable`` bool -> bool

-  ``objectTemplate.isOpenVehicle`` bool -> bool

   Allows the ragdoll to slide off when killed from a vehicle position. Used in Technicals. If this is option. the passenger animation must have a die animation specified otherwise the ragdolls will float in the air.

-  ``objectTemplate.isOvergrowth`` bool -> bool

-  ``objectTemplate.isPortalPassing`` bool -> bool

-  ``objectTemplate.isSelectable`` bool -> bool

-  ``objectTemplate.isSleeping`` bool -> bool

-  ``objectTemplate.isStatic`` bool -> bool

-  ``objectTemplate.isStaticSystem`` bool -> bool

-  ``objectTemplate.isUnderwaterEffect`` bool -> bool

-  ``objectTemplate.isUnstrategicControlPoint`` bool -> bool

-  ``objectTemplate.itemIndex`` int -> int

   -  What number in the keyboard is mapped to what weapon/tool.
   -  Max is 9, not sure about 0.
   -  Also positions the weapon icon square.

-  ``objectTemplate.itemType`` int -> int

-  ``objectTemplate.keepProjectiles`` float -> float Weapons

   -  Time to keep the projectile in the world in seconds after you or the weapon dies

-  ``objectTemplate.killHeatSeekingMissile`` bool -> bool

-  ``objectTemplate.kitTeam`` int -> int

-  ``objectTemplate.kitType`` hfe::KitType -> hfe::KitType

-  ``objectTemplate.lesserYawAtSpeed`` float -> float

-  ``objectTemplate.liftRegulated`` bool -> bool

-  ``objectTemplate.LightAffectionFactor`` float -> float

-  ``objectTemplate.lightMapIntensityOffset`` float -> float

-  ``objectTemplate.lightType`` std::string -> std::string

-  ``objectTemplate.linkAttachMovement`` float -> float

-  ``objectTemplate.linkAttachTime`` float -> float

-  ``objectTemplate.linkedEffectContainer`` std::string -> std::string

-  ``ObjectTemplate.list`` std::string -> std::string

-  ``objectTemplate.listenerObstruction`` float -> float

   -  Vehicles ``.tweak``
   -  How muffled is the sound.
   -  Lower value is least muffled.

-  ``ObjectTemplate.listTemplateClasses`` -> std::string

-  ``objectTemplate.listTemplates`` -> std::string

-  ``ObjectTemplate.loadAll`` -> bool

-  ``objectTemplate.localPredictOnClient`` bool -> bool

   -  Used with Grenades and if there’s any effect projectiles.
   -  Seems like it tells the server to predict what’s going to happen.

      -  Maybe used with the Networkable Setting

-  ``objectTemplate.lodDistance`` float -> float

-  ``objectTemplate.LodDistance`` std::string -> std::string

-  ``objectTemplate.loopCount`` int -> int

-  ``objectTemplate.looping`` bool -> bool

-  ``objectTemplate.loseControlWhenEnemyClose`` bool -> bool

-  ``objectTemplate.loseControlWhenNotClose`` bool -> bool

-  ``objectTemplate.lowSamples`` int -> int

-  ``objectTemplate.maintainCameraOnEnter`` bool -> bool

-  ``objectTemplate.maintainCameraOnExit`` bool -> bool

-  ``objectTemplate.manDownCameraOffsetInDof`` float -> float

-  ``objectTemplate.manDownCameraOffsetInUp`` float -> float

-  ``objectTemplate.mapMaterial`` uint std::string uint -> void

-  ``objectTemplate.maskOffset`` Vec3 -> Vec3

-  ``objectTemplate.maskType`` hfe::MaskObjectType -> hfe::MaskObjectType

-  ``objectTemplate.mass`` float -> float

   -  Used in Vehicles, Deployables, etc.
   -  Mass is the weight of the vehicle in KG and also taking into account the GravityModifier value

-  ``objectTemplate.material`` int -> int

-  ``objectTemplate.maxAngleOfAttack`` float -> float

-  ``objectTemplate.maxCorner`` Vec3 -> Vec3

-  ``objectTemplate.maxDistance`` float -> float

-  ``objectTemplate.maxDistanceUnderWaterSurface`` float -> float

-  ``objectTemplate.maxGasCloudRadius`` float -> float

-  ``objectTemplate.maxNrOfObjectSpawned`` U32 -> U32

-  ``objectTemplate.maxResetSpeed`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.MaxRopeLength`` float -> float

   Fastropes confirmed ?!?!?!?!

-  ``objectTemplate.maxRotation`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.maxSpawnDelay`` float -> float

-  ``objectTemplate.maxSpeed`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.maxSpeed`` float -> float

-  ``objectTemplate.maxTracerScaler`` float -> float

   -  Used in Projectiles (Weapons)
   -  How long the tracer effect can be depending on projectile speed.
   -  Reference: http://www.battlefieldsingleplayer.com/forum/index.php?showtopic-8592&mode-threaded&pid-84936

-  ``objectTemplate.maxTriggerDistance`` float -> float

-  ``objectTemplate.maxVertRegAngle`` float -> float

-  ``objectTemplate.MaxZiplineLength`` float -> float

-  ``objectTemplate.mediumSamples`` int -> int

-  ``objectTemplate.minCorner`` Vec3 -> Vec3

-  ``objectTemplate.minDamage`` float -> float

-  ``objectTemplate.minDistance`` float -> float

-  ``objectTemplate.minDistanceUnderWaterSurface`` float -> float

-  ``objectTemplate.minGasCloudRadius`` float -> float

-  ``objectTemplate.minimapNameOffset`` Vec2 -> Vec2

-  ``objectTemplate.minimumTimeBetweenTriggering`` float -> float

   -  ``AmbientObjects.con`` (Map)
   -  The time when the trigger will repeat again after entering the trigger radius.
   -  Happens after the effect plays. In seconds.
   -  Depends also on ``ObjectTemplate.chance``

-  ``objectTemplate.minNrToTakeControl`` U32 -> U32

-  ``objectTemplate.minRotation`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.minSpawnDelay`` float -> float

-  ``objectTemplate.minTimeBetweenActivation`` float -> float

-  ``objectTemplate.minTracerScaler`` float -> float

-  ``objectTemplate.minTrailVelocity`` float -> float

-  ``objectTemplate.minYNormal`` float -> float

-  ``objectTemplate.movementSpeed`` float -> float

-  ``objectTemplate.movementType`` int -> int

-  ``objectTemplate.moveToWaterSurface`` bool -> bool

-  ``objectTemplate.name`` -> std::string

-  ``objectTemplate.nameTagOffset`` Vec3 -> Vec3

-  ``objectTemplate.nearCullingEnable`` bool -> bool

-  ``objectTemplate.networkableInfo`` std::string -> std::string

   -  ``Networkables.con``
   -  Needs to be set for objects that won’t work online without them.
   -  Depends on the way it’s set and if it crashes immediately, is laggy, or crashes unexpectantly”

-  ``objectTemplate.neverDrawAs1p`` bool -> bool

   -  Vehicle, Weapons, Effects
   -  Makes the effect not draw in front of you when in 1p mode.
   -  Link: http://www.realitymod.com/forum/f388-pr-bf2-community-modding/113277-1p-animations-pcos-3.html

-  ``objectTemplate.newCar2.brakeTorque`` float -> float

-  ``objectTemplate.newCar2.engineBrakeTorque`` float -> float

-  ``objectTemplate.newCar2.engineFeedbackMod`` float -> float

-  ``objectTemplate.newCar2.frictionMod`` float -> float

-  ``objectTemplate.newCar2.frictionTorque`` float -> float

-  ``objectTemplate.newCar2.maxRpm`` float -> float

-  ``objectTemplate.newCar2.minRpm`` float -> float

-  ``objectTemplate.newCar2.slopeTorqueMod`` float -> float

-  ``objectTemplate.newCar2.useClutchedTorque`` bool -> bool

-  ``objectTemplate.newCar2.wheelInertia`` float -> float

-  ``objectTemplate.newCar2.wheelLatDriveFrictionMod`` float -> float

-  ``objectTemplate.newCar2.wheelLatFrictionMod`` float -> float

-  ``objectTemplate.newCar2.wheelLatMinDynamicFriction`` float -> float

-  ``objectTemplate.newCar2.wheelLatPeakAt`` float -> float

-  ``objectTemplate.newCar2.wheelLatScale`` float -> float

-  ``objectTemplate.newCar2.wheelLongDriveFrictionMod`` float -> float

-  ``objectTemplate.newCar2.wheelLongFrictionMod`` float -> float

-  ``objectTemplate.newCar2.wheelLongMinDynamicFriction`` float -> float

-  ``objectTemplate.newCar2.wheelLongPeakAt`` float -> float

-  ``objectTemplate.newCar2.wheelLongScale`` float -> float

-  ``objectTemplate.noEffectAtPerpSpeed`` float -> float

-  ``objectTemplate.noPassengerTimeToLive`` int -> int

-  ``objectTemplate.noPhysics`` bool -> bool

-  ``objectTemplate.noPropellerEffectAtSpeed`` float -> float

-  ``objectTemplate.nosePos`` Vec3 -> Vec3

-  ``objectTemplate.notCycledIfOccupied`` bool -> bool

-  ``objectTemplate.noVertRegAngle`` float -> float

-  ``objectTemplate.nrOfObjectToSpawn`` int -> int

-  ``objectTemplate.nrOfRespawns`` int -> int

-  ``objectTemplate.numberOfGears`` int -> int

-  ``objectTemplate.NumberOfLinks`` int -> int

-  ``objectTemplate.numNetworkedEffects`` int -> int

-  ``objectTemplate.numPlanes`` int -> int

-  ``objectTemplate.objectShadows`` bool -> bool

-  ``objectTemplate.objectTemplate`` std::string -> std::string

-  ``objectTemplate.onlyTakeableByTeam`` U32 -> U32

-  ``objectTemplate.onlyWhenOccupied`` bool -> bool

-  ``objectTemplate.otherCollisionLod`` int -> int

-  ``objectTemplate.overheatPenalty`` float -> float

-  ``objectTemplate.pan`` float -> float

-  ``objectTemplate.ParticleMaxSize`` float -> float

   -  Used in Vehicle ``.con`` and ``.tweak`` files
   -  Defines what materials the vehicle should use, which references the materialdefine file.
   -  Use BfMeshViewer to find out what numbers belong to what sides.

-  ``objectTemplate.particleSystemTemplate`` std::string -> std::string

   Same as above

-  ``objectTemplate.particleType`` std::string -> std::string

-  ``objectTemplate.pcoFlags`` int -> int

-  ``objectTemplate.pcoId`` int -> int

-  ``objectTemplate.penetrate.allowLiquidPenetration`` bool -> bool

-  ``objectTemplate.penetrate.allowSolidPenetration`` bool -> bool

-  ``objectTemplate.penetrate.neverPenetrate`` bool -> bool

-  ``objectTemplate.physicsFrequency`` int -> int

-  ``objectTemplate.physicsType`` PhysicsType -> PhysicsType

   -  Vehicles
   -  ``None`` for no collision
   -  ``Point`` for projectile (Ignores mesh)
   -  ``Mesh`` if object has collision mesh”

-  ``objectTemplate.pitch`` float -> float

-  ``objectTemplate.pitchEnvelope`` std::string -> std::string

-  ``objectTemplate.pitchOffset`` float -> float

-  ``objectTemplate.pivotOffset`` Vec2 -> Vec2

-  ``objectTemplate.PivotPosition`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.playAtEventPosition`` bool -> bool

-  ``objectTemplate.playAtPlayerPosition`` bool -> bool

-  ``objectTemplate.portalPassingPosition`` Vec3 -> Vec3

-  ``objectTemplate.poseCameraPosition`` int Vec3 -> void

-  ``objectTemplate.position`` Vec3 -> Vec3

-  ``objectTemplate.positionalSpeedInDof`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.positionalSpeedInRight`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.positionalSpeedInUp`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.positionOffset`` Math::Vec3 -> Math::Vec3

-  ``objectTemplate.postProcess.tvDistortionFreq`` float -> float

-  ``objectTemplate.postProcess.tvDistortionRoll`` float -> float

-  ``objectTemplate.postProcess.tvDistortionScale`` float -> float

-  ``objectTemplate.postProcess.tvInterference`` float -> float

-  ``objectTemplate.preCacheObject`` bool -> bool

-  ``objectTemplate.preWarmTime`` float -> float

-  ``ObjectTemplate.printScript`` world::IObjectTemplate_ptrproxy -> std::string

-  ``objectTemplate.projectileTemplate`` std::string -> std::string

   -  Used in Weapons and Vehicle ``.tweak``
   -  GenericFirearm
   -  Defines the projectile that the ``GenericFirearm`` should use.
   -  Looks for the ``GenericProjectile`` that is defined in all ``.tweak`` files.

-  ``objectTemplate.projectOnHeightmap`` bool -> bool

-  ``objectTemplate.projectorApplyMask`` bool -> bool

-  ``objectTemplate.projectorAspect`` float -> float

-  ``objectTemplate.projectorFar`` float -> float

-  ``objectTemplate.projectorFov`` float -> float

-  ``objectTemplate.projectorNear`` float -> float

-  ``objectTemplate.projectorTexture`` std::string -> std::string

-  ``objectTemplate.propRotAxis`` int -> int

-  ``objectTemplate.pureRotational`` bool -> bool

-  ``objectTemplate.QualityLevel`` std::string -> std::string

-  ``objectTemplate.radialDirection`` float -> float

-  ``objectTemplate.radio.destroyedMessage`` std::string -> std::string

-  ``objectTemplate.radio.failMessage`` std::string -> std::string

-  ``objectTemplate.radio.repairedMessage`` std::string -> std::string

-  ``objectTemplate.radio.spottedMessage`` std::string -> std::string

-  ``objectTemplate.radio.useMessage`` std::string -> std::string

-  ``objectTemplate.radius`` float -> float

-  ``objectTemplate.radiusOffset`` Vec3 -> Vec3

-  ``objectTemplate.ragdollLandedDelay`` float -> float

-  ``objectTemplate.randomAgeFactor`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.randomColorIntensity`` float -> float

-  ``objectTemplate.randomDirectionAngle`` Vec3 -> Vec3

-  ``objectTemplate.randomIntensity`` float -> float

-  ``objectTemplate.randomizeGeomPart`` bool -> bool

-  ``objectTemplate.randomRadialDirection`` float -> float

-  ``objectTemplate.randomRotation`` float -> float

-  ``objectTemplate.randomRotation`` Vec3 -> Vec3

-  ``objectTemplate.randomRotationSpeed`` Vec3 -> Vec3

-  ``objectTemplate.randomRotationSpeed`` float -> float

-  ``objectTemplate.randomSize`` float -> float

-  ``objectTemplate.randomSpeed`` float -> float

-  ``objectTemplate.randomTimeToLive`` float -> float

-  ``objectTemplate.rcType`` RemoteControlledObjectType -> RemoteControlledObjectType

-  ``objectTemplate.readBinary`` std::string -> void

-  ``objectTemplate.recoil.cameraRecoilSize`` float -> float

-  ``objectTemplate.recoil.cameraRecoilSpeed`` float -> float

-  ``objectTemplate.recoil.goBackOnRecoil`` bool -> bool

-  ``objectTemplate.recoil.hasRecoilForce`` bool -> bool

-  ``objectTemplate.recoil.recoilForce`` float -> float

-  ``objectTemplate.recoil.recoilForceLeftRight`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.recoil.recoilForceUp`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.recoil.recoilGraphExponent`` float -> float

-  ``objectTemplate.recoil.recoilGraphFrameCount`` int -> int

-  ``objectTemplate.recoil.recoilGraphTotalMovement`` float -> float

-  ``objectTemplate.recoil.recoilSize`` float -> float

-  ``objectTemplate.recoil.recoilSpeed`` float -> float

-  ``objectTemplate.recoil.recoilSpeedGB`` float -> float

-  ``objectTemplate.recoil.zoomModifier`` float -> float

-  ``objectTemplate.refillAmmoSpeed`` float -> float

-  ``objectTemplate.regulatePitch`` Vec2 -> Vec2

-  ``objectTemplate.regulatePitchInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.regulateRoll`` Vec2 -> Vec2

-  ``objectTemplate.regulateRollInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.regulateToLift`` float -> float

-  ``objectTemplate.regulateVerticalPos`` Vec2 -> Vec2

-  ``objectTemplate.regulateVerticalPosInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.regulateYaw`` Vec2 -> Vec2

-  ``objectTemplate.regulateYawInput`` io::PlayerInputMap -> io::PlayerInputMap

   -  In the effects .tweak when creating an effect
   -  Allows an effect template to be used with custom settings.

-  ``objectTemplate.regWhenMinInput`` float -> float

-  ``objectTemplate.relativePositionInDof`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.relativePositionInRight`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.relativePositionInUp`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.relativePositionOffset`` Vec3 -> Vec3

-  ``objectTemplate.rememberExcessInput`` bool -> bool

-  ``objectTemplate.remoteEngineInput`` int -> int

-  ``objectTemplate.removeTemplate`` int -> void

-  ``objectTemplate.replaceItem`` std::string -> void

   In the ``.con`` and ``.tweak``

-  ``objectTemplate.respawnDelay`` float -> float

   In the ``.con`` and ``.tweak``

-  ``objectTemplate.restoreRotationOnExit`` bool -> bool

-  ``objectTemplate.restoreSpeed`` float -> float

-  ``objectTemplate.reverbLevel`` float -> float

-  ``objectTemplate.ropeScaleFactor`` float -> float

-  ``objectTemplate.rotateAsAnimatedUV`` bool -> bool

-  ``objectTemplate.rotateAsAnimatedUVObject`` std::string -> std::string

-  ``objectTemplate.rotateAsAnimatedUVReverse`` bool -> bool

-  ``objectTemplate.rotateUV`` bool -> bool

-  ``objectTemplate.rotation`` float -> float

-  ``objectTemplate.rotationalForce`` Vec3 -> Vec3

-  ``objectTemplate.rotationalSpeedInDof`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.rotationalSpeedInRight`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.rotationalSpeedInUp`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.rotationAxle`` int -> int

-  ``objectTemplate.rotationGraph`` Vec4 -> Vec4

-  ``objectTemplate.rotationSpeed`` Vec3 -> Vec3

-  ``objectTemplate.rotationSpeed`` float -> float

-  ``objectTemplate.rotationSpeedMod`` float -> float

-  ``objectTemplate.rotationSpeedModBlur`` float -> float

-  ``ObjectTemplate.save`` world::IObjectTemplate_ptrproxy -> bool

-  ``ObjectTemplate.saveAll`` -> bool

-  ``objectTemplate.saveInSeparateFile`` bool -> bool

-  ``objectTemplate.scale`` Vec3 -> Vec3

-  ``objectTemplate.seatAnimationSystem`` std::string -> std::string

   -  In Vehicles ``.tweak``
   -  Defines the location of the ``.inc`` animation file for the seat.
   -  Example: ``Passenger.inc``

-  ``objectTemplate.seatInformation`` std::string Vec3 Vec3 -> void

-  ``objectTemplate.seatLeftRotationLimit`` float -> float

-  ``objectTemplate.seatParent`` std::string -> std::string

-  ``objectTemplate.seatPosition`` Vec3 -> Vec3

-  ``objectTemplate.seatRightRotationLimit`` float -> float

-  ``objectTemplate.seatRotation`` Vec3 -> Vec3

   -  In Vehicles ``.tweak``
   -  Allows the PCO to be rotated.
   -  Uses X/Y/Z.
   -  Relevant to Seat X Y Z Arrow.
   -  See BF2Editor Vehicle for more info.
   -  For example -10/0/0 wil rotate the player backwards.

-  ``objectTemplate.secondaryProjectileTemplate`` std::string -> std::string

-  ``objectTemplate.seek.directionBonus`` float -> float

-  ``objectTemplate.seek.maxAngleLock`` float -> float

-  ``objectTemplate.seek.maxDistLock`` float -> float

-  ``objectTemplate.seek.reLockTime`` float -> float

-  ``objectTemplate.seek.targetType`` TargetType -> TargetType

-  ``objectTemplate.seek.trackingDelay`` float -> float

-  ``objectTemplate.selfLights`` bool -> bool

-  ``objectTemplate.selfShadowIntensity`` float -> float

-  ``objectTemplate.selfShadows`` bool -> bool

-  ``objectTemplate.setActiveTemplate`` int -> void

-  ``objectTemplate.setAIEnterOnSpawn`` bool -> void

-  ``objectTemplate.setAllowSpawnCloseToVehicle`` bool -> void

-  ``objectTemplate.setAnimationFrameHeightRelative`` float -> void

-  ``objectTemplate.setAnimationFrameWidthRelative`` float -> void

-  ``objectTemplate.setAxisFixation`` Math::Vec3 -> void

-  ``objectTemplate.setCollisionMesh`` std::string -> void

-  ``objectTemplate.setEnterOnSpawn`` bool -> void

-  ``objectTemplate.setExplodePartAtDestroy`` bool -> void

-  ``objectTemplate.setGearRatios`` float float float -> void

-  ``objectTemplate.setHasTarget`` bool -> void

-  ``objectTemplate.setHealth`` int float float -> void

-  ``objectTemplate.setHeatBarType`` heatBarType -> void

-  ``objectTemplate.setMinSpawnHeight`` float -> void

-  ``objectTemplate.setNumWindows`` int -> void

-  ``objectTemplate.setObjectTemplate`` int std::string -> void

-  ``objectTemplate.setOnlyForAI`` bool -> void

-  ``objectTemplate.setOnlyForHuman`` bool -> void

-  ``objectTemplate.setPosition`` Math::Vec3 int -> void

-  ``objectTemplate.setPositionalFixation`` Math::Vec3 -> void

-  ``objectTemplate.setRotation`` Math::Vec3 int -> void

-  ``objectTemplate.setScatterSpawnPositions`` bool -> void

-  ``objectTemplate.setSkeletonCollisionBone`` std::string int Vec3 -> void

-  ``objectTemplate.setSoldierExitLocation`` Vec3 Vec3 -> void

-  ``objectTemplate.setSpawnAsParaTroper`` bool -> void

-  ``objectTemplate.setSpawnDelay`` float -> void

-  ``objectTemplate.setSpawnPositionOffset`` Math::Vec3 -> void

-  ``objectTemplate.setSpawnPreventionDelay`` float -> void

-  ``objectTemplate.setSpawnRotation`` Math::Vec3 -> void

-  ``objectTemplate.setTeamGeometry`` int std::string -> void

-  ``objectTemplate.setToolTipType`` dice::hfe::world::ToolTipType -> void

-  ``objectTemplate.setVehicleType`` dice::hfe::world::VehicleType -> void

-  ``objectTemplate.shadowIntensity`` float -> float

-  ``objectTemplate.shakeFactor`` float -> float

-  ``objectTemplate.sharedStorageSize`` float -> float

-  ``objectTemplate.showInFirstPerson`` bool -> bool

-  ``objectTemplate.showInThirdPerson`` bool -> bool

-  ``objectTemplate.showOnMinimap`` bool -> bool

-  ``objectTemplate.signalTriggerId`` int -> int

-  ``objectTemplate.sinkingSpeedMod`` float -> float

-  ``objectTemplate.size`` float -> float

-  ``objectTemplate.size`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.sizeGraph`` Vec4 -> Vec4

-  ``objectTemplate.sizeModifier`` Vec3 -> Vec3

-  ``objectTemplate.sizeModifierX`` float -> float

-  ``objectTemplate.sizeModifierY`` float -> float

-  ``objectTemplate.sizeModifierZ`` float -> float

-  ``objectTemplate.sizeOverTime`` OverTimeDistribution -> OverTimeDistribution

-  ``objectTemplate.skeleton`` std::string -> void

-  ``objectTemplate.skeleton1P`` std::string -> void

-  ``objectTemplate.skeleton3P`` std::string -> void

-  ``objectTemplate.snapToZeroOnNoInput`` bool -> bool

-  ``objectTemplate.softness`` float -> float

-  ``objectTemplate.soldierExitPosition`` Vec3 -> Vec3

-  ``objectTemplate.soldierExitRotation`` Vec3 -> Vec3

-  ``objectTemplate.sound.maxSoundsPerBurst`` int -> int

-  ``objectTemplate.sound.noisy`` bool -> bool

-  ``objectTemplate.soundFilename`` std::string -> std::string

-  ``objectTemplate.soundFilter`` std::string -> std::string

-  ``objectTemplate.soundIntensityFromAcceleration`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityFromAltitude`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityFromEngine`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityFromRotationalSpeed`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityFromSpeed`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityFromSpeedInDof`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityRange`` Vec2 -> Vec2

-  ``objectTemplate.soundIntensityUsed`` bool -> bool

-  ``objectTemplate.soundRadius`` float -> float

-  ``objectTemplate.spawnDelay`` float -> void

-  ``objectTemplate.spawnDelayAtStart`` bool -> bool

-  ``objectTemplate.spawnOffset`` Vec3 -> Vec3

-  ``objectTemplate.speccolor`` Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

-  ``objectTemplate.specialToggleWeaponInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.speed`` float -> float

-  ``objectTemplate.speedFromParticle`` float -> float

-  ``objectTemplate.speedFromPhysics`` bool -> bool

-  ``objectTemplate.spinWhenNoEngineInAir`` float -> float

-  ``objectTemplate.sprintDissipationTime`` float -> float

-  ``objectTemplate.sprintFactor`` float -> float

-  ``objectTemplate.sprintGear1Dampen`` float -> float

-  ``objectTemplate.sprintGear2Dampen`` float -> float

-  ``objectTemplate.sprintGear3Dampen`` float -> float

-  ``objectTemplate.sprintGear4Dampen`` float -> float

-  ``objectTemplate.sprintGear5Dampen`` float -> float

-  ``objectTemplate.sprintLimit`` float -> float

-  ``objectTemplate.sprintLossAtJump`` float -> float

-  ``objectTemplate.sprintRecoverTime`` float -> float

-  ``objectTemplate.sprintStaminaDissipationFactor`` float -> float

-  ``objectTemplate.startAgeFromAcceleration`` Vec2 -> Vec2

-  ``objectTemplate.startAgeFromAltitude`` Vec2 -> Vec2

-  ``objectTemplate.startAgeFromEngine`` Vec2 -> Vec2

-  ``objectTemplate.startAgeFromRotationalSpeed`` Vec2 -> Vec2

-  ``objectTemplate.startAgeFromSpeed`` Vec2 -> Vec2

-  ``objectTemplate.startAgeFromSpeedInDof`` Vec2 -> Vec2

-  ``objectTemplate.startAgeRange`` Vec2 -> Vec2

-  ``objectTemplate.startAgeUsed`` bool -> bool

-  ``objectTemplate.startAtCreation`` bool -> bool

-  ``objectTemplate.startAutoRotateOnEnter`` bool -> bool

-  ``objectTemplate.startDelay`` float -> float

-  ``objectTemplate.startDistance`` float -> float

-  ``objectTemplate.startLodPercentageOfLodDistance`` float -> float

-  ``objectTemplate.startOnEffects`` int -> int

-  ``objectTemplate.startProbability`` float -> float

-  ``objectTemplate.startRotation`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.startTeam`` int -> int

-  ``objectTemplate.stopOnEffects`` int -> int

-  ``objectTemplate.stopType`` int -> int

-  ``objectTemplate.strategicObject.3dMapIcon`` int -> int

-  ``objectTemplate.strategicObject.destroyedIcon`` std::string -> std::string

-  ``objectTemplate.strategicObject.intactIcon`` std::string -> std::string

-  ``objectTemplate.strategicObject.isOnePiece`` bool -> bool

-  ``objectTemplate.strategicObject.part`` int -> int

-  ``objectTemplate.strategicObject.strategicObjectName`` std::string -> std::string

-  ``objectTemplate.strength`` float -> float

-  ``objectTemplate.supplyGroupId`` int -> int

-  ``objectTemplate.supplyGroupNeeded`` int int bool -> void

-  ``objectTemplate.supplyValueNeededTeam1`` int -> int

-  ``objectTemplate.supplyValueNeededTeam2`` int -> int

-  ``objectTemplate.supplyValueTeam1`` int -> int

-  ``objectTemplate.supplyValueTeam2`` int -> int

-  ``objectTemplate.supportsEmitter`` bool -> bool

-  ``objectTemplate.supportsGlow`` bool -> bool

-  ``objectTemplate.supportsPerPixel`` bool -> bool

-  ``objectTemplate.supportsPerVertex`` bool -> bool

-  ``objectTemplate.target.connectionEffect`` std::string -> std::string

-  ``objectTemplate.target.connectionEffectOnlyWhenZoomed`` bool -> bool

-  ``objectTemplate.target.disableFireWhenActiveMissile`` bool -> bool

-  ``objectTemplate.target.disableGuidanceOnReload`` bool -> bool

-  ``objectTemplate.target.lockAngle`` float -> float

-  ``objectTemplate.target.lockDelay`` float -> float

-  ``objectTemplate.target.loseLockDelay`` float -> float

-  ``objectTemplate.target.maxDistance`` float -> float

-  ``objectTemplate.target.maxVelocity`` float -> float

-  ``objectTemplate.target.minVelocity`` float -> float

-  ``objectTemplate.target.onLockChangeToWeapon`` bool std::string -> void

-  ``objectTemplate.target.sendVehicleLockWarning`` bool -> bool

-  ``objectTemplate.target.setTargetAtMaxDistance`` bool -> bool

-  ``objectTemplate.target.targetInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.target.targetObjectTemplate`` std::string -> std::string

-  ``objectTemplate.target.targetSystem`` TargetSystem -> TargetSystem

-  ``objectTemplate.target.updateInterval`` float -> float

-  ``objectTemplate.target.useCameraDirectionToTarget`` bool -> bool

-  ``objectTemplate.target.useDynamicVelocity`` bool -> bool

-  ``objectTemplate.target.velocityModifier`` float -> float

-  ``objectTemplate.targetType`` TargetType -> TargetType

-  ``objectTemplate.team`` int -> int

-  ``objectTemplate.team`` U32 -> U32

-  ``objectTemplate.team`` int -> void

-  ``objectTemplate.teamChange`` bool -> bool

-  ``objectTemplate.teamFromClosestCP`` bool -> bool

-  ``objectTemplate.teamOnVehicle`` bool -> bool

-  ``objectTemplate.template`` std::string -> std::string

-  ``objectTemplate.templateHasBeenUsed`` bool -> bool

-  ``objectTemplate.textureName`` std::string -> std::string

-  ``objectTemplate.textureOffsetVelocity`` float -> float

-  ``objectTemplate.textureTileFactor`` float -> float

-  ``objectTemplate.throwStrength`` float -> float

-  ``objectTemplate.throwStrength2`` float -> float

-  ``objectTemplate.Timeout`` float -> float

-  ``objectTemplate.timeToGetControl`` float -> float

-  ``objectTemplate.timeToLive`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.timeToLive`` float -> float

-  ``objectTemplate.timeToLiveAfterDeath`` float -> float

-  ``objectTemplate.timeToLoseControl`` float -> float

-  ``objectTemplate.timeToRemoveTK`` float -> float

-  ``objectTemplate.toggleMouseLook`` bool -> bool

-  ``objectTemplate.toggleWeapon`` bool -> bool

-  ``objectTemplate.tolerance`` float -> float

-  ``objectTemplate.torque`` float -> float

-  ``objectTemplate.tracerConvergeDistance`` float -> float

   -  Used in Projectiles (Weapons)
   -  “At what distance the tracers (which start from the gunbarrel) and the projectile which start from the camera converges.
   -  Only relevant if ``FireInCameraDof`` is checked.

-  ``objectTemplate.tracerInterval`` int -> int

   -  Used in Projectiles (Weapons)
   -  Set one for tracer on every shot, 2 for every other, and so on.

-  ``objectTemplate.tracerScaler`` float -> float

   -  Used in Projectiles (Weapons)
   -  How long the tracer effect will be as default.

-  ``objectTemplate.tracerSizeModifier`` float -> float

   -  Used in Projectiles (Weapons)
   -  How fat the tracer will be.

-  ``objectTemplate.tracerTemplate`` std::string -> std::string

-  ``objectTemplate.trackTurnAcceleration`` float -> float

-  ``objectTemplate.trackTurnHighAmplitude`` float -> float

-  ``objectTemplate.trackTurnHighOffset`` float -> float

-  ``objectTemplate.trackTurnLowAmplitude`` float -> float

-  ``objectTemplate.trackTurnLowOffset`` float -> float

-  ``objectTemplate.trackTurnSpeed`` float -> float

-  ``objectTemplate.trailEffectTemplate`` std::string -> std::string

-  ``objectTemplate.Transparency`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.transparencyGraph`` Vec4 -> Vec4

-  ``objectTemplate.treeCollisionDiameter`` float -> float

-  ``objectTemplate.triggerForEachActivatingPlayer`` bool -> bool

-  ``objectTemplate.triggerId`` int -> int

-  ``objectTemplate.triggerRadius`` float -> float

-  ``objectTemplate.turnVelocity`` float -> float

-  ``ObjectTemplate.type`` world::IObjectTemplate_ptrproxy -> std::string

-  ``objectTemplate.type`` int -> int

-  ``objectTemplate.uavVehicleFlightHeight`` float -> float

-  ``objectTemplate.uavVehicleRadius`` float -> float

-  ``objectTemplate.uavVehicleSampleResolution`` float -> float

-  ``objectTemplate.uavVehicleSpeed`` float -> float

-  ``objectTemplate.uavVehicleTemplate`` std::string -> std::string

-  ``objectTemplate.unableToChangeTeam`` bool -> bool

-  ``objectTemplate.unlockIndex`` int -> int

-  ``objectTemplate.unlockLevel`` int -> int

-  ``ObjectTemplate.update`` world::IObjectTemplate_ptrproxy -> void

-  ``ObjectTemplate.updateAll`` -> void

-  ``objectTemplate.upDropBoost`` float -> float

-  ``objectTemplate.upThrowBoost`` float -> float

-  ``objectTemplate.upThrowBoost2`` float -> float

-  ``objectTemplate.useAbsoluteDirection`` bool -> bool

-  ``objectTemplate.useButtonRadius`` float -> float

-  ``objectTemplate.useCameraOrientation`` bool -> bool

-  ``objectTemplate.usedByAi`` bool -> bool

-  ``objectTemplate.useDeAcceleration`` bool -> bool

-  ``objectTemplate.usedOnTransparentMaterials`` bool -> bool

-  ``objectTemplate.usedOnTransparentSurface`` bool -> bool

-  ``objectTemplate.useGeomPart`` int -> int

-  ``objectTemplate.useProjectileCamera`` bool -> bool

-  ``objectTemplate.vehicleCameraShake`` CameraShakeTriggers -> CameraShakeTriggers

-  ``objectTemplate.vehicleCategory`` dice::hfe::world::VehicleCategory -> dice::hfe::world::VehicleCategory

-  ``objectTemplate.vehicleFov`` float -> float

-  ``objectTemplate.vehicleHud.AbilityIcon`` std::string -> std::string

-  ``objectTemplate.vehicleHud.addAbilityIcon`` std::string -> void

-  ``objectTemplate.vehicleHud.addShowOnCamMode`` int -> void

-  ``objectTemplate.vehicleHud.addVehicleIcon`` std::string -> void

-  ``objectTemplate.vehicleHud.disableOnSprint`` bool -> bool

-  ``objectTemplate.vehicleHud.displaySelectionOnEnter`` bool -> bool

-  ``objectTemplate.vehicleHud.enablePostProcessingOnGuiIndex`` bool -> bool

-  ``objectTemplate.vehicleHud.getShowOnCamMode`` int -> bool

-  ``objectTemplate.vehicleHud.guiIndex`` int -> int

   -  Vehicles and Weapons ``.tweak``
   -  Defines the Vehicle General User Inferface Index to use like the Blackhawk green HUD.
   -  Gui Index is located in the ``.con``\ s of ``menu\HUD\HudSetup\Vehicles``

-  ``objectTemplate.vehicleHud.hasTurretIcon`` bool -> bool

-  ``objectTemplate.vehicleHud.hudName`` std::string -> std::string

-  ``objectTemplate.vehicleHud.injurySound`` std::string -> std::string

-  ``objectTemplate.vehicleHud.isCoDriver`` bool -> bool

-  ``objectTemplate.vehicleHud.maxClimbSpeed`` int -> int

-  ``objectTemplate.vehicleHud.miniMapIcon`` std::string -> std::string

-  ``objectTemplate.vehicleHud.miniMapIconLeaderSize`` std::string -> std::string

-  ``objectTemplate.vehicleHud.miniMapIconSize`` int -> int

-  ``objectTemplate.vehicleHud.pantingSound`` std::string -> std::string

-  ``objectTemplate.vehicleHud.showCrossHair`` bool -> bool

-  ``objectTemplate.vehicleHud.showInfo`` bool -> bool

-  ``objectTemplate.vehicleHud.showOnCamMode`` int -> int

-  ``objectTemplate.vehicleHud.spottedIcon`` std::string -> std::string

-  ``objectTemplate.vehicleHud.spottedIconSize`` int -> int

-  ``objectTemplate.vehicleHud.standardHelpEnabled`` bool -> bool

-  ``objectTemplate.vehicleHud.typeIcon`` std::string -> std::string

-  ``objectTemplate.vehicleHud.useChildHud`` bool -> bool

-  ``objectTemplate.vehicleHud.usePlayerIcon`` bool -> bool

-  ``objectTemplate.vehicleHud.useSelectionIcons`` bool -> bool

-  ``objectTemplate.vehicleHud.useVehicleCommRose`` bool -> bool

-  ``objectTemplate.vehicleHud.vehicleIcon`` std::string -> std::string

-  ``objectTemplate.vehicleHud.vehicleIconPos`` Vec2 -> Vec2

-  ``objectTemplate.vehicleHud.vehicleType`` int -> int

-  ``objectTemplate.velocity`` float -> float

   -  Used in ``GenericFirearms`` (Weapons, Projectiles)
   -  The speed of the projectile measured in Rate of Fire (ROF)
   -  Lower ROF are affected by gravity/bullet drop while higher ones fire with lower bullet drop”

-  ``objectTemplate.visibleOn3dMap`` bool -> bool

-  ``objectTemplate.volume`` float -> float

   The loudness of the sound.

-  ``objectTemplate.volumeEnvelope`` std::string -> std::string

-  ``objectTemplate.volumeGroup`` int -> int

-  ``objectTemplate.warningHud.firstWarningSound`` std::string -> std::string

   -  Used in Vehicle ``.tweak``
   -  Defines the 1st warning sound when getting locked onto.
   -  Uses the file path pointing to a ``.wav`` or an ``.ogg`` file along with usual sound configuration code. *Beep Beep Beep*

-  ``objectTemplate.warningHud.secondWarningSound`` std::string -> std::string

   -  Used in Vehicle ``.tweak``
   -  Defines the 2nd warning sound when getting locked onto.
   -  Uses the file path pointing to a ``.wav`` or an ``.ogg`` file along with usual sound configuration code. *Beeeeeeeeeeep*

-  ``objectTemplate.warningHud.warningIcon`` std::string -> std::string

   -  Used in Vehicle ``.tweak``
   -  Defines the location of the warning icon.
   -  Example: ``ObjectTemplate.WarningHud.warningIcon Ingame\GeneralIcons\Action_Icons\mylaserlockicon.tga``

-  ``objectTemplate.warningHud.warningType`` int -> int

-  ``objectTemplate.waterHeight`` float -> float

-  ``objectTemplate.waterSurfaceOffset`` float -> float

-  ``objectTemplate.weaponHud.addShowOnCamMode`` int -> void

-  ``objectTemplate.weaponHud.altCrosshairIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.altGuiIndex`` int -> int

-  ``objectTemplate.weaponHud.altWeaponIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.ammoBarBackIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.ammoBarFrontIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.ammoIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.clipIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.crosshairIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.crosshairIconSize`` int -> int

-  ``objectTemplate.weaponHud.deviationFactor`` int -> int

-  ``objectTemplate.weaponHud.disableOnSprint`` bool -> bool

   -  Used in Weapons and Vehicle ``.tweak``

-  ``objectTemplate.weaponHud.displaySelectOnActivation`` bool -> bool

-  ``objectTemplate.weaponHud.enableMouse`` bool -> bool

-  ``objectTemplate.weaponHud.enablePostProcessingOnGuiIndex`` int -> int

   -  Used in Weapons and Vehicle ``.tweak``
   -  Makes the GuiIndex have a black and white effect
   -  Use with all ``objectTemplate.postProcess.tv`` code to adjust the TV effect

-  ``objectTemplate.weaponHud.firstLockSound`` std::string -> std::string

   The first lock sound that plays when there is a lock in progress on the jet

-  ``objectTemplate.weaponHud.getShowOnCamMode`` int -> bool

-  ``objectTemplate.weaponHud.guiIndex`` int -> int

   -  Used in Weapons and Vehicle ``.tweak``
   -  Defines the Weapon General User Inferface Index to use like the repair bar
   -  Gui Index is located in the ``.con``\ s of ``menu\HUD\HudSetup\Vehicles``

-  ``objectTemplate.weaponHud.hasFireRate`` bool -> bool

   Used in Weapons and Vehicle ``.tweak``

-  ``objectTemplate.weaponHud.hasMag`` bool -> bool

-  ``objectTemplate.weaponHud.hasRangeFinder`` bool -> bool

-  ``objectTemplate.weaponHud.hudName`` std::string -> std::string

-  ``objectTemplate.weaponHud.maxVisualDeviation`` int -> int

-  ``objectTemplate.weaponHud.minVisualDeviation`` int -> int

-  ``objectTemplate.weaponHud.overheatSound`` std::string -> std::string

   -  Used in Weapons and Vehicle ``.tweak``
   -  For the overheat sound. Adding it makes the engine reference the std::string defined with MenuSound.con.

      -  Usually it’s ``S_Weapon_Handheld_Overheat``
      -  ``S_Vehicle_Handheld_Overheat`` but can be anything and custom ones can be used if needed

-  ``objectTemplate.weaponHud.secondLockSound`` std::string -> std::string

   -  Used in Weapons and Vehicle ``.tweak``
   -  The second lock sound that plays when the lock has been set

-  ``objectTemplate.weaponHud.selectIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.showAmmo`` bool -> bool

-  ``objectTemplate.weaponHud.ShowClips`` bool -> bool

-  ``objectTemplate.weaponHud.showInfo`` bool -> bool

-  ``objectTemplate.weaponHud.showOnCamMode`` int -> int

-  ``objectTemplate.weaponHud.specialAbilityIcon`` std::string -> std::string

-  ``objectTemplate.weaponHud.switchGuiOnCamera`` bool -> bool

-  ``objectTemplate.weaponHud.weaponIcon`` std::string -> std::string

-  ``objectTemplate.weaponType`` int -> int

-  ``objectTemplate.widnBlowTime`` float -> float

-  ``objectTemplate.windAffectionFactor`` float -> float

-  ``objectTemplate.windAgingFactor`` float -> float

-  ``objectTemplate.windBlowTime`` float -> float

-  ``objectTemplate.windDirection`` Vec3 -> Vec3

-  ``objectTemplate.windFalloff`` float -> float

-  ``objectTemplate.windIsDynamic`` bool -> bool

-  ``objectTemplate.windowSizeVector`` Vec3 -> Vec3

   “Used in Projectiles, Vehicles, Effect

-  ``objectTemplate.windRadialFalloff`` float -> float

-  ``objectTemplate.windSpeed`` float -> float

-  ``objectTemplate.windSpeedAgeDistance`` float -> float

-  ``objectTemplate.windType`` std::string -> std::string

-  ``objectTemplate.wingLift`` float -> float

   -  Planes and Helis
   -  How much speed will affect object lifting on control surface.

-  ``objectTemplate.wingToRegulatorRatio`` float -> float

-  ``objectTemplate.workOnSoldiers`` bool -> bool

   -  Supply Objects
   -  Allows the soldier to receive HP/Ammo depending on the type of supply set

-  ``objectTemplate.workOnVehicles`` bool -> bool

   -  Supply Objects
   -  Allows the vehicle to receive HP/Ammo depending on the type of supply set

-  ``objectTemplate.worldFOV`` float -> float

-  ``objectTemplate.writeBinary`` std::string -> void

-  ``objectTemplate.writeZ`` bool -> bool

-  ``objectTemplate.yawSpeed`` float -> float

-  ``objectTemplate.ziplineSoldierHeight`` float -> float

-  ``objectTemplate.zoom.addZoomFactor`` float -> void

-  ``objectTemplate.zoom.allowUntoggledFire`` bool -> bool

-  ``objectTemplate.zoom.changeCameraId`` int -> int

-  ``objectTemplate.zoom.changeCameraViewMode`` CameraViewMode -> CameraViewMode

-  ``objectTemplate.zoom.changeFovDelay`` float -> float

-  ``objectTemplate.zoom.disableMuzzleWhenZoomed`` bool -> bool

-  ``objectTemplate.zoom.mouseSpeedMod`` float -> float

-  ``objectTemplate.zoom.onlyZoomWhenProne`` bool -> bool

-  ``objectTemplate.zoom.startCameraId`` int -> int

-  ``objectTemplate.zoom.startCameraViewMode`` CameraViewMode -> CameraViewMode

-  ``objectTemplate.zoom.useProjectileCamera`` bool -> bool

-  ``objectTemplate.zoom.zoomDelay`` float -> float

-  ``objectTemplate.zoom.zoomInput`` io::PlayerInputMap -> io::PlayerInputMap

-  ``objectTemplate.zoom.zoomLod`` int -> int

-  ``objectTemplate.zoom.zoomOutAfterFire`` bool -> bool

-  ``objectTemplate.zRotation`` RandomDistribution -> RandomDistribution

-  ``objectTemplate.zRotationSnap`` float -> float

-  ``object.togglePause`` -> void

``overgrowth``
--------------

-  ``overgrowth.addMaterial`` std::string uint -> bool
-  ``overgrowth.addType`` std::string -> bool
-  ``overgrowth.closeDistFade`` float -> float
-  ``overgrowth.closeDistPercentage`` float -> float
-  ``overgrowth.editorEnable`` float -> float
-  ``overgrowth.exportToTerrainTexture`` -> void
-  ``overgrowth.generateAll`` -> void
-  ``overgrowth.generateAtlas`` -> void
-  ``overgrowth.getActiveMaterialName`` -> std::string
-  ``overgrowth.getGeometryList`` -> std::string
-  ``overgrowth.getLodDistance`` -> float
-  ``overgrowth.getMaterialList`` -> std::string
-  ``overgrowth.getTypeList`` -> std::string
-  ``overgrowth.lodTimer`` float -> float
-  ``overgrowth.paintMaterial`` float float float -> void
-  ``overgrowth.paintShadowmap`` float float float -> void
-  ``overgrowth.path`` std::string -> std::string
-  ``overgrowth.postLoad`` -> void
-  ``overgrowth.preLoad`` -> void
-  ``overgrowth.removeActiveMaterial`` -> bool
-  ``overgrowth.removeActiveType`` -> bool
-  ``overgrowth.save`` -> void
-  ``overgrowth.setActiveMaterial`` std::string -> void
-  ``overgrowth.setActiveType`` std::string -> void
-  ``overgrowthType.density`` float -> float
-  ``overgrowthType.geometry`` std::string -> std::string
-  ``overgrowthType.minRadiusToOthers`` float -> float
-  ``overgrowthType.minRadiusToSame`` float -> float
-  ``overgrowthType.normalScale`` float -> float
-  ``overgrowthType.randomScale`` Vec2 -> Vec2
-  ``overgrowthType.rotationScale`` float -> float
-  ``overgrowth.viewDistance`` float -> float
-  ``overgrowth.viewDistanceScale`` float -> float
-  ``Particles.enableOldParticles`` bool -> bool
-  ``Particles.enableParticles`` bool -> bool

``particleSystemManager``
-------------------------

-  ``particleSystemManager.affectedByWind`` bool -> bool
-  ``particleSystemManager.drawBoundingBoxEnable`` bool -> bool
-  ``particleSystemManager.drawStats`` bool -> bool
-  ``particleSystemManager.generateTexture`` -> bool
-  ``particleSystemManager.overdrawScale`` float -> float
-  ``particleSystemManager.particleSystemShaderQuality`` uint -> uint
-  ``particleSystemManager.qualityLevel`` int -> int
-  ``particleSystemManager.resetStats`` -> void
-  ``particleSystemManager.startFadePercentageOfViewDistance`` float -> float
-  ``particleSystemManager.startLodPercentageOfLodDistance`` float -> float
-  ``particleSystemManager.viewDistance`` float -> float
-  ``physics.airDensityZeroAtHeight`` float -> float
-  ``physics.gravity`` float -> float
-  ``physics.listProperties`` -> std::string
-  ``physics.wind`` Vec3 -> Vec3

``Player``
----------

-  ``Player.active`` IPlayer\* -> IPlayer\*
-  ``Player.create`` std::string std::string -> IPlayer\*
-  ``player.isAi`` bool -> bool
-  ``player.isAlive`` bool -> bool
-  ``player.isNetwork`` bool -> bool
-  ``player.kit`` int -> int
-  ``Player.list`` -> std::string
-  ``Player.listPlayerClasses`` -> std::string
-  ``player.moveTo`` Vec3 -> std::string
-  ``player.name`` -> std::string
-  ``player.pickup`` std::string -> void
-  ``Player.saveAll`` std::string -> bool
-  ``player.setFov`` float float -> void
-  ``player.setVehicleWithInputId`` IObject_ptrproxy int -> bool
-  ``player.spawnGroup`` int -> int
-  ``player.team`` int -> int
-  ``player.vehicle`` IObject_ptrproxy -> IObject_ptrproxy
-  ``portal.debugLevel`` int -> int
-  ``portal.showStats`` bool -> bool

``profile``
-----------

-  ``profile.activateCharacterProfile`` std::string -> bool
-  ``profile.activatePlayerProfile`` std::string -> bool
-  ``profile.activeCharacterProfile`` std::string -> std::string
-  ``profile.activeMod`` std::string -> std::string
-  ``profile.activePlayerProfile`` std::string -> std::string
-  ``profile.addCharacterProfile`` std::string -> bool
-  ``profile.addModSetting`` std::string -> bool
-  ``profile.applySettings`` -> void
-  ``profile.createPlayerProfile`` std::string -> bool
-  ``profile.defaultKit`` int -> int
-  ``profile.getIndexForKit`` std::string int -> void
-  ``profile.playerName`` std::string -> std::string
-  ``profile.rank`` int -> int
-  ``profile.setIndexForKit`` std::string int int -> void
-  ``profile.tagIcon`` std::string -> std::string
-  ``profile.tagText`` std::string -> std::string
-  ``profile.visualUnlockLevel`` int -> int

``pythonHost``
--------------

-  ``pythonHost.reinitialize`` -> bool
-  ``pythonHost.sendCommand`` std::string std::string std::string -> bool

``radio``
---------

-  ``radio.answer`` bool -> void
-  ``radio.callForAmmo`` -> void
-  ``radio.callForMedic`` -> void
-  ``radio.callForRepair`` -> void
-  ``radioInterface.selectOrder`` std::string -> bool
-  ``radioInterface.setstd::stringMap`` std::string std::string std::string -> void
-  ``radio.sendKitMessage`` -> void
-  ``radio.sendSpottedMessage`` bool world::VehicleType -> void
-  ``radio.setSpottedMenuActive`` -> void
-  ``radioVehicleInterface.selectOrder`` std::string -> bool
-  ``radioVehicleInterface.setstd::stringMap`` std::string std::string std::string -> void
-  ``ragDoll.active`` bool -> void
-  ``ragDoll.addAngularConstraint`` int int int -> void
-  ``ragDoll.addBone`` int int -> void
-  ``ragDoll.addCapsuleCollision`` int int -> void
-  ``ragDoll.addConstraint`` int int -> void
-  ``ragDoll.addDihedralAngleConstraint`` int int int -> void
-  ``ragDoll.addDistanceLessThanConstraint`` int int float -> void
-  ``ragDoll.addForce`` int Vec3 -> void
-  ``ragDoll.addJointConstraint`` int int -> void
-  ``ragDoll.addParticle`` int float -> void
-  ``ragDoll.drawConstraints`` bool -> void
-  ``ragDoll.gravity`` float -> void
-  ``ragDoll.linkMode`` int int -> void
-  ``ragDoll.lockBone`` int int -> void
-  ``ragDoll.removeConstraint`` int int -> void
-  ``ragDoll.reset`` -> void
-  ``ragDoll.save`` -> void
-  ``ragDoll.setParticleCollisionCriteria`` float float -> void
-  ``ragDoll.skeleton`` std::string -> void
-  ``ragDoll.toSkeleton`` int int int -> void

``renderer``
------------

-  ``renderer.allowA2M`` bool -> bool

-  ``renderer.allowOnDemandPostProcessing`` bool -> bool

-  ``renderer.ambientIlluminationRange`` Vec4 -> Vec4

-  ``renderer.ambientSun`` bool -> bool

-  ``renderer.clearColor`` BaseVector3 -> BaseVector3

-  ``renderer.coronaFadeSpeed`` float -> float

-  ``renderer.disableFadeOnRoads`` bool -> bool

-  ``renderer.distanceCullConst`` float -> float

-  ``renderer.distanceCullConstPCO`` float -> float

-  ``renderer.divAccum`` float -> float

-  ``renderer.draw1pMeshes`` bool -> bool

-  ``renderer.draw1pZOnly`` bool -> bool

-  ``renderer.drawBundledMeshes`` bool -> bool

-  ``renderer.drawConsole`` bool -> bool

   Turns off access to the in-game console if set to 0

-  ``renderer.drawDeferred`` bool -> bool

-  ``renderer.drawFps`` int -> int

   Displays the current frames per seconds and the time in milliseconds between frames

-  ``renderer.drawGraphs`` bool -> bool

-  ``renderer.drawHud`` bool -> bool

   Turns the heads up display (HUD) on or off

-  ``renderer.drawNametags`` bool -> bool

-  ``renderer.drawObjects`` bool -> bool

-  ``renderer.drawOvergrowth`` bool -> bool

-  ``renderer.drawParticles`` bool -> bool

-  ``renderer.drawPostProduction`` bool -> bool

-  ``renderer.drawRoads`` bool -> bool

-  ``renderer.drawSkinnedMeshes`` bool -> bool

-  ``renderer.drawSkyDome`` bool -> bool

-  ``renderer.drawStaticMeshes`` bool -> bool

-  ``renderer.drawSunFlare`` bool -> bool

-  ``renderer.drawTerrain`` bool -> bool

-  ``renderer.drawTrees`` bool -> bool

-  ``renderer.drawUndergrowth`` bool -> bool

-  ``renderer.drawWatermark`` bool -> bool

-  ``renderer.dumpScreen`` std::string -> void

-  ``renderer.enableHWOcclusion`` bool -> bool

-  ``renderer.fakeHDRBlendingFactor`` float -> float

-  ``renderer.fakeHDRBlendingTimeDark`` double -> double

-  ``renderer.fakeHDRBlendingTimeLight`` double -> double

-  ``renderer.fakeHDREnabled`` bool -> bool

-  ``renderer.fakeHDRHorizWeights`` std::string -> std::string

-  ``renderer.fakeHDRPassGate`` float -> float

-  ``renderer.fakeHDRVertWeights`` std::string -> std::string

-  ``renderer.fakeHDRWeights`` std::string -> std::string

-  ``Renderer.fieldOfView1p`` float -> float

-  ``renderer.fogColor`` Vec3 -> Vec3

-  ``renderer.fogStartEndAndBase`` Vec4 -> Vec4

-  ``renderer.forceBundledMeshLod`` int -> int

-  ``renderer.forceSkinnedMeshLod`` int -> int

-  ``renderer.forceStaticMeshMaxPolyPercentage`` int -> int

-  ``renderer.forceStaticMeshSkipLod`` int -> int

-  ``renderer.getQualityLodDistanceBM`` int -> float

-  ``renderer.getQualityLodDistanceSKM`` int -> float

-  ``renderer.getQualityLodDistanceSTM`` int -> float

-  ``renderer.globalBundleMeshLodDistanceScale`` float -> float

-  ``renderer.globalSkinnedMeshLodDistanceScale`` float -> float

-  ``renderer.globalStaticMeshLodDistanceScale`` float -> float

-  ``renderer.glowEnabled`` bool -> bool

-  ``renderer.glowStrength`` float -> float

-  ``renderer.isNightMap`` bool -> bool

-  ``renderer.lightBlurStrength`` float -> float

-  ``renderer.listScreenModes`` -> void

-  ``renderer.makeTopWorldScreen`` U32 std::string Vec3 -> void

-  ``renderer.minCullDistance`` float -> float

-  ``renderer.nightMode`` uint -> uint

-  ``renderer.nightVisionEnabled`` bool -> bool

-  ``renderer.nightVisionGradient`` std::string -> std::string

-  ``renderer.nightVisionMaxPower`` float -> float

-  ``renderer.nightVisionRegenRPS`` float -> float

-  ``renderer.occlusionObjectsMaxFrames`` int -> int

-  ``renderer.occlusionTerrainMaxFrames`` int -> int

-  ``renderer.presentAsync`` bool -> bool

-  ``renderer.presentSpinIfBusy`` bool -> bool

-  ``renderer.qualityLodEnabled`` bool -> bool

-  ``renderer.renderAheadLimit`` uint -> uint

-  ``renderer.roadDepthBias`` float -> float

-  ``renderer.roadLodDistMod`` float -> float

-  ``renderer.roadSlopeScaleDepthBias`` float -> float

-  ``renderer.screenDumpPath`` std::string -> std::string

-  ``renderer.screenMode`` int -> int

-  ``renderer.setQualityLodDistanceALL`` int float -> void

-  ``renderer.setQualityLodDistanceBM`` int float -> void

-  ``renderer.setQualityLodDistanceSKM`` int float -> void

-  ``renderer.setQualityLodDistanceSTM`` int float -> void

-  ``Renderer.soldier.debugCharacterMode`` int -> int

-  ``Renderer.soldier.debugDrawCollision`` bool -> bool

-  ``Renderer.soldier.debugDrawSkeletons`` bool -> bool

-  ``renderer.stopRenderMovie`` -> void

-  ``renderer.tearGasStrength`` float -> float

-  ``renderer.tvAmbient`` float -> float

-  ``renderer.tvColor`` Vec3 -> Vec3

-  ``renderer.tvEnabled`` bool -> bool

-  ``renderer.tvGranularity`` float -> float

-  ``renderer.tvInterference`` float -> float

-  ``renderer.tweakFarPlane1p`` float -> float

-  ``renderer.tweakNearPlane`` float -> float

-  ``renderer.tweakNearPlane1p`` float -> float

-  ``renderer.vsync`` bool -> bool

-  ``renderer.waterAnimSpeed`` float -> float

   Sets the water speed.

-  ``renderer.waterColor`` Vec3 -> Vec3

-  ``renderer.waterFogColor`` Vec3 -> Vec3

-  ``renderer.waterFogStartEndAndBase`` Vec4 -> Vec4

-  ``renderer.watermarkFilename`` std::string -> std::string

-  ``renderer.watermarkPos`` Vec2 -> Vec2

-  ``renderer.watermarkScale`` float -> float

-  ``renderer.waterNormalMap`` std::string -> std::string

-  ``renderer.waterScroll`` Vec2 -> Vec2

-  ``renderer.waterSpecularColor`` Vec4 -> Vec4

-  ``renderer.waterSpecularPower`` float -> float

-  ``renderer.xpPerfFlags`` int -> int

-  ``renderer.xpPerfFlags2`` int -> int

-  ``reservedSlots.addNick`` std::string -> void

-  ``reservedSlots.clear`` -> void

-  ``reservedSlots.configFile`` std::string -> std::string

-  ``reservedSlots.list`` -> std::string

-  ``reservedSlots.load`` -> bool

-  ``reservedSlots.removeNick`` std::string -> void

-  ``reservedSlots.save`` -> bool

``scoreboard``
--------------

-  ``scoreboard.setToggleShow`` int -> void
-  ``scoreboard.singleClick`` int -> void

``scoreManager``
----------------

-  ``scoreManager.ammo`` int -> int
-  ``scoreManager.ammoScoreLimit`` float -> float
-  ``scoreManager.assistKill`` int -> int
-  ``scoreManager.controlPointCapture`` int -> int
-  ``scoreManager.death`` int -> int
-  ``scoreManager.driverPassenger`` int -> int
-  ``scoreManager.flagCapture`` int -> int
-  ``scoreManager.flagReturn`` int -> int
-  ``scoreManager.heal`` int -> int
-  ``scoreManager.healScoreLimit`` float -> float
-  ``scoreManager.inDirectKill`` int -> int
-  ``scoreManager.kill`` int -> int
-  ``scoreManager.objective`` int -> int
-  ``scoreManager.repair`` int -> int
-  ``scoreManager.repairScoreLimit`` float -> float
-  ``scoreManager.soldierRevive`` int -> int
-  ``scoreManager.teamDamage`` int -> int
-  ``scoreManager.teamDamageLimit`` float -> float
-  ``scoreManager.teamVehicleDamage`` int -> int
-  ``scoreManager.teamVehicleDamageLimit`` float -> float
-  ``scoreManager.TK`` int -> int
-  ``scoreManager.vehicleRevive`` int -> int
-  ``SettingsManager.boolGet`` std::string -> bool
-  ``SettingsManager.boolSet`` std::string bool -> bool
-  ``SettingsManager.floatGet`` std::string -> float
-  ``SettingsManager.floatSet`` std::string float -> bool
-  ``SettingsManager.intGet`` std::string -> int
-  ``SettingsManager.intSet`` std::string int -> bool
-  ``SettingsManager.std::stringGet`` std::string -> std::string
-  ``SettingsManager.std::stringSet`` std::string std::string -> bool
-  ``SettingsManager.U32Get`` std::string -> U32
-  ``SettingsManager.U32Set`` std::string U32 -> bool

``shadermanager``
-----------------

-  ``shadermanager.byPassDiceStates`` bool -> bool
-  ``shadermanager.compileDebugTerrain`` bool -> bool
-  ``shadermanager.compilePartialPrecisionTypes`` bool -> bool
-  ``shadermanager.compileSkipOptimizations`` bool -> bool
-  ``shadermanager.compileUsePartialPrecision`` bool -> bool
-  ``shadermanager.compileUsePreShaders`` bool -> bool
-  ``shadermanager.compileUsePS2A`` bool -> bool
-  ``shadermanager.compileWithDebug`` bool -> bool
-  ``shadermanager.listEffects`` -> void
-  ``shadermanager.reloadAllEffects`` -> void
-  ``shadermanager.reloadEffect`` std::string -> void
-  ``shadowManager.allowAlphaShadows`` bool -> bool
-  ``shadowManager.alphaShadowThreshold`` float -> float
-  ``shadowManager.dropShadowClipHeightOffset`` float -> float
-  ``shadowManager.dynamic1pShadowsEnabled`` bool -> bool
-  ``shadowManager.dynamicShadowsEnabled`` bool -> bool
-  ``shadowManager.dynamicStaticMeshShadowsEnabled`` bool -> bool
-  ``shadowManager.lightmapIntensityBias`` float -> float
-  ``shadowManager.occludedSkyNightIntensity`` float -> float
-  ``shadowManager.shadow80Line`` float -> float
-  ``shadowManager.shadowFromBundledMeshLod`` int -> int
-  ``shadowManager.shadowFromSkinnedMeshLod`` int -> int
-  ``shadowManager.shadowFromStaticMeshLod`` int -> int
-  ``shadowManager.shadowFromTerrainLod`` int -> int
-  ``shadowManager.shadowIntensityBias`` float -> float
-  ``shadowManager.shadowMapBitDepth`` int -> int
-  ``shadowManager.shadowMapDepthBias`` float -> float
-  ``shadowManager.shadowMapDepthDistance`` float -> float
-  ``shadowManager.shadowMapIncludeStaticMeshes`` bool -> bool
-  ``shadowManager.shadowMapObjectSize`` int -> int
-  ``shadowManager.shadowMapSize`` int -> int
-  ``shadowManager.shadowMapSlopeBias`` float -> float
-  ``shadowManager.shadowMergeDynamicShadowFrustums`` bool -> bool
-  ``shadowManager.shadowOccluderOversizeFactor`` float -> float
-  ``shadowManager.shadowOverrideQuality`` int -> int
-  ``shadowManager.shadowPSMFovY`` float -> float
-  ``shadowManager.shadowPSMUseSlideback`` bool -> bool
-  ``shadowManager.shadowPSMUseUnitCubeClipping`` bool -> bool
-  ``shadowManager.shadowPSMZFarOffset`` float -> float
-  ``shadowManager.shadowPSMZMinInfinityZ`` float -> float
-  ``shadowManager.shadowPSMZNearOffset`` float -> float
-  ``shadowManager.shadowShowFrustums`` bool -> bool
-  ``shadowManager.shadowSunExtrusionLength`` float -> float
-  ``shadowManager.shadowSunHeightOverFade`` Vec2 -> Vec2
-  ``shadowManager.shadowSunScalePower`` float -> float
-  ``shadowManager.shadowTestBelowRayLenght`` float -> float
-  ``shadowManager.shadowTSMFocus`` float -> float
-  ``shadowManager.shadowUpdateFactor`` float -> float
-  ``shadowManager.shadowUpdatesEnabled`` bool -> bool
-  ``shadowManager.shadowUseSweepTest`` bool -> bool
-  ``shadowManager.useLSSMOptimizations`` bool -> bool
-  ``shadowManager.usePSMOptimizations`` bool -> bool
-  ``skinnedMeshRenderer.shaderQuality`` ShaderQuality -> ShaderQuality
-  ``skyDome.cloudLerpFactors`` Vec2 -> Vec2
-  ``skyDome.cloudTemplate`` std::string -> std::string
-  ``skyDome.cloudTexture`` std::string -> std::string
-  ``skyDome.cloudTexture2`` std::string -> std::string
-  ``skyDome.domePosition`` Vec3 -> Vec3
-  ``skyDome.domeRotation`` float -> float
-  ``skyDome.domeSize`` float -> float
-  ``skyDome.fadeCloudsDistances`` Vec2 -> Vec2
-  ``skyDome.flareDirection`` Vec3 -> Vec3
-  ``skyDome.flareFadeAdd`` float -> float
-  ``skyDome.flareFadeMul`` float -> float
-  ``skyDome.flareTemplate`` std::string -> std::string
-  ``skyDome.flareTexture`` std::string -> std::string

   -  Map: ``Sky.con``
   -  The texture of the sunflare/actual sunflare.
   -  When switching to a map with no sunflare, it will still use the previous maps one.

      -  So for maps like Fallujah West/Saaremaa, an invisible texture needs to be defined instead to prevent the sunflare bug.

   -  Usage: ``Skydome.flareTexture common\textures\sunflare\Sunglow_no``

-  ``skyDome.hasCloudLayer`` bool -> bool
-  ``skyDome.hasCloudLayer2`` bool -> bool
-  ``skyDome.lightingBlend`` float -> float
-  ``skyDome.lightingColor`` Vec3 -> Vec3
-  ``skyDome.scrollDirection`` Vec2 -> Vec2
-  ``skyDome.scrollDirection2`` Vec2 -> Vec2
-  ``skyDome.skyTemplate`` std::string -> std::string
-  ``skyDome.skyTexture`` std::string -> std::string
-  ``sound.addMenuSound`` std::string std::string float -> void
-  ``sound.addSound`` std::string -> void
-  ``sound.addTrigger`` std::string -> void
-  ``sound.dopplerEffect`` float -> float
-  ``sound.getAllSoundTemplates`` -> std::string
-  ``sound.getProperty`` std::string -> std::string
-  ``sound.getVolumeForGroup`` int -> float
-  ``sound.initialize`` int std::string int -> SoundInitResult
-  ``sound.interactiveMode`` bool -> bool
-  ``sound.listenerReverb`` float -> float
-  ``sound.loadMusic`` std::string -> bool
-  ``sound.masterVolume`` float -> float
-  ``sound.playMusic`` -> bool
-  ``sound.playSound`` std::string -> void
-  ``sound.removeAllTriggers`` -> void
-  ``sound.setProperty`` std::string float -> void
-  ``sound.setReverb`` std::string -> void
-  ``sound.setVolumeForGroup`` int float -> void
-  ``sound.showSoundSources`` bool -> bool
-  ``sound.showStats`` bool -> bool
-  ``Sound.startEngines`` bool -> bool
-  ``sound.stopMusic`` float -> bool
-  ``sound.stopSound`` std::string -> void
-  ``sound.tinnitusSetup`` std::string float float -> void
-  ``sound.tweakTemplate`` std::string float float -> void
-  ``sound.windSetup`` std::string float -> void
-  ``spawnManager.commitSuicide`` -> void
-  ``spawnManager.listSpawnGroups`` -> void
-  ``spawnManager.selectNextUnlock`` int -> void
-  ``spawnManager.setPlayerKit`` int -> void
-  ``spawnManager.setPlayerTeam`` int -> void
-  ``spawnManager.toggleMembers`` bool -> void
-  ``squadInterface.selectOrder`` std::string -> bool
-  ``squadInterface.setstd::stringMap`` std::string std::string std::string -> void
-  ``squadLeaderInterface.selectOrder`` std::string -> bool
-  ``squadLeaderInterface.setstd::stringMap`` std::string std::string std::string -> void
-  ``squadLeader.sendOrder`` int bool -> void
-  ``squadLeader.sendRequest`` int bool -> void
-  ``squadLeader.sendRequestForOrder`` -> void
-  ``squad.leaveSquad`` -> void
-  ``squadManager.changeSquadName`` std::string bool -> void
-  ``squadManager.joinSquad`` int -> void
-  ``squadManager.leaveSquad`` int -> void
-  ``squadManager.listSquadMembers`` int int -> std::string
-  ``squadManager.listSquads`` int -> std::string
-  ``squadManager.makeMeCommander`` -> void
-  ``squadManager.popNextCommanderApplicant`` int -> void
-  ``squadMenu.applyInviteList`` -> void
-  ``squadMenu.createSquad`` -> void
-  ``squadMenu.doubleClickInvite`` -> void
-  ``squadMenu.doubleClickNew`` -> void
-  ``squadMenu.setShowInviteList`` bool -> void
-  ``squadMenu.setSquadCreateSelect`` bool -> void
-  ``squadMenu.setSquadNameSelect`` -> void
-  ``squadMenu.singleClickInvite`` -> void
-  ``squadMenu.singleClickNew`` -> void
-  ``squadMenu.squadCreateLockToggle`` -> void
-  ``staticMeshRenderer.allowAnisoFiltering`` bool -> bool
-  ``staticMeshRenderer.convertLightmapName`` std::string -> std::string
-  ``staticMeshRenderer.enableLightIndexes`` bool -> bool
-  ``staticMeshRenderer.enableLightMapAtlas`` bool -> bool
-  ``staticMeshRenderer.enableNewLightmapNames`` bool -> bool
-  ``staticMeshRenderer.enableRendering`` bool -> bool
-  ``staticMeshRenderer.enableUnifiedIndexlist`` bool -> bool
-  ``staticMeshRenderer.loadAllLightMapFiles`` std::string std::string -> bool
-  ``staticMeshRenderer.loadAllLightMapFilesDLL`` std::string std::string -> bool
-  ``staticMeshRenderer.materialCullingEnabled`` bool -> bool
-  ``staticMeshRenderer.maxLightMappedLod`` int -> int
-  ``staticMeshRenderer.noLods`` bool -> bool

``sv``
------

-  ``sv.adminScript`` std::string -> std::string
-  ``sv.allowExternalViews`` bool -> bool
-  ``sv.allowFreeCam`` bool -> bool
-  ``sv.allowNATNegotiation`` bool -> bool
-  ``sv.allowNoseCam`` bool -> bool
-  ``sv.autoBalanceTeam`` bool -> bool
-  ``sv.autoDemoHook`` std::string -> std::string
-  ``sv.autoRecord`` bool -> bool
-  ``sv.communityLogoURL`` std::string -> std::string
-  ``sv.configFile`` std::string -> std::string
-  ``sv.coopBotCount`` int -> int
-  ``sv.coopBotDifficulty`` float -> float
-  ``sv.coopBotRatio`` float -> float
-  ``sv.demoDownloadURL`` std::string -> std::string
-  ``sv.demoIndexURL`` std::string -> std::string
-  ``sv.demoQuality`` int -> int
-  ``sv.endDelay`` int -> int
-  ``sv.endOfRoundDelay`` int -> int
-  ``sv.friendlyFireWithMines`` bool -> bool
-  ``sv.gameSpyPort`` int -> int
-  ``sv.hitIndicator`` bool -> bool
-  ``sv.interfaceIP`` std::string -> std::string
-  ``sv.internet`` bool -> std::string

   -  1 - Adds the server to the server list.
   -  Tested this with the ``PRBF2_repo_w32ded.exe`` shortcut tool

-  ``sv.load`` -> bool
-  ``sv.manDownTime`` float -> float
-  ``sv.maxConnectionType`` ConnectionType -> ConnectionType
-  ``sv.maxPlayers`` int -> std::string

   -  Increases the player number count in the W32 Dedicated to the number specified.
   -  Effect Unknown.
   -  Maximum allowed is 100 though not sure if it’s a BF2 thing or not

-  ``sv.minPlayersForVoting`` int -> int
-  ``sv.notEnoughPlayersRestartDelay`` float -> float
-  ``sv.noVehicles`` float -> float
-  ``sv.numPlayersNeededToStart`` int -> int
-  ``sv.numReservedSlots`` int -> std::string
-  ``sv.password`` std::string -> std::string
-  ``sv.punkBuster`` bool -> bool
-  ``sv.radioBlockedDurationTime`` int -> int
-  ``sv.radioMaxSpamFlagCount`` int -> int
-  ``sv.ranked`` bool -> bool
-  ``sv.roundsPerMap`` int -> int
-  ``sv.save`` -> bool
-  ``sv.scoreLimit`` int -> int
-  ``sv.serverIP`` std::string -> std::string
-  ``sv.serverName`` std::string -> std::string
-  ``sv.serverPort`` int -> std::string
-  ``sv.soldierFriendlyFire`` int -> int
-  ``sv.soldierSplashFriendlyFire`` int -> int
-  ``sv.spawnTime`` float -> float
-  ``sv.sponsorLogoURL`` std::string -> std::string
-  ``sv.sponsorText`` std::string -> std::string
-  ``sv.startDelay`` int -> int
-  ``sv.teamRatioPercent`` float -> float
-  ``sv.teamVoteOnly`` bool -> bool
-  ``sv.ticketRatio`` int -> int
-  ``sv.timeBeforeRestartMap`` float -> float
-  ``sv.timeLimit`` int -> int
-  ``sv.tkNumPunishToKick`` int -> int
-  ``sv.tkPunishByDefault`` bool -> bool
-  ``sv.tkPunishEnabled`` bool -> bool
-  ``sv.useGlobalRank`` bool -> bool
-  ``sv.useGlobalUnlocks`` bool -> bool
-  ``sv.vehicleFriendlyFire`` int -> int
-  ``sv.vehicleSplashFriendlyFire`` int -> int
-  ``sv.voipBFClientPort`` int -> int
-  ``sv.voipBFServerPort`` int -> int
-  ``sv.voipEnabled`` bool -> bool
-  ``sv.voipQuality`` int -> int
-  ``sv.voipServerPort`` int -> int
-  ``sv.voipServerRemote`` bool -> bool
-  ``sv.voipServerRemoteIP`` std::string -> std::string
-  ``sv.voipSharedPassword`` std::string -> std::string
-  ``sv.voteTime`` int -> int
-  ``sv.votingEnabled`` bool -> bool
-  ``sv.welcomeMessage`` std::string -> std::string
-  ``swiffHost.addAward`` int int int -> void
-  ``swiffHost.addCredit`` std::string int -> void
-  ``swiffHost.addGameMode`` std::string std::string -> void
-  ``swiffHost.addRank`` int int int -> void
-  ``swiffHost.enableScroller`` bool -> void
-  ``swiffHost.loadImage`` std::string -> bool
-  ``swiffHost.serverBrowserFrameSkips`` int -> int
-  ``swiffHost.setScrollerRect`` int int int -> void
-  ``swiffHost.setScrollFadeSpeed`` int -> void
-  ``swiffHost.setScrollSpeed`` float -> void
-  ``terrain.ambientColor`` Vec3 -> Vec3
-  ``terrain.create`` std::string -> void
-  ``terrainCuller.baseCellSize`` int -> int
-  ``terrainCuller.checkInside`` bool -> bool
-  ``terrainCuller.cullerType`` int -> int
-  ``terrainCuller.detailCullMaxLevel`` int -> int
-  ``terrainCuller.lod0SwitchStart`` float -> float
-  ``terrainCuller.lod0SwitchStop`` float -> float
-  ``terrainCuller.lod1SwitchStart`` float -> float
-  ``terrainCuller.lod1SwitchStop`` float -> float
-  ``terrainCuller.lod2Start`` float -> float
-  ``terrainCuller.lodSwitchDistance`` int -> int
-  ``terrainCuller.updateLodLevel`` bool -> bool
-  ``terrainCuller.useStitchedLods`` bool -> bool
-  ``terrain.forceRenderStyle`` int -> int
-  ``terrain.GIColor`` Vec3 -> Vec3
-  ``terrain.GIColorHigh`` Vec3 -> Vec3
-  ``terrain.GIColorLow`` Vec3 -> Vec3
-  ``terrain.init`` -> void
-  ``terrain.load`` std::string -> void
-  ``terrain.refreshTerrainSampling`` -> void
-  ``terrain.sunColor`` Vec3 -> Vec3
-  ``terrain.terrainWaterColor`` Vec3 -> Vec3
-  ``terrain.waterAlphaAdd`` float -> float
-  ``terrain.waterAlphaHeightMul`` float -> float
-  ``terrain.waterAnimSpeed`` float -> float
-  ``terrain.waterColor`` Vec3 -> Vec3
-  ``terrain.waterNormalMap`` std::string -> std::string
-  ``terrain.waterQuality`` int -> int
-  ``terrain.waterReflectivity`` float -> float
-  ``terrain.waterScroll`` Vec2 -> Vec2
-  ``terrain.waterSpecularColor`` Vec4 -> Vec4
-  ``terrain.waterSpecularPower`` float -> float
-  ``terrain.waterSunIntensity`` float -> float
-  ``terrain.waterTransparency`` float -> float
-  ``texturemanager.customTextureSuffix`` std::string -> std::string
-  ``undergrowth.dynamicShadowsEnable`` bool -> bool
-  ``undergrowth.enabled`` bool -> bool
-  ``undergrowth.load`` std::string -> void
-  ``undergrowth.reload`` -> void
-  ``undergrowth.simpleShaderEnable`` bool -> bool
-  ``undergrowth.test`` uint -> uint
-  ``undergrowth.test2`` float -> float
-  ``undergrowth.viewDistanceFade`` float -> float
-  ``undergrowth.viewDistanceScale`` float -> float
-  ``undergrowth.zPassPatchCount`` uint -> uint
-  ``Vars.set`` std::string std::string -> void
-  ``videoSettings.setAntialiasing`` std::string -> void
-  ``videoSettings.setDynamicLightingQuality`` int -> void
-  ``videoSettings.setDynamicShadowsQuality`` int -> void
-  ``videoSettings.setEffectsQuality`` int -> void
-  ``videoSettings.setGeometryQuality`` int -> void
-  ``videoSettings.setLightingQuality`` int -> void
-  ``videoSettings.setResolution`` std::string -> void
-  ``videoSettings.setTerrainQuality`` int -> void
-  ``videoSettings.setTextureFilteringQuality`` int -> void
-  ``videoSettings.setTextureQuality`` int -> void
-  ``videoSettings.setVideoOptionScheme`` int -> void
-  ``videoSettings.setViewDistanceScale`` float -> void
-  ``weatherManager.doubleStrikeMaxDelay`` float -> float
-  ``weatherManager.doubleStrikeMinDelay`` float -> float
-  ``weatherManager.doubleStrikeProbability`` float -> float
-  ``weatherManager.inFadeSegments`` float -> float
-  ``weatherManager.lightningBlendOutTime`` float -> float
-  ``weatherManager.lightningColor`` Vec4 -> Vec4
-  ``weatherManager.lightningDuration`` float -> float
-  ``weatherManager.lightningGroundPenetration`` float -> float
-  ``weatherManager.lightningMaxInterval`` float -> float
-  ``weatherManager.lightningMaxPos`` Vec3 -> Vec3
-  ``weatherManager.lightningMinInterval`` float -> float
-  ``weatherManager.lightningMinPos`` Vec3 -> Vec3
-  ``weatherManager.lightningPertubation`` float -> float
-  ``weatherManager.lightningScale`` Vec2 -> Vec2
-  ``weatherManager.lightningSegments`` int -> int
-  ``weatherManager.lightningSFXDelay`` float -> float
-  ``weatherManager.lightningSFXName`` std::string -> std::string
-  ``weatherManager.outFadeSegments`` float -> float
-  ``weatherManager.skyBlendOutTime`` float -> float
-  ``weatherManager.stormEnabled`` bool -> bool
-  ``windManager.globalWindDirection`` Vec3 -> Vec3
-  ``windManager.globalWindSpeed`` float -> float

All ``Vars.Set`` Codes
----------------------

-  ``EngineRunningTimer`` 5.000000

-  ``anim-soldier-1p-speed-crouch`` 1.700000

-  ``anim-soldier-1p-speed-prone`` 3.000000

-  ``anim-soldier-spring-clamp`` 0.001000

-  ``anim-soldier-spring-zoom-factor`` 6.000000

-  ``anim_offsetBackwardTime`` 0.500000

-  ``anim_playCameraAnimations`` 1

-  ``anim_playSoldierAnimations`` 1

-  ``anim_playSoldierPostAnimations`` 1

-  ``anim_playVehicleAnimations`` 1

-  ``anim_playWeaponAnimations`` 1

-  ``anim_skipSync`` 0

-  ``anim_smoothSet`` 10.000000

-  ``anim_startJumpAtSpeed`` 2.500000

-  ``anim_startLandAtHeight`` 1.000000

-  ``anim_startLandAtSpeed`` -0.500000

-  ``anim_startLeftOffset`` 0.200000

-  ``anim_startRightOffset`` 0.700000

-  ``anim_test`` 0.250000

-  ``armor-invunerable-time`` 1.000000

-  ``armor-invunerable-time-afterwreck`` 1.000000

-  ``armor-max-soldier-wrecktime`` 60.000000

-  ``armor-water-safetycheck-time`` 2.500000

-  ``cFric`` 1.000000

-  ``cRest`` 1.000000

-  ``cam-dist`` 2.000000

-  ``cam-fast`` 10.000000

-  ``cam-interpolate-attachobject`` 1.200000

-  ``cam-normal`` 1.000000

-  ``cam-slow`` 0.100000

-  ``cam-stiffness`` 1.500000

-  ``cam_use_acc`` 0.000000

-  ``camera-check-closevehicle-freq`` 1.000000

-  ``camera-expshake-amp`` 5.000000

-  ``camera-expshake-freq`` 10.000000

-  ``camera-expshake-insidevehicle-mod`` 5.000000

-  ``camera-expshake-time`` 0.400000

-  ``camera-movement-speed-on-crouch`` 0.150000

-  ``camera-movement-speed-on-prone`` 0.100000

-  ``camera-movement-speed-on-stand`` 0.100000

-  ``camera-recoil-amplitude`` 0.600000

-  ``camera-recoil-speedmod`` 1.000000

-  ``camera-recoil-type`` 0

-  ``camera-shake-amp`` 2.0

-  ``camera-shake-amplitude`` 0.200000

-  ``camera-shake-distance`` 7.000000

-  ``camera-shake-freq`` 10.0

-  ``camera-shake-frequency`` 10.000000

-  ``camera-shake-time`` 0.2

-  ``camera-surface-snap-offset`` 0.090000

-  ``coll-cull-sphere-obb`` 1

-  ``coll-depth`` 3.000000

-  ``coll-draw-cyl`` 0

-  ``coll-draw-int`` 0

-  ``coll-draw-line-width`` 0.010000

-  ``coll-draw-lines`` 0

-  ``coll-draw-point-physics-radius`` 0.000000

-  ``coll-draw-soldier`` 0

-  ``coll-draw-tested_faces`` 0

-  ``coll-dump-all-tests`` 0

-  ``coll-edge`` 1

-  ``coll-edge-limit`` 0.866000

-  ``coll-forceOff-debugmeshes`` 0

-  ``coll-load-debugmeshes`` 0

-  ``coll-normal-limit`` 0.100000

-  ``coll-obb-cull-mode`` 1

-  ``coll-obb-cull-radius`` 0.577350

-  ``coll-obb-cull-vertex-limit`` 10

-  ``coll-soldier-collision-adjust-mod`` 2.000000

-  ``coll-soldier-collision-test-count`` 8

-  ``coll-soldier-collision-test-count-start-backAt`` 3

-  ``coll-soldier-collision-test-radius-mod`` 0.999000

-  ``coll-soldier-crouch-height`` 1.400000

-  ``coll-soldier-crush-depth`` 0.050000

-  ``coll-soldier-debug-proj-hit`` 0

-  ``coll-soldier-extend-ray`` 0.900000

-  ``coll-soldier-overrun-impact-mod`` 2.500000

-  ``coll-soldier-pivot-height`` 1.000000

-  ``coll-soldier-prone-height`` 0.800000

-  ``coll-soldier-radius`` 0.250000

-  ``coll-soldier-stand-height`` 1.700000

-  ``coll-static-vertex-limit`` 20

-  ``coll-use-cyl`` 1

-  ``coll-use-cyl-normal`` 1

-  ``coll-use-face`` 1

-  ``coll-use-fast-sphere-at-length`` 0.010000

-  ``coll-vel-dot-norm`` 0

-  ``collision-debug-default-terrain`` 0

-  ``collision-impact-speed-limit`` 4.000000

-  ``collision-skip-multcolls`` 1

-  ``collision-skip-multcolls-debug`` 0

-  ``collision-skip-multcolls-th`` 0.010000

-  ``collision-test-lod-distance-factor`` 0.060000

-  ``collision-test-lod-min-distance`` 25.000000

-  ``collision-test-projectile-lod-distance-factor`` 3.000000

-  ``collision-use-cubic-speedmod`` 0

-  ``collision-use-mod-on-soldier`` 1

-  ``conn-packetsize-override`` 0

-  ``damage-angle-mod-choke`` 0.000000

-  ``deathcam-terrainoffset`` 0.800000

-  ``debug-draw-test-ray`` 0

-  ``debug-engine`` 0 bool -> bool

   -  Activate in Console in Debugger
   -  Shows the RPM, Speed, Acceleration in a 3d text
   -  May need !restart to work and is somewhat buggy

-  ``debug-outputNewObject`` 0

-  ``debug-spring`` 0 bool -> bool

   -  Activate in Console in Debugger and normal
   -  Shows lines when approaching a vehicle.
   -  You can see what direction the vehicle will go when turning and has a bunch of other information regarding wheels”

-  ``demo-cam-360-capture`` 0

-  ``demo-cam-360-capture-move`` 0.000000

-  ``demo-cam-mouse-wheel-scale`` 0.850000

-  ``demo-cam-offset`` 1

-  ``demo-cam-offset-min`` 0.200000

-  ``demo-cam-offset-slow`` 0.800000

-  ``demo-cam-offset-speed`` 1.000000

-  ``demo-fspeed`` 100.000000

-  ``demo-slomo-cam`` 0.000000

-  ``detonation-collface-offset`` 0.070000

-  ``detonation-collface-offset-speedmod`` 0.050000

-  ``detonation-collface-offset-speedmod-max`` 500.000000

-  ``engine-audio-material-tweak`` 10.000000

-  ``engine-audio-sway-amplitude-first`` 0.050000

-  ``engine-audio-sway-amplitude-last`` 0.010000

-  ``engine-audio-sway-frequency-first`` 80.000000

-  ``engine-audio-sway-frequency-last`` 35.000000

-  ``engine-audio-sway-time-first`` 0.700000

-  ``engine-audio-sway-time-last`` 0.700000

-  ``engine-inertia`` 0.050000

-  ``engine-inertia2`` 0.990000

-  ``engine-inertia3`` 0.960000

-  ``engine-slope-no-gear-up-limit`` 0.174000

-  ``engine-slope-torque-mod-1st-gear`` 0.000000

-  ``engine-sound-smooth-time`` 0.100000

-  ``event-delay`` 0

-  ``event-delay-ticks`` 32

-  ``explosion-camshake-insidevehicle-mod`` 0.200000

-  ``explosion-camshake-maxdamage`` 150.000000

-  ``explosion-camshake-maxforce`` 20.000000

-  ``explosion-camshake-mod`` 4.000000

-  ``explosion-camshake-ownvehicle-mod`` 0.100000

-  ``explosion-hotspot`` 0.200000

-  ``explosion-hotspot-ray`` 0.020000

-  ``explosion-hotspot-ray-max`` 0.500000

-  ``explosion-latencyComp`` 1

-  ``explosion-soldier-expforce-ymod`` 5.000000

-  ``fb-mod`` 1.000000

-  ``feedback-mod`` 1.000000

-  ``fire-delay-after-jump`` 1.100000

-  ``fire-delay-from-prone`` 0.600000

-  ``flying_height`` 110.000000

-  ``follow-component-prediction-factor`` 0.100000

-  ``force-reg-limit`` 20.000000

-  ``hack-ignore-asserts`` 1

-  ``hc_dump`` 0

-  ``hc_freeze`` 0

-  ``hc_normals`` 0

-  ``hc_water`` 0

-  ``ignoreFriendlyTimer`` 1.000000

-  ``jump-delay-after-prone`` 1.200000

   -  ``Vars.set``
   -  Delay in seconds after prone to block the jump input.
   -  Setting it to 0 allows jumping when pressing space while moving from prone to standing

-  ``ladder-bottom-marginal`` 0.050000

-  ``ladder-climb-speed-mod`` 0.045000

-  ``ladder-down-angle-limit`` 35.000000

-  ``ladder-down-ray-mag`` 0.200000

-  ``ladder-down-ray-mag-skid`` 0.300000

-  ``ladder-end-camera-offset`` 0.400000

-  ``ladder-exit-offset`` 0.750000

-  ``ladder-getoff-ray-min`` 0.300000

-  ``ladder-getoff-speed-mod`` 1.150000

-  ``ladder-offset-top`` 0.360000

-  ``ladder-ray-debug`` 0

-  ``ladder-ray-debug2`` 0

-  ``ladder-skid-speed-mod`` 4.000000

-  ``ladder-soldier-dist`` 0.600000

-  ``ladder-soldier-start-getoff`` 1.800000

-  ``ladder-step-size`` 0.300000

-  ``ladder-top-exit-offset`` 0.750000

-  ``ladder-up-ray-mag-skid`` 1.700000

-  ``ladder-water-limit`` 1.200000

-  ``local-prediction`` 0

-  ``local-prediction-confirmtime`` 30

-  ``local-prediction-lerpTime`` 1.000000

-  ``local-prediction-minDelay`` 0.150000

-  ``maxDistKillMissile`` 15.000000

-  ``network-engine-fullPrecision`` 0

-  ``network-spring-fullPrecision`` 0

-  ``objectManager-cullHandleUpdateOnClientFactor`` 0.500000

-  ``objectspawner-draw-lines`` 0

-  ``objectspawner-inner-circle`` 0.300000

-  ``objectspawner-num-tries`` 7

-  ``old-turn-limit`` 1.000000

-  ``old-turn-mod`` 1.500000

-  ``opt-late-loading`` 0

-  ``opt-nosound`` 1

-  ``overheadCamera-acceleration`` 250.000000

-  ``overheadCamera-maxPositionDelta`` 7.000000

-  ``p-pos-damp`` 0.990000

-  ``p-pos-damp-water`` 0.900000

-  ``p-rot-damp`` 0.990000

-  ``p-rot-damp-water`` 0.900000

-  ``parachute-collapse-angle`` 0.300000

-  ``parachute-collapse-time`` 0.050000

-  ``parachute-collapse-time-water`` 0.050000

-  ``parachute-debug`` 0

-  ``parachute-spawn-debug`` 0

-  ``parachute-start-landing-height`` 8.000000

-  ``pco-exitpos-testlod`` 2

-  ``pco-min-playing-ticks`` 20

-  ``pco-show-gcs-stats`` 0

-  ``pco-unmanned-max-minor-axis`` 0.400000

-  ``pco-unmanned-min-major-axis`` 0.600000

-  ``phy-ang-vel`` 0.500000

-  ``phy-break-mod`` 0.950000

-  ``phy-bsp-stats`` 0

-  ``phy-contact-adjust-gravity-count`` 2

-  ``phy-convert-collision-meshes`` 0

-  ``phy-damage-frame-count`` 3

-  ``phy-damage-scale`` 100.000000

-  ``phy-damage-scale-limit`` 0.500000

-  ``phy-draw-soldier-bullet-collision`` 0

-  ``phy-engine-inertia`` 0.050000

-  ``phy-engine-slope`` 1.000000

-  ``phy-force-awake`` 0

-  ``phy-force-sleeping`` 0

-  ``phy-fri-dyn`` 0.800000

-  ``phy-fri-exp`` 3

-  ``phy-fri-lat`` 5.000000

-  ``phy-fri-mod`` 1.000000

-  ``phy-fri-mul`` 1.000000

-  ``phy-fri-stat`` 1.200000

-  ``phy-fri-wheel`` 0.990000

-  ``phy-fri-wheel2`` 1.000000

-  ``phy-gas`` 1.000000

-  ``phy-gravity-compensation-size`` 0.500000

-  ``phy-gravity-contact-mod`` 0.100000

-  ``phy-hand-break-adjust`` 0.050000

-  ``phy-hand-break-release`` 10

-  ``phy-hand-break-rpm`` 0.100000

-  ``phy-i-mod`` 1.500000

-  ``phy-imp-mod`` 1.000000

-  ``phy-imp-wakeup`` 1.000000

-  ``phy-impulse-limit`` 0.050000

-  ``phy-latencyComp-debug`` -1.000000

-  ``phy-latencyComp-default`` 0.050000

-  ``phy-latencyComp-max`` 0.300000

-  ``phy-latencyComp-maxRenderAheadTime`` 0.033333

-  ``phy-latencyComp-pingFactor`` 0.500000

-  ``phy-latencyComp-useClientWindow`` 1

-  ``phy-latencyComp-useInput`` 1

-  ``phy-latencyComp-useRenderAhead`` 0

-  ``phy-lin-acc`` 1.600000

-  ``phy-lin-mod`` 0.500000

-  ``phy-lin-vel`` 0.500000

-  ``phy-list-physics-nodes`` 0

-  ``phy-list-response-physics`` 0

-  ``phy-max-imp`` 1000.000000

-  ``phy-max-speed`` 1500.000000

-  ``phy-new-collision-meshes`` 0

-  ``phy-print`` -1

-  ``phy-proj-collision-count`` 3

-  ``phy-proj-collision-depth`` 0.050000

-  ``phy-proj-precision`` 0.001000

-  ``phy-proj-spring-on-up-axis`` 1

-  ``phy-sep-fifty-fifty`` 10.000000

-  ``phy-soldier-acceleration`` 0.120000

-  ``phy-soldier-air-movement-factor`` 0

-  ``phy-soldier-crawl-speed`` 0.800000

-  ``phy-soldier-crouch-speed`` 2.000000

-  ``phy-soldier-crush-minposspeedsqr`` 12.000000

-  ``phy-soldier-crush-minrotspeedsqr`` 0.010000

-  ``phy-soldier-crush-minvehicleposspeedsqr`` 2.000000

-  ``phy-soldier-deceleration`` 0.350000

-  ``phy-soldier-elasticity`` 0.000000

-  ``phy-soldier-feet-contact-normal`` 0.500000

-  ``phy-soldier-feet-level`` -0.040000

-  ``phy-soldier-friction`` 1.000000

-  ``phy-soldier-imp-feet`` 1.000000

-  ``phy-soldier-inair-speed`` 2.000000

-  ``phy-soldier-jump-factor`` 0.800000

-  ``phy-soldier-jump-length-factor`` 0.980000

-  ``phy-soldier-look-factor-x`` 5.000000

-  ``phy-soldier-look-factor-y`` 5.000000

-  ``phy-soldier-resistance`` 0.020000

-  ``phy-soldier-run-speed`` 3.900000

-  ``phy-soldier-skydive-speed`` 15.000000

-  ``phy-soldier-skydiveat-speed`` -10.000000

-  ``phy-soldier-speed-factor`` 0.850000

-  ``phy-soldier-sprint-dissipation-time`` 10.000000

-  ``phy-soldier-sprint-limit`` 0.500000

-  ``phy-soldier-sprint-recover-time`` 120.000000

-  ``phy-soldier-sprint-speed`` 7.000000

-  ``phy-soldier-start-float`` 0.990000

-  ``phy-soldier-stop-float`` 0.900000

-  ``phy-soldier-swim-speed`` 2.100000

-  ``phy-soldier-swimcrawl-speed`` 3.645000

-  ``phy-soldier-take-fall-damage`` 1

-  ``phy-soldier-walk-speed`` 1.500000

-  ``phy-spring-client-debug`` 0

-  ``phy-spring-server-debug`` 1

-  ``phy-tank-engine-inertia`` 0.070000

-  ``phy-turn`` 0.100000

-  ``phy-wing-water-mod`` 10.000000

-  ``phy-wreck`` 1

-  ``pose-crawl-crouch`` 0.500000

-  ``pose-crawl-run`` 0.500000

-  ``pose-crawl-sprint`` 0.500000

-  ``pose-crawl-swim`` 0.500000

-  ``pose-crawl-swimCrawl`` 0.500000

-  ``pose-crawl-walk`` 0.500000

-  ``pose-crouch-crawl`` 0.500000

-  ``pose-crouch-run`` 0.250000

-  ``pose-crouch-sprint`` 0.250000

-  ``pose-crouch-swim`` 0.500000

-  ``pose-crouch-swimCrawl`` 0.500000

-  ``pose-crouch-walk`` 0.250000

-  ``pose-run-crawl`` 0.500000

-  ``pose-run-crouch`` 0.250000

-  ``pose-run-sprint`` 0.250000

-  ``pose-run-swim`` 0.500000

-  ``pose-run-swimCrawl`` 0.500000

-  ``pose-run-walk`` 0.250000

-  ``pose-sprint-crawl`` 0.500000

-  ``pose-sprint-crouch`` 0.250000

-  ``pose-sprint-run`` 0.250000

-  ``pose-sprint-swim`` 0.500000

-  ``pose-sprint-swimCrawl`` 0.500000

-  ``pose-sprint-walk`` 0.250000

-  ``pose-walk-crawl`` 0.500000

-  ``pose-walk-crouch`` 0.250000

-  ``pose-walk-run`` 0.250000

-  ``pose-walk-sprint`` 0.250000

-  ``pose-walk-swim`` 0.500000

-  ``pose-walk-swimCrawl`` 0.500000

-  ``prone-delay-after-jump`` 1.200000

-  ``prone-delay-from-stand`` 1.200000

-  ``ragdoll-max-inherit-speed`` 5.000000

-  ``ragdoll_bodyBoneSize`` 0.120000

-  ``ragdoll_boneSize`` 0.100000

-  ``ragdoll_clientMaxUpdateTime`` 0.002000

-  ``ragdoll_collMid`` 0.999900

-  ``ragdoll_completeCollRadius`` 1.500000

-  ``ragdoll_dT`` 0.011111

-  ``ragdoll_enableForce`` 0

-  ``ragdoll_expRotateForce`` 13.000000

-  ``ragdoll_gravityOverTime`` 0.500000

-  ``ragdoll_iterations`` 2

-  ``ragdoll_kneeBoneSize`` 0.050000

-  ``ragdoll_legBackAngle`` -0.100000

-  ``ragdoll_legForwardAngle`` 10.000000

-  ``ragdoll_legForwardFactor`` 0.000000

-  ``ragdoll_legPointForwardAngle`` 0.500000

-  ``ragdoll_legPointForwardFactor`` 0.010000

-  ``ragdoll_net_boneEnable`` 15

-  ``ragdoll_net_debug`` 0

-  ``ragdoll_net_interpolate`` 0.100000

-  ``ragdoll_sleep`` 5.000000

-  ``ragdoll_sleepDelta`` 0.020000

-  ``ragdoll_slowMotion`` 1.000000

-  ``ragdoll_useAngularConstraints`` 1

-  ``ragdoll_useCapsuleCollision`` 1

-  ``ragdoll_useConstraints`` 1

-  ``ragdoll_useLandCollision`` 1

-  ``ragdoll_useObjectCollision`` 1

-  ``rd_dieForce`` 0.0

-  ``rd_dieInVehicleForce`` 100.000000

-  ``rd_expForceMod`` 1.000000

-  ``rd_hitForce`` 0.000000

-  ``rd_hitUp`` 0.000000

-  ``replenish-checkaim-freq`` 1.000000

-  ``replenish-checkaim-maint-freq`` 0.500000

-  ``replenish-ignoreteam`` 0

-  ``rot-use-old`` 1

-  ``rotationalbundle-max-speed-mod`` 30.000000

-  ``rotationalbundle-sound-smooth-time`` 0.150000

-  ``rpm-k`` 10.000000

-  ``rpm-wheel`` 0.060000

   No effect

-  ``server-sleep-overhead-time`` 0.005000

-  ``shoot-mag`` 10.000000

   No effect

-  ``show-damage-ndicator-for-all`` 1

-  ``show-engine`` 0

   No effect

-  ``soldier-drop-max`` 1.500000

-  ``soldier-drop-min`` 0.500000

-  ``soldier-drown-damage`` 8.000000

-  ``soldier-footstep-effect-cull-distance`` 20.000000

-  ``soldier-footstep-offset-dof-prone`` 0.000000

-  ``soldier-footstep-offset-dof-stand`` 0.130000

-  ``soldier-footstep-offset-y`` -0.990000

-  ``soldier-fov1p`` 0.820000

   No effect

-  ``soldier-impact-speed-limit`` 10.000000

-  ``soldier-impact-speed-limit-2`` 3.000000

-  ``soldier-lookDown`` 70.000000

   No effect

-  ``soldier-lookMaxAngle`` 40.000000/85.000000/0.000000

-  ``soldier-lookSideRestore`` 4.000000

-  ``soldier-lookUp`` -70.000000

-  ``soldier-mandown-rotspeed`` 0.100000

-  ``soldier-mandown-speed`` 5.000000

-  ``soldier-prone-inwater-limit`` 1.100000

   -  ``Vars.Set``
   -  The number referenced is the angle.
   -  Setting it to 0 allows you to prone into water.

      -  Can shoot walls when it’s in water but not walls from the surface.

   -  Setting it to 2 prevents you from proning near water in which you automatically go to the standing position

-  ``soldier-proneLookDown`` 5.000000

-  ``soldier-proneLookUp`` -30.000000

-  ``soldier-revive-disableinputtime`` 2.100000

-  ``soldier-terrain-speed-limit`` 9.100000

-  ``soldier-timeToEnableWeapon`` 1.250000

-  ``soldier_lookIdleAngle`` 15.000000

-  ``soldier_lookIdleTime`` 2.500000

-  ``soldier_lookSmooth`` 10.000000

-  ``soldier_throwGun`` 0.025000

-  ``soldier_throwGunForward`` 1.000000

-  ``soldier_throwHelmet`` 0.025000

-  ``soldier_throwKitPartsDelay`` 0.300000

-  ``sound-listener-radius`` 0.200000

-  ``sound-obstruction-disable`` 0

-  ``sound-obstruction-max`` 0.800000

-  ``sound-obstruction-max-reuse-frames`` 15

-  ``sound-obstruction-opt0`` 1

-  ``sound-obstruction-opt1`` 1

-  ``sound-obstruction-radius`` 2.000000

-  ``sound-obstruction-reuse-frames`` 0

-  ``sound-tinnitus-range`` 0.600000

-  ``spawnpoint-scatter-maxdist`` 9.000000

-  ``spawnpoint-scatter-mindist`` 3.000000

-  ``spawnpoint-scatter-testlod`` 2

-  ``spawnpoint-terrain-offset`` 1.010000

-  ``sprint-recharge-delay-after-jump`` 2.000000

-  ``stand-delay-from-prone`` 1.500000

-  ``stick-default-distance`` 0.050000

-  ``tank-square`` 1

-  ``targetYOffset`` 0.000000

-  ``use-loading-profiler`` 0

-  ``weapon-detonationDebug`` 0

-  ``weapon-detonationTriggerFreq`` 0.250000

-  ``wh-torque-mult`` 0.500000

-  ``wh-torque-offs`` 1.000000

-  ``wh-use-slip-ratio`` 0

-  ``wheel-inertia`` 0.100000

-  ``wheel-mod`` 1.000000

-  ``wp-delay-pingfactor`` 2

-  ``wp-delay-reloadfactor`` 1

-  ``wp-delay-ticks`` 15

-  ``zipline-soldier-height`` 1.490000
