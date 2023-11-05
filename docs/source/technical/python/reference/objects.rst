
BF2 Objects
===========

.. _physicalobject:

``PhysicalObject``
------------------

``PhysicalObject`` represent physical things in the BF2 game world; as such, they have the properties of real objects in the physical world: properties like position (X, Y, Z coordinates) and orientation (rotation), and can contain, and be contained by, other ``PhysicalObject`` objects. A ``PhysicalObject`` appears to be implemented as C++ objects in the game engine which the embedded Python engine has access to, but since they are game engine objects, they are not defined anywhere in Python, and cannot be created directly in Python - but they can be accessed from Python. No special imports are necessary to manipulate these objects.

Please note that since these are not native Python objects, we don't know what they are actually named inside the game engine; ``PhysicalObject``, as well as the names of other types of objects that inherit from that class, are made up for convienience. We also can't see into the game engine code to see if the hierarchial structure of these classes is what is presented here - for example, ``VehicleObject`` and ``SoldierObject`` may, in fact, be a single class; the hierarchy of ``PhysicalObject``'s decendents given here should nevertheless be equivalent to whatever the real hierarchy is.

Methods
~~~~~~~

-  ``physicalObject.isValid()``

-  ``physicalObject.getTemplateProperty()``

-  ``physicalObject.getPosition()``

-  ``physicalObject.setPosition( (X, Y, Z) )``

-  ``physicalObject.getRotation()``

-  ``physicalObject.setRotation( (A, B, C) )``

-  ``physicalObject.getParent()``

   Returns ``PhysicalObject`` that contains this instance, if any.

-  ``physicalObject.getChildren()``

   Returns a tuple of multiple ``PhysicalObject`` contained by this instance

For information about the coordinate system used by the Position and Rotation methods, see the page on :doc:`BF2 Coordinates <../../engine/coordinates>`.

The known properties available via the ``getTemplateProperty`` method are:

-  ``radius``

   For control points only.

-  ``ControlPointID``

   For control points only.

Attributes
~~~~~~~~~~

-  ``physicalObject.templateName``
-  ``physicalObject.isControlPoint``
-  ``physicalObject.isPlayerControlObject``
-  ``physicalObject.hasArmor``
-  ``physicalObject.token``

.. _weaponobject:

``WeaponObject``
----------------

A ``WeaponObject`` is used to represent a weapon in BF2. The ``WeaponObject`` class inherits the methods and attributes of ``physicalObject``, with no additonal methods or attributes.

.. _kitobject:

``KitObject``
-------------

A ``KitObject`` is used to represent a “kit” in BF2. The ``KitObject`` class inherits the methods and attributes of ``physicalObject``, with no additonal methods or attributes.

.. _controlpointobject:

``ControlPointObject``
----------------------

A ``ControlPointObject`` is used to represent a control point in BF2. The ``ControlPointObject`` class inherits the methods and attributes of ``physicalObject``, with the following additional methods and attributes:

-  ``ControlPointObject.cp_getParam('parameter')``
-  ``ControlPointObject.cp_setParam('parameter', value)``

Attributes
~~~~~~~~~~

-  ``ControlPointObject.flagPosition``

   Returns:

   -  ``0`` = top
   -  ``1`` = middle
   -  ``2`` = bottom

-  ``ControlPointObject.lastAttackingTeam``

-  ``ControlPointObject.triggerId``

Internal Properties
~~~~~~~~~~~~~~~~~~~

``ControlPointObject`` also have a number of internal properties that are accessed through the ``cp_getParam`` and ``cp_setParam`` methods:

-  ``isHemisphere``

   0 or 1, indicating if the control point capture area is a hemisphere or not.

-  ``team``

   Team the capture point belongs to: 0 for neutral, 1 for team 1, and 2 for team 2. Updating this value also changes the minimap and flag tag indicator.

-  ``flag``

   The flag image used in the control point; 1 for team 1's flag, 2 for team 2's.

-  ``areaValue``

   The weighting value for this control point

-  ``unableToChangeTeam``

   Whether or not this control point is capturable (0) or not (1)

-  ``timeToGetControl``

   How many seconds it takes to get control of this control point

-  ``timeToLoseControl``

   How many seconds it takes to get control of this control point

-  ``onlyTakeableByTeam``

   Whether (1) or not (0) this control point is only capturable by one team

-  ``takeOverChangePerSecond``

   Capture speed; speed at which the flag at this control point raises or lowers.

-  ``enemyTicketLossWhenCaptured``

   Ticket loss caused to the enemy when this control point is captured *(needs to be verified)*

-  ``playerId``

   *Unknown; may set the ``playerID`` of the player that captured this control point first (the first player to arrive, not assisting players?)*

.. _vehicleobject:

``VehicleObject``
-----------------

A ``VehicleObject`` represents a BF2 vehicle. The ``VehicleObject`` class inherits the methods and attributes of PhysicalObject, with several additional methods. ``SoldierObject``, used to represent the physical body of player, is a sub-class of ``VehicleObject``.

-  ``vehicleObject.getDamage()``

-  ``vehicleObject.setDamage(intValue)``

-  ``vehicleObject.getIsWreck()``

   Returns boolean, 1 if the vehicle is destroyed

-  ``vehicleObject.getOccupyingPlayers()``

   Returns an array with index 0 being the driver

-  ``vehicleObject.getIsRemoteControlled()``

The ``getDamage()`` and ``setDamage()`` methods actually read/set the health of the vehicle. Transport helicopters start with 1500, tanks with 1000 and light jeeps with 750. They all explode when the damage reaches 0.

.. _soldierobject:

``SoldierObject``
-----------------

A ``SoldierObject`` represents the physical body of a human or AI player in BF2. The ``SoldierObject`` class inherits the methods and attributes of ``vehicleObject``, with no additonal methods or attributes. (Note: it appears that within the game engine, ``SoldierObject`` and ``vehicleObject`` may actually be the exact same thing; conceptually, though, it helps to think of ``SoldierObject`` as a subclass of ``vehicleObject``).

It is important to pay attention to the destinction between a player's “physical” body in the game, which is represented by an instance of the ``SoldierObject`` class, having position, orientation, health, etc., and the in-game “spirit” of that player, which is represented by an instance of the ``bf2.PlayerManager.Player`` class, having properties like a name, squad, profile ID, etc. ``The bf2.PlayerManager.Player`` (“spirit”) is created when a player connects to the server, and persists as long as the server continues running, even across game rounds (and disconnect/reconnects - if the player disconnects and then reconnects, the server tries to match them up with an existing ``bf2.PlayerManager.Player`` object). By contrast, a player remains associated with a ``SoldierObject`` only as long as they remain alive; as soon as they die, their association with the ``SoldierObject`` is broken; when they respawn, a new ``SoldierObject`` instance is created, and becomes associated with the player. That is to say, between dying and respawning, the player's “spirit” leaves their first “body” and is “reincarnated” in a new “body”.

Is that metaphysical enough for you?
