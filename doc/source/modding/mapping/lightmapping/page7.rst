
Cleaning Up Objects
===================

There are going to be a lot of objects in your files that you either don't want to generate lightmaps for, can't have them generated for, don't want them to cast a shadow on the map and so on. As such we want to sort the wheat from the chaff and to do this we need to go though all your import object types. This sounds worse than it really is since we are only talking about each type of unique object and not each individual static.

First hide all the objects on your map by simply not selecting anything then right click on the viewport and click :guilabel:`Hide Unselected`.

Then right click on your viewport again and go :guilabel:`Unhide By Name` and go though your list, selecting objects to unhide which you want to change. For example this :guilabel:`Bundled Mesh` :guilabel:`civiliancar1`, can not be lightmapped, but we do want it casting a shadow, but it also has first person and wreck meshes ontop of its normal mesh. As such first we should unhide it so we can work with it.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000044.jpg

----

Next lets select and delete :guilabel:`geom0` and :guilabel:`geom2` and its sub tree by just typing in :guilabel:`geom0` (1p mesh) into the search first, with :guilabel:`select sub tree` selected, and do the same for :guilabel:`geom2` (wreck mesh), leaving just :guilabel:`geom1` which is actually the only thing players see ingame in this objects current setup.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000046.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000047.jpg

----

Now select the objects name, in this case "0" and then select :guilabel:`inverse`, which will select all the helpers, and delete them leaving only the mesh:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000048.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000049.jpg

----

Lastly because in this rare case, the mesh name is bugged we should select all the meshes and go to :menuselection:`Tools --> Rename` Objects and rename it to its proper name of :guilabel:`civiliancar1` like so:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000050.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000051.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000053.jpg

----

Next example is I have a lot of static placed overgrowth in my ``staticobjects.con`` and as such I need to remove all the lods and helpers to ensure the script doesn't try to lightmap them, since it can't and because we don't want the lods casting shadows.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000054.jpg

Same basic principles above I'll show you in pics, although this time I select the helpers for deletion by unchecking geom from the selection list.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000055.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000056.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000057.jpg

Another example is the runway paving slabs which don't need lightmaps nor to cast shadows so just totally delete them and its helpers.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000058.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000059.jpg

Last example is the wirefence series, since these can't be lightmapped (well they can be the lightmaps are screwy on them from non-proper lightmap UVs) but we do want them casting shadows. We are also later going to set the wire up on them to be transparent so they don't cast a solid shadow on the ground like they do in the Bf2editor and let some light pass though them. As such, we want to delete all but its :guilabel:`lod0` mesh.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000060.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000061.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000062.jpg

Lastly for now I'm going to select all these objects we have unhidden that are left just to cast shadows and group them up into a group called ``_OVERGROWTH``, since even though some objects like the civilian car in there are not overgrowth, most of it is.

.. note::

   This does not include the Overgrowth helpers we have imported earlier, this is just the overgrowth etc. we have sorted out from the main statics.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000063.jpg
