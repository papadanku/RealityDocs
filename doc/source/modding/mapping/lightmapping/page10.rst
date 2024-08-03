
Sorting Statics for Lightmapping
================================

First thing we will want to do is unhide all your :guilabel:`LOD0` meshes of your statics. The simplest way to do this is go to Unhide by name, then do an object search for :guilabel:`*=0` (without the quotes) which will select all the :guilabel:`LOD0` meshes we want to unhide.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000143.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000144.jpg

Next go to :menuselection:`BF2 --> Bf2 Lightmapping`` and hit the :guilabel:`Save/Update File`` in the :guilabel:`Lightmap Size Control` segment and call the ``.txt`` file something like ``YourMap_LightmapSizes.txt``.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000145.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000146.jpg

Open that file it creates and it should look something like this, which is what it produced for my map.

   .. code-block::

      hotel  undefined  undefined  undefined  undefined
      house_high_02_v2  undefined  undefined  undefined  undefined
      house_high_03  undefined  undefined  undefined  undefined
      house_high_04  undefined  undefined  undefined  undefined
      house_high_05  undefined  undefined  undefined  undefined
      house_high_06  undefined  undefined  undefined  undefined
      house_medium_02  undefined  undefined  undefined  undefined
      house_medium_05  undefined  undefined  undefined  undefined
      citybuilding_2a_part1  undefined  undefined  undefined  undefined
      citybuilding_2a_part2  undefined  undefined  undefined  undefined
      citybuilding_3a  undefined  undefined  undefined  undefined
      housingblock_1_groundfloor  undefined  undefined  undefined  undefined
      housingblock_1_midfloor_v2  undefined  undefined  undefined  undefined
      housingblock_1_midfloor_v1  undefined  undefined  undefined  undefined
      housingblock_1_topfloor  undefined
      house_double_02  undefined  undefined  undefined  undefined
      house_double_04  undefined  undefined  undefined  undefined
      citybuilding_4a  undefined  undefined  undefined  undefined
      dock_straight_30m  undefined  undefined
      dock_bend_122degs  undefined  undefined
      house_detached_02  undefined  undefined  undefined  undefined
      house_detached_03  undefined  undefined  undefined  undefined
      house_detached_01  undefined  undefined  undefined
      house_low_01  undefined  undefined  undefined  undefined
      house_low_03  undefined  undefined  undefined
      house_low_02_v2  undefined  undefined  undefined
      mi_hangar_mec  undefined  undefined  undefined
      xp1_airtower  undefined  undefined  undefined  undefined
      fishingboat  undefined  undefined  undefined  undefined
      boxesonpallet_01  undefined  undefined  undefined
      woodencrate_3m  undefined  undefined  undefined
      marketstand_1  undefined  undefined
      parkbench  undefined  undefined  undefined
      plant_box  undefined
      phonebooth  undefined  undefined  undefined
      rockpile_1  undefined  undefined  undefined
      rockpile_large  undefined  undefined  undefined
      rockpile_medium  undefined  undefined  undefined
      rockpile_medium_02  undefined  undefined  undefined
      container_cl_blue  undefined  undefined
      container_cl_green_trash  undefined  undefined  undefined
      container_cl_red  undefined  undefined
      container_cl_yellow  undefined  undefined
      container_op_yellow_cluster  undefined  undefined
      basket_hoops  undefined  undefined
      smallboat1  undefined  undefined  undefined
      smallboat2  undefined  undefined  undefined
      smallboat3  undefined  undefined  undefined
      lighthouse  undefined  undefined  undefined  undefined
      tyre_stack_v1  undefined  undefined  undefined
      shack_v4  undefined  undefined  undefined
      boatwreck_small  undefined  undefined  undefined  undefined
      pier  undefined  undefined  undefined
      car1  undefined  undefined  undefined  undefined
      water_cart_v1  undefined  undefined  undefined
      palletstack  undefined  undefined  undefined
      bus_stop  undefined  undefined  undefined
      cafechair  undefined  undefined  undefined
      trash_dumpster  undefined  undefined
      tvset  undefined  undefined  undefined
      lamppost_highway_01  undefined  undefined  undefined
      shack_v2  undefined  undefined  undefined
      construct_metal_plate  undefined  undefined
      shack_v3  undefined  undefined  undefined
      lamp_post  undefined  undefined  undefined
      shack_v5  undefined  undefined  undefined
      spawn_shack  undefined  undefined  undefined
      shack_v1  undefined  undefined  undefined
      water_tower  undefined  undefined  undefined
      gb_carrier_invincible_back  undefined  undefined  undefined  undefined
      gb_carrier_invincible_bridge  undefined  undefined  undefined  undefined
      gb_carrier_invincible_front  undefined  undefined  undefined  undefined
      gb_carrier_invincible_mid  undefined  undefined  undefined  undefined
      gb_carrier_invincible_skijump  undefined  undefined  undefined  undefined
      gb_carrier_invincible_interior_pt2  undefined  undefined  undefined  undefined
      gb_carrier_invincible_interior_pt1  undefined  undefined  undefined  undefined
      air_repairstation_no_supply  undefined  undefined  undefined
      mi_antenna  undefined  undefined  undefined
      mi_plane_stair  undefined  undefined  undefined
      mi_barrack_mech  undefined  undefined  undefined  undefined
      bunker  undefined  undefined  undefined

