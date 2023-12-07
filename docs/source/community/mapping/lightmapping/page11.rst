
Importing Sun & Preparing your Lights
=====================================

Now its time to finally get some light in here.

Lets first start off by loading your sun from your sky settings. Go to **BF2 > BF2 Lightmapping** and hit the **Load Sun** button. Then browse to your map folder and select your ``sky.con`` file and by magic a direct light will be created in the location your sun is ingame.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000171.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000172.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000173.jpg

Now since this is a 4km map the light has been created far too close to the terrain, since the script for making it was only designed for 2km and smaller maps, and as such, the far sides of the map are basically behind the sun and wont receive lighting from it. As such the first thing you need to do, if your working on a 4km or larger map, is to move the sun further away, but without affecting its rotation at all. To do this, first select your "BF2_SunLight", then select the Move Tool (W) and then switch to Local Transformation mode in the dropdown box at the top. Now your "Gizmo" will be at the same rotation as your sun:

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000175.jpg

Now what you want to do is in the bottom centre, click the "Absolute Mode Transform Type-In" until it turns yellow which means its in "Offset Mode Transform Type-In". Then in the Z Axis box, type in 10000 (for a 4km map, larger maps will require more) and then your sun will be moved +10000 units (which is 1km) away along the Z Axis.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000178.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000179.jpg

Now to fix up your Sun's Light Settings. There are two main types of shadow casting methods to use for your Sun Light *(and point light but we will come to that later)* in 3DsMax. These are "Ray Traced Shadows" and "Adv. Ray Traced". I will go into more detail into these in a second but first, lets set up the common settings both of these methods use.

Select your sun and go into the modifier tab. First Check the "On" box under Shadows and for now leave the drop-down box under that on "Shadow Map" *(we will be changing this in a bit t either "Ray Traced Shadows" and "Adv. Ray Traced")*. Then under Intensity/Color/Attenuation, set your Sun's Light Multipler to 2 if its a sunny map (like mine) or 1 if its a cloudy map, or anywhere in-between but DO NOT go under 1 as you should never darken a map though lightmaps, when you can far more easily darken a map though the map's light settings and if its a night map, with no moon, you can fully get rid of the sun light by just setting the sun light colour to 100% black. Next we want to change the Sun Light Colour to 0, 255, 0 (RGB - aka 100% Green) in the box to the right of the multiplier, which will be white by default. This is because we are going to generate all the light types together and Sun Light uses the Green Channel in an RGB Lightmap Texture. Next in Directional Parameters, if your working with a 4km map, change the "hotspot/Beam" to have a value of 30000, more if its a larger map so it include the entire map (note the big circle around the map) in the image below. Other than that you can leave the rest of the settings at default but check them against my settings in the image below, with the exception of the Shadow Drop Down Box setting which we will get into next:

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000181.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000180.jpg

Now for the different shadow types and you will want to pick which ever works best for you and your map.

Ray-Tracing
-----------

.. list-table::
   :header-rows: 1
   :widths: auto
   :align: center

   * - BF2 Editor (Final Quality)
     - 3DsMax (Ray-Traced Shadows)
     - 3DsMax (Advanced Ray-Traced)
   * - |image1|
     - |image2|
     - |image3|
   * - |image4|
     - |image5|
     - |image6|
   * - |image7|
     - |image8|
     - |image9|

.. |image1| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg15_terrain_BF2Editor.jpg
.. |image2| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg15_terrain_RayTracedShadows.jpg
.. |image3| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg15_terrain_AdvRayTraced.jpg
.. |image4| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg17_terrain_BF2Editor.jpg
.. |image5| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg17_terrain_RayTracedShadows.jpg
.. |image6| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg17_terrain_AdvRayTraced.jpg
.. |image7| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg14_terrain_BF2Editor_LM.jpg
.. |image8| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg14_terrain_RayTracedShadows_LM.jpg
.. |image9| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg14_terrain_AdvRayTraced_LM.jpg

Ray-Traced Shadows
^^^^^^^^^^^^^^^^^^

   This is the "High Quality, Slow Rendering" Option for anyone who has a really good computer and/or has a lot of time to be able to lightmap their map in, like if you have a spare computer sitting around which otherwise would not be used and can lightmap solidly for a week or so. It should be noted that I would only recommend using this setting if your map is truly 100% final, being fully tested before hand and your absolutely sure that no changes are needed for it that will affect its lightmaps.

   In this mode, Object Lightmaps take around **6mins / object** (and its LODs), when lightmapping a high rez LM for a complex object, and it takes around **3x Longer than "Adv. Ray Traced"** and around 2x as long as the BF2 Editor's Final Quality Lightmaps.

   But when it comes to Terrain, at least with a lot of Overgrowth on it, Ray Traced Shadow takes only around **5/7th** of the time of the BF2 Editor with the BF2 Editor taking 11mins 41secs to render a patch, where 3DsMax with Ray Traced Shadows took only **8mins 20secs** to Render the same patch.

   Having said that the quality of these shadows is far superior than "Adv. Ray Traced" Shadows *(and the BF2 Editor)*, and if you can put the extra time in, the results are well worth it:

   For this setting all the above settings remain the same from above, with the exception of changing the **Shadows** Drop Down Box to **Ray Traced Shadows** as per this image:

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000181.jpg

