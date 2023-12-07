
Importing Terrain into 3DsMax
=============================

Once your 3DsMax scene is setup with the right units etc go to **BF2 > BF2 Lightmapping** and click **Load Land**. Then browse to your map's main folder in **/pr_edit/levels/\*your map*/** and select/open your map's ``Heightdata.con`` file. It should now start to import your terrain, this may take a little time.

   .. note::

      If you get a ``Out of scripter memory`` error, Open up the Listener Window (F11) and type in ``heapsize += 1000000000``, and you now should be able to import your terrain.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000013.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000014.jpg

Once its done you should end up with something like this.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000015.jpg

Now your terrain is imported, to help you distinguish and navigate it more easily, as well as a few things to help with LMing it later on, I would first recommend you first rename your terrain object from ``Object01`` (or something similar) to ``_TERRAIN`` and Convert your Terrain to an Edible Polygon.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000019.jpg

Next to make things easier to work with Apply an Optimize Modifier to your Terrain and set the ``Face Fresh`` to ``1`` to ensure it only optimizing the mesh without changing its shape.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000020.jpg

Now you may need to clean up the edges (and possibly some other areas) of your terrain manually which may have been imported "badly", like these bits here in my case.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000315.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000316.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000319.jpg

Now you can either fix these up manually in in Max, but even though these errors may not be visible to your in the BF2Editor, they are on your heightmap and this is what causes these invisible walls choppers/jets etc crash into around the edges of a map. As such, its best to fix them at the source, on the heightmap itself.

Load up Photoshop and open your map's ``HeightmapPrimary.raw`` file (backing it up first) with a channels count of ``1``, Depth in 16 Bits and the Byte Order to IBM PC like so.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000320.jpg

Then it should look something like this, with the whiter the colour, the higher the terrain and the darker, the lower etc, and if you look at the edges you can clearly see the errors on the edges of the map.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000321.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000322.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000323.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000324.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000325.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000326.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000327.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000328.jpg

Once done, resave your HeightmapPrimary.raw (making sure you have a backup of the old one first) in IBM PC Byte Order (you will possibly want to also save it in .psd format with the extra layer you've got somewhere too) and check your heightmap in the editor to ensure its all still good.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000329.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000330.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000331.jpg

You may want to do a little bit of manual smoothing on some of the edges now to clean them up a little.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000332.jpg

Once done with your edits/checking, make sure you save your terrain and Complied Terrain (File Re-Save if you haven't made any edits).

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000333.jpg

Now if you repeat the above processes of importing your terrain (deleting your old one first) and your terrain should be mostly cleaned up now. Mine still has a tiny lip and a little bit I missed on the beach but nothing to really worry about.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000334.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000335.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000336.jpg

Remember to optimize and name your terrain again once your happy with your edits and if not, go back over them and fix them up again.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000337.jpg

Convert your terrain back to an Edible Poly and then apply an ``Unwrap UVW`` Modifier to it.

   #. Click the Edit button in the modifier panel
   #. Go to face selection mode
   #. Select all faces (Ctrl+A)
   #. On the right in the modifier panel, in the Map Parameters rollout, hit the "Planar" button with "Normalized Map" Checked

      It will UV your terrain in the same way it is in-game.

   #. Make sure that the North of your map is in the top of the UV etc
   #. Once you are happy, click on the "Planar" button again and you can also uncheck "Show Pelt Seam" and "Show Map Seam" in the Display roll-out above it to make for easier viewing
   #. Double-check that your UVs extend all the way to the very edge of the UV box

      Best way to do this is to select the bottom left UV Vert, and ensure its at "U: 0.0, V: 0.0" and that the very top right vert is at "U: 1.0, V: 1.0".

      If the UVs do not extend to the very edges of the UV Window, then your generated terrain shadows later will be slightly offset from the objects of the map, especially at the edges of your map, and there will be a big gap around your map edges of a missing generated lightmap.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000338.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000339.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000340.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000343.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000342.jpg

Once your happy with all that collapse that modifier and while this step is optional, I would now recommend applying your minimap as a texture to your terrain to first ensure your UV map is first correct and second to help you navigate your map more easily.

   #. Take a minimap render of your map in the editor
   #. Save the minimap render as a ``.png``
   #. Select an unused material slot
   #. Set the material slot to use a **Standard Material** (should be by default)
   #. Expand the **Maps Rollout**
   #. Click on the **None** button next to `Diffuse Color`

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000022.jpg

   #. Select ``Bitmap`` at the top of the list

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000347.jpg

   #. Browse to your minimap file

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000023.jpg

Now,

   #. Click **Go to Parent** in the top right, below the material slots, above the **Bitmap** button
   #. Click the checkered-cube **Show Map in Viewport** button
   #. Rename the material to something like "Terrain"
   #. Apply this material to your terrain

You should have something like so.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000344.jpg

Finally I would recommend now setting your Terrain's Object Color to something else other than white, I would recommend 100% black so when in edged or wire mode you can distinguish it more easily from the other statics, which will be imported, by default, with a white colour like your terrain was, and now in edged-frame/wire mode, you can much more easily see your terrain.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000345.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000346.jpg

Finally, Save and Backup your 3DsMax Lightmapping Scene before you go any further.
