
``combatArea``
==============

``combatArea.active``
   std::string -> void

``combatArea.addAreaPoint``
   Vec2 -> void

``combatArea.create``
   std::string -> void

``combatArea.deleteActiveCombatArea``
   -> void

``combatArea.getActiveCombatAreaName``
   -> std::string

``combatArea.inverted``
   bool -> bool

``combatArea.layer``
   int -> int

``combatAreaManager.addVehicleDamage``
   world::VehicleCategory float -> void

``combatAreaManager.addVehicleTimer``
   world::VehicleCategory float -> void

``combatAreaManager.damage``
   float -> float

``combatAreaManager.timeAllowedOutside``
   float -> float

``combatAreaManager.use``
   bool -> void

``combatArea.max``
   Vec2 -> Vec2

``combatArea.min``
   Vec2 -> Vec2

``combatArea.team``
   int -> int

``combatArea.usedByPathFinding``
   bool -> bool

``combatArea.vehicles``
   int -> int

   Controls what kind of vehicle is effected by the combat zone. This can be used for crating an extra large, separate combat zone around the base combat zone only for jets, to give them a much larger area to fly in and when you hop into a jet, you can still see the base combat zone, but the area between the base and the jet combat zone will be 1/2 transparent. When hand coding this, the values are:

      :VehicleType 0: Land
      :VehicleType 1: Sea
      :VehicleType 2: Planes
      :VehicleType 3: Choppers
      :VehicleType 4: All
      :VehicleType 5: Planes & Choppers