
``objectTemplate``
==================

``objectTemplate.3dMapIcon``
   int -> int

   - Used in GenericFirearms (Mine etc) .tweak
   - The image number sequence referenced in ``Objects.dds``.
   - Use the vBF2 file and count the images. 9 is the mine icon.
   - Using this system, you could have custom 3D Mine Icons, as long as they are the same size as the original.

``objectTemplate.ability.hasAmmoAbility``
   bool -> bool

``objectTemplate.ability.hasHealingAbility``
   bool -> bool

``objectTemplate.ability.hasRepairingAbility``
   bool -> bool

``objectTemplate.ability.radarRadius``
   int -> int

``objectTemplate.abilityHud.ammoSound``
   std::string -> std::string

``objectTemplate.abilityHud.healingSound``
   std::string -> std::string

``objectTemplate.abilityHud.repairingSound``
   std::string -> std::string

``objectTemplate.abilityInVehicleMaterial``
   int -> int

``objectTemplate.abilityInVehicleRadius``
   float -> float

``objectTemplate.abilityInVehicleStrength``
   float -> float

``objectTemplate.abilityRestoreRate``
   float -> float

``objectTemplate.acceleration``
   Math::Vec3 -> Math::Vec3

``objectTemplate.acceleration``
   float -> float

``objectTemplate.accumulate``
   bool -> bool

``ObjectTemplate.active``
   world::IObjectTemplate_ptrproxy -> world::IObjectTemplate_ptrproxy

``ObjectTemplate.activeSafe``
   std::string world::IObjectTemplate_ptrproxy -> void

``objectTemplate.addAmmoType``
   int int float -> void

``objectTemplate.addChild``
   bool -> bool

``objectTemplate.addEmitterSpeed``
   bool -> bool

``objectTemplate.addKitVehicleMod``
   std::string int -> void

``objectTemplate.addLinePoint``
   Vec2 -> void

``objectTemplate.addPcoPosId``
   int -> void

``objectTemplate.addTargetObjectTypeToWatch``
   int -> void

``objectTemplate.addTemplate``
   std::string -> void

``objectTemplate.addToCollisionGroup``
   U32 -> void

``objectTemplate.addToProjectileList``
   bool -> bool

``objectTemplate.addTriggerableTarget``
   std::string -> void

``objectTemplate.addVehicleType``
   std::string int float -> void

``objectTemplate.addVehicleType``
   VehicleCategory -> void

``objectTemplate.addWorkOnMaterial``
   int -> void

``objectTemplate.affectingType``
   int -> int

``objectTemplate.affectLightmappedObjects``
   bool -> bool

``objectTemplate.AgeScaleFactorFromAcceleration``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorFromAltitude``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorFromEngine``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorFromRotationalSpeed``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorFromSpeed``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorFromSpeedInDof``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorRange``
   Vec2 -> Vec2

``objectTemplate.AgeScaleFactorUsed``
   bool -> bool

``objectTemplate.airFlowAffect``
   float -> float

``objectTemplate.airFriction``
   float -> float

``objectTemplate.airResistance``
   float -> float

``objectTemplate.airResistanceGraph``
   Vec4 -> Vec4

``objectTemplate.aiTemplate``
   std::string -> std::string

``objectTemplate.alignEffectTransformation``
   bool -> bool

``objectTemplate.alignRotationToSpeed``
   bool -> bool

``objectTemplate.allowDucking``
   bool -> bool

``objectTemplate.allowInsideDynamicLights``
   bool -> bool

``objectTemplate.allowInsideStaticSun``
   bool -> bool

``objectTemplate.alphaCull``
   float -> float

``objectTemplate.alphaIntensityFromAcceleration``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityFromAltitude``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityFromEngine``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityFromRotationalSpeed``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityFromSpeed``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityFromSpeedInDof``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityRange``
   Vec2 -> Vec2

``objectTemplate.alphaIntensityUsed``
   bool -> bool

``objectTemplate.alphaOverTime``
   OverTimeDistribution -> OverTimeDistribution

``objectTemplate.alternateTemplate0``
   std::string -> std::string

``objectTemplate.alternateTemplate1``
   std::string -> std::string

``objectTemplate.alternateTemplate2``
   std::string -> std::string

``objectTemplate.alternateTemplate3``
   std::string -> std::string

``objectTemplate.alternateTemplate4``
   std::string -> std::string

``objectTemplate.altSoldierExitPosition``
   Vec3 -> Vec3

``objectTemplate.ammo.abilityCost``
   float -> float

``objectTemplate.ammo.abilityDrain``
   float -> float

``objectTemplate.ammo.abilityMaterial``
   int -> int

``objectTemplate.ammo.abilityRadius``
   float -> float

``objectTemplate.ammo.abilityStrength``
   float -> float

``objectTemplate.ammo.ammoType``
   int -> int

``objectTemplate.ammo.autoReload``
   bool -> bool

``objectTemplate.ammo.changeMagAt``
   float -> float

``objectTemplate.ammo.firstShotExtraTime``
   float -> float

``objectTemplate.ammo.instantReloadOnEnable``
   bool -> bool

``objectTemplate.ammo.lastShotExtraTime``
   float -> float

``objectTemplate.ammo.magLinkWeapon``
   std::string -> std::string

   - Weapons, Vehicles ``.tweak``
   - Allows two weapons to share the same amount of bullets and magazines.
   - Enter the weapon name to maglink.
   - The weapon that's referenced must also have the same code.
   - Weapons with fire selector code causes it to not work properly (citation needed)

``objectTemplate.ammo.magSize``
   int -> int

   - Weapons ``.tweak``
   - Number of bullets in a magazine.

      - -1 for Infinity
      - Maximum non-infinity allowed is 1023
      - Any more will cause a crash

   - Bug: In the Battlerecorder, it doesn't pickup a gun that fires for 10 seconds on with 1000 bullets for some reason. Tested with the L4Bren on Auto.

``objectTemplate.ammo.minimumTimeUntilReload``
   float -> float

``objectTemplate.ammo.nrOfMags``
   int -> int

   Number of magazines allowed for a weapon.

``objectTemplate.ammo.onlyActiveWhileFiring``
   bool -> bool

   Prevents the Medibag and Ammo Bag from being thrown when firing. Used in PR's Medikit and Repair Bag

``objectTemplate.ammo.reloadAmount``
   int -> int

``objectTemplate.ammo.reloadTime``
   float -> float

   - Time in seconds of how long it takes to reload.
   - Must be the same number as the reload animation time from AnimationSystem1p.inc to sync properly.

``objectTemplate.ammo.reloadWithoutPlayer``
   bool -> bool

   - If enabled, weapon will autoreload regardless client settings for autoreload.
   - 1 - Enabled
   - 0 - Disabled

``objectTemplate.ammo.replenishingType``
   ReplenishingType -> ReplenishingType

``objectTemplate.ammo.toggleWhenNoAmmo``
   bool -> bool

   - Weapons ``.tweak``
   - When no ammo, switch to previous selected weapon.

``objectTemplate.ammoStorageSize``
   float -> float

``objectTemplate.anchor``
   Vec3 -> Vec3

``objectTemplate.anchorOffset``
   Vec3 -> Vec3

``objectTemplate.animatedUVRotation``
   int -> int

``objectTemplate.animatedUVRotationIndex``
   int -> int

``objectTemplate.animatedUVRotationRadius``
   float -> float

``objectTemplate.animatedUVRotationReverse``
   bool -> bool

``objectTemplate.animatedUVRotationScale``
   Vec2 -> Vec2

``objectTemplate.animatedUVTranslation``
   bool -> bool

``objectTemplate.animatedUVTranslationIndex``
   int -> int

``objectTemplate.animatedUVTranslationMax``
   Vec2 -> Vec2

``objectTemplate.animatedUVTranslationReverse``
   bool -> bool

``objectTemplate.animatedUVTranslationSize``
   Vec2 -> Vec2

``objectTemplate.animatedUVTranslationSpeed``
   Vec2 -> Vec2

``objectTemplate.animation.animateOnZoom``
   bool -> bool

``objectTemplate.animation.loopingFire``
   float -> float

``objectTemplate.animation.shiftDelay``
   float -> float

``objectTemplate.animation.useShiftAnimation``
   bool -> bool

``objectTemplate.animationEnable``
   bool -> bool

``objectTemplate.animationFrameCount``
   int -> int

``objectTemplate.animationFrameCountX``
   int -> int

``objectTemplate.animationFrameHeight``
   int -> int

``objectTemplate.animationFrameWidth``
   int -> int

``objectTemplate.animationPlayOnce``
   bool -> bool

``objectTemplate.animationRandomizedStartFrame``
   bool -> bool

``objectTemplate.animationSpeed``
   float -> float

``objectTemplate.animationSystem1P``
   std::string -> void

``objectTemplate.animationSystem3P``
   std::string -> void

``objectTemplate.antenna.accelerationFactor``
   float -> float

``objectTemplate.antenna.damping``
   float -> float

``objectTemplate.antenna.maxSwayAngle``
   Vec2 -> Vec2

``objectTemplate.antenna.skeleton``
   std::string -> std::string

``objectTemplate.antenna.speedFactor``
   float -> float

``objectTemplate.antenna.stiffness``
   float -> float

``objectTemplate.areaValueTeam1``
   U32 -> U32

``objectTemplate.areaValueTeam2``
   U32 -> U32

``objectTemplate.armingDelay``
   float -> float

   - Weapons ``.tweak``
   - Delay in seconds until the collision event is active.
   - Used in the tripflares, which has a 15 second delay before passing through it will trigger the collision.

      - Also could just be the seconds before the grenade explodes though not sure

``objectTemplate.armor.addArmorEffect``
   int std::string Vec3 -> void

``objectTemplate.armor.addArmorEffectSpectacular``
   int std::string Vec3 -> void

``objectTemplate.armor.addWreckArmorEffect``
   int std::string Vec3 -> void

``objectTemplate.armor.alignLastEffectToHitDirection``
   bool -> bool

``objectTemplate.armor.angleMod``
   float -> float

``objectTemplate.armor.attackDamage``
   float -> float

``objectTemplate.armor.canBeDestroyed``
   bool -> bool

``objectTemplate.armor.canBeRepairedWhenWreck``
   bool -> bool

   - Vehicles .tweak, Weapons ``.tweak``
   - Used in the AA Ship Boats.
   - Basically, when it's a wreck, it can be repaired back to life.

``objectTemplate.armor.criticalDamage``
   float -> float

``objectTemplate.armor.deepWaterDamageDelay``
   float -> float

``objectTemplate.armor.deepWaterLevel``
   float -> float

``objectTemplate.armor.defaultMaterial``
   int -> int

``objectTemplate.armor.destroyOnSpectacularDeath``
   bool -> bool

``objectTemplate.armor.explosionDamage``
   float -> float

``objectTemplate.armor.explosionForce``
   float -> float

``objectTemplate.armor.explosionForceMax``
   float -> float

``objectTemplate.armor.explosionForceMod``
   float -> float

``objectTemplate.armor.explosionMaterial``
   int -> int

``objectTemplate.armor.explosionRadius``
   float -> float

``objectTemplate.armor.hideChildrenOnSpectacularDeath``
   bool -> bool

``objectTemplate.armor.hitPoints``
   float -> float

   - Vehicles ``.tweak``
   - The health of the vehicle.
   - 0 - Dead.

``objectTemplate.armor.hpLostWhileCriticalDamage``
   float -> float

``objectTemplate.armor.hpLostWhileInDeepWater``
   float -> float

``objectTemplate.armor.hpLostWhileInWater``
   float -> float

``objectTemplate.armor.hpLostWhileUpSideDown``
   float -> float

