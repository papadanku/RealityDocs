
How to Manually Fix Ambient Objects
===================================

This is a guide on how to format and fix your Ambient Objects manually. It's recommended to first use the BF2Editor to load your level to look at the debugger logs.

The 3 things that need to be created in order are:

    #. Trigger
        Creates the settings of a player triggered radius where a player can fire, move, time (wait), or explode an area to trigger the ambient effect. Marked as blue in the editor.

    #. Ambient Effect
        Defines the effect properties of the Trigger. Must have _AmbientEffect attached to the trigger name. Marked as red in the editor.

    #. Ambient Sounds (Or Ambient Sound Effects)
        Defines the atmospheric sounds that will play on all parts of the map, and even in certain parts like in a creek environment. Marked as green in the editor.

1. ``Trigger``
--------------

``ObjectTemplate.create Trigger [Object] -> object.Create``
    The purpose of ``ObjectTemplate.create Trigger`` is to define the Trigger ID, and the properties of the soldier trigger.
``objectTemplate.triggerId (int -> int)``
    The trigger identification number created in the game. Must be defined in the Trigger and the ``[Object]_AmbientObject``. The same number can be used for an ``_AmbientObject`` to trigger another effect as long as the naming is the same. For example: Sandstorm -> ``Sandstorm_AmbientObject_1``, ``Sandstorm_AmbientObject_2``.
``objectTemplate.radius (float -> float)``
    The dome to detect the soldiers collision and execute the ``AmbientEffectArea`` which can be viewed in the BF2Editor.
``objectTemplate.events (int -> int)``
    The command in which the ``Trigger`` Type number is entered. See ``Trigger`` Types.
``objectTemplate.averageTimeBetweenTests (float -> float)``
    The time the effect lasts for. Used primarily for sound effects like dogs. Value must be a minimum of ``1``.
``objectTemplate.chance (float -> float)``
    The chance of the effect being played. It ranges from ``0`` to ``1``, with ``1`` being always, and ``0`` being never. Setting it to ``0.5`` makes the effect have a five in ``10`` chance to play.
``objectTemplate.minimumTimeBetweenTriggering (float -> float)``
    After an effect plays, the number of seconds needed for the effect to recharge again.
``objectTemplate.create``
    The effect position, used for both the ``Trigger`` and ``AmbientObject``. Use the BF2Editor to set the effect.

Trigger Types
-------------

The type of trigger. There are 4 types, and in ``ObjectTemplate.events``, add the following numbers (inside ``[]``)
    :Time [1]: When the time is defined, the trigger will play independently to the value set in ``ObjectTemplate.time`` (seconds)
    :Fire [2]: When someone is in the radius, and someone fires, the trigger will play.
    :Move [4]: When someone moves to the radius.
    :Explosion [8]: When an explosion happens in the radius.

    You can also use multiple numbers ones, such as ``14`` (Time and Move) i.e. ``ObjectTemplate.event 128`` (Time, Fire, Explosion)

After the Trigger is defined, the object needs to be created with Object.create using the same name to be placed on the map. It uses the absolute position, rotation and the layer the trigger is for.

.. code-block::
    :caption: Example

    rem [TriggerTemplate: Trigger_birds1]
    rem *********** TriggerTrigger ***********
    rem [TriggerTemplate: Trigger_birds1]
    ObjectTemplate.create Trigger Trigger_birds1
    ObjectTemplate.activeSafe Trigger Trigger_birds1
    ObjectTemplate.modifiedByUser esj
    ObjectTemplate.isNotSaveable 1
    ObjectTemplate.hasMobilePhysics 0
    ObjectTemplate.triggerId 1
    ObjectTemplate.radius 30
    ObjectTemplate.events 10
    ObjectTemplate.averageTimeBetweenTests 1
    ObjectTemplate.chance 0.5
    ObjectTemplate.minimumTimeBetweenTriggering 30

       rem [Trigger: Trigger_birds1]
       Object.create Trigger_birds1
       Object.absolutePosition 82.964/153.389/-19.101
       Object.rotation 0.000/0.000/0.000
       Object.layer 1

