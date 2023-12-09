Terrain Sun & Sky Lightmaps
===========================

Its now time to setup the terrain for its Sun and Sky Lightmaps. Note that the Red channel isn't used for point light on the terrain and its used for water transparency instead which we will do later sepratly.

First load your map back up in 3DsMax\ **9** and turn off (or altenrativly, delete) all your point lights if you have any as otherwise they will conflict with the water depth lighting channel.

.. note::

   If you wish to have Man Made (Point) Lighting on your terrain then the best way to go about it is to turn them Blue/Green and have them in your Sky/Sun Light Channel BUT, doing them this way means you can't turn them off in day map layers and they will use the same light colour/intensity as your Sky/Sun light.

Next thing we need to do is create your "Sea Water Level" so that shadows cast on your water are cast on the sea water surface and not on the sea bed.

Select your Terrain mesh *(\_TERRAIN)* and add a **Vol. Select** modifier to it. Switch the **Stack Selection Level** to **Vertex** and **Selection Method** to **Replace** and check **Invert**. This means that any verts outside of this Volume Selection box will now be selected, which by default, is nothing since the box is created to the very limits of your object.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000266.jpg

Expand the modifier, selecting **Gizmo** and switching to **Offset Mode Transform Type-in** with the **Move Tool** selected, offset the **Volume Selection** box by the depth of your sea water of your map. My map has a sea water Level of 5m so I need to offset my **Vol. Selection** box by 50 Units (since 10 Units = 1m).

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000270.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000271.jpg

Turn on **Percentage Snapping** and open up the **Grid and Snap Settings** window (Right click on the snapping button to open it or go to **Customise > Grid** and Snap Settings...) and in the **Options Tab** set the **Percent** box to ``100%``. Then add an **Edit Poly** modifier to your terrain and go into **Vertex Selection** mode and all the vertices selected by the **Vol. Select** modifier should now be selected for you in this new **Edit Poly** Modifier. Switch to the **Scale** Tool and with **Percentage Snapping** still enabled, select the ``Z`` Axis and scale it down to ``0%``, which will make all the vertices in your selection totally flat.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000272.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000273.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000275.jpg

Finally switch to the **Move** tool and in **Absolute Mode Transform Type-In** set the Z amount for your vertices to that of your sea water level, which in my case is 5m, 50 Units:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000277.jpg

Now if you look at your terrain where your sea water should be closely it should be all flat and at the level your sea water is ingame:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000278.jpg

And if we turn off the **Edit Poly** modifier, we still have our sea bed, which we will need later *(and if you plan on re-lightmapping any objects since you don't want your sea water level to cast a shadow on your objects)*

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000279.jpg

Now with your Terrain selected hit the ``0`` key on your keyboard to bring up the **Render to Texture** window ( alternatively, go to **Render > Render to Texture**). At the top you, will see a little **Output** box under the **General Settings** rollout and next to **Path**, hit the **...** button, then browse to your lightmap scene folder and make a new **Terrain** folder and select it.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000259.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000260.jpg

Next scroll down to the **Output** Rollout and hit the **Add...** button, then add a **LightingMap** element. By default it should be created as a ``.tga``, which is what we want:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000262.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000263.jpg

Next you need to change the element's width and height settings. This depends on the size of your map, and/or how much detail you want on your terrain's lightmap. Generally speaking, however, a normal map has a terrain lightmap ratio of 2px/meter and these are the normal width and height settings you should use for the following sizes of map:

   - **1km x 1km:** 2048 x 2048

      16 512x512 Patches

   - **2km x 2km:** 4096 x 4096

      64 512x512 Patches

   - **4km x 4km:** 8192 x 8192

      64 1024x1024 Patches

Since I'm working on a 4km by 4km map, I'm going to be using a 8192 width and 8192 height:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000265.jpg

Now we just need to unhide any objects we want to cast shadows on our terrain. You should still have all your LOD0 Static Meshes unhidden but if not, unhide them *(by searching for "\*=0" in unhide by name as before)* and unhide your Overgrowth layer/group and make sure it has the correct leaf material applied to it etc.

Then once all that is done and your Sun and Sky lights are the only ones active, save your scene back it up, and save a separate scene to be loaded in a later version of 3DsMax if your using one (pretty much a requirement for an 8192 or above render).

Then restart your PC, optimize it for lightmapping like you did before for your final object lightmaps and render away by clicking the **Render** button in the bottom left of the **Render to Texture** window.

.. note::

   Small little tip for better render preview window, is to turn off your diffuse texture for your terrain material as it will only conflict with the render preview, but will not affect the final saved LM.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000280.jpg

I lightmapped my Sun and Sky Terrain lightmaps in **2hrs and 7mins** with Adv. Ray Traced Shadows and once your done you should have something like this:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_Terrain_Sun_LM.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_Terrain_Sky_LM.jpg