``objectTemplate.armor.maxHitPoints``
   float -> float

``objectTemplate.armor.showDamageAsDirt``
   float -> float

``objectTemplate.armor.speedMod``
   float -> float

``objectTemplate.armor.timeToStayAfterDestroyed``
   float -> float

   - Vehicles ``.tweak``
   - Interesting code. If set to PR's Jets and Helis, when they explode from wreck, the non-flaming wreck model stays though it shows in the minimap as an occupied vehicle.

``objectTemplate.armor.timeToStayAsWreck``
   float -> float

``objectTemplate.armor.useMMOnDeath``
   bool -> bool

   - Use the Material Manager on Death. Not too sure about this one

``objectTemplate.armor.waterDamageDelay``
   float -> float

``objectTemplate.armor.waterLevel``
   float -> float

``objectTemplate.armor.wreckDelay``
   float -> float

``objectTemplate.armor.wreckExplosionDamage``
   float -> float

``objectTemplate.armor.wreckExplosionForce``
   float -> float

``objectTemplate.armor.wreckExplosionForceMax``
   float -> float

``objectTemplate.armor.wreckExplosionForceMod``
   float -> float

``objectTemplate.armor.wreckExplosionMaterial``
   int -> int

``objectTemplate.armor.wreckExplosionRadius``
   float -> float

``objectTemplate.armor.wreckHitPoints``
   float -> float

``objectTemplate.artPos``
   bool -> bool

``objectTemplate.attachClimberRadius``
   float -> float

``objectTemplate.attachToEventObject``
   bool -> bool

``objectTemplate.attackSpeed``
   float -> float

``objectTemplate.attenuationRange1``
   float -> float

   - Used in ``.tweak`` Effect Files for Lightsource Templates
   - How wide you want the lightsource effect to be, used with ``ObjectTemplate.isDynamic 1``.
   - Range1 - X, which is the horizontal range.
   - Max is 100, more than that will trigger an error message

``objectTemplate.attenuationRange2``
   float -> float

   - Used in ``.tweak`` Effect Files for Lightsource Templates
   - The height at which the lightsource will begin to drop.
   - Range2 - Y, which is the vertical range.
   - Max is 100, like above.

      - To know the difference, set one to 50 and one to 100 and count the number of seconds the lightsource effect will last and compare.

``objectTemplate.audio.newStyleAudio``
   bool -> bool

``objectTemplate.audio.transformationRelativeRoot``
   bool -> bool

``objectTemplate.audioReset``
   -> void

``objectTemplate.automaticPitchStabilization``
   bool -> bool

``objectTemplate.automaticReset``
   bool -> bool

``objectTemplate.automaticYawStabilization``
   bool -> bool

``objectTemplate.autoUseAbility``
   int -> int

``objectTemplate.averageTimeBetweenTests``
   float -> float

``objectTemplate.awakeTime``
   float -> float

``objectTemplate.blendMode``
   std::string -> std::string

``objectTemplate.blockInputOnRotBundle``
   std::string -> std::string

``objectTemplate.blurryVisionHoldTime``
   float -> float

``objectTemplate.blurryVisionTime``
   float -> float

``objectTemplate.boneName``
   std::string -> std::string

``objectTemplate.bounceDamping``
   float -> float

``objectTemplate.bounceLength``
   float -> float

``objectTemplate.bounceSensitivity``
   float -> float

``objectTemplate.bounceStrength``
   float -> float

``objectTemplate.boundingRadiusModifierWhenOccupied``
   float -> float

``objectTemplate.cameraId``
   int -> int

``objectTemplate.cameraShakeMaxSpeed``
   float -> float

``objectTemplate.cameraShakeSensitivity``
   float -> float

``objectTemplate.cameraShakeStartSpeed``
   float -> float

``objectTemplate.cameraSwayDofMax``
   float -> float

``objectTemplate.cameraSwayDofMin``
   float -> float

``objectTemplate.cameraSwayRightMax``
   float -> float

``objectTemplate.cameraSwayRightMin``
   float -> float

``objectTemplate.cameraSwayRodLength``
   float -> float

``objectTemplate.cameraSwaySensitivity``
   float -> float

``objectTemplate.cameraSwaySpringDamping``
   float -> float

``objectTemplate.cameraSwaySpringStrength``
   float -> float

``objectTemplate.canFireGuiIndex``
   int -> int

``objectTemplate.cannotFireGuiIndex``
   int -> int

``objectTemplate.cannotFireTimer``
   float -> float

``objectTemplate.canPickup``
   bool -> bool

   - Weapons
   - Allows explosives to be picked up using the wrench/repair object
   - Example: ``at_mine``

``objectTemplate.canReverse``
   bool -> bool

``objectTemplate.capMaxSpeed``
   bool -> bool

``objectTemplate.castsDynamicShadow``
   bool -> bool

   - Vehicles, Weapons, and Soldiers
   - Enables the rendering of shadows.

``objectTemplate.castsStaticShadow``
   bool -> bool

``objectTemplate.centerOfCollisionOffset``
   Vec3 -> Vec3

``objectTemplate.centerOfMassOffset``
   Vec3 -> Vec3

   To offset the center of mass using 0/0/0 - ``X/Y/Z.`` Setting it to X/0.5/Z will make a Logistics Truck survive a direct ram to a Van while setting to 0 makes the truck crash. Tested while holding shift.

``objectTemplate.chance``
   float -> float

   - ``AmbientObjects.con``
   - Chance that the triggerable effect may play when the player steps inside the radius.

      - 1 means it will always play
      - 0 means it will never play

``objectTemplate.changeLodAt``
   float -> float

``objectTemplate.chaseAngle``
   float -> float

``objectTemplate.chaseDistance``
   float -> float

``objectTemplate.chaseOffset``
   Vec3 -> Vec3

``objectTemplate.clearTemplateList``
   -> void

``objectTemplate.clientHitDetection``
   bool -> bool

``objectTemplate.climbableAngle``
   float -> float

``objectTemplate.climbersAttachForce``
   float -> float

``objectTemplate.climbingSpeed``
   float -> float

``objectTemplate.clockwise``
   bool -> bool

``objectTemplate.cockpitLod``
   int -> int

``objectTemplate.cockpitLod``
   U32 -> U32

``objectTemplate.cockpitSubGeom``
   int -> int

``objectTemplate.cockpitSubGeom``
   U32 -> U32

``objectTemplate.collision.bouncing``
   bool -> bool

``objectTemplate.collision.hasCollisionEffect``
   bool -> bool

``objectTemplate.collision.maxStickAngle``
   float -> float

``objectTemplate.collision.replenishingStrength``
   float -> float

``objectTemplate.collision.replenishingType``
   ReplenishingType -> ReplenishingType

``objectTemplate.collision.restoreHP``
   float -> float

``objectTemplate.collision.resurrectDamage``
   float -> float

``objectTemplate.collision.stickToStaticObjects``
   bool -> bool

``objectTemplate.collision.stickToTerrain``
   bool -> bool

``objectTemplate.collision.stickToVehicles``
   bool -> bool

``objectTemplate.collisionEffectName``
   std::string -> std::string

``objectTemplate.collisionEnable``
   bool -> bool

``objectTemplate.collisionGroups``
   U32 -> U32

``objectTemplate.collisionMesh``
   std::string -> void

``objectTemplate.collisionMesh``
   std::string -> std::string

``objectTemplate.collisionPart``
   int -> int

``objectTemplate.collisionSpeedAlongNormal``
   float -> float

``objectTemplate.collisionSpeedAlongPlane``
   float -> float

``objectTemplate.collisionStartRadius``
   float -> float

``objectTemplate.color``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.color``
   Vec3ColorFloat -> Vec3ColorFloat

``objectTemplate.color1``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.color2``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.colorBlendGraph``
   Vec4 -> Vec4

``objectTemplate.coneAngle1``
   float -> float

``objectTemplate.coneAngle2``
   float -> float

``objectTemplate.coneDirection``
   Vec3 -> Vec3

``objectTemplate.coneInnerAngle``
   float -> float

``objectTemplate.coneOuterAngle``
   float -> float

``objectTemplate.coneOuterVolume``
   float -> float

``objectTemplate.constantForce``
   float -> float

``objectTemplate.constantRpm``
   bool -> bool

``objectTemplate.continousRotationSpeed``
   Math::Vec3 -> Math::Vec3

``objectTemplate.controlPointId``
   int -> int

``objectTemplate.ControlPointId``
   U32 -> U32

``objectTemplate.controlPointName``
   std::string -> std::string

``objectTemplate.controlsCategory``
   dice::hfe::world::VehicleCategory -> dice::hfe::world::VehicleCategory

``objectTemplate.coolDownPerSec``
   float -> float

``objectTemplate.coolingFactor``
   float -> float

``objectTemplate.copyLinksCount``
   int -> int

``ObjectTemplate.create``
   std::string std::string -> IObjectTemplate\*

``objectTemplate.createComponent``
   std::string -> void

``objectTemplate.createdInEditor``
   bool -> bool

``objectTemplate.createInvisible``
   bool -> bool

   - Creates the object as invisible.
   - Collisions and Functions still work.
   - Tested on the ``at_mine``

``objectTemplate.createNotInGrid``
   bool -> bool

``objectTemplate.createVisibleInEditor``
   bool -> bool

``objectTemplate.crewKitIndex``
   int -> int

   - ``kits.con`` (example: ``gb82_pilot.con``)
   - Defines what Geom to use for the kit.
   - Looks up the Geom1 etc in the ``.skinnedmesh``, which is located in the Meshes folder. For example, arg82/Meshes/arg82_kits1.skinnedmeshes.
   - Open with BfMeshViewer to know what each number looks like.

``objectTemplate.crosshairFireTime``
   float -> float

``objectTemplate.cullRadiusScale``
   float -> float

   Used in Weapons, Vehicle, Statics etc.

``objectTemplate.CVMChase``
   bool -> bool

   - Vehicle ``.tweak`` files
   - Used to set at what distance the object is culled from display.
   - Each number represents a distance of 25m.
   - For example: ``ObjectTemplate.cullRadiusScale 6`` - VD of 150m

``objectTemplate.CVMExternTrace``
   bool -> bool

   Vehicle ``.tweak`` files

``objectTemplate.CVMFlyBy``
   bool -> bool

   Vehicle ``.tweak`` files

``objectTemplate.CVMFrontChase``
   bool -> bool

   Vehicle ``.tweak`` files

``objectTemplate.CVMInside``
   bool -> bool

   Vehicle ``.tweak`` files

``objectTemplate.CVMNose``
   bool -> bool

   Vehicle ``.tweak`` files

``objectTemplate.CVMTrace``
   bool -> bool

   Vehicles ``.tweak`` files

``objectTemplate.cycles``
   int -> int

``objectTemplate.damage``
   float -> float

``objectTemplate.damagedAmbientSoundLimit``
   float -> float

``objectTemplate.damageForBeingOutSideWorld``
   float -> float

``objectTemplate.damageMandownSoldiers``
   bool -> bool

``objectTemplate.damageOwner``
   bool -> bool

``objectTemplate.damageSpeed``
   float -> float

``objectTemplate.damageWhenLost``
   float -> float

``objectTemplate.dampenSprintRotationalForceInAirMod``
   float -> float

``objectTemplate.dampHorizontalVel``
   float -> float

``objectTemplate.dampHorizontalVelFactor``
   float -> float

``objectTemplate.damping``
   float -> float

``objectTemplate.deAcceleration``
   Math::Vec3 -> Math::Vec3

``objectTemplate.debugAutoRotate``
   bool -> bool

``objectTemplate.debugForceGearUp``
   bool -> bool

``objectTemplate.decalTextureName``
   std::string -> std::string

