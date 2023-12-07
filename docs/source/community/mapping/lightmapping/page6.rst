
Importing Overgrowth into 3DsMax
================================

#. Once your PC has restarted, before we import the overgrowth, to save ourselves a hell of a lot of time in the long run, you should go to your ``EA GAMES\Battlefield 2\mods\pr_edit\Objects`` folder and temporarily move the ``vegitation`` folder outside of your ``pr_edit`` folder, somewhere on your computer, so that the import scripts can't find the objects its trying to import, and instead just places a helper for them.
#. Once you've moved your vegitation folder load up 3DsMax again and with a brand new scene, with the same units setup as before, repeat the above process for importing statics into 3DsMax **but** importing your Overgrowth ``Staticobjects.con``

   Should be named something along the lines of ``Staticobjects_Overgrowth.con`` as per the :doc:`Converting the Overgrowth to Static Step <page2>`.

#. We are using a brand new blank sceen to make it easier on the importing script to do its job as for some reason it seems to slow down when the scene is already populated with lots of objects and we are going to merge the imported Overgrowth helpers into the proper scene once the importing has finished.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000032.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000038.jpg

   Once the importing has finished you should have something like this.

#. Now Save this max scene as the same name as your map but with an **_Overgrowth** suffix.

   Mine is called ``Jamaica_Overgrowth.max``

#. Back it up and finally move the ``vegitation`` folder you just moved out of your ``\pr_edit\Objects`` folder, back into it where it belongs.
#. Open up your normal Lightmapping Scene with your terrain and statics in and then go to **File > Merge** and select your scene with your imported Overgrowth Helpers in. Then click the "All" button in the bottom left to select everything and click ok and it will import all the selected files into your current scene.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000037.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000039.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000040.jpg

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000041.jpg

I would then recommend adding the selected to a new "Overgrowth Helpers" Layer.

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000042.jpg

Then save and backup your lightmapping scene.
