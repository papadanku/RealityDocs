Combining & Splitting Terrain Lightmap
======================================

Now that you have generated all your Sun, Sky and Water Lightmaps of your terrain the first thing to do is to combine them. Open up both of your :guilabel:`Sun & Sky`and your :guilabel:`Water` Terrain Lightmaps in Photoshop. Your Terrain Water lightmap should be just Red and Black and should look something like this:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000461.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000462.jpg

In your :guilabel:`Terrain Water` lightmap, go into the :guilabel:`Channels` tab, select the :guilabel:`Red` Channel, in :guilabel:`selection` mode, select the entire canvas :kbd:`Ctrl-A` and copy it :kbd:`Ctrl-C`.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000463.jpg

Switch to your :guilabel:`Sun` and :guilabel:`Sky` Terrain lightmap and then switch to its :guilabel:`Red` channel, which should be totally blank, and paste the :guilabel:`Red` Channel you copied from your terrain's water Lightmap into that lightmap:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000464.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000465.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000466.jpg


If you now switch back to the RGB channels, your lightmap should now look like this:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000467.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000468.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000469.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000470.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000471.jpg

:guilabel:`Save As` your Lightmap, I would advise under a different name, something like ``_TERRAINLightingMap_Combined.tga``, and make sure you save it as a 24bit ``.tga``

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000472.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000473.jpg

Now that you've got your combined terrain lightmap sorted with all sun, sky and water lighting in it, it's time to split it up into lots of little ``.dds`` images so that the game can use them. First download this script kindly made by [R-DEV]AncientMan for this tutorial and install it on your computer by extracting the folder inside the ``.zip`` to anywhere on your computer: :download:`https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/SplitTgaToMultipleDDS.zip`

.. note::

   You may also need to download and install `Visual C++ Redistributable Packages <https://www.microsoft.com/en-gb/download/details.aspx?id=40784>`_ in order for the script to work.

   Once you have done that, copy your combined terrain lightmap ``_TERRAINLightingMap_Combined.tga`` into the tools ``input`` folder.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000474.jpg

Now this Tool/Script by default is setup for 2km x 2km and 4km x 4km Maps, which use a 8x8 (64) Patch Setup and if your working with a 1km (or smaller) map you will need to change the settings for this script since a 1km x 1km map only uses a 4x4 (16) patch setup.

**ONLY IF YOU ARE WORKING WITH A 1km OR SMALLER MAP**

   #. Open up the ``SplitTgaToMultipleDds.bat`` script with a text editor such as notepad or notepad++
   #. Change the :guilabel:`set num_x=8` and :guilabel:`set num_y=8` to :guilabel:`set num_x=4` and :guilabel:`set num_y=4`

   It will split the image into only the 16 patches used by a 1km by 1km map.

   If your working on a map smaller than a 1km map, like a 512m x 512m map, then I believe it only uses a 2 x 2 (4) patch setup but you would have to look inside your map files to determine that for sure.

Once you have put your combined terrain lightmap in the input folder and ensured the ``SplitTgaToMultipleDds.bat`` script is setup as you need, run that ``.bat`` script and a cmd window should pop up telling you its splitting your ``.tga`` image into lots of little ``.dds`` images and once it's finished if you look in the output folder, there should now be a sub folder with the same name as the ``.tga`` image you put into the input folder and in it should be all your terrain lightmap patches, note it says there is 64 total items in this folder, which is what I want:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000475.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000476.jpg

Finally its just a matter of copying all these patches over into your ``\mods\pr_edit\levels\*YOUR MAP*\Lightmaps`` folder and overwriting all the old patch lightmaps in there.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000477.jpg

And here are the results of my 3DsMax terrain lightmap in the editor (note the transparent water dose not work in the editor, only ingame):

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000514.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000513.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000511.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000512.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000515.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000516.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000517.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000518.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000519.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000520.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000521.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000522.jpg
