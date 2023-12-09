
Replacing Objects with Reference Objects
========================================

What we are going to do now is replace all different types of Overgrowth and other objects with the Reference Objects we have just made, type by type.

First, unhidden your Overgrowth Group, ungroup it and unhide your Overgrowth Helpers layer and anything else containing objects you will want to replace that are not meant to receive lightmaps, keeping everything else, other than your Reference Meshes hidden.

First we are going to replace our ``af_palmbush_01``, since it is the first one on the list alphabetically Select the object by name, not including the ``=0`` at the end in your search since the helpers won't have that if they are in both, otherwise you wont select them, and since our Reference object is prefixed with a ``_REF_`` it wont be selected.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000120.jpg

#. Go to **MaxScript > Run Script**
#. Go into the ``bf2`` folder in your scripts folder and select the ``instance replace.ms`` script that is included in the PR:BF2 3DsMax9 v0.40 Tools and hit open
#. A small window will pop up, hit **Pick Master** and then hit **H** to select by name
#. Select the Reference object you want to replace all selected objects with, which in this case is the ``_REF_af_palmbush_01`` mesh
#. Hit **Make Instances** and it will replace our entire selection of ``af_palmbush_01`` with the ``_REF_af_palmbush_01`` mesh

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000121.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000122.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000123.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000124.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000125.jpg

Once that has finished apply the ``Overgrowth`` Material to the selection

   Unless its something like the civi car 1, which does not need it and applying it will most likley mess it up from its MatIDs not matching the bark mat and you should now see all these objects with transparent leaves.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000126.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000127.jpg

Carry on doing this until all your old Objects are replaced with the new Reference Objects. Once you are done, you should have something like this.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000128.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000129.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000130.jpg

If you have FPS issues with all your Overgrowth using transparent textures in your viewport, then you can temporarily assign a blank material to them and then before lightmapping, put the correct material back on but in order to do this you first must have all the objects compatible with your material, such as the logs and civi cars which currently in my case, are not.

As such, I am now going set them up so they can have them applied to them without issue by first doing a search for all the logs in my map, by searching for ``*log``, which will then select all objects with the word ``log`` in its name, which in my case is two types of log, the ``nc_deadlog01``" and the ``me_deadlog01``.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000131.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000132.jpg

Then to all my selected objects I'm going to apply a ``Material`` modifier and have it set all the selected objects to have Material 1 applied to all faces.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000133.jpg

Then I'm going to do the same thing to my civiliancar1 and then if I select all my OG etc and apply a blank material to them they will all go grey and my FPS will increase.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000134.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000135.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000136.jpg

And if I apply the material back onto the entire selection note how the cars and logs are now brown since they use the bark material

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000137.jpg

You can alternatively just go though each material and turn off the **show in viewport**, button which then *should* still have the material render with its transparent leaves when doing the lightmaps but this takes longer than just swapping materials, depending on your system, how many transparent objects and materials you have etc.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000138.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000139.jpg

Last things I would now recommend you do is first set all these objects to use a "Green" colour so you can easily see them from the other objects in wire frame view etc and then to add all these objects, except the Reference Objects, to the *Overgrowth Helpers* layer (I'm also going to rename mine to *Overgrowth*).

Then finally I would also recommend you group them all up into an *Overgrowth* Group so they don't take up loads of room on the object selection list.

Then do the same to the Reference objects, except give them a different colour like Yellow or something

   #. Make a new *References* layer for them
   #. Set the Layer so it is not included in the render by clicking on the little teapot icon so it goes away

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000140.jpg

      .. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000141.jpg

   #. Hide that layer

      .. figure:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000142.jpg

         Since we should not need them any more but best to keep them in the scene in-case we do and since all the objects are now instanced to them, if we want to make any tweaks we can just change the main Reference object and have it applied to all the others
