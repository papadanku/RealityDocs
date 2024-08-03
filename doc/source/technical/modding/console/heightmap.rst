
Heightmap
=========

``heightmapcluster``
--------------------

``heightmapcluster.addHeightmap``
   std::string int int -> void

``heightmapcluster.compileWaterMeshesIntoHeightmap``
   -> void

``heightmapcluster.create``
   std::string -> void

``heightmapcluster.importSurroundingRawHeightMap``
   std::string -> bool

``heightmapcluster.intersectCameraRay``
   -> void

``heightmapcluster.setClusterSize``
   int -> void

``heightmapcluster.setHeightmapSize``
   int -> void

``heightmapcluster.setSeaWaterLevel``
   float -> void

``heightmapcluster.smoothEdges``
   int float float -> void

``heightmapcluster.stitchEdges``
   -> void

``heightmap``
-------------

``heightmap.loadHeightData``
   std::string -> void

``heightmap.loadMaterialData``
   std::string -> void

``heightmap.setBitResolution``
   int -> void

``heightmap.setMaterialScale``
   int -> void

``heightmap.setModified``
   bool -> void

``heightmap.setScale``
   Vec3 -> void

``heightmap.setSize``
   int int -> void
