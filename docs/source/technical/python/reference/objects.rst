
BF2 Objects
===========

.. py:class:: PhysicalObject

   ``PhysicalObject`` represent physical things in the BF2 game world; as such, they have the properties of real objects in the physical world: properties like position (X, Y, Z coordinates) and orientation (rotation), and can contain, and be contained by, other ``PhysicalObject`` objects. A ``PhysicalObject`` appears to be implemented as C++ objects in the game engine which the embedded Python engine has access to, but since they are game engine objects, they are not defined anywhere in Python, and cannot be created directly in Python - but they can be accessed from Python. No special imports are necessary to manipulate these objects.

   Please note that since these are not native Python objects, we don't know what they are actually named inside the game engine; ``PhysicalObject``, as well as the names of other types of objects that inherit from that class, are made up for convienience. We also can't see into the game engine code to see if the hierarchial structure of these classes is what is presented here - for example, :py:class:`vehicleObject` and :py:class:`soldierObject` may, in fact, be a single class; the hierarchy of ``PhysicalObject``'s decendents given here should nevertheless be equivalent to whatever the real hierarchy is.

   .. py:attribute:: templateName
   .. py:attribute:: isControlPoint
   .. py:attribute:: isPlayerControlObject
   .. py:attribute:: hasArmor
   .. py:attribute:: token

   .. py:method:: isValid()
   .. py:method:: getTemplateProperty()

      The known properties available via the ``getTemplateProperty`` method are:

      -  ``radius``

         For control points only.

      -  ``ControlPointID``

         For control points only.

   .. py:method:: getPosition()
   .. py:method:: setPosition((X, Y, Z))
   .. py:method:: getRotation()
   .. py:method:: setRotation((A, B, C))
   .. py:method:: getParent()

      :returns: ``PhysicalObject`` that contains this instance, if any.

   .. py:method:: getChildren()

      :returns: A tuple of multiple ``PhysicalObject`` contained by this instance.

   For information about the coordinate system used by the Position and Rotation methods, see the page on :doc:`BF2 Coordinates <../../engine/coordinates>`.

.. py:class:: weaponObject

   A ``weaponObject`` is used to represent a weapon in BF2. The ``weaponObject`` class inherits the methods and attributes of ``physicalObject``, with no additonal methods or attributes.

.. py:class:: kitObject

   A ``kitObject`` is used to represent a “kit” in BF2. The ``kitObject`` class inherits the methods and attributes of ``physicalObject``, with no additonal methods or attributes.

.. py:class:: controlPointObject

   A ``controlPointObject`` is used to represent a control point in BF2. The ``controlPointObject`` class inherits the methods and attributes of ``physicalObject``, with the following additional methods and attributes:

   .. py:attribute:: flagPosition

      Returns:

      -  ``0`` = top
      -  ``1`` = middle
      -  ``2`` = bottom

   .. py:attribute:: lastAttackingTeam
   .. py:attribute:: triggerId

   .. py:method:: cp_getParam(parameter)
   .. py:method:: cp_setParam(parameter, value)

   ``controlPointObject`` also have a number of internal properties that are accessed through the ``cp_getParam`` and ``cp_setParam`` methods:

   .. py:property:: isHemisphere

      0 or 1, indicating if the control point capture area is a hemisphere or not.

   .. py:property:: team

      Team the capture point belongs to: 0 for neutral, 1 for team 1, and 2 for team 2. Updating this value also changes the minimap and flag tag indicator.

   .. py:property:: flag

      The flag image used in the control point; 1 for team 1's flag, 2 for team 2's.

   .. py:property:: areaValue

      The weighting value for this control point

   .. py:property:: unableToChangeTeam

      Whether or not this control point is capturable (0) or not (1)

   .. py:property:: timeToGetControl

      How many seconds it takes to get control of this control point

   .. py:property:: timeToLoseControl

      How many seconds it takes to get control of this control point

   .. py:property:: onlyTakeableByTeam

      Whether (1) or not (0) this control point is only capturable by one team

   .. py:property:: takeOverChangePerSecond

      Capture speed; speed at which the flag at this control point raises or lowers.

   .. py:property:: enemyTicketLossWhenCaptured

      Ticket loss caused to the enemy when this control point is captured *(needs to be verified)*

   .. py:property:: playerId

      *Unknown; may set the ``playerID`` of the player that captured this control point first (the first player to arrive, not assisting players?)*

.. py:class:: vehicleObject

   A :py:class:`vehicleObject` represents a BF2 vehicle. The :py:class:`vehicleObject` class inherits the methods and attributes of :py:class:`PhysicalObject`, with several additional methods. :py:class:`soldierObject`, used to represent the physical body of player, is a sub-class of :py:class:`vehicleObject`.

   .. py:method:: getDamage()
   .. py:method:: setDamage(intValue)
   .. py:method:: getIsWreck()

      :returns: Boolean, 1 if the vehicle is destroyed.

   .. py:method:: getOccupyingPlayers()

      :returns: An array with index 0 being the driver.

   .. py:method:: getIsRemoteControlled()

   The :py:meth:`getDamage` and :py:meth:`setDamage` methods actually read/set the health of the vehicle. Transport helicopters start with 1500, tanks with 1000 and light jeeps with 750. They all explode when the damage reaches 0.

.. py:class:: soldierObject

   A :py:class:`soldierObject` represents the physical body of a human or AI player in BF2. The :py:class:`soldierObject` class inherits the methods and attributes of :py:class:`vehicleObject`, with no additonal methods or attributes. (Note - it appears that within the game engine, :py:class:`soldierObject` and :py:class:`vehicleObject` may actually be the exact same thing; conceptually, though, it helps to think of :py:class:`soldierObject` as a subclass of :py:class:`vehicleObject`).

   It is important to pay attention to the destinction between a player's “physical” body in the game, which is represented by an instance of the :py:class:`soldierObject` class, having position, orientation, health, etc., and the in-game “spirit” of that player, which is represented by an instance of the :py:class:`bf2.PlayerManager.Player` class, having properties like a name, squad, profile ID, etc. The :py:class:`bf2.PlayerManager.Player` (“spirit”) is created when a player connects to the server, and persists as long as the server continues running, even across game rounds (and disconnect/reconnects - if the player disconnects and then reconnects, the server tries to match them up with an existing :py:class:`bf2.PlayerManager.Player` object). By contrast, a player remains associated with a :py:class:`soldierObject` only as long as they remain alive; as soon as they die, their association with the :py:class:`soldierObject` is broken; when they respawn, a new :py:class:`soldierObject` instance is created, and becomes associated with the player. That is to say, between dying and respawning, the player's “spirit” leaves their first “body” and is “reincarnated” in a new “body”.

   Is that metaphysical enough for you?
