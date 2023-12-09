Full Object Lightmaps
=====================

First of all if you can, I would recommend you do your full lightmaps in a later version of max than Max9, ideally a 64bit version too, so you have the fastest and most stable rendering you can get. To do this you just need to install the `PR:BF2 3DsMax9 Tools <https://www.realitymod.com/forum/f189-modding-tutorials/134050-pr-bf2-3dsmax9-tools-v0-40-a.html>`_ to the newer version of max you wish to lightmap with, and while the importing, exporting and a bunch of other scripts wont work for later versions, the lightmap generation scripts should work fine and have been tested on 3DsMax 2010 and 2012, but should hopefully work on later versions too.

.. note::

   It is advised that you backup your Max scene and save a separate version of your lightmap scene to be loaded by the newer version since once the scene is saved with the newer version, it can't be re-opened by the older version.

I would then recommend you restart your computer and when it starts up close down all unnecessary programs you don't need to free up as much of your CPU and RAM as possible since even having something like Skype running in the background will use up some CPU and RAM and will ultimately take longer for your lightmaps to generate as a result.

Once restarted and your system is optimized for lightmapping, start up the version of max your going to use for lightmapping and then like in the Test Lightmaps section, go to **BF2 > Bf2 Lightmapping**, but instead of hitting the **Render Selected Objects** button. you will want to press the **Render All Lightmaps** button. But before you do this, you should check that the **Light Pass** dropdown box is blank *(which means all lights pass, the other options are sun, sky or point light passes separately as done in the past)*, Specific LOD is set to All and if you want to keep/skip any previously generated lightmaps you can check the **Resume** button which will check if the objects lod its about to generate has a lightmap already *(In your Temp Folder)*, and if it dose, skip it and move onto the next object/lod. If your system crashes for whatever reason 1/2 way though lightmapping, this tool can be a life saver. Also ensure your temporary directory is correct and your lightmap size file is loaded. Once you've confirmed all the settings are good, render away!

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000255.jpg

In all it took me under 7hrs to render the 200 objects in my map at around 2mins / object with **Adv. Ray Traced** Shadows. I can not be sure how long it actually took because I was asleep during this time and time **Total Time Taken** bugged out as it normally dose after rendering lots of objects and said it took something like 50hrs.

And here are the results of my Object LMing, note the terrain is still Medium Editor lightmaps:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000223.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000224.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000225.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000226.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000227.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000228.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000229.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000230.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000231.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000232.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000233.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000234.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000235.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000236.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000237.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000238.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000239.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000240.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000241.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000242.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000243.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000244.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000245.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000246.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000247.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000248.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000249.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000250.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000251.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000252.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000253.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000254.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000256.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000257.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000258.jpg
