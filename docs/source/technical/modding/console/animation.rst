
``Animation``
=============

``AnimationBundle``
-------------------

``animationBundle.abruptPlayback``
   bool -> bool

``animationBundle.addAnimation``
   std::string -> void

``animationBundle.addEvent``
   std::string -> void

``animationBundle.fadeInTime``
   float -> float

   :Used in: AnimationSystem1p and 3p :file:`.inc` files
   :Fade-in: Animation Start. Allows a smooth transition between animations.

      - The lower it is, the quicker it is.
      - A high value makes the transition slower and longer.
      - Fade in 0.01.

   :Example: Idle/Walking to Sprinting

``animationBundle.fadeOutTime``
   float -> float

   :Used in: AnimationSystem1p and 3p :file:`.inc` files
   :Fade out: Animation End.

      - Same as above, Fadeout ``0.1``.
      - Fadeout ``0.4`` would make it take ``0.4`` seconds to finish an animation

   :Example: From Sprinting to Walk/Idle

``animationBundle.getAnimationLength``
   std::string -> float

``animationBundle.getAnimationStartTime``
   std::string -> float

``animationBundle.getEventStartTime``
   std::string -> float

``animationBundle.isLooping``
   bool -> bool

``animationBundle.jumpToLastAnimationAtStop``
   bool -> bool

``animationBundle.length``
   float -> float

``animationBundle.listAnimations``
   -> std::string

``animationBundle.listEvents``
   -> std::string

``animationBundle.playBackward``
   bool -> bool

``animationBundle.playForever``
   bool -> bool

``animationBundle.removeAnimation``
   std::string -> void

``animationBundle.removeEvent``
   std::string -> void

``animationBundle.setAnimationLength``
   std::string float -> void

``animationBundle.setAnimationStartTime``
   std::string float -> void

``animationBundle.setEventStartTime``
   std::string float -> void

``animationBundle.useSpeedAsTime``
   bool -> bool

``AnimationManager``
--------------------

``animationManager.fadeInTime``
   float -> float

``animationManager.ignoreMotherOrientation``
   int -> int

``animationManager.length``
   float -> float

   :Description: The length of the animation. Must match up with ``ObjectTemplate.ammo.reloadTime`` to sync.
   :Used in: “AnimationSystem1p, AnimationSystem3p.inc”
   :Lower value: Animation will be sped up.
   :Higher value: Animation will be slowed down.

``animationManager.looping``
   bool -> bool

   :Used in: “AnimationSystem1p, AnimationSystem3p.inc”

``animationManager.noiceAmplitude``
   float -> float

``animationManager.noiceFreq``
   int -> int

``animationManager.originalLength``
   -> float

``AnimationSystem``
-------------------

``animationSystem.activestd::string``
   -> std::string

``animationSystem.activeAnimation``
   std::string -> std::string

``animationSystem.activeBundle``
   std::string -> std::string

``animationSystem.activeTrigger``
   std::string -> std::string

``animationSystem.activeValueHolder``
   std::string -> std::string

``animationSystem.cameraSpring.amplitude``
   Vec3 -> Vec3

``animationSystem.cameraSpring.fire``
   Vec3 -> Vec3

``animationSystem.cameraSpring.hit``
   Vec3 -> Vec3

``animationSystem.cameraSpring.look``
   Vec2 -> Vec2

``animationSystem.cameraSpring.move``
   Vec3 -> Vec3

``animationSystem.cameraSpring.stiffness``
   Vec3 -> Vec3

``animationSystem.cameraSpring.use``
   bool -> bool

``animationSystem.cameraSpring.zoomDamping``
   Vec3 -> Vec3

``animationSystem.create``
   std::string -> void

``animationSystem.createAnimation``
   std::string -> anim.BoneAnimation\*

``animationSystem.createBundle``
   std::string -> anim.Bundle\*

``animationSystem.createTrigger``
   std::string std::string -> anim.Trigger\*

``animationSystem.createValueHolder``
   std::string -> void

``animationSystem.deleteActiveBundle``
   -> void

``animationSystem.deleteActiveTrigger``
   -> void

``animationSystem.hide``
   -> void

``animationSystem.list``
   -> std::string

``animationSystem.listAnimations``
   -> std::string

``animationSystem.listBundles``
   -> std::string

``animationSystem.listTriggers``
   -> std::string

``AnimationSystem.listTriggerTypes``
   -> std::string

``animationSystem.listValueHolders``
   -> std::string

``animationSystem.playbackModifier``
   float -> float

``animationSystem.reloadScript``
   -> void

``animationSystem.save``
   std::string -> void

``animationSystem.saveActive``
   -> void

``animationSystem.saveValueHolders``
   -> void

``animationTrigger``
--------------------

``animationTrigger.addBundle``
   std::string -> void

``animationTrigger.addChild``
   std::string -> void

``animationTrigger.clearValueHolder``
   -> void

``animationTrigger.fadeInTime``
   float -> float

``animationTrigger.getTypeName``
   -> std::string

``animationTrigger.idleTime``
   Vec2 -> Vec2

``animationTrigger.listBundles``
   -> std::string

``animationTrigger.message``
   int -> int

``animationTrigger.removeBundle``
   std::string -> void

``animationTrigger.removeChild``
   std::string -> void

``animationTrigger.triggerOnAcceleration``
   bool -> bool

``animationTrigger.useDirection``
   bool -> bool

``animationTrigger.valueHolder``
   std::string -> std::string

``animationValueHolder``
------------------------

``animationValueHolder.getFilename``
   -> std::string

``animationValueHolder.max``
   float -> float

``animationValueHolder.min``
   float -> float

``animationValueHolder.normal``
   float -> float

``animationValueHolder.passOnMessage``
   unsigned int -> unsigned int

``animationValueHolder.stopOnMessage``
   unsigned int -> unsigned int

``animationValueHolder.values``
   float float float -> void