These are all the statics and their LODs in your map that can now be lightmapped, but currently each LOD has its lightmap size :guilabel:`undefined` and we need to define it.

   #. Merge our ``Master LightmapSizes`` file which, has most of the static lightmap sizes already defined.
   #. :download:`master_size.txt <https://files.realitymod.com/lightmapping/master_size.txt>`
   #. Open it with a text editor, then paste it onto the end of your ``master_size.txt`` file and save it: `<https://files.realitymod.com/lightmapping/master_size.txt>`_

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000155.jpg

Now we need to sort all our objects by Alphabetical order and the simplest way I know to do this with also keeping each object using its LODs is to import this list into a Spreadsheet and for this tut I'm going to use Google Docs/Drive since most people should have that already and if not can use it, if nothing else.

----

First Create a new Spreadsheet on your Google Drive, then go to :menuselection:`File --> Import` and select the ``.txt`` file you just saved and in the import file settings I would recommend you use :guilabel:`Replace spreadsheet` and for separator character you need to set it to use a " " (a Space, without the quotes) as the separator then hit import and you should have something like this.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000147.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000148.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000149.jpg

Now with :guilabel:`Column A`, selected go to :menuselection:`Data --> Sort --> Sheet by column A --> A > Z`` and it will sort all the rows out into alphabetical order

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000150.jpg

And do a search in the file for :guilabel:`undefined` and you will be able to see if the settings are already defined in the master, like this :guilabel:`air_repairstation_no_supply` which you can see, is already defined by the row above it.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000160.jpg

When you find one which isn't already defined, like the bunker here, copy it into the master ``.txt`` file like so.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000161.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000162.jpg

Now we need to update the :guilabel:`undefined` lod lightmap sizes to the correct ones. The simplest way to find out what sizes it uses is to browse to the object's ligthmap samples and open them with BFMeshView, with the ``.samples`` being the ``lod0`` sample, ``.samp_01`` being the LOD1 sample, ``.samp_02`` being the ``lod2`` sample etc.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000166.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000164.jpg

Once open you will be able to see the width and height of the lightmap settings in the top left.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000165.jpg

Some of the lightmap samples for many objects are much higher resolution than they need to be and in many cases you can make them much smaller, especially for the LODs which for this bunker :guilabel:`lod1` also has a lightmap sample size of 128 by default by we can make it 64 for this bunker with ease and 32 for :guilabel:`lod2`.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000167.jpg

If an object has a different Width and Height resolution then instead of defining them with just one number, you would put a \* in the middle of the Width and Height, for example 256*64 for a lightmap texture width of ``256px`` and a height of ``64px``. Note you should only define objects with different width and height width resolutions that have been setup to have them, which is only a few objects so far with custom lightmap UVs, such as the `Wooden Fence Series <https://www.realitymod.com/forum/f196-pr-highlights/93602-new-wooden-fence-statics.html>`_.

If you find an object without any samples then its a matter of best judgement and/or trial and error to finding the right lightmap size. It must be noted that the resolution for the width and height of each lightmap must be a power of two, ie either a value of 8, 16, 32, 64, 128, 256, 512, 1024 or 2048.

Once you have defined lightmap sizes for all the LODs of your statics into the :guilabel:`Master Lightmap Sizes` file, go back into max and go to :guilabel:`BF2 --> BF2 Lightmapping` and by :menuselection:`Lightmap Size File --> ... --> Master_LightmapSizes.txt` file you have updated with all your lightmap sizes. Then hit the :guilabel:`Apply Lightmap Settings` button and it will apply all these lightmap size settings to all the LODs of your statics.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000168.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000169.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000170.jpg
