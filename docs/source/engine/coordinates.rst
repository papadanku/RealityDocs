
BF2 Coordinates
===============

Battlefield 2 uses basic a basic 3-dimensional coordinate system to specify the position and orientation of objects within the game world.

Note that only objects of the :ref:`PhysicalObject` class and classes that inherit from it (:ref:`SoldierObject`, :ref:`ControlPointObject`, and so on) that “exist” in the game world and posssess positons and orientations. So, for example, instances of :ref:`bf2.PlayerManager.Player <bf2-playermanager-player>` do **not** have positions or orientations.

So, to retrieve position and orientation for a vehicle (say, an Abrams tank), representated by the :ref:`VehicleObject` ``tank``:

.. code-block:: python

   position = tank.getPosition()
   rotation = tank.getRotation()

On the other hand, to get the position and orientation of a player, representated by the :ref:`bf2.PlayerManager.Player <bf2-playermanager-player>` object ``andreas``:

.. code-block:: python

   # Get the SoldierObject containing andreas
   andreasSoldier = andreas.getVehicle()
   position = andreasSoldier.getPosition()
   rotation = andreasSoldier.getRotation()

Position
--------

Coordinates are specified by a three-element tuple, ``(X, Y, Z)``. For example:

.. code-block:: python

   (-160.95599365234375, 162.54800415039062, -266.01699829101562)

Within ``.con`` files these coordinates are written with slashes: ``X/Y/Z``.

These coordinates spell out a position along three axes:

-  The ``X`` value tells how far east or west an object is; moving further east causes ``X`` to increase, moving further west causes it to decrease.
-  The ``Y`` value tells your altitude; as you go higher, ``Y`` increases.
-  The ``Z`` value tells how far north or south an object is; moving further north causes ``Z`` to increase, moving further south causes it to decrease.

In all BF2 maps, the origin of the coordinate system (0, 0) is at the point in the very center of the map. Each unit in the coordinate system equals approximately 1 meter in the game world. Therefore, the example coordinate listed above will be a point 160.96 meters east and 266.02 meters south of map center, at an altitude of 162.55 meters. Note, however, that this is an “absolute” altitude; the altitude relative to the ground will depend on how high the surface of the ground is at that point; “sea level” varies quite a bit from map to map.

There are two sizes of map included with the basic Battlefield 2 game; the size of map may be determined by using the ``bf2.gameLogic.getWorldSize()`` method. This method returns a two-element tuple that gives the number of meters E/W and N/S along the edges of the map. All maps except Strike at Karkand return (2048, 2048), indicating the maps cover 4 square kilometers (2048x2048 meters), with coordinates running from -1024 to +1024 along each dimension. Strike at Karkand is the only map of a different size, and returns (1024, 1024), indicating a map covering 1 square kilometer, with coordinates running from -512 to +512 along each dimension.

   ``bf2.gameLogic.getWorldSize()`` appears to get it’s information from the ``heightmapcluster.setHeightmapSize`` parameter in the file ``Battlefield 2/mods/bf2/Levels/<name of map>/server.zip/Heightdata.con``.

.. code-block:: python
   :caption: The distance between any two points can easily be found by using the Pythagorean Theorem

      import math

      def findDistance(point1, point2):
         '''Use Pythagorean Theorem to find distance between two sets of coordinates.
         With normal BF2 scaling, the resulting distance will be in meters.'''
         deltaX = math.fabs(point1[0] - point2[0])
         deltaY = math.fabs(point1[1] - point2[1])
         deltaZ = math.fabs(point1[2] - point2[2])

         distance = math.sqrt(deltaX * deltaX +
                              deltaY * deltaY +
                              deltaZ * deltaZ)

         return distance

Rotation
--------

.. code-block:: python
   :caption: Rotational orientation (attitude) is specified by another three-element tuple, (A, P, R)

   (166.29025268554687, 0.0, 0.0)

Within .con files, these angles are written with slashes: ``A/P/R``.

-  ``A`` (“azimuth”, also known as “yaw”) gives rotation from due north going clockwise (if A is positive) or counter-clockwise (if A is negative), (or, the amount our viewpoint is rotated around a vertical axis passing through our viewpoint) measured in degrees:

   -  ``A=0`` (due north)
   -  ``A=90`` (due east)
   -  ``A=180`` (due south)
   -  ``A=270`` (due west)

-  ``P`` (“pitch”) tells how much we’re tilting down compared to horizontal, (or, the amount tilted up or down along the axis passing through our viewpoint from left to right) measured in degrees:

   -  ``P=0`` (horizontal)
   -  ``P=45`` (tilting down halfway between horizontal and vertical)
   -  ``P=90`` (looking straight down)
   -  ``P=-45`` (tilting up halfway between horizonal and vertical)
   -  ``P=-90`` (looking straight up)

-  ``R`` (“roll”) gives the amount the viewpoint has rolled around an axis passing from the back of our viewpoint through the front of the viewpoint, measured in degrees:

   -  ``R=0`` (no roll)
   -  ``R=45`` (viewpoint is rolled counter-clockwise by 45 degrees)
   -  ``R=-45`` (viewpoint is rolled clockwise by 45 degrees)

Note
~~~~

Note: The pitch and roll rotational coordinates apply to aircraft and cameras in BF2, but do **not** apply to players or vehicles on the ground. Ground players and vehicles **always** show ``P`` and ``R`` to be 0, regardless of their actual attitude (a soldier looking straight up in the air will still have a ``P`` value of 0, for example).
