
``collisionManager``
====================

``CollisionCheck.checkStaticCollisionMeshes``
   int -> void

``collisionManager.buildDebugCollisionMeshes``
   -> void

``collisionManager.create``
   std::string -> void

``collisionManager.createTemplate``
   std::string -> void

   :Description: Creates a Collision Mesh template from the collision mesh name so it can be used in other files without creating a duplicate mesh
   :Used in: ``.con`` files for collision meshes

``collisionManager.drawBoundingBoxes``
   bool -> void

``collisionManager.drawForces``
   bool -> void

``collisionManager.drawIntersectFaces``
   bool -> void

``collisionManager.drawMeshes``
   bool -> void

``collisionManager.drawNormals``
   bool -> void

``collisionManager.drawOnlyRoot``
   float -> void

``collisionManager.drawPivots``
   bool -> void

``collisionManager.drawPrimitives``
   bool -> void

``collisionManager.drawSoldierMesh``
   bool -> void

``collisionManager.drawTestedFaces``
   bool -> void

``collisionManager.getNameOfObjectInFocus``
   -> void

``collisionManager.identityRotateObjectInFocus``
   -> void

``collisionManager.rotateObjectInFocusAroundAxis``
   uint float -> void

``collisionManager.rotateObjectInFocusAroundVector``
   Vec3 float -> void

``collisionManager.setActiveLod``
   int -> void

``collisionManager.setDrawDistance``
   float -> void

``collisionManager.setGeometry``
   bool -> void

``collisionManager.setSleepinessOfObjectInFocus``
   int -> void

   - ``.con`` presumably
   - Effect Unknown. Causes a game crash during loading when using ``collisionManager.setSleepinessOfObjectInFocus 0`` in a ``.con`` of a ``GenericFirearm``

``collisionManager.updateFlagsOfObjectInFocus``
   U32 U32 -> void

``collisionManager.useDeferredLoading``
   bool -> bool
