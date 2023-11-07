
Game Engine Object Types
========================

This is a list of C++ game engine "object types" that can be used in the `bf2.objectManager.getObjectsOfType` method. As an example, to get a list of all control points, you could use: :py:class:`getChildren() <PhysicalObject.getChildren>`

.. code-block:: python

   controlPoints = bf2.objectManager.getObjectsOfType('dice.hfe.world.ObjectTemplate.ControlPoint')
   for cp in controlPoints:
      # do stuff to each control point``

Confirmed ObjectTypes
---------------------

.. list-table::
   :header-rows: 1

   * - ObjectType
     - Description
     - Parent
     - Children
   * - ``dice.hfe.world.ObjectTemplate.PlayerControlObject``
     - Returns a tuple of vehicle(?) objects that are controllable by a player (Includes the Commander assets). Vehicles are constructed of many objects, use the :py:class:`getChildren() <PhysicalObject.getChildren>` method to get a tuple of all objects in a vehicle.
     - None
     - None
   * - ``dice.hfe.world.ObjectTemplate.ControlPoint``
     - Returns A tuple of :py:class:`ControlPoint objects <controlPointObject>`. A controlpoint is constructed of a flagpole and a flag. Depending on which team controls the controlpoint, a different flag image is displayed.
     - None
     - Type :py:class:`PhysicalObject` (flagpole, flag_us, flag_mec, flag_ch, flag_neutral)
   * - ``dice.hfe.world.ObjectTemplate.Trigger``
     - Returns a tuple of type unknown objects.
     - None
     - None
   * - ``dice.hfe.world.ObjectTemplate.AmbientEffectArea``
     - Returns a tuple of type unknown objects.
     - None
     - None
   * - ``dice.hfe.world.ObjectTemplate.Ladder``
     - Returns a tuple of type unknown objects.
     - None
     - None
   * - ``dice.hfe.world.ObjectTemplate.TargetObject``
     - Returns a tuple of type unknown objects. These appear to always be of the template UniqueTarget. The first two objects in the tuple seem to always correspond to artillery. The first object is MEC or China artillery, while the second object always appears to be US artillery. When the round begins all the TargetObjects positions are set to (0.0, 0.0, 0.0). When artillery is fired, its corresponding TargetObject's position is set to the location of the artillery. This position remains until the artillery is fired again, and the position is overwritten with the new location. The other objects in the tuple correspond to guided missiles and such throughout the level(ie TV-Guided Missiles).
     - None
     - None
   * - ``dice.hfe.world.ObjectTemplate.ObjectSpawner``
     - Returns a tuple of :py:class:`PhysicalObject objects <PhysicalObject>`. Spawned objects are defined in the `GamePlayObjects.con` file that is located in server.zip (`GameModes//`). Examples of spawned objects are UAV, JEEP_AAV, destroyable bridges.
     - None
     - Mixed type depending on the type of the parent object.
   * - ``dice.hfe.world.ObjectTemplate.Soldier``
     - Returns a tuple of type unknown objects.
     - None
     - Unknown type
   * - ``dice.hfe.world.ObjectTemplate.AnimatedBundle``
     - Returns a tuple of type unknown objects.
     - None
     - None
   * - ``dice.hfe.world.ObjectTemplate.Kit``
     - Returns a tuple of type unknown objects.
     - None
     - Unknown type
   * - ``dice.hfe.world.ObjectTemplate.DestroyableObject``
     - Returns a tuple of type unknown objects.
     - None
     - None

Unconfirmed ObjectTypes
-----------------------

These objects are valid but return an empty tuple. They are probably not accessible from python, or only valid when these objects exist in the map. This is not tested. Any insight on these objects is highly appreciated.