2. ``AmbientEffectArea``
------------------------

``ObjectTemplate.create AmbientEffectArea [Object]_AmbientEffect_# (Where # is the number in order)``, ``object.Create``
    The purpose of ``AmbientEffectArea`` is to define the radius of the effect, what effect is used, the properties of the effect.
``objectTemplate.numNetworkedEffects``
    For a trigger that plays multiple effects at once.
``objectTemplate.projectOnHeightmap``
    Makes the effect come off the ground. Set with 1. If 0, the effect will play relative to the position of the effect (Default).

``objectTemplate.playAtEventPosition``

``objectTemplate.playAtPlayerPosition``

``objectTemplate.radius (float -> float)``
    The dome that stops the effect once it reaches the boundaries. (I think).
``objectTemplate.linkedEffectContainer (std::string -> std::string)``
    The effect that will play when a soldier triggers the radius of the ``AmbientEffectArea`` i.e. ``e_dAmb_bird``.

.. note::

    ``AmbientEffects`` must have the ``_AmbientEffect`` line added otherwise it won't work. Best way to add it is to search for the effect, and replace with the effect name and the ``_AmbientEffect``.

    It uses the same Trigger ID as the Trigger Trigger.

After the ``AmbientEffectArea`` is defined, the object needs to be created with ``Object.create`` using the same name to be placed on the map. You can use the same ``Object.create`` coordinates as the trigger.

It uses the absolute position, rotation and the layer the trigger is for.

.. code-block::
    :caption: Example

    rem ********** AmbientEffectArea **********
    rem TriggerID needs to be the same as the TriggerTrigger
    rem [AmbientEffectAreaTemplate: Trigger_birds1_AmbientEffect_1]
    ObjectTemplate.create AmbientEffectArea Trigger_birds1_AmbientEffect_1
    ObjectTemplate.activeSafe AmbientEffectArea Trigger_birds1_AmbientEffect_1
    ObjectTemplate.modifiedByUser esj
    ObjectTemplate.isNotSaveable 1
    ObjectTemplate.hasMobilePhysics 0
    ObjectTemplate.radius 2
    ObjectTemplate.triggerId 1
    ObjectTemplate.numNetworkedEffects 1
    ObjectTemplate.projectOnHeightmap 0
    ObjectTemplate.linkedEffectContainer e_dAmb_bird

       rem [AmbientEffectArea: Trigger_birds1_AmbientEffect_1]
       Object.create Trigger_birds1_AmbientEffect_1
       Object.absolutePosition 83.191/159.486/-19.643
       Object.rotation 0.000/0.000/0.000
       Object.layer 1

3. AmbientSounds
----------------

``ObjectTemplate.create Sound S_``, ``ObjectTemplate.activeSafe Sound S_``, ``Sound.addTrigger S_``, ``Object.create S_``
    The purpose of Ambient Sounds is to define both the sound effects to play throughout the map, like a wind or rain sound and the sound to play at specific areas.
``objectTemplate.lowSamples (int -> int)``
    The low sample audio bitrate. Shouldn't be touched.
``objectTemplate.mediumSamples (int -> int)``
    The medium sample audio bitrate. Shouldn't be touched.
``objectTemplate.soundFilename (std::string -> std::string)``
    The filepath of the sound. The BF2Editor is useful for finding these.
``objectTemplate.loopCount (int -> int)``
    :0: Endless loops
    :1: Play once
    :2: Play twice and so on

    The number of loops of the song.
``objectTemplate.is3dSound (bool -> bool)``
    Only enable this if the sound file is mono, and it needs to be played in both speakers. If it is enabled for a stereo sound file, the sound will play all over the map.
``objectTemplate.volume (float -> float)``
    Sets the volume of the sound.
``objectTemplate.pan (float -> float)``
    :0: Left
    :1: Right

    Default is 0.5. The value at which the sound will be directed to the left or right speaker.
``objectTemplate.reverbLevel (float -> float)``
    Default is 0. Reverberation level is set between 0 and 1.