``objectTemplate.decreaseAngleToZero``
   bool -> bool

``objectTemplate.decreaseAngleToZeroSpeed``
   float -> float

``objectTemplate.decreaseAngleToZeroVerticalVel``
   float -> float

``objectTemplate.defaultAngleOfAttack``
   float -> float

``objectTemplate.defaultWeaponIndex``
   int -> int

``objectTemplate.degradeDropStrength``
   float -> float

``objectTemplate.degradeThrowStrength``
   float -> float

``objectTemplate.degradeThrowStrength2``
   float -> float

``objectTemplate.delay``
   RandomDistribution -> RandomDistribution

``objectTemplate.delayBeforeCycle``
   float -> float

``objectTemplate.delayBeforeEnd``
   float -> float

``objectTemplate.delayBeforeStart``
   float -> float

``objectTemplate.delayToUse``
   float -> float

``ObjectTemplate.delete``
   world::IObjectTemplate_ptrproxy -> void

``objectTemplate.deleteComponent``
   std::string -> void

``objectTemplate.deployAnimationTime``
   float -> float

``objectTemplate.destroyableWindowsTemplate``
   std::string -> std::string

``objectTemplate.destroyOnExit``
   bool -> bool

``objectTemplate.destroyWhenEmptyStorage``
   bool -> bool

``objectTemplate.detonateAfterProjectileStopped``
   bool -> bool

``objectTemplate.detonateAfterProjectileStoppedMinSpeed``
   float -> float

``objectTemplate.detonation.allowFriendlyFireDetonation``
   bool -> bool

``objectTemplate.detonation.detectionRadius``
   float -> float

``objectTemplate.detonation.detonateDistanceToTarget``
   float -> float

``objectTemplate.detonation.detonateOnWaterCollision``
   bool -> bool

``objectTemplate.detonation.effectRotation``
   Vec3 -> Vec3

``objectTemplate.detonation.endEffectTemplate``
   std::string -> std::string

``objectTemplate.detonation.explosionConeAngle``
   float -> float

``objectTemplate.detonation.explosionDamage``
   float -> float

``objectTemplate.detonation.explosionForce``
   float -> float

``objectTemplate.detonation.explosionInnerConeRadius``
   float -> float

``objectTemplate.detonation.explosionLineOfSightMinimumDamage``
   float -> float

``objectTemplate.detonation.explosionMaterial``
   int -> int

``objectTemplate.detonation.explosionRadius``
   float -> float

``objectTemplate.detonation.explosionSoldierLineOfSight``
   float -> float

``objectTemplate.detonation.explosionSoldierLineOfSightHealRate``
   float -> float

``objectTemplate.detonation.explosionSoldierLineOfSightTimer``
   float -> float

``objectTemplate.detonation.explosionYMod``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMaxAlpha``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMaxHealTime``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMaxHoldTime``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMaxRampTime``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMinAlpha``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMinHealTime``
   float -> float

``objectTemplate.detonation.flashbangAdditiveGlowMinHoldTime``
   float -> float

``objectTemplate.detonation.flashbangBillboardMaxAlpha``
   float -> float

``objectTemplate.detonation.flashbangBillboardMaxHealTime``
   float -> float

``objectTemplate.detonation.flashbangBillboardMaxHoldTime``
   float -> float

``objectTemplate.detonation.flashbangBillboardMaxRampTime``
   float -> float

``objectTemplate.detonation.flashbangBillboardMinAlpha``
   float -> float

``objectTemplate.detonation.flashbangBillboardMinHealTime``
   float -> float

``objectTemplate.detonation.flashbangBillboardMinHoldTime``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMaxAlpha``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMaxHealTime``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMaxHoldTime``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMaxRampTime``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMinAlpha``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMinHealTime``
   float -> float

``objectTemplate.detonation.flashbangMotionBlurMinHoldTime``
   float -> float

``objectTemplate.detonation.flashbangRadiusWithNightVision``
   float -> float

``objectTemplate.detonation.invisibleAtEndEffect``
   bool -> bool

``objectTemplate.detonation.maxDepthForExplosion``
   float -> float

``objectTemplate.detonation.minDetonationSpeed``
   float -> float

``objectTemplate.detonation.playMaterialEffectAtSurface``
   bool -> bool

``objectTemplate.detonation.radiusDetonateWithAirVehicles``
   bool -> bool

``objectTemplate.detonation.replenishingStrength``
   float -> float

``objectTemplate.detonation.replenishingType``
   ReplenishingType -> ReplenishingType

``objectTemplate.detonation.showMineIndicationIcon``
   bool -> bool

``objectTemplate.detonation.stopAtEndEffect``
   bool -> bool

``objectTemplate.detonation.timeUntilCanDetonate``
   float -> float

``objectTemplate.detonation.triggerAngle``
   float -> float

``objectTemplate.detonation.triggerRadius``
   float -> float

``objectTemplate.detonation.triggerTime``
   float -> float

``objectTemplate.detonation.triggerType``
   RadiusTriggerType -> RadiusTriggerType

``objectTemplate.detonation.triggerVictimMinSpeed``
   float -> float

``objectTemplate.detonation.useCollisionNormal``
   bool -> bool

``objectTemplate.detonation.useMMOnEndEffect``
   bool -> bool

``objectTemplate.deviation.devModCrouch``
   float -> float

``objectTemplate.deviation.devModLie``
   float -> float

``objectTemplate.deviation.devModStand``
   float -> float

``objectTemplate.deviation.devModZoom``
   float -> float

``objectTemplate.deviation.fireDevAdd``
   float -> float

``objectTemplate.deviation.fireDevMax``
   float -> float

``objectTemplate.deviation.fireDevSub``
   float -> float

``objectTemplate.deviation.minDev``
   float -> float

``objectTemplate.deviation.miscDevAddJump``
   float -> float

``objectTemplate.deviation.miscDevMax``
   float -> float

``objectTemplate.deviation.miscDevSub``
   float -> float

``objectTemplate.deviation.radius``
   float -> float

``objectTemplate.deviation.setFireDev``
   float float float -> void

``objectTemplate.deviation.setMiscDev``
   float float float -> void

``objectTemplate.deviation.setSpeedDev``
   float float float -> void

``objectTemplate.deviation.setTurnDev``
   float float float -> void

``objectTemplate.deviation.speedDevAddForward``
   float -> float

``objectTemplate.deviation.speedDevAddStrafe``
   float -> float

``objectTemplate.deviation.speedDevMax``
   float -> float

``objectTemplate.deviation.speedDevSub``
   float -> float

``objectTemplate.deviation.subProjectileDev``
   float -> float

``objectTemplate.deviation.turnDevAddPitch``
   float -> float

``objectTemplate.deviation.turnDevAddYaw``
   float -> float

``objectTemplate.deviation.turnDevMax``
   float -> float

``objectTemplate.deviation.turnDevSub``
   float -> float

``objectTemplate.differential``
   float -> float

``objectTemplate.direction``
   Vec3 -> Vec3

``objectTemplate.directionalScale``
   float -> float

``objectTemplate.disableIfEnemyInsideRadius``
   bool -> bool

``objectTemplate.disableInputWhileDucking``
   bool -> bool

``objectTemplate.disableSpawnPointsOnEnter``
   bool -> bool

``objectTemplate.disableWhenEmptyVehicle``
   bool -> bool

``objectTemplate.disableWhenEmptyVehicleDelay``
   float -> float

``objectTemplate.disableWhenLosingControl``
   bool -> bool

``objectTemplate.disableWhenWreck``
   bool -> bool

``objectTemplate.dismountAngle``
   float -> float

``objectTemplate.dismountCheckOffset``
   float -> float

``objectTemplate.distance``
   float -> float

``objectTemplate.distanceCannotEnter``
   float -> float

``objectTemplate.distToMinDamage``
   float -> float

``objectTemplate.distToStartLoseDamage``
   float -> float

``objectTemplate.dontAllowExit``
   bool -> bool

``objectTemplate.dontClearTeamOnExit``
   bool -> bool

``objectTemplate.drag``
   float -> float

   - How much the drag from the body of a vehicle affects its speed.
   - Without it, a vehicle will have an infinite top speed.

``objectTemplate.drag``
   RandomDistribution -> RandomDistribution

``objectTemplate.dragModifier``
   Vec3 -> Vec3

``objectTemplate.dragModifier``
   float -> float

``objectTemplate.dragOffset``
   Vec3 -> Vec3

   To offset the drag using 0/0/0 - ``X/Y/Z``

``objectTemplate.dragOverTime``
   OverTimeDistribution -> OverTimeDistribution

``objectTemplate.drawOrder``
   std::string -> std::string

``objectTemplate.dropHeadwear``
   std::string -> std::string

``objectTemplate.dropStrength``
   float -> float

``objectTemplate.effectChangeWaterHeight``
   float -> float

``objectTemplate.effectOnSpawn``
   std::string -> std::string

``objectTemplate.effectTemplateBaseName``
   std::string -> std::string

``objectTemplate.elasticity``
   float -> float

``objectTemplate.emitDelay``
   float -> float

``objectTemplate.emitDirection``
   Vec3 -> Vec3

``objectTemplate.emitDirectionZFromSpeedDof``
   bool -> bool

``objectTemplate.emitFrequency``
   float -> float

``objectTemplate.emitFrequencyScaleFactorLowerBound``
   float -> float

``objectTemplate.emitPrio``
   std::string -> std::string

``objectTemplate.emitRadius``
   Vec3 -> Vec3

``objectTemplate.emitRangeX``
   RandomDistribution -> RandomDistribution

``objectTemplate.emitRangeY``
   RandomDistribution -> RandomDistribution

``objectTemplate.emitRangeZ``
   RandomDistribution -> RandomDistribution

``objectTemplate.emitScaleFactorFromAcceleration``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorFromAltitude``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorFromEngine``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorFromRotationalSpeed``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorFromSpeed``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorFromSpeedInDof``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorRange``
   Vec2 -> Vec2

``objectTemplate.emitScaleFactorUsed``
   bool -> bool

``objectTemplate.emitSpeed``
   float -> float

``objectTemplate.emitSpeedGraph``
   Vec4 -> Vec4

``objectTemplate.emitSpeedScaleFromAcceleration``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleFromAltitude``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleFromEngine``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleFromRotationalSpeed``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleFromSpeed``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleFromSpeedInDof``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleRange``
   Vec2 -> Vec2

``objectTemplate.emitSpeedScaleUsed``
   bool -> bool

``objectTemplate.emitterSpeedScale``
   float -> float

``objectTemplate.emitterType``
   std::string -> std::string

``objectTemplate.emitTime``
   float -> float

``objectTemplate.enabled``
   bool -> bool

``objectTemplate.enemyTicketLossWhenCaptured``
   int -> int

``objectTemplate.engineInfluence``
   float -> float

``objectTemplate.engineName``
   std::string -> std::string

``objectTemplate.engineType``
   int -> int

   - What kind of vehicle the engine is for.
   - Car, tank, plane, ship, or helicopter.

``objectTemplate.entryRadius``
   float -> float

``objectTemplate.events``
   int -> int

``objectTemplate.exitSpeedMod``
   float -> float

``objectTemplate.fadeInFactor``
   float -> float

``objectTemplate.fadeOutFactor``
   float -> float

``objectTemplate.fire.addBarrelName``
   std::string -> void

``objectTemplate.fire.addFireRate``
   int -> void

   - Used in Weapons and Vehicle ``.tweak``
   - “Defines the fire mode selector. You can add three lines max of each one.

      - 0 - Single
      - 1 - Burst
      - 2 - Auto”

``objectTemplate.fire.addTimeEvent``
   WeaponTrigger WeaponAction float -> void