Adv. Ray-Traced Shadows
^^^^^^^^^^^^^^^^^^^^^^^

   This is the "Medium Quality, Fast Rendering" Option for anyone who doesn't have the time or a decent enough computer to do "Ray Traced Shadows". If you plan on changing your map in the future which will require the map to be totally re-lightmapped, then this is the option to pick.

   In this mode Object Lightmaps take around **2mins 30secs / Object** (and its LODs), when lightmapping a high rez LM for a complex object, which is around **1/3 of the time it takes to generate "Ray Traced Shadows"** and almost 1/2 the time the BF2 Editor's takes on Final Quality Lightmaps.

   When it comes to Terrain Lightmaps it is considerably faster taking only around **2/9th** of the time of the BF2 Editor with the BF2 Editor taking 11mins 41secs to render a patch, where 3DsMax in Adv. Ray Traced took only **2mins 38secs** to Render the same patch.

   But the quality of these shadows is isn't as good as Ray Traced Shadows and with the exception of transparent leaf rendering, isn't that much better than the BF2 Editor's shadows and in some small cases, slightly worse, but that is mainly when the BF2 Editor generates a higher rez than you've set in 3DsMax. Overall these are still better quality than the BF2 Editors, especially if you have lots of overgrowth.

   For this setting all the above common settings remain the same from above, with the exception of changing the **Shadows** Drop Down Box to **Adv. Ray Traced** and in the new Optimizations Roll out, turn on ``Transparent Shadows`` (to allow for the transparent leaf textures to work) and to set the Antialasing Threshold Colour to 100% Black.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000222.jpg

Main Tutorial
-------------

For this tutorial I will be using "**Adv. Ray Traced**" Shadows since I'm trying to get this map done in the shortest time possible and I may be updating it later on with a few changes that may require new lightmaps to be rendered.

Import Lights
^^^^^^^^^^^^^

Now its time to import the Sky Lights we are going to use. Download this file here which has the recommend Sky Lights and Settings I'm going to be using in this tutorial and are at the very least a good base for your map for you to tweak from: `https://media.realitymod.com/tutoria...t_Template.zip <https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Lightmaps_Sky_Light_Template.zip>`_

Then go to **File > Merge** and browse to and select this file, and import all the lights inside of it into your map:

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000182.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000183.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000184.jpg

Configure Lights
^^^^^^^^^^^^^^^^

Now there are two lights in this:

- ``_Sky01``

   Your main sky light and produces pretty realistic light bounding affects which light up the outside more but still allows some light to filter into rooms though windows, doorways etc.

- ``_Ambient_Fill_light``

   Casts a flat light all over your map, no matter if it,s at the bottom of the deepest darkest cave of your map, or on the roof of a skyscraper. This light is to ensure that the interiors of your buildings are not pitch black which if it was just the sky light working on its own, some areas inside would be.

Currently the ``_Sky01`` has a Multiplier of 1 and the ``_Ambient_Fill_light`` has one of 0.4. If you want brighter interiors increase the ``_Ambient_Fill_light`` multiplier, and decrease the ``_Sky01`` multiplier.

   Both of these Sky Lights have a colour of ``0, 0, 255`` (RGB - aka 100% Blue, a bit like the sunlight but Blue instead of Green), because we are generating all lights together and the sky light uses the blue channel in the light map texture.

Finally its time to setup our "Point Lights", which are basically man made lights from lamp posts etc. I'm not planning to have a "night layer" for this map which is the main place this type of light really comes in, other than also for deep dark caves etc, but for the purpose of this tutorial I'm going to put in a few. For the main example,

I'm going to make a big Omni light in the Lighthouse by:

   #. Going to the object creation button in the top right

      #. Click the light icon
      #. Click the **Omni** button

         .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000185.jpg

      #. Place it in the Lighthouse

         .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000190.jpg

   #. Turn on shadows

      #. Give it the same type of Shadows your using for your Sun Light *(In my case, "Adv. Ray Traced")*
      #. Give it a Multiplier of 1 and a light colour of ``255, 0, 0`` (RGB - aka 100% Red)

         .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000186.jpg

      #. Give it a decay type:

         - Inverse Square and starting at 100 (10m)
         - Far Attenuation starting at 200 (20m) and ending at 1000 (100m)
         - Everything else on default

      .. note::

         - The last bunch of settings can be tweaked quite a bit depending on how powerful the light is and how far your want the light to travel etc.
         - Getting it right will take a bit of trial and error and to get it right you can do a quick render of your viewport in max and/or do Test LM Renders which I'll get into later in this tutorial.

I'm also going to apply my Lighting Template for the Carrier that I've done for other maps since that takes me only a few seconds to apply and here are the settings of the three type of lights used on it, which are two types of **Spot Light** and one type of **Omni Light**, which are all instances of each other so changing the settings on one will change the settings on all the other instances (which is what you should also be doing for your lighting) and if you want to use this Carrier Light Template on your map you can download it here and just align it to the Bridge, note however this is setup for HMS Invincible and if used on the USS Essex there will be a few differences: `https://media.realitymod.com/tutoria...s_Template.zip <https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Lightmaps_Carrier_Lights_Template.zip>`_

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000188.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000189.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000191.jpg

   .. note::

      You can setup templates of lights for a type of static, like for example a bunch of lights for each light bulb in a building, then setting each instance of that static to use that light template but this is pretty tricky so if someone really wants to know how to do this and can't work it out for themselves let me know and I might look into adding it into this tutorial at a later date.