- ``dice.hfe.world.TemplateComponent.PreDestinedFollowComp``
- ``dice.hfe.world.TemplateComponent.DefaultFollowComp``
- ``dice.hfe.world.TemplateComponent.FixedTargetComp``
- ``dice.hfe.world.TemplateComponent.SeekClosestTargetComp``
- ``dice.hfe.world.TemplateComponent.DefaultRicochetComp``
- ``dice.hfe.world.TemplateComponent.DefaultPenetrateComp``
- ``dice.hfe.world.TemplateComponent.DefaultProjSoundComp``
- ``dice.hfe.world.TemplateComponent.ReplenishDetonationComp``
- ``dice.hfe.world.TemplateComponent.DefaultDetonationComp``
- ``dice.hfe.world.TemplateComponent.StickyCollisionComp``
- ``dice.hfe.world.TemplateComponent.ResurrectCollisionComp``
- ``dice.hfe.world.TemplateComponent.ReplenishCollisionComp``
- ``dice.hfe.world.TemplateComponent.DefaultCollisionComp``
- ``dice.hfe.world.TemplateComponent.ExplosivesFireComp``
- ``dice.hfe.world.TemplateComponent.ThrownFireComp``
- ``dice.hfe.world.TemplateComponent.SpawnObjectFireComp``
- ``dice.hfe.world.TemplateComponent.LPFireComp``
- ``dice.hfe.world.TemplateComponent.SimpleTargetComp``
- ``dice.hfe.world.TemplateComponent.LPTargetComp``
- ``dice.hfe.world.TemplateComponent.MultiFireArmTargetComp``
- ``dice.hfe.world.TemplateComponent.ThrownAnimationComp``
- ``dice.hfe.world.TemplateComponent.DefaultAnimationComp``
- ``dice.hfe.world.TemplateComponent.TargetDeviationComp``
- ``dice.hfe.world.TemplateComponent.SimpleDeviationComp``
- ``dice.hfe.world.TemplateComponent.SoldierDeviationComp``
- ``dice.hfe.world.TemplateComponent.WeaponBasedRecoilComp``
- ``dice.hfe.world.TemplateComponent.SoldierBasedRecoilComp``
- ``dice.hfe.world.TemplateComponent.DefaultSoundComp``
- ``dice.hfe.world.TemplateComponent.ToggleCameraComp``
- ``dice.hfe.world.TemplateComponent.DefaultZoomComp``
- ``dice.hfe.world.TemplateComponent.ReplenishingAmmoComp``
- ``dice.hfe.world.TemplateComponent.DefaultAmmoComp``
- ``dice.hfe.world.TemplateComponent.MultiFireComp``
- ``dice.hfe.world.TemplateComponent.SingleFireComp``
- ``dice.hfe.world.TemplateComponent.StrategicObject``
- ``dice.hfe.world.TemplateComponent.HelpHud``
- ``dice.hfe.world.TemplateComponent.WarningHud``
- ``dice.hfe.world.TemplateComponent.AbilityHud``
- ``dice.hfe.world.TemplateComponent.WeaponHud``
- ``dice.hfe.world.TemplateComponent.VehicleHud``
- ``dice.hfe.world.TemplateComponent.PostProcess``
- ``dice.hfe.world.ObjectTemplate.GenericProjectile``
- ``dice.hfe.world.ObjectTemplate.TurnableRemoteControlledObject``
- ``dice.hfe.world.ObjectTemplate.RemoteControlledObject``
- ``dice.hfe.world.ObjectTemplate.LadderContainer``
- ``dice.hfe.world.ObjectTemplate.AreaObject``
- ``dice.hfe.world.ObjectTemplate.Obstacle``
- ``dice.hfe.world.ObjectTemplate.SupplyObject``
- ``dice.hfe.world.ObjectTemplate.SupplyDepot``
- ``dice.hfe.world.ObjectTemplate.KitPart``
- ``dice.hfe.world.ObjectTemplate.Parachute``
- ``dice.hfe.world.ObjectTemplate.GenericFireArm``
- ``dice.hfe.world.ObjectTemplate.AntennaObject``
- ``dice.hfe.world.ObjectTemplate.DestroyableWindow``
- ``dice.hfe.world.ObjectTemplate.DestroyableWindowsBundle``
- ``dice.hfe.world.ObjectTemplate.ItemContainer``
- ``dice.hfe.world.ObjectTemplate.Item``