``objectTemplate.fire.altFireInput``
   io::PlayerInputMap -> io::PlayerInputMap

   Which PlayerInput map to use for the right-click function. Usually PIAlt

``objectTemplate.fire.batchSize``
   int -> int

``objectTemplate.fire.burstSize``
   int -> int

``objectTemplate.fire.busyUntilButtonRelease``
   bool -> bool

``objectTemplate.fire.detonatorObject``
   std::string -> std::string

``objectTemplate.fire.dropLod``
   int -> int

``objectTemplate.fire.dropWeaponAfterFiringDelay``
   float -> float

``objectTemplate.fire.dropWeaponAfterReloadDelay``
   float -> float

``objectTemplate.fire.fireInCameraDof``
   bool -> bool

``objectTemplate.fire.fireInCameraDofLocked``
   bool -> bool

``objectTemplate.fire.fireInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.fire.fireLaunchDelay``
   float -> float

``objectTemplate.fire.fireLaunchDelaySoft``
   float -> float

``objectTemplate.fire.fireStartDelay``
   RandomDistribution -> RandomDistribution

``objectTemplate.fire.hideLod``
   int -> int

``objectTemplate.fire.hideWeaponAfterFiringDelay``
   float -> float

``objectTemplate.fire.hideWeaponAfterReloadDelay``
   float -> float

``objectTemplate.fire.ignoreFireButton``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.fire.isBarrel``
   std::string -> bool

``objectTemplate.fire.maxProjectilesInWorld``
   int -> int

   - The max amount of projectiles in the weapon that can be set before the engine cleans up each one.
   - If the limit is 10, deploying one any further will delete an existing projectile.
   - Used for explosives, mines, and maybe bullets.

``objectTemplate.fire.onlyFireWhenProne``
   bool -> bool

   Restricts the weapon to fire only when prone. Though when firing during prone, a player can then stand and run to deploy an explosive for example. FH2 uses these for the machine gunner kits

``objectTemplate.fire.projectileStartPosition``
   Vec3 -> Vec3

   Position in X/Y/Z from the crosshair or PCO from where the projectile will launch.

``objectTemplate.fire.projectileStartRotation``
   Vec3 -> Vec3

``objectTemplate.fire.pullbackTime``
   float -> float

``objectTemplate.fire.radioMessageDelay``
   float -> float

``objectTemplate.fire.randomRotationSpeed``
   float -> float

``objectTemplate.fire.removeBarrelName``
   std::string -> void

``objectTemplate.fire.roundsPerMinute``
   int -> int

   - Used in GenericFirearms (Weapons, Projectiles)
   - The rate of fire, measured in Rounds Per Minute (RPM).
   - Must be dividable by 1800.
   - Check: http://researchmaniacs.com/Math/Divisible-By/What-is-1800-divisible-by.html

``objectTemplate.fire.showWeaponAfterReloadDelay``
   float -> float

``objectTemplate.fire.timeToReachMaxStrengthSlow``
   float -> float

``objectTemplate.fire.toggleWeaponTime``
   float -> float

``objectTemplate.fire.triggerChargesTime``
   float -> float

``objectTemplate.fire.useDummyProjectiles``
   bool -> bool

``objectTemplate.fixAxisSpring``
   bool -> bool

``objectTemplate.flagTemplateTeam0``
   std::string -> std::string

``objectTemplate.flagTemplateTeam1``
   std::string -> std::string

``objectTemplate.flagTemplateTeam2``
   std::string -> std::string

``objectTemplate.flapLift``
   float -> float

``objectTemplate.flicker``
   float -> float

``objectTemplate.floaterMod``
   float -> float

``objectTemplate.floatMaxLift``
   float -> float

``objectTemplate.floatMinLift``
   float -> float

``objectTemplate.follow.changePitch``
   float -> float

``objectTemplate.follow.changeYaw``
   float -> float

``objectTemplate.follow.maxPitch``
   float -> float

``objectTemplate.follow.maxYaw``
   float -> float

``objectTemplate.follow.minDist``
   float -> float

``objectTemplate.followStiffness``
   float -> float

``objectTemplate.force``
   float -> float

``objectTemplate.forceSustainedFire``
   bool -> bool

``objectTemplate.forceToWaterSurface``
   bool -> bool

``objectTemplate.ForSoldierOnly``
   bool -> bool

``objectTemplate.fov``
   float -> float

``objectTemplate.gasCloudDamage``
   float -> float

``objectTemplate.gasCloudRadiusTime``
   float -> float

``objectTemplate.gasCloudType``
   geom::GasCloudType -> geom::GasCloudType

``objectTemplate.gasMaskSprintFactor``
   float -> float

``objectTemplate.gearChangeTime``
   float -> float

``objectTemplate.gearDown``
   float -> float

``objectTemplate.gearDownDelay``
   float -> float

``objectTemplate.gearDownHeight``
   float -> float

``objectTemplate.gearDownSpeed``
   float -> float

``objectTemplate.gearUp``
   float -> float

``objectTemplate.gearUpDelay``
   float -> float

``objectTemplate.gearUpHeight``
   float -> float

``objectTemplate.gearUpSpeed``
   float -> float

``objectTemplate.geometry``
   std::string -> std::string

``objectTemplate.geometry.dropGeom``
   int -> int

``objectTemplate.geometry.kit``
   int -> int

``objectTemplate.geometry1P``
   std::string -> void

``objectTemplate.geometry3P``
   std::string -> void

``objectTemplate.geometryPart``
   int -> int

``objectTemplate.getHeatBarType``
   -> int

``objectTemplate.getPosition``
   int -> Math::Vec3

``objectTemplate.getRotation``
   int -> Math::Vec3

``objectTemplate.getTemplate``
   int -> std::string

``objectTemplate.globalEffectLevel``
   float -> float

``objectTemplate.gravity``
   float -> float

   Sets the gravity for the map. Can use minus values as well

``objectTemplate.gravityGraph``
   Vec4 -> Vec4

``objectTemplate.gravityModifier``
   float -> float

   - Sets the gravity for the vehicle.
   - Can use minus values as well which makes the projectile go upwards

``objectTemplate.gravityModifier``
   RandomDistribution -> RandomDistribution

``objectTemplate.gravityModifierOverTime``
   OverTimeDistribution -> OverTimeDistribution

``objectTemplate.grip``
   PhysicsGripFlags -> PhysicsGripFlags

   - “Set only for wheels.
   - Roll grip for wheels that are not powered.
   - Engine grip for wheels that are powered.
   - Engine dummy grip for wheel you want to make looking like they are powered, but actually aren't.

``objectTemplate.groundContactVolume``
   float -> float

``objectTemplate.group``
   U32 -> U32

``objectTemplate.halfVolumeDistance``
   float -> float

``objectTemplate.handleCollisionSpeed``
   float -> float

``objectTemplate.hasAltEffect``
   bool -> bool

``objectTemplate.hasCollisionPhysics``
   bool -> bool

   - Check for all objects that has a collision mesh.
   - Allows it to be hit by both bullets, players, and vehicles

``objectTemplate.HasGreyCapturingState``
   bool -> bool

``objectTemplate.hasMobilePhysics``
   bool -> bool

   Check for objects and parts that can move.

``objectTemplate.hasOnTimeEffect``
   bool -> bool

``objectTemplate.hasOverDamage``
   bool -> bool

``objectTemplate.hasPartner``
   bool -> bool

``objectTemplate.hasPointPhysics``
   bool -> void

``objectTemplate.hasRelativeOffset``
   bool -> bool

``objectTemplate.hasResponsePhysics``
   bool -> void

``objectTemplate.hasRestrictedExit``
   bool -> bool

``objectTemplate.hasRotationalPointPhysics``
   bool -> void

``objectTemplate.HDRIntensity``
   float -> float

``objectTemplate.healSpeed``
   float -> float

``objectTemplate.healStorageSize``
   float -> float

``objectTemplate.heatAddWhenFire``
   float -> float

``objectTemplate.heatIncrement``
   float -> float

``objectTemplate.height``
   float -> float

``objectTemplate.heightOffset``
   float -> float

``objectTemplate.helpHud.altHelpSoundKey``
   std::string -> std::string

``objectTemplate.helpHud.altHelpstd::stringKey``
   std::string -> std::string

``objectTemplate.helpHud.closeToDistance``
   int -> int

``objectTemplate.helpHud.closeToHelpSoundKeyEnemy``
   std::string -> std::string

``objectTemplate.helpHud.closeToHelpSoundKeyFriendly``
   std::string -> std::string

``objectTemplate.helpHud.closeToHelpSoundKeyNeutral``
   std::string -> std::string

``objectTemplate.helpHud.closeToHelpstd::stringKeyEnemy``
   std::string -> std::string

``objectTemplate.helpHud.closeToHelpstd::stringKeyFriendly``
   std::string -> std::string

``objectTemplate.helpHud.closeToHelpstd::stringKeyNeutral``
   std::string -> std::string

``objectTemplate.helpHud.helpSoundKey``
   std::string -> std::string

``objectTemplate.helpHud.helpstd::stringKey``
   std::string -> std::string

``objectTemplate.helpHud.lowAmmoHelpSoundKey``
   std::string -> std::string

``objectTemplate.helpHud.lowAmmoHelpstd::stringKey``
   std::string -> std::string

``objectTemplate.helpHud.lowArmorHelpSoundKey``
   std::string -> std::string

``objectTemplate.helpHud.lowArmorHelpstd::stringKey``
   std::string -> std::string

``objectTemplate.hideFirstPerson``
   bool -> bool

``objectTemplate.hoistFlag``
   bool -> bool

``objectTemplate.hoistMinMax``
   Vec2 -> Vec2

``objectTemplate.holdObject``
   bool -> bool

``objectTemplate.horizontalDampAngle``
   float -> float

``objectTemplate.horizontalDampAngleFactor``
   float -> float

``objectTemplate.horizontalSpeedMagnifier``
   float -> float

``objectTemplate.hullHeight``
   float -> float

``objectTemplate.ik.poleVectorLeft``
   Vec3 -> Vec3

``objectTemplate.ik.poleVectorRight``
   Vec3 -> Vec3

``objectTemplate.ik.positionLeft``
   Vec3 -> Vec3

``objectTemplate.ik.positionRight``
   Vec3 -> Vec3

``objectTemplate.ik.rotationLeft``
   Vec3 -> Vec3

``objectTemplate.ik.rotationRight``
   Vec3 -> Vec3

``objectTemplate.inertiaModifier``
   Vec3 -> Vec3

``ObjectTemplate.info``
   world::IObjectTemplate_ptrproxy -> std::string

``objectTemplate.inheritHeatFromPrimary``
   bool -> bool

``objectTemplate.initiallyWalkable``
   bool -> bool

``objectTemplate.input``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.inputToPitch``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.inputToRoll``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.inputToYaw``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.insideDamageFrequency``
   float -> float

``objectTemplate.insideDamageThreshold``
   float -> float

``objectTemplate.insideFOV``
   float -> float

``objectTemplate.insideStaticSunAmbientColor``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.insideStaticSunColor``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.insideStaticSunDamageColor``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.insideStaticSunDirection``
   Vec3 -> Vec3

``objectTemplate.intensity``
   float -> float

``objectTemplate.intensity``
   RandomDistribution -> RandomDistribution

``objectTemplate.intensityAtSpeed``
   float -> float

``objectTemplate.intensityOverTime``
   OverTimeDistribution -> OverTimeDistribution

``objectTemplate.inventorySize``
   U32 -> U32

``objectTemplate.inverseHeatBar``
   bool -> bool

``objectTemplate.invertGear``
   bool -> bool

``objectTemplate.invisible``
   bool -> bool