``objectTemplate.pitch (float -> float)``
    Sets the pitch of the sound. Default is 1 for normal pitch.
``objectTemplate.minDistance (float -> float)``
    The minimum distance of the sound to be heard from the set position. Needs to be set otherwise the sound will not play.
``objectTemplate.soundRadius (float -> float)``
    The radius in which the sound will start playing when a player moves inside. Needs to be set along with minDistance.
``objectTemplate.stopType (int -> int)``
    (stopType 0, 1, 2). Recommended: Set to 0 for ambient weather sounds and large areas. These sounds are in the ``common/sound/levelambients`` folder outside of Objects. The sound will play again and overlap each other when entering and exiting the radius. Set to 1 for ambient sound effects like chimes, birds, swamp creeks, anything.
``objectTemplate.position (Vec3 -> Vec3)``
    The position of the sound effect. Must be the same value as the ``ObjectTemplate.absolutePosition`` set in ``Object.create``.

.. code-block::
    :caption: Example

    rem ************ AmbientSounds ************
    Below is the global ambient sound played throughout the level:
    rem [SoundObjectTemplate: S_GlobalAmbient]
    ObjectTemplate.create Sound S_GlobalAmbient
    ObjectTemplate.activeSafe Sound S_GlobalAmbient
    ObjectTemplate.modifiedByUser esj
    ObjectTemplate.lowSamples 2147483647
    ObjectTemplate.mediumSamples 2147483647
    ObjectTemplate.soundFilename "common/sound/levelambients/dalian_plant/dalian_plant_global_ambience.ogg"
    ObjectTemplate.loopCount 0
    ObjectTemplate.is3dSound 0
    ObjectTemplate.stopType 0
    ObjectTemplate.volume 0.74
    ObjectTemplate.pitch 1
    ObjectTemplate.pan 0.5
    ObjectTemplate.reverbLevel 0
    ObjectTemplate.minDistance 300000

    Sound.addTrigger S_GlobalAmbient

.. code-block::
    :caption: Ambient sound played at a specific position

    rem [SoundObjectTemplate: S_Carrier_Ambience_1]
    ObjectTemplate.create Sound S_Carrier_Ambience_1
    ObjectTemplate.activeSafe Sound S_Carrier_Ambience_1
    ObjectTemplate.modifiedByUser esj
    ObjectTemplate.isNotSaveable 1
    ObjectTemplate.lowSamples 2147483647
    ObjectTemplate.mediumSamples 2147483647
    ObjectTemplate.soundFilename "common/sound/levelambients/gulf_of_oman/carrier_ambient.ogg"
    ObjectTemplate.loopCount 0
    ObjectTemplate.is3dSound 0
    ObjectTemplate.stopType 0
    ObjectTemplate.volume 1
    ObjectTemplate.pitch 1
    ObjectTemplate.pan 0.5
    ObjectTemplate.reverbLevel 0
    ObjectTemplate.position 776.031/155.718/77.343
    ObjectTemplate.minDistance 50

    Sound.addTrigger S_Carrier_Ambience_1

    Object.create S_Carrier_Ambience_1
    Object.absolutePosition 776.031/155.718/77.343
    Object.rotation 0.000/0.000/0.000
    Object.layer 1

And that's it! To test in-game:

#. Edit the ``AmbientObject.con`` in ``server.zip``
#. Change ``ObjectTemplate.chance`` value to ``1``, ``ObjectTemplate.minimumTimeBetweenTriggering`` to ``0``
#. Open up the BF2Editor first, switch to :guilabel:`LevelEditor`, and go to :menuselection:`File --> Load`

After loading,

#. Go to the resources bar and open :guilabel:`Ambient`
#. Go to :guilabel:`AmbientTrigger`, click on the sub-folder and click on each effect
#. On the right, under level settings, there's the :guilabel:`Minimap` section
#. Click on :guilabel:`Show`. Then load the level up in-game, and test each `AmbientEffect` pointed out in the Editor

After clicking on a new trigger, you may need to move the camera for the position in the minimap to update each time though.

Hope this helps!
