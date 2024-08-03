
``object``
==========

``objectManager``
-----------------

``objectManager.drawStats``
   int -> int

``objectDrawer``
----------------

``objectDrawer.collectPlanesDistance``
   float -> float

``objectDrawer.drawDebugPlanes``
   bool -> bool

``objectDrawer.faceForwardThreshold``
   float -> float

``objectDrawer.showCullStats``
   bool -> bool

``objectDrawer.useExactTest``
   bool -> bool

``objectDrawer.useOcclusion``
   bool -> bool

``object``
----------

``object.absolutePosition``
   Vec3 -> Vec3

``object.absolutePositionSecondary``
   Vec3 -> Vec3

``object.absoluteTransformation``
   Mat4 -> Mat4

``Object.active``
   world::IObject_ptrproxy -> world::IObject_ptrproxy

``object.addAbsolutePoint``
   -> void

``object.attenuationRange1``
   float -> float

``object.attenuationRange2``
   float -> float

``object.color``
   Vec3 -> Vec3

``object.coneAngle1``
   float -> float

``object.coneAngle2``
   float -> float

``Object.create``
   world::IObjectTemplate_ptrproxy Vec3 Vec3 -> world::IObject_ptrproxy

``Object.delete``
   world::IObject_ptrproxy -> void

``Object.deleteAll``
   -> std::string

``object.direction``
   Vec3 -> Vec3

``object.disableChildren``
   bool -> bool

``Object.forceStart``
   world::IObject_ptrproxy -> void

``Object.forceStop``
   world::IObject_ptrproxy -> void

``object.fov``
   float -> float

``object.geometry.color``
   Vec4 -> Vec4

``object.geometry.GenerateLightmapForThisInstance``
   bool -> bool

``object.geometry.loadMesh``
   std::string -> void

``object.geometry.subGeometry``
   int -> int

``object.geometry.subGeometryCount``
   -> int

``object.geometry.technique``
   std::string -> std::string

``object.geometry.template``
   -> IGeometryTemplate\*

``object.getControlPointId``
   -> int

``Object.getGroundPos``
   Vec3 -> Vec3

``object.getLightSourceMask``
   -> int

``object.getVisibleTeam``
   -> int

``object.group``
   int -> int

``object.hasCollision``
   bool -> bool

``object.hasUpdate``
   bool -> bool

``object.HDRIntensity``
   float -> float

``Object.info``
   world::IObject_ptrproxy -> std::string

``object.initGrid``
   Vec2 Vec2 int -> void

``object.isInGrid``
   bool -> bool

``object.isOvergrowth``
   bool -> bool

``object.isSaveable``
   bool -> bool

``object.isVisible``
   bool -> bool

``object.layer``
   int -> int

``Object.list``
   -> std::string

``Object.listObjectsOfTemplate``
   world::IObjectTemplate_ptrproxy -> std::string

``Object.loadAll``
   std::string -> bool

``object.name``
   std::string -> std::string

``object.notInAI``
   bool -> bool

``Object.printScript``
   world::IObject_ptrproxy -> std::string

``object.rotation``
   Vec3 -> Vec3

``object.rotationSecondary``
   Vec3 -> Vec3

``Object.saveAll``
   std::string -> bool

``object.scale``
   Vec3 -> Vec3

``object.setActive``
   bool -> void

``object.setAsSkyLight``
   -> void

``object.setControlPointId``
   int -> void

``object.setIsDisabledRecursive``
   bool -> void

``object.setIsInTweakModeRecursive``
   bool -> void

``object.setIsSaveableRecursive``
   bool -> void

``object.setIsVisibleRecursive``
   bool -> void

``object.setLightSourceMask``
   int -> void

``Object.setObjectToGround``
   world::IObject_ptrproxy -> Vec3

``object.setTeam``
   int -> void

``object.setVisibleTeam``
   int -> void

``object.spawnOffset``
   Vec3 -> Vec3

``Object.start``
   world::IObject_ptrproxy -> void

``Object.stop``
   world::IObject_ptrproxy -> void

``object.team``
   int -> int

``object.template``
   -> const IObjectTemplate\*

``object.togglePause``
   -> void