``objectTemplate.is3dSound``
   bool -> bool

   If the .wav file is Mono, setting it to 1 will tell the engine to play it on both channels. If applied to a .wav that is Stereo, it will play on the entire map. Same with .ogg files though it's usually experimentation.

``objectTemplate.isCounterForce``
   bool -> bool

``objectTemplate.isDestructable``
   bool -> bool

   Check only if object is a destroyable static object.

``objectTemplate.isDynamic``
   bool -> bool

``objectTemplate.isGasMask``
   bool -> bool

``objectTemplate.isHemisphere``
   bool -> bool

``objectTemplate.isLocalSystem``
   bool -> bool

   - Makes the effect follow the projectile and allows it to arch.
   - Used for the M67 *Zippo* Tank Flamethrower Effect.
   - Without it, the flame effect just shoots straight but not following the projectile

``objectTemplate.isLooping``
   bool -> bool

``objectTemplate.isNightVision``
   bool -> bool

``objectTemplate.isNotSaveable``
   bool -> bool

``objectTemplate.isOpenVehicle``
   bool -> bool

   Allows the ragdoll to slide off when killed from a vehicle position. Used in Technicals. If this is option. the passenger animation must have a die animation specified otherwise the ragdolls will float in the air.

``objectTemplate.isOvergrowth``
   bool -> bool

``objectTemplate.isPortalPassing``
   bool -> bool

``objectTemplate.isSelectable``
   bool -> bool

``objectTemplate.isSleeping``
   bool -> bool

``objectTemplate.isStatic``
   bool -> bool

``objectTemplate.isStaticSystem``
   bool -> bool

``objectTemplate.isUnderwaterEffect``
   bool -> bool

``objectTemplate.isUnstrategicControlPoint``
   bool -> bool

``objectTemplate.itemIndex``
   int -> int

   - What number in the keyboard is mapped to what weapon/tool.
   - Max is 9, not sure about 0.
   - Also positions the weapon icon square.

``objectTemplate.itemType``
   int -> int

``objectTemplate.keepProjectiles``
   float -> float Weapons

   - Time to keep the projectile in the world in seconds after you or the weapon dies

``objectTemplate.killHeatSeekingMissile``
   bool -> bool

``objectTemplate.kitTeam``
   int -> int

``objectTemplate.kitType``
   hfe::KitType -> hfe::KitType

``objectTemplate.lesserYawAtSpeed``
   float -> float

``objectTemplate.liftRegulated``
   bool -> bool

``objectTemplate.LightAffectionFactor``
   float -> float

``objectTemplate.lightMapIntensityOffset``
   float -> float

``objectTemplate.lightType``
   std::string -> std::string

``objectTemplate.linkAttachMovement``
   float -> float

``objectTemplate.linkAttachTime``
   float -> float

``objectTemplate.linkedEffectContainer``
   std::string -> std::string

``ObjectTemplate.list``
   std::string -> std::string

``objectTemplate.listenerObstruction``
   float -> float

   - Vehicles ``.tweak``
   - How muffled is the sound.
   - Lower value is least muffled.

``ObjectTemplate.listTemplateClasses``
   -> std::string

``objectTemplate.listTemplates``
   -> std::string

``ObjectTemplate.loadAll``
   -> bool

``objectTemplate.localPredictOnClient``
   bool -> bool

   - Used with Grenades and if there's any effect projectiles.
   - Seems like it tells the server to predict what's going to happen.

      - Maybe used with the Networkable Setting

``objectTemplate.lodDistance``
   float -> float

``objectTemplate.LodDistance``
   std::string -> std::string

``objectTemplate.loopCount``
   int -> int

``objectTemplate.looping``
   bool -> bool

``objectTemplate.loseControlWhenEnemyClose``
   bool -> bool

``objectTemplate.loseControlWhenNotClose``
   bool -> bool

``objectTemplate.lowSamples``
   int -> int

``objectTemplate.maintainCameraOnEnter``
   bool -> bool

``objectTemplate.maintainCameraOnExit``
   bool -> bool

``objectTemplate.manDownCameraOffsetInDof``
   float -> float

``objectTemplate.manDownCameraOffsetInUp``
   float -> float

``objectTemplate.mapMaterial``
   uint std::string uint -> void

``objectTemplate.maskOffset``
   Vec3 -> Vec3

``objectTemplate.maskType``
   hfe::MaskObjectType -> hfe::MaskObjectType

``objectTemplate.mass``
   float -> float

   - Used in Vehicles, Deployables, etc.
   - Mass is the weight of the vehicle in KG and also taking into account the GravityModifier value

``objectTemplate.material``
   int -> int

``objectTemplate.maxAngleOfAttack``
   float -> float

``objectTemplate.maxCorner``
   Vec3 -> Vec3

``objectTemplate.maxDistance``
   float -> float

``objectTemplate.maxDistanceUnderWaterSurface``
   float -> float

``objectTemplate.maxGasCloudRadius``
   float -> float

``objectTemplate.maxNrOfObjectSpawned``
   U32 -> U32

``objectTemplate.maxResetSpeed``
   Math::Vec3 -> Math::Vec3

``objectTemplate.MaxRopeLength``
   float -> float

   Fastropes confirmed ?!?!?!?!

``objectTemplate.maxRotation``
   Math::Vec3 -> Math::Vec3

``objectTemplate.maxSpawnDelay``
   float -> float

``objectTemplate.maxSpeed``
   Math::Vec3 -> Math::Vec3

``objectTemplate.maxSpeed``
   float -> float

``objectTemplate.maxTracerScaler``
   float -> float

   - Used in Projectiles (Weapons)
   - How long the tracer effect can be depending on projectile speed.
   - Reference: http://www.battlefieldsingleplayer.com/forum/index.php?showtopic-8592&mode-threaded&pid-84936

``objectTemplate.maxTriggerDistance``
   float -> float

``objectTemplate.maxVertRegAngle``
   float -> float

``objectTemplate.MaxZiplineLength``
   float -> float

``objectTemplate.mediumSamples``
   int -> int

``objectTemplate.minCorner``
   Vec3 -> Vec3

``objectTemplate.minDamage``
   float -> float

``objectTemplate.minDistance``
   float -> float

``objectTemplate.minDistanceUnderWaterSurface``
   float -> float

``objectTemplate.minGasCloudRadius``
   float -> float

``objectTemplate.minimapNameOffset``
   Vec2 -> Vec2

``objectTemplate.minimumTimeBetweenTriggering``
   float -> float

   - ``AmbientObjects.con`` (Map)
   - The time when the trigger will repeat again after entering the trigger radius.
   - Happens after the effect plays. In seconds.
   - Depends also on ``ObjectTemplate.chance``

``objectTemplate.minNrToTakeControl``
   U32 -> U32

``objectTemplate.minRotation``
   Math::Vec3 -> Math::Vec3

``objectTemplate.minSpawnDelay``
   float -> float

``objectTemplate.minTimeBetweenActivation``
   float -> float

``objectTemplate.minTracerScaler``
   float -> float

``objectTemplate.minTrailVelocity``
   float -> float

``objectTemplate.minYNormal``
   float -> float

``objectTemplate.movementSpeed``
   float -> float

``objectTemplate.movementType``
   int -> int

``objectTemplate.moveToWaterSurface``
   bool -> bool

``objectTemplate.name``
   -> std::string

``objectTemplate.nameTagOffset``
   Vec3 -> Vec3

``objectTemplate.nearCullingEnable``
   bool -> bool

``objectTemplate.networkableInfo``
   std::string -> std::string

   - ``Networkables.con``
   - Needs to be set for objects that won't work online without them.
   - Depends on the way it's set and if it crashes immediately, is laggy, or crashes unexpectantly”

``objectTemplate.neverDrawAs1p``
   bool -> bool

   - Vehicle, Weapons, Effects
   - Makes the effect not draw in front of you when in 1p mode.
   - Link: http://www.realitymod.com/forum/f388-pr-bf2-community-modding/113277-1p-animations-pcos-3.html

``objectTemplate.newCar2.brakeTorque``
   float -> float

``objectTemplate.newCar2.engineBrakeTorque``
   float -> float

``objectTemplate.newCar2.engineFeedbackMod``
   float -> float

``objectTemplate.newCar2.frictionMod``
   float -> float

``objectTemplate.newCar2.frictionTorque``
   float -> float

``objectTemplate.newCar2.maxRpm``
   float -> float

``objectTemplate.newCar2.minRpm``
   float -> float

``objectTemplate.newCar2.slopeTorqueMod``
   float -> float

``objectTemplate.newCar2.useClutchedTorque``
   bool -> bool

``objectTemplate.newCar2.wheelInertia``
   float -> float

``objectTemplate.newCar2.wheelLatDriveFrictionMod``
   float -> float

``objectTemplate.newCar2.wheelLatFrictionMod``
   float -> float

``objectTemplate.newCar2.wheelLatMinDynamicFriction``
   float -> float

``objectTemplate.newCar2.wheelLatPeakAt``
   float -> float

``objectTemplate.newCar2.wheelLatScale``
   float -> float

``objectTemplate.newCar2.wheelLongDriveFrictionMod``
   float -> float

``objectTemplate.newCar2.wheelLongFrictionMod``
   float -> float

``objectTemplate.newCar2.wheelLongMinDynamicFriction``
   float -> float

``objectTemplate.newCar2.wheelLongPeakAt``
   float -> float

``objectTemplate.newCar2.wheelLongScale``
   float -> float

``objectTemplate.noEffectAtPerpSpeed``
   float -> float

``objectTemplate.noPassengerTimeToLive``
   int -> int

``objectTemplate.noPhysics``
   bool -> bool

``objectTemplate.noPropellerEffectAtSpeed``
   float -> float

``objectTemplate.nosePos``
   Vec3 -> Vec3

``objectTemplate.notCycledIfOccupied``
   bool -> bool

``objectTemplate.noVertRegAngle``
   float -> float

``objectTemplate.nrOfObjectToSpawn``
   int -> int

``objectTemplate.nrOfRespawns``
   int -> int

``objectTemplate.numberOfGears``
   int -> int

``objectTemplate.NumberOfLinks``
   int -> int

``objectTemplate.numNetworkedEffects``
   int -> int

``objectTemplate.numPlanes``
   int -> int

``objectTemplate.objectShadows``
   bool -> bool

``objectTemplate.objectTemplate``
   std::string -> std::string

``objectTemplate.onlyTakeableByTeam``
   U32 -> U32

``objectTemplate.onlyWhenOccupied``
   bool -> bool

``objectTemplate.otherCollisionLod``
   int -> int

``objectTemplate.overheatPenalty``
   float -> float

``objectTemplate.pan``
   float -> float

``objectTemplate.ParticleMaxSize``
   float -> float

   - Used in Vehicle ``.con`` and ``.tweak`` files
   - Defines what materials the vehicle should use, which references the materialdefine file.
   - Use BfMeshViewer to find out what numbers belong to what sides.

``objectTemplate.particleSystemTemplate``
   std::string -> std::string

   Same as above

``objectTemplate.particleType``
   std::string -> std::string

``objectTemplate.pcoFlags``
   int -> int

``objectTemplate.pcoId``
   int -> int

``objectTemplate.penetrate.allowLiquidPenetration``
   bool -> bool

``objectTemplate.penetrate.allowSolidPenetration``
   bool -> bool

``objectTemplate.penetrate.neverPenetrate``
   bool -> bool

``objectTemplate.physicsFrequency``
   int -> int

``objectTemplate.physicsType``
   PhysicsType -> PhysicsType

   - Vehicles
   - ``None`` for no collision
   - ``Point`` for projectile (Ignores mesh)
   - ``Mesh`` if object has collision mesh”

``objectTemplate.pitch``
   float -> float

``objectTemplate.pitchEnvelope``
   std::string -> std::string

