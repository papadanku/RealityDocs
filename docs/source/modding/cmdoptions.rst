
Command Line Options
====================

Battlefield 2 supports quite a few command line options. Most of you are probably already familiar with ones such as ``+fullscreen 1``. Incase some of you don't know, you can set a command line option by bringing up a shortcut's properties, going to the shorcut tab, and adding any of these options to the end of the 'Target' field. Command line options can only be set on shorcuts, which is useful because it allows you to have multiple shortcuts, all with different command line options. The following is a list of known command line options.

NOTE: The following options were found with the debug version of the BF2.exe, so some of these options may not work with the normal BF2.exe. The debug build can be obtained by downloading and installing the Battlefield 2 Editor. Once installed the debug build is named BF2_r.exe in your main Battlefield 2 directory. The Battlefield 2 Editor can be downloaded at `Battlefield 2 Editor <http://www.fileplanet.com/155852/download/Battlefield-2-Editor>`__ Also, case does matter when using these options.

Basic Options
-------------

.. list-table::
   :header-rows: 1

   * - Command
     - Description
     - Usage
   * - ``+multi``
     - Allows you to start multiple instances of Battlefield 2 at the same time.
     - ``+multi``
   * - ``+joinServer``
     - Joins the specified server. Accepts either a server ip or a hostname.
     - ``+joinServer`` ``OR``
   * - ``+playerName``
     - Sets the player name.
     - ``+playerName``
   * - ``+password``
     - Used in conjunction with ``+joinServer`` when the server requires a password. Possibly also sets the password for a dedicated server?
     - ``+password``
   * - ``+lowPriority``
     - Runs Battlefield 2 with a lower process priority(less CPU intensive, lower performance)
     - ``+lowPriority``
   * - ``+loadLevel``
     - Loads the specified level.
     - ``+loadLevel``
   * - ``+wx``
     - When Battlefield 2 is running in windowed mode, this sets the window's horizontal position on the screen. When setting this option, keep in mind that 0 corresponds to the left of the screen, and that the window is being positioned from its left side.
     - ``+wx``
   * - ``+wy``
     - When Battlefield 2 is running in windowed mode, this sets the window's vertical position on the screen. When setting this option, keep in mind that 0 corresponds to the top of the screen, and that the window is being positioned from its top side.
     - ``+wy``
   * - ``+szx``
     - When Battlefield 2 is running in windowed mode, this sets the window's horizontal size.
     - ``+szx``
   * - ``+szy``
     - When Battlefield 2 is running in windowed mode, this sets the window's vertical size.
     - ``+szy``
   * - ``+loadObfuscated``
     - Load obfuscated shaders. No idea what that means.
     - ``+loadObfuscated``
   * - ``+fullscreen``
     - Toggles Battlefield 2 between windowed and full screen mode.
     - ``+fullscreen``
   * - ``+noSound``
     - Starts Battlefield 2 with sound disabled.
     - ``+noSound``
   * - ``+lateLoading``
     - If set to 1, then resources (only sound at the moment) will be loaded on first use.
     - ``+lateLoading``
   * - ``+skipMips``
     - Sets how many mip-levels to skip in textures.
     - ``+skipMips``
   * - ``+mergeMaterials``
     - Concatenate materials at load time.
     - ``+mergeMaterials``
   * - ``+managedTextures``
     - Decides whether system memory should be used for textures.
     - ``+managedTextures``
   * - ``+debugOutput``
     - Enables or disables debug output.
     - ``+debugOutput``
   * - ``+demo``
     - Sets the con-file with demo options. Not sure what this does.
     - ``+demo <??>``
   * - ``+pyVerbose``
     - Display verbose Python script output. Nothing too interesting here.
     - ``+pyVerbose``
   * - ``+modPath``
     - Sets Battlefield 2's mod path. This is normally ``mods/bf2``.
     - ``+modPath``
   * - ``+ignoreAsserts``
     - Ignores debug assertion errors. This can only be used in conjunction with ``+developer 1`` or ``+dedicated 1``.
     - ``+ignoreAsserts``
   * - ``+disableShaderCache``
     - Disables the shader cache. This should only be used in conjunction with ``+developer 1``.
     - ``+disableShaderCache``
   * - ``+dumpAllConFiles``
     - Writes the names of every ``.con`` file to ``mods/$MOD$/allConFiles.con``.
     - ``+dumpAllConFiles``
   * - ``+customConFile``
     - Uses the specified ``.con`` file instead of loading all of the ``.con`` files. This file should be used to specify which con files to run, using the ``run`` command.
     - ``+customConFile``
   * - ``+help``
     - Displays command line option help, which lists all command line options and gives some descriptions.
     - ``+help``
   * - ``+?``
     - Does the same thing as ``+help``.
     - ``+?``
   * - ``+fileMonitor``
     - Enables automatic update of changed files (shaders, etc). This could prove to be very useful if it applies to ``.con`` and ``.py`` files.
     - ``+fileMonitor``
   * - ``+playerPassword``
     - Sets the player's password
     - ``+playerPassword``
   * - ``+developer``
     - Does not auto-login, and also allows other command line options to be used in conjunction with it.
     - ``+developer``
   * - ``+disableSwiff``
     - Disables swiff player. Basically this disables the flash that is used at the main menu area. Swiff refers to ``.swf``, the flash file format.
     - ``+disableSwiff``
   * - ``+debugSwiff``
     - Enables swiff debug output. Swiff refers to ``.swf``, the flash file format.
     - ``+debugSwiff``
   * - ``+playNow``
     - Starts up the game and automatically uses the 'Play Now' functionality.
     - ``+playNow``
   * - ``+pbPath``
     - Sets the path to Punkbuster for multiple-instance configurations. This is normally ``{install_dir}/pb``.
     - ``+pbPath``
   * - ``+keepCollisionForNavMeshes``
     - Keep collision mesh lods needed to generate AI navigation meshes. Not sure what this does.
     - ``+keepCollisionForNavMeshes``
   * - ``+restart``
     - Used by BF2 to restart the game without showing video for example when mod switching - can also be used to start BF 2 without showing videos using your own shortcuts
     - ``+restart``
   * - ``+port``
     - Used for specifying a port number to connect to in conjuntion with ``+joinServer``
     - ``+port``

