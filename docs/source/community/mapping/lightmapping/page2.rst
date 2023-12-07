
Converting Overgrowth to Static
===============================

Unfortunately 3DsMAx can't import the Overgrowth in your map, placed with the Overgrowth tool, directly from BF2 into 3DsMax. As such we need to convert every Overgrowth object placed with the Overgrowth tool to a static placed object, so then we can import it into 3DsMax.

First of all backup your ``Staticobjects.con`` with all your buildings, props etc in at least once before doing anything else, calling it something like ``Staticobjects_Final_*DATE*.con``

   We now need to first delete everything out of it in the editor (or you can do it outside of the editor by just deleting its entire contents with a text editor if you want to reload the editor). Simplest way to do this inside the editor is to go into the layer bit, right click on the main layer and click "select all in layer". Once that's finished (will take a bit of time) delete all the objects and ensure there are no staticobjects in any of the other layers (some times they can find there way in). Make sure all static objects in all layers are deleted and its worth checking your ``staticobjects.con`` after to ensure its empty of objects (will still have the "run" lines for your OG thou) and if it should look something like this:

   .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000348.jpg

Now this next part is not straight forward as some of you will probably get this same error I do after lightmapping which disables your view which is a real pain in the \*ss since it makes the bit after it 100x harder so I can't give you any pics of that part but I'll try and explain it as best as possible.

First position your camera/view so you can see your entire map (you may need to increase your editor VD settings to do so). Drag in a small simple object like a 1m crate and place it anywhere and lightmap it on low settings. Once its lightmapped, delete it right away.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000002.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000003.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000004.jpg

You overgrowth will now be converted to staticobjects and should be selectable (even if you can't see it if your view is disabled like mine is). Drag a selection box over your entire map which your camera/view should be able to see if you positioned it before hand, note if your view is disabled you might not see the selection box and you should click and hold in the first corner and wait a few seconds before dragging out to ensure the editor has time to keep up with your input as its probaly running very slowly at this point. Once you've dragged the selection box across your map you will probably have to wait some time for the editor to select all the objects, and if you have the output bar visible you should see a load of "[Tweaker] Load Object (Object)" popping up over and over again in it.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000006.jpg

Once all your OG is selected you will need to check ``IsSaveable`` box in the tweaker bar (green box = checked) and apply it to all objects in selection:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000007.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000008.jpg

Once done save your objects.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000009.jpg

Now if you look in your staticobjects.con now you should see all your overgrowth in it.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000010.jpg

You should now rename your Staticobjects.con with all your OG in it to something like ``Staticobjects_Overgrowth.con`` and then put your proper ``Staticobjects.con`` backup (with all your buildings etc. in), back into its orignal place.
