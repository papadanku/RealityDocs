
``sound``
=========

``sound.addMenuSound``
   std::string std::string float -> void

``sound.addSound``
   std::string -> void

``sound.addTrigger``
   std::string -> void

``sound.dopplerEffect``
   float -> float

``sound.getAllSoundTemplates``
   -> std::string

``sound.getProperty``
   std::string -> std::string

``sound.getVolumeForGroup``
   int -> float

``sound.initialize``
   int std::string int -> SoundInitResult

``sound.interactiveMode``
   bool -> bool

``sound.listenerReverb``
   float -> float

``sound.loadMusic``
   std::string -> bool

``sound.masterVolume``
   float -> float

``sound.playMusic``
   -> bool

``sound.playSound``
   std::string -> void

``sound.removeAllTriggers``
   -> void

``sound.setProperty``
   std::string float -> void

``sound.setReverb``
   std::string -> void

``sound.setVolumeForGroup``
   int float -> void

``sound.showSoundSources``
   bool -> bool

``sound.showStats``
   bool -> bool

``Sound.startEngines``
   bool -> bool

``sound.stopMusic``
   float -> bool

``sound.stopSound``
   std::string -> void

``sound.tinnitusSetup``
   std::string float float -> void

``sound.tweakTemplate``
   std::string float float -> void

``sound.windSetup``
   std::string float -> void