Dedicated Server Options
------------------------

.. list-table::
   :header-rows: 1

   * - Command
     - Description
     - Usage
   * - ``+dedicated``
     - Starts Battlefield 2 in dedicated server mode. Not needed on Linux
     - ``+dedicated``
   * - ``+port``
     - Specifies which port the server should use.
     - ``+port``
   * - ``+maxPlayers``
     - Sets max number of players for the server.
     - ``+maxPlayers``
   * - ``+gameMode``
     - Sets the gamemode for the server.
     - ``+gameMode``
   * - ``+config``
     - Sets the path to the ServerSettings.con file to use.
     - ``+config``
   * - ``+mapList``
     - Sets the path to the mapList.con file to use.
     - ``+mapList``
   * - ``+noStatusMonitor``
     - If you don't want to run bf2 inside screen you need to use this.
     - ``+noStatusMonitor`` with values 1 (or 0 the default if you don't specify this option at all)
   * - ``+ranked``
     - Allows gamespy snapshot sending. This setting will do nothing unless EA has the IP of the server in their database.
     - ``+ranked``

Advanced Options
----------------

.. list-table::
   :header-rows: 1

   * - Command
     - Description
     - Usage
   * - ``+hostServer``
     - Unknown at the moment. Most likely starts a local server.
     - ``+hostServer <??>``
   * - ``+checkForAvailablePatch``
     - Unknown at the moment. Most likely does what the name says. When used with the debug build, returns an error message on startup. Appears to be broken.
     - ``+checkForAvailablePatch <??>``
   * - ``+checkForPatch``
     - Unknown at the moment. How does this differ from ``+checkForAvailablePatch``? When used with the debug build, returns an error message on startup. Appears to be broken.
     - ``+checkForPatch <??>``
   * - ``+aidll``
     - Unknown at the moment. Perhaps disables or enables the Battlefield 2 aidll.dll?
     - ``+aidll <??>``
   * - ``+ai``
     - Used to Force BF2 to load AI BOTS! No matter the map, requirements, or settings. --MasterX
     - ``+ai <0/1>``
   * - ``+refresh``
     - Unknown at the moment.
     - ``+refresh <??>``
   * - ``+renderMode``
     - Sets the current render mode. Possible render modes are 0-5, not sure what each one does yet.
     - ``+renderMode``
   * - ``+rp``
     - Unknown at the moment.
     - ``+rp <??>``
   * - ``+deviceType``
     - Unknown at the moment.
     - ``+deviceType <??>``
   * - ``+deviceBehavior``
     - Unknown at the moment.
     - ``+deviceBehavior <??>``
   * - ``+skipMeshLods``
     - Unknown at the moment. `LOD <http://en.wikipedia.org/wiki/Level_of_Detail>`__
     - ``+skipMeshLods <??>``
   * - ``+keepTemplates``
     - Unknown at the moment.
     - ``+keepTemplates <??>``
   * - ``+profileTextureUsage``
     - Unknown at the moment.
     - ``+profileTextureUsage <??>``
   * - ``+convertCollisionMeshes``
     - Unknown at the moment.
     - ``+convertCollisionMeshes <??>``
   * - ``+generateLightMaps``
     - Unknown at the moment.
     - ``+generateLightMaps <??>``
   * - ``+debugNetwork``
     - Unknown at the moment.
     - ``+debugNetwork <??>``
   * - ``+debugGhostManager``
     - Unknown at the moment.
     - ``+debugGhostManager <??>``
   * - ``+compile``
     - Unknown at the moment.
     - ``+compile <??>``
   * - ``+useCompiled``
     - Unknown at the moment.
     - ``+useCompiled <??>``
   * - ``+NoEffectTextureAtlas``
     - Unknown at the moment.
     - ``+NoEffectTextureAtlas <??>``
   * - ``+menu``
     - Unknown at the moment. This is used by Battlefield 2's default shortcut as ``+menu 1``.
     - ``+menu``
