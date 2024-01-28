Optimizing "Flat" Lightmaps
===========================

If you have a map with a lot of sea water like mine your bond to have a bunch of "flat" Lightmaps, which are basically lightmaps of a flat sea and nothing else on them like this for example:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000478.jpg

.. warning::

   Having a 683kb texture of just flat white is quite a waste, especially when you have multiple ones all adding up together which in my case I have a total of 46 blank patches, currently using a total memory of 30.6mb, on nothing...

   To state the obvious, wasted file space is not just about the maps/mods download size, while yes that is a small factor, its mainly about the Players RAM usage.

   All of these textures need to be loaded into the players RAM and for starters, there is a limit on how much a player can load on his RAM since BF2 is a 32bit game, but on top of that, having to process these large textures, even if they are blank, slows down FPS and overall simply just is not good for performance, where instead we can seriously optimize them without any ill affects since they are simply just blank images.

First to find out which patches are used and are not used the simplest way is to overlay a little patch grid over our terrain lightmap.

   #. Take your complied terrain lightmap and resave it as a ``.psd`` under the name of something like ``_TERRAINLightingMap_Patches.psd``

      If your working with a 4km map and your terrain lightmap is at ``8192x8192`` you should resize it down to ``4096x4096``

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000479.jpg

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000480.jpg

   #. Go to **Image > Image Rotation > Flip Canvas Vertical** to put your lightmap up in the same way as the game reads it and the patches are in order

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000481.jpg

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000482.jpg

   #. :download:`terrain_patch_grid.png <http://realitymodfiles.com/rhino/editor/terrain_patch_grid.png>`

      #. *(Right Click, Save As)*
      #. Open it up with Photoshop

         .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000483.jpg

      #. Duplicate it over your ``_TERRAINLightingMap_Patches.psd`` image

         .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000484.jpg

You should end up with something like this:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000485.jpg

If your working with a 1km map and have a terrain lightmap size of 2048x2048 this patch should duplicate over your image correctly too, with its 4x4 (16) Patch Setup:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000486.jpg

Now you can clearly see what goes in each patch and as you can see, a lot of my patches are just flat white images like the one I showed you above. Note down which patches are blank, in my case its easier to note down the ones which are used, which are:

.. code-block::

   tx02x03, tx02x04, tx03x03, tx03x04, tx03x06, tx03x07, tx04x02, tx04x03, tx04x04, tx04x07, tx05x03, tx05x04, tx05x07, tx06x00, tx06x03, tx06x07, tx07x00, tx07x07

.. note::

   Even though ``tx05x04`` and ``tx06x03``, along with some others, are hardly used and being mostly blank, can't be optimized since they are still somewhat used:

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000487.jpg

Some however like ``tx06x02`` which have tiny little specs of water transparency difference since they have some little hills under the water.

   *In hindsight I should have probably totally removed them, since they are just small islands in real-life, which where part of the DEM data but are not above the surface of the water ingame after downsizing the DEMs scale to fit on the ingame map, but oh well*

I am going to optimize since it is not worth the tiny little difference in water transparency for them, which in their case is probably going to look odd if I keep them anyways:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000488.jpg

Once you have noted down all the files you want to optimize / do not want to optimize, close all images in Photoshop and then open up all the images you want to optimize:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000490.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000489.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000494.jpg

#. Click on the **Actions** tab (**Windows > Actions** if you can't see it)
#. Click on the little **Create new set**, folder icon in the bottom

   Call the new set something like ``Resie``.

#. Create the little **Create new Action** icon

   Call it something like ``8x8 DDS DXT1``

#. Hit the **Record** button

   Anything you do from here in Photoshop will be recoded in this action until you hit the stop recording button so do not do anything other than what I say.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000495.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000496.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000497.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000498.jpg

#. Go to **Image > Image Size**

   Change the pixel dimensions to ``8x8 px``.

#. Go to **File > Save**

   Save the image as a ``DXT1 RGB 4bpp | no alpha`` DDS Image with **Generate MIP Maps** and make sure **All** is selected in the drop-down box next to it.

#. Hit **Save**
#. Go to **File > Close**

   Finally hit the **Stop Recording** button to stop the action from recoding your actions.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000499.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000500.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000501.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000502.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000503.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000504.jpg

Now if you open up the image you just optimized/resized in NVIDA WTV, you should now see its a 8x8 DXT1 DDS Image with 4 mips total and a total memory usage of ``0.1kb``:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000505.jpg

Now if you select another opened image you want to optimize, select the header of your action **8x8 DDX DXT1 Action**, and hit play, it should now automatically resize this image, save it with the same DDS settings and close it. Ensure you open up the image in WTV after its done to check it is all good:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000506.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000507.jpg

Once you've confirmed your Action is all good its time to apply this Action to all opened files automatically.

   #. Go to **File > Automate > Batch**
   #. In the **Play** section, make sure the correct set and action are selected, and for Source have it set to **Opened Files**

      Making sure of course you don't have any other files opened in photoshop you don't want to resize and are not ``.dds`` images

   #. Hit **Ok** and it will apply this action to all opened files.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000508.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000509.jpg

Now the same images that where using up a total of ``30.6mb`` are now using only ``8.26kb`` and are doing exactly the same job, but are far easier for the client to process and takes up only a tiny bit of RAM!

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000510.jpg