``objectTemplate.pitchOffset``
   float -> float

``objectTemplate.pivotOffset``
   Vec2 -> Vec2

``objectTemplate.PivotPosition``
   Math::Vec3 -> Math::Vec3

``objectTemplate.playAtEventPosition``
   bool -> bool

``objectTemplate.playAtPlayerPosition``
   bool -> bool

``objectTemplate.portalPassingPosition``
   Vec3 -> Vec3

``objectTemplate.poseCameraPosition``
   int Vec3 -> void

``objectTemplate.position``
   Vec3 -> Vec3

``objectTemplate.positionalSpeedInDof``
   RandomDistribution -> RandomDistribution

``objectTemplate.positionalSpeedInRight``
   RandomDistribution -> RandomDistribution

``objectTemplate.positionalSpeedInUp``
   RandomDistribution -> RandomDistribution

``objectTemplate.positionOffset``
   Math::Vec3 -> Math::Vec3

``objectTemplate.postProcess.tvDistortionFreq``
   float -> float

``objectTemplate.postProcess.tvDistortionRoll``
   float -> float

``objectTemplate.postProcess.tvDistortionScale``
   float -> float

``objectTemplate.postProcess.tvInterference``
   float -> float

``objectTemplate.preCacheObject``
   bool -> bool

``objectTemplate.preWarmTime``
   float -> float

``ObjectTemplate.printScript``
   world::IObjectTemplate_ptrproxy -> std::string

``objectTemplate.projectileTemplate``
   std::string -> std::string

   - Used in Weapons and Vehicle ``.tweak``
   - GenericFirearm
   - Defines the projectile that the ``GenericFirearm`` should use.
   - Looks for the ``GenericProjectile`` that is defined in all ``.tweak`` files.

``objectTemplate.projectOnHeightmap``
   bool -> bool

``objectTemplate.projectorApplyMask``
   bool -> bool

``objectTemplate.projectorAspect``
   float -> float

``objectTemplate.projectorFar``
   float -> float

``objectTemplate.projectorFov``
   float -> float

``objectTemplate.projectorNear``
   float -> float

``objectTemplate.projectorTexture``
   std::string -> std::string

``objectTemplate.propRotAxis``
   int -> int

``objectTemplate.pureRotational``
   bool -> bool

``objectTemplate.QualityLevel``
   std::string -> std::string

``objectTemplate.radialDirection``
   float -> float

``objectTemplate.radio.destroyedMessage``
   std::string -> std::string

``objectTemplate.radio.failMessage``
   std::string -> std::string

``objectTemplate.radio.repairedMessage``
   std::string -> std::string

``objectTemplate.radio.spottedMessage``
   std::string -> std::string

``objectTemplate.radio.useMessage``
   std::string -> std::string

``objectTemplate.radius``
   float -> float

``objectTemplate.radiusOffset``
   Vec3 -> Vec3

``objectTemplate.ragdollLandedDelay``
   float -> float

``objectTemplate.randomAgeFactor``
   RandomDistribution -> RandomDistribution

``objectTemplate.randomColorIntensity``
   float -> float

``objectTemplate.randomDirectionAngle``
   Vec3 -> Vec3

``objectTemplate.randomIntensity``
   float -> float

``objectTemplate.randomizeGeomPart``
   bool -> bool

``objectTemplate.randomRadialDirection``
   float -> float

``objectTemplate.randomRotation``
   float -> float

``objectTemplate.randomRotation``
   Vec3 -> Vec3

``objectTemplate.randomRotationSpeed``
   Vec3 -> Vec3

``objectTemplate.randomRotationSpeed``
   float -> float

``objectTemplate.randomSize``
   float -> float

``objectTemplate.randomSpeed``
   float -> float

``objectTemplate.randomTimeToLive``
   float -> float

``objectTemplate.rcType``
   RemoteControlledObjectType -> RemoteControlledObjectType

``objectTemplate.readBinary``
   std::string -> void

``objectTemplate.recoil.cameraRecoilSize``
   float -> float

``objectTemplate.recoil.cameraRecoilSpeed``
   float -> float

``objectTemplate.recoil.goBackOnRecoil``
   bool -> bool

``objectTemplate.recoil.hasRecoilForce``
   bool -> bool

``objectTemplate.recoil.recoilForce``
   float -> float

``objectTemplate.recoil.recoilForceLeftRight``
   RandomDistribution -> RandomDistribution

``objectTemplate.recoil.recoilForceUp``
   RandomDistribution -> RandomDistribution

``objectTemplate.recoil.recoilGraphExponent``
   float -> float

``objectTemplate.recoil.recoilGraphFrameCount``
   int -> int

``objectTemplate.recoil.recoilGraphTotalMovement``
   float -> float

``objectTemplate.recoil.recoilSize``
   float -> float

``objectTemplate.recoil.recoilSpeed``
   float -> float

``objectTemplate.recoil.recoilSpeedGB``
   float -> float

``objectTemplate.recoil.zoomModifier``
   float -> float

``objectTemplate.refillAmmoSpeed``
   float -> float

``objectTemplate.regulatePitch``
   Vec2 -> Vec2

``objectTemplate.regulatePitchInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.regulateRoll``
   Vec2 -> Vec2

``objectTemplate.regulateRollInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.regulateToLift``
   float -> float

``objectTemplate.regulateVerticalPos``
   Vec2 -> Vec2

``objectTemplate.regulateVerticalPosInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.regulateYaw``
   Vec2 -> Vec2

``objectTemplate.regulateYawInput``
   io::PlayerInputMap -> io::PlayerInputMap

   - In the effects .tweak when creating an effect
   - Allows an effect template to be used with custom settings.

``objectTemplate.regWhenMinInput``
   float -> float

``objectTemplate.relativePositionInDof``
   RandomDistribution -> RandomDistribution

``objectTemplate.relativePositionInRight``
   RandomDistribution -> RandomDistribution

``objectTemplate.relativePositionInUp``
   RandomDistribution -> RandomDistribution

``objectTemplate.relativePositionOffset``
   Vec3 -> Vec3

``objectTemplate.rememberExcessInput``
   bool -> bool

``objectTemplate.remoteEngineInput``
   int -> int

``objectTemplate.removeTemplate``
   int -> void

``objectTemplate.replaceItem``
   std::string -> void

   In the ``.con`` and ``.tweak``

``objectTemplate.respawnDelay``
   float -> float

   In the ``.con`` and ``.tweak``

``objectTemplate.restoreRotationOnExit``
   bool -> bool

``objectTemplate.restoreSpeed``
   float -> float

``objectTemplate.reverbLevel``
   float -> float

``objectTemplate.ropeScaleFactor``
   float -> float

``objectTemplate.rotateAsAnimatedUV``
   bool -> bool

``objectTemplate.rotateAsAnimatedUVObject``
   std::string -> std::string

``objectTemplate.rotateAsAnimatedUVReverse``
   bool -> bool

``objectTemplate.rotateUV``
   bool -> bool

``objectTemplate.rotation``
   float -> float

``objectTemplate.rotationalForce``
   Vec3 -> Vec3

``objectTemplate.rotationalSpeedInDof``
   RandomDistribution -> RandomDistribution

``objectTemplate.rotationalSpeedInRight``
   RandomDistribution -> RandomDistribution

``objectTemplate.rotationalSpeedInUp``
   RandomDistribution -> RandomDistribution

``objectTemplate.rotationAxle``
   int -> int

``objectTemplate.rotationGraph``
   Vec4 -> Vec4

``objectTemplate.rotationSpeed``
   Vec3 -> Vec3

``objectTemplate.rotationSpeed``
   float -> float

``objectTemplate.rotationSpeedMod``
   float -> float

``objectTemplate.rotationSpeedModBlur``
   float -> float

``ObjectTemplate.save``
   world::IObjectTemplate_ptrproxy -> bool

``ObjectTemplate.saveAll``
   -> bool

``objectTemplate.saveInSeparateFile``
   bool -> bool

``objectTemplate.scale``
   Vec3 -> Vec3

``objectTemplate.seatAnimationSystem``
   std::string -> std::string

   - In Vehicles ``.tweak``
   - Defines the location of the ``.inc`` animation file for the seat.
   - Example: ``Passenger.inc``

``objectTemplate.seatInformation``
   std::string Vec3 Vec3 -> void

``objectTemplate.seatLeftRotationLimit``
   float -> float

``objectTemplate.seatParent``
   std::string -> std::string

``objectTemplate.seatPosition``
   Vec3 -> Vec3

``objectTemplate.seatRightRotationLimit``
   float -> float

``objectTemplate.seatRotation``
   Vec3 -> Vec3

   - In Vehicles ``.tweak``
   - Allows the PCO to be rotated.
   - Uses X/Y/Z.
   - Relevant to Seat X Y Z Arrow.
   - See BF2Editor Vehicle for more info.
   - For example -10/0/0 wil rotate the player backwards.

``objectTemplate.secondaryProjectileTemplate``
   std::string -> std::string

``objectTemplate.seek.directionBonus``
   float -> float

``objectTemplate.seek.maxAngleLock``
   float -> float

``objectTemplate.seek.maxDistLock``
   float -> float

``objectTemplate.seek.reLockTime``
   float -> float

``objectTemplate.seek.targetType``
   TargetType -> TargetType

``objectTemplate.seek.trackingDelay``
   float -> float

``objectTemplate.selfLights``
   bool -> bool

``objectTemplate.selfShadowIntensity``
   float -> float

``objectTemplate.selfShadows``
   bool -> bool

``objectTemplate.setActiveTemplate``
   int -> void

``objectTemplate.setAIEnterOnSpawn``
   bool -> void

``objectTemplate.setAllowSpawnCloseToVehicle``
   bool -> void

``objectTemplate.setAnimationFrameHeightRelative``
   float -> void

``objectTemplate.setAnimationFrameWidthRelative``
   float -> void

``objectTemplate.setAxisFixation``
   Math::Vec3 -> void

``objectTemplate.setCollisionMesh``
   std::string -> void

``objectTemplate.setEnterOnSpawn``
   bool -> void

``objectTemplate.setExplodePartAtDestroy``
   bool -> void

``objectTemplate.setGearRatios``
   float float float -> void

``objectTemplate.setHasTarget``
   bool -> void

``objectTemplate.setHealth``
   int float float -> void

``objectTemplate.setHeatBarType``
   heatBarType -> void

``objectTemplate.setMinSpawnHeight``
   float -> void

``objectTemplate.setNumWindows``
   int -> void

``objectTemplate.setObjectTemplate``
   int std::string -> void

``objectTemplate.setOnlyForAI``
   bool -> void

``objectTemplate.setOnlyForHuman``
   bool -> void

``objectTemplate.setPosition``
   Math::Vec3 int -> void

``objectTemplate.setPositionalFixation``
   Math::Vec3 -> void

``objectTemplate.setRotation``
   Math::Vec3 int -> void

``objectTemplate.setScatterSpawnPositions``
   bool -> void

``objectTemplate.setSkeletonCollisionBone``
   std::string int Vec3 -> void

``objectTemplate.setSoldierExitLocation``
   Vec3 Vec3 -> void

``objectTemplate.setSpawnAsParaTroper``
   bool -> void

``objectTemplate.setSpawnDelay``
   float -> void

``objectTemplate.setSpawnPositionOffset``
   Math::Vec3 -> void

``objectTemplate.setSpawnPreventionDelay``
   float -> void

``objectTemplate.setSpawnRotation``
   Math::Vec3 -> void

``objectTemplate.setTeamGeometry``
   int std::string -> void

``objectTemplate.setToolTipType``
   dice::hfe::world::ToolTipType -> void

``objectTemplate.setVehicleType``
   dice::hfe::world::VehicleType -> void

