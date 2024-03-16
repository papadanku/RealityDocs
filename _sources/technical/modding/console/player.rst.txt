
``Player``
==========

``Player.active``
   IPlayer\* -> IPlayer\*

``Player.create``
   std::string std::string -> IPlayer\*

``player.isAi``
   bool -> bool

``player.isAlive``
   bool -> bool

``player.isNetwork``
   bool -> bool

``player.kit``
   int -> int

``Player.list``
   -> std::string

``Player.listPlayerClasses``
   -> std::string

``player.moveTo``
   Vec3 -> std::string

``player.name``
   -> std::string

``player.pickup``
   std::string -> void

``Player.saveAll``
   std::string -> bool

``player.setFov``
   float float -> void

``player.setVehicleWithInputId``
   IObject_ptrproxy int -> bool

``player.spawnGroup``
   int -> int

``player.team``
   int -> int

``player.vehicle``
   IObject_ptrproxy -> IObject_ptrproxy