
``skyDome``
===========

``skyDome.cloudLerpFactors``
   Vec2 -> Vec2

``skyDome.cloudTemplate``
   std::string -> std::string

``skyDome.cloudTexture``
   std::string -> std::string

``skyDome.cloudTexture2``
   std::string -> std::string

``skyDome.domePosition``
   Vec3 -> Vec3

``skyDome.domeRotation``
   float -> float

``skyDome.domeSize``
   float -> float

``skyDome.fadeCloudsDistances``
   Vec2 -> Vec2

``skyDome.flareDirection``
   Vec3 -> Vec3

``skyDome.flareFadeAdd``
   float -> float

``skyDome.flareFadeMul``
   float -> float

``skyDome.flareTemplate``
   std::string -> std::string

``skyDome.flareTexture``
   std::string -> std::string

   - Map: ``Sky.con``
   - The texture of the sunflare/actual sunflare.
   - When switching to a map with no sunflare, it will still use the previous maps one.

      - So for maps like Fallujah West/Saaremaa, an invisible texture needs to be defined instead to prevent the sunflare bug.

   - Usage: ``Skydome.flareTexture common\textures\sunflare\Sunglow_no``

``skyDome.hasCloudLayer``
   bool -> bool

``skyDome.hasCloudLayer2``
   bool -> bool

``skyDome.lightingBlend``
   float -> float

``skyDome.lightingColor``
   Vec3 -> Vec3

``skyDome.scrollDirection``
   Vec2 -> Vec2

``skyDome.scrollDirection2``
   Vec2 -> Vec2

``skyDome.skyTemplate``
   std::string -> std::string

``skyDome.skyTexture``
   std::string -> std::string