``objectTemplate.shadowIntensity``
   float -> float

``objectTemplate.shakeFactor``
   float -> float

``objectTemplate.sharedStorageSize``
   float -> float

``objectTemplate.showInFirstPerson``
   bool -> bool

``objectTemplate.showInThirdPerson``
   bool -> bool

``objectTemplate.showOnMinimap``
   bool -> bool

``objectTemplate.signalTriggerId``
   int -> int

``objectTemplate.sinkingSpeedMod``
   float -> float

``objectTemplate.size``
   float -> float

``objectTemplate.size``
   RandomDistribution -> RandomDistribution

``objectTemplate.sizeGraph``
   Vec4 -> Vec4

``objectTemplate.sizeModifier``
   Vec3 -> Vec3

``objectTemplate.sizeModifierX``
   float -> float

``objectTemplate.sizeModifierY``
   float -> float

``objectTemplate.sizeModifierZ``
   float -> float

``objectTemplate.sizeOverTime``
   OverTimeDistribution -> OverTimeDistribution

``objectTemplate.skeleton``
   std::string -> void

``objectTemplate.skeleton1P``
   std::string -> void

``objectTemplate.skeleton3P``
   std::string -> void

``objectTemplate.snapToZeroOnNoInput``
   bool -> bool

``objectTemplate.softness``
   float -> float

``objectTemplate.soldierExitPosition``
   Vec3 -> Vec3

``objectTemplate.soldierExitRotation``
   Vec3 -> Vec3

``objectTemplate.sound.maxSoundsPerBurst``
   int -> int

``objectTemplate.sound.noisy``
   bool -> bool

``objectTemplate.soundFilename``
   std::string -> std::string

``objectTemplate.soundFilter``
   std::string -> std::string

``objectTemplate.soundIntensityFromAcceleration``
   Vec2 -> Vec2

``objectTemplate.soundIntensityFromAltitude``
   Vec2 -> Vec2

``objectTemplate.soundIntensityFromEngine``
   Vec2 -> Vec2

``objectTemplate.soundIntensityFromRotationalSpeed``
   Vec2 -> Vec2

``objectTemplate.soundIntensityFromSpeed``
   Vec2 -> Vec2

``objectTemplate.soundIntensityFromSpeedInDof``
   Vec2 -> Vec2

``objectTemplate.soundIntensityRange``
   Vec2 -> Vec2

``objectTemplate.soundIntensityUsed``
   bool -> bool

``objectTemplate.soundRadius``
   float -> float

``objectTemplate.spawnDelay``
   float -> void

``objectTemplate.spawnDelayAtStart``
   bool -> bool

``objectTemplate.spawnOffset``
   Vec3 -> Vec3

``objectTemplate.speccolor``
   Vec3ColorFloatIntensity -> Vec3ColorFloatIntensity

``objectTemplate.specialToggleWeaponInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.speed``
   float -> float

``objectTemplate.speedFromParticle``
   float -> float

``objectTemplate.speedFromPhysics``
   bool -> bool

``objectTemplate.spinWhenNoEngineInAir``
   float -> float

``objectTemplate.sprintDissipationTime``
   float -> float

``objectTemplate.sprintFactor``
   float -> float

``objectTemplate.sprintGear1Dampen``
   float -> float

``objectTemplate.sprintGear2Dampen``
   float -> float

``objectTemplate.sprintGear3Dampen``
   float -> float

``objectTemplate.sprintGear4Dampen``
   float -> float

``objectTemplate.sprintGear5Dampen``
   float -> float

``objectTemplate.sprintLimit``
   float -> float

``objectTemplate.sprintLossAtJump``
   float -> float

``objectTemplate.sprintRecoverTime``
   float -> float

``objectTemplate.sprintStaminaDissipationFactor``
   float -> float

``objectTemplate.startAgeFromAcceleration``
   Vec2 -> Vec2

``objectTemplate.startAgeFromAltitude``
   Vec2 -> Vec2

``objectTemplate.startAgeFromEngine``
   Vec2 -> Vec2

``objectTemplate.startAgeFromRotationalSpeed``
   Vec2 -> Vec2

``objectTemplate.startAgeFromSpeed``
   Vec2 -> Vec2

``objectTemplate.startAgeFromSpeedInDof``
   Vec2 -> Vec2

``objectTemplate.startAgeRange``
   Vec2 -> Vec2

``objectTemplate.startAgeUsed``
   bool -> bool

``objectTemplate.startAtCreation``
   bool -> bool

``objectTemplate.startAutoRotateOnEnter``
   bool -> bool

``objectTemplate.startDelay``
   float -> float

``objectTemplate.startDistance``
   float -> float

``objectTemplate.startLodPercentageOfLodDistance``
   float -> float

``objectTemplate.startOnEffects``
   int -> int

``objectTemplate.startProbability``
   float -> float

``objectTemplate.startRotation``
   RandomDistribution -> RandomDistribution

``objectTemplate.startTeam``
   int -> int

``objectTemplate.stopOnEffects``
   int -> int

``objectTemplate.stopType``
   int -> int

``objectTemplate.strategicObject.3dMapIcon``
   int -> int

``objectTemplate.strategicObject.destroyedIcon``
   std::string -> std::string

``objectTemplate.strategicObject.intactIcon``
   std::string -> std::string

``objectTemplate.strategicObject.isOnePiece``
   bool -> bool

``objectTemplate.strategicObject.part``
   int -> int

``objectTemplate.strategicObject.strategicObjectName``
   std::string -> std::string

``objectTemplate.strength``
   float -> float

``objectTemplate.supplyGroupId``
   int -> int

``objectTemplate.supplyGroupNeeded``
   int int bool -> void

``objectTemplate.supplyValueNeededTeam1``
   int -> int

``objectTemplate.supplyValueNeededTeam2``
   int -> int

``objectTemplate.supplyValueTeam1``
   int -> int

``objectTemplate.supplyValueTeam2``
   int -> int

``objectTemplate.supportsEmitter``
   bool -> bool

``objectTemplate.supportsGlow``
   bool -> bool

``objectTemplate.supportsPerPixel``
   bool -> bool

``objectTemplate.supportsPerVertex``
   bool -> bool

``objectTemplate.target.connectionEffect``
   std::string -> std::string

``objectTemplate.target.connectionEffectOnlyWhenZoomed``
   bool -> bool

``objectTemplate.target.disableFireWhenActiveMissile``
   bool -> bool

``objectTemplate.target.disableGuidanceOnReload``
   bool -> bool

``objectTemplate.target.lockAngle``
   float -> float

``objectTemplate.target.lockDelay``
   float -> float

``objectTemplate.target.loseLockDelay``
   float -> float

``objectTemplate.target.maxDistance``
   float -> float

``objectTemplate.target.maxVelocity``
   float -> float

``objectTemplate.target.minVelocity``
   float -> float

``objectTemplate.target.onLockChangeToWeapon``
   bool std::string -> void

``objectTemplate.target.sendVehicleLockWarning``
   bool -> bool

``objectTemplate.target.setTargetAtMaxDistance``
   bool -> bool

``objectTemplate.target.targetInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.target.targetObjectTemplate``
   std::string -> std::string

``objectTemplate.target.targetSystem``
   TargetSystem -> TargetSystem

``objectTemplate.target.updateInterval``
   float -> float

``objectTemplate.target.useCameraDirectionToTarget``
   bool -> bool

``objectTemplate.target.useDynamicVelocity``
   bool -> bool

``objectTemplate.target.velocityModifier``
   float -> float

``objectTemplate.targetType``
   TargetType -> TargetType

``objectTemplate.team``
   int -> int

``objectTemplate.team``
   U32 -> U32

``objectTemplate.team``
   int -> void

``objectTemplate.teamChange``
   bool -> bool

``objectTemplate.teamFromClosestCP``
   bool -> bool

``objectTemplate.teamOnVehicle``
   bool -> bool

``objectTemplate.template``
   std::string -> std::string

``objectTemplate.templateHasBeenUsed``
   bool -> bool

``objectTemplate.textureName``
   std::string -> std::string

``objectTemplate.textureOffsetVelocity``
   float -> float

``objectTemplate.textureTileFactor``
   float -> float

``objectTemplate.throwStrength``
   float -> float

``objectTemplate.throwStrength2``
   float -> float

``objectTemplate.Timeout``
   float -> float

``objectTemplate.timeToGetControl``
   float -> float

``objectTemplate.timeToLive``
   RandomDistribution -> RandomDistribution

``objectTemplate.timeToLive``
   float -> float

``objectTemplate.timeToLiveAfterDeath``
   float -> float

``objectTemplate.timeToLoseControl``
   float -> float

``objectTemplate.timeToRemoveTK``
   float -> float

``objectTemplate.toggleMouseLook``
   bool -> bool

``objectTemplate.toggleWeapon``
   bool -> bool

``objectTemplate.tolerance``
   float -> float

``objectTemplate.torque``
   float -> float

``objectTemplate.tracerConvergeDistance``
   float -> float

   - Used in Projectiles (Weapons)
   - “At what distance the tracers (which start from the gunbarrel) and the projectile which start from the camera converges.
   - Only relevant if ``FireInCameraDof`` is checked.

``objectTemplate.tracerInterval``
   int -> int

   - Used in Projectiles (Weapons)
   - Set one for tracer on every shot, 2 for every other, and so on.

``objectTemplate.tracerScaler``
   float -> float

   - Used in Projectiles (Weapons)
   - How long the tracer effect will be as default.

``objectTemplate.tracerSizeModifier``
   float -> float

   - Used in Projectiles (Weapons)
   - How fat the tracer will be.

``objectTemplate.tracerTemplate``
   std::string -> std::string

``objectTemplate.trackTurnAcceleration``
   float -> float

``objectTemplate.trackTurnHighAmplitude``
   float -> float

``objectTemplate.trackTurnHighOffset``
   float -> float

``objectTemplate.trackTurnLowAmplitude``
   float -> float

``objectTemplate.trackTurnLowOffset``
   float -> float

``objectTemplate.trackTurnSpeed``
   float -> float

``objectTemplate.trailEffectTemplate``
   std::string -> std::string

``objectTemplate.Transparency``
   RandomDistribution -> RandomDistribution

``objectTemplate.transparencyGraph``
   Vec4 -> Vec4

``objectTemplate.treeCollisionDiameter``
   float -> float

``objectTemplate.triggerForEachActivatingPlayer``
   bool -> bool

``objectTemplate.triggerId``
   int -> int

``objectTemplate.triggerRadius``
   float -> float

``objectTemplate.turnVelocity``
   float -> float

``ObjectTemplate.type``
   world::IObjectTemplate_ptrproxy -> std::string

``objectTemplate.type``
   int -> int

``objectTemplate.uavVehicleFlightHeight``
   float -> float

``objectTemplate.uavVehicleRadius``
   float -> float

``objectTemplate.uavVehicleSampleResolution``
   float -> float

``objectTemplate.uavVehicleSpeed``
   float -> float

``objectTemplate.uavVehicleTemplate``
   std::string -> std::string

``objectTemplate.unableToChangeTeam``
   bool -> bool

``objectTemplate.unlockIndex``
   int -> int

``objectTemplate.unlockLevel``
   int -> int

``ObjectTemplate.update``
   world::IObjectTemplate_ptrproxy -> void

``ObjectTemplate.updateAll``
   -> void

``objectTemplate.upDropBoost``
   float -> float

``objectTemplate.upThrowBoost``
   float -> float

``objectTemplate.upThrowBoost2``
   float -> float

``objectTemplate.useAbsoluteDirection``
   bool -> bool

``objectTemplate.useButtonRadius``
   float -> float

