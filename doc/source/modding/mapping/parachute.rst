
Parachute Spawns
================

There is not a lot to worry about, most is done by python. The planes travel at 50-60m/s (180-216km/h)

The spawner:

- **MUST** have ``paradrop`` in the name
- **MUST** have the team set else it might create markers for wrong team
- **MUST** have timeToLive of 0
- **MUST** have distance set
- **SHOULD** be linked to the main base. Make sure flag team matches template team!

Examples
--------

.. code-block::
    :caption: This spawner will spawn two planes with 10sec in between that travel 2km before disappearing.

    ObjectTemplate.create ObjectSpawner bullseye_blue_paradrop_02
    ObjectTemplate.activeSafe ObjectSpawner bullseye_blue_paradrop_02
    ObjectTemplate.modifiedByUser "Wouter"
    ObjectTemplate.isNotSaveable 1
    ObjectTemplate.hasMobilePhysics 0
    ObjectTemplate.setObjectTemplate 2 paradrop
    ObjectTemplate.minSpawnDelay 10
    ObjectTemplate.maxSpawnDelay 10
    ObjectTemplate.TimeToLive 0
    ObjectTemplate.Distance 2000
    ObjectTemplate.teamOnVehicle 1
    ObjectTemplate.maxNrOfObjectSpawned 2
    ObjectTemplate.team 2

.. code-block::
    :caption: This will only spawn one plane that travels 1km.

    ObjectTemplate.create ObjectSpawner bullseye_blue_paradrop
    ObjectTemplate.activeSafe ObjectSpawner bullseye_blue_paradrop
    ObjectTemplate.modifiedByUser "Wouter"
    ObjectTemplate.isNotSaveable 1
    ObjectTemplate.hasMobilePhysics 0
    ObjectTemplate.setObjectTemplate 2 paradrop
    ObjectTemplate.minSpawnDelay 99999
    ObjectTemplate.maxSpawnDelay 99999
    ObjectTemplate.TimeToLive 0
    ObjectTemplate.Distance 1000
    ObjectTemplate.teamOnVehicle 1
    ObjectTemplate.team 2

The direction they move is simply set by the rotation of the ``ObjectSpawner``.

Some other things to consider:

- Make sure the distance is not too long. If it reaches out of the map, the markers will wrap around and show on the wrong side. Always make sure the planes end inside map borders
- Make sure to set it high enough so players wont get injured when pulling the parachute. Also make sure it is not on the ground. Forgot to move it into the air on one test and was puzzled why it moved so weirdly
- Don't give any other rotation besides yaw (x-value)
- Don't place the start of the planes close to a spawn point. It will create the green parachute icon and will look like that spawnpoint is a parachute one.