``objectTemplate.useCameraOrientation``
   bool -> bool

``objectTemplate.usedByAi``
   bool -> bool

``objectTemplate.useDeAcceleration``
   bool -> bool

``objectTemplate.usedOnTransparentMaterials``
   bool -> bool

``objectTemplate.usedOnTransparentSurface``
   bool -> bool

``objectTemplate.useGeomPart``
   int -> int

``objectTemplate.useProjectileCamera``
   bool -> bool

``objectTemplate.vehicleCameraShake``
   CameraShakeTriggers -> CameraShakeTriggers

``objectTemplate.vehicleCategory``
   dice::hfe::world::VehicleCategory -> dice::hfe::world::VehicleCategory

``objectTemplate.vehicleFov``
   float -> float

``objectTemplate.vehicleHud.AbilityIcon``
   std::string -> std::string

``objectTemplate.vehicleHud.addAbilityIcon``
   std::string -> void

``objectTemplate.vehicleHud.addShowOnCamMode``
   int -> void

``objectTemplate.vehicleHud.addVehicleIcon``
   std::string -> void

``objectTemplate.vehicleHud.disableOnSprint``
   bool -> bool

``objectTemplate.vehicleHud.displaySelectionOnEnter``
   bool -> bool

``objectTemplate.vehicleHud.enablePostProcessingOnGuiIndex``
   bool -> bool

``objectTemplate.vehicleHud.getShowOnCamMode``
   int -> bool

``objectTemplate.vehicleHud.guiIndex``
   int -> int

   - Vehicles and Weapons ``.tweak``
   - Defines the Vehicle General User Inferface Index to use like the Blackhawk green HUD.
   - Gui Index is located in the ``.con``\ s of ``menu\HUD\HudSetup\Vehicles``

``objectTemplate.vehicleHud.hasTurretIcon``
   bool -> bool

``objectTemplate.vehicleHud.hudName``
   std::string -> std::string

``objectTemplate.vehicleHud.injurySound``
   std::string -> std::string

``objectTemplate.vehicleHud.isCoDriver``
   bool -> bool

``objectTemplate.vehicleHud.maxClimbSpeed``
   int -> int

``objectTemplate.vehicleHud.miniMapIcon``
   std::string -> std::string

``objectTemplate.vehicleHud.miniMapIconLeaderSize``
   std::string -> std::string

``objectTemplate.vehicleHud.miniMapIconSize``
   int -> int

``objectTemplate.vehicleHud.pantingSound``
   std::string -> std::string

``objectTemplate.vehicleHud.showCrossHair``
   bool -> bool

``objectTemplate.vehicleHud.showInfo``
   bool -> bool

``objectTemplate.vehicleHud.showOnCamMode``
   int -> int

``objectTemplate.vehicleHud.spottedIcon``
   std::string -> std::string

``objectTemplate.vehicleHud.spottedIconSize``
   int -> int

``objectTemplate.vehicleHud.standardHelpEnabled``
   bool -> bool

``objectTemplate.vehicleHud.typeIcon``
   std::string -> std::string

``objectTemplate.vehicleHud.useChildHud``
   bool -> bool

``objectTemplate.vehicleHud.usePlayerIcon``
   bool -> bool

``objectTemplate.vehicleHud.useSelectionIcons``
   bool -> bool

``objectTemplate.vehicleHud.useVehicleCommRose``
   bool -> bool

``objectTemplate.vehicleHud.vehicleIcon``
   std::string -> std::string

``objectTemplate.vehicleHud.vehicleIconPos``
   Vec2 -> Vec2

``objectTemplate.vehicleHud.vehicleType``
   int -> int

``objectTemplate.velocity``
   float -> float

   - Used in ``GenericFirearms`` (Weapons, Projectiles)
   - The speed of the projectile measured in Rate of Fire (ROF)
   - Lower ROF are affected by gravity/bullet drop while higher ones fire with lower bullet drop”

``objectTemplate.visibleOn3dMap``
   bool -> bool

``objectTemplate.volume``
   float -> float

   The loudness of the sound.

``objectTemplate.volumeEnvelope``
   std::string -> std::string

``objectTemplate.volumeGroup``
   int -> int

``objectTemplate.warningHud.firstWarningSound``
   std::string -> std::string

   - Used in Vehicle ``.tweak``
   - Defines the 1st warning sound when getting locked onto.
   - Uses the file path pointing to a ``.wav`` or an ``.ogg`` file along with usual sound configuration code. *Beep Beep Beep*

``objectTemplate.warningHud.secondWarningSound``
   std::string -> std::string

   - Used in Vehicle ``.tweak``
   - Defines the 2nd warning sound when getting locked onto.
   - Uses the file path pointing to a ``.wav`` or an ``.ogg`` file along with usual sound configuration code. *Beeeeeeeeeeep*

``objectTemplate.warningHud.warningIcon``
   std::string -> std::string

   - Used in Vehicle ``.tweak``
   - Defines the location of the warning icon.
   - Example: ``ObjectTemplate.WarningHud.warningIcon Ingame\GeneralIcons\Action_Icons\mylaserlockicon.tga``

``objectTemplate.warningHud.warningType``
   int -> int

``objectTemplate.waterHeight``
   float -> float

``objectTemplate.waterSurfaceOffset``
   float -> float

``objectTemplate.weaponHud.addShowOnCamMode``
   int -> void

``objectTemplate.weaponHud.altCrosshairIcon``
   std::string -> std::string

``objectTemplate.weaponHud.altGuiIndex``
   int -> int

``objectTemplate.weaponHud.altWeaponIcon``
   std::string -> std::string

``objectTemplate.weaponHud.ammoBarBackIcon``
   std::string -> std::string

``objectTemplate.weaponHud.ammoBarFrontIcon``
   std::string -> std::string

``objectTemplate.weaponHud.ammoIcon``
   std::string -> std::string

``objectTemplate.weaponHud.clipIcon``
   std::string -> std::string

``objectTemplate.weaponHud.crosshairIcon``
   std::string -> std::string

``objectTemplate.weaponHud.crosshairIconSize``
   int -> int

``objectTemplate.weaponHud.deviationFactor``
   int -> int

``objectTemplate.weaponHud.disableOnSprint``
   bool -> bool

   - Used in Weapons and Vehicle ``.tweak``

``objectTemplate.weaponHud.displaySelectOnActivation``
   bool -> bool

``objectTemplate.weaponHud.enableMouse``
   bool -> bool

``objectTemplate.weaponHud.enablePostProcessingOnGuiIndex``
   int -> int

   - Used in Weapons and Vehicle ``.tweak``
   - Makes the GuiIndex have a black and white effect
   - Use with all ``objectTemplate.postProcess.tv`` code to adjust the TV effect

``objectTemplate.weaponHud.firstLockSound``
   std::string -> std::string

   The first lock sound that plays when there is a lock in progress on the jet

``objectTemplate.weaponHud.getShowOnCamMode``
   int -> bool

``objectTemplate.weaponHud.guiIndex``
   int -> int

   - Used in Weapons and Vehicle ``.tweak``
   - Defines the Weapon General User Inferface Index to use like the repair bar
   - Gui Index is located in the ``.con``\ s of ``menu\HUD\HudSetup\Vehicles``

``objectTemplate.weaponHud.hasFireRate``
   bool -> bool

   Used in Weapons and Vehicle ``.tweak``

``objectTemplate.weaponHud.hasMag``
   bool -> bool

``objectTemplate.weaponHud.hasRangeFinder``
   bool -> bool

``objectTemplate.weaponHud.hudName``
   std::string -> std::string

``objectTemplate.weaponHud.maxVisualDeviation``
   int -> int

``objectTemplate.weaponHud.minVisualDeviation``
   int -> int

``objectTemplate.weaponHud.overheatSound``
   std::string -> std::string

   - Used in Weapons and Vehicle ``.tweak``
   - For the overheat sound. Adding it makes the engine reference the std::string defined with MenuSound.con.

      - Usually it's ``S_Weapon_Handheld_Overheat``
      - ``S_Vehicle_Handheld_Overheat`` but can be anything and custom ones can be used if needed

``objectTemplate.weaponHud.secondLockSound``
   std::string -> std::string

   - Used in Weapons and Vehicle ``.tweak``
   - The second lock sound that plays when the lock has been set

``objectTemplate.weaponHud.selectIcon``
   std::string -> std::string

``objectTemplate.weaponHud.showAmmo``
   bool -> bool

``objectTemplate.weaponHud.ShowClips``
   bool -> bool

``objectTemplate.weaponHud.showInfo``
   bool -> bool

``objectTemplate.weaponHud.showOnCamMode``
   int -> int

``objectTemplate.weaponHud.specialAbilityIcon``
   std::string -> std::string

``objectTemplate.weaponHud.switchGuiOnCamera``
   bool -> bool

``objectTemplate.weaponHud.weaponIcon``
   std::string -> std::string

``objectTemplate.weaponType``
   int -> int

``objectTemplate.widnBlowTime``
   float -> float

``objectTemplate.windAffectionFactor``
   float -> float

``objectTemplate.windAgingFactor``
   float -> float

``objectTemplate.windBlowTime``
   float -> float

``objectTemplate.windDirection``
   Vec3 -> Vec3

``objectTemplate.windFalloff``
   float -> float

``objectTemplate.windIsDynamic``
   bool -> bool

``objectTemplate.windowSizeVector``
   Vec3 -> Vec3

   “Used in Projectiles, Vehicles, Effect

``objectTemplate.windRadialFalloff``
   float -> float

``objectTemplate.windSpeed``
   float -> float

``objectTemplate.windSpeedAgeDistance``
   float -> float

``objectTemplate.windType``
   std::string -> std::string

``objectTemplate.wingLift``
   float -> float

   - Planes and Helis
   - How much speed will affect object lifting on control surface.

``objectTemplate.wingToRegulatorRatio``
   float -> float

``objectTemplate.workOnSoldiers``
   bool -> bool

   - Supply Objects
   - Allows the soldier to receive HP/Ammo depending on the type of supply set

``objectTemplate.workOnVehicles``
   bool -> bool

   - Supply Objects
   - Allows the vehicle to receive HP/Ammo depending on the type of supply set

``objectTemplate.worldFOV``
   float -> float

``objectTemplate.writeBinary``
   std::string -> void

``objectTemplate.writeZ``
   bool -> bool

``objectTemplate.yawSpeed``
   float -> float

``objectTemplate.ziplineSoldierHeight``
   float -> float

``objectTemplate.zoom.addZoomFactor``
   float -> void

``objectTemplate.zoom.allowUntoggledFire``
   bool -> bool

``objectTemplate.zoom.changeCameraId``
   int -> int

``objectTemplate.zoom.changeCameraViewMode``
   CameraViewMode -> CameraViewMode

``objectTemplate.zoom.changeFovDelay``
   float -> float

``objectTemplate.zoom.disableMuzzleWhenZoomed``
   bool -> bool

``objectTemplate.zoom.mouseSpeedMod``
   float -> float

``objectTemplate.zoom.onlyZoomWhenProne``
   bool -> bool

``objectTemplate.zoom.startCameraId``
   int -> int

``objectTemplate.zoom.startCameraViewMode``
   CameraViewMode -> CameraViewMode

``objectTemplate.zoom.useProjectileCamera``
   bool -> bool

``objectTemplate.zoom.zoomDelay``
   float -> float

``objectTemplate.zoom.zoomInput``
   io::PlayerInputMap -> io::PlayerInputMap

``objectTemplate.zoom.zoomLod``
   int -> int

``objectTemplate.zoom.zoomOutAfterFire``
   bool -> bool

``objectTemplate.zRotation``
   RandomDistribution -> RandomDistribution

``objectTemplate.zRotationSnap``
   float -> float