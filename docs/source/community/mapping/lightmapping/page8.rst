
Creating Reference, Shadow Casting Objects
==========================================

Here we are going to be replacing all our current Overgrowth meshes, helpers and other objects with "Reference" objects that are setup with transparent materials etc so they cast the shadows we want them to. We unfortunately can't just slap a material on the current Overgrowth meshes you've imported since they don't have the proper UVs to do so. As such we must import some.

Note that after reading this section, it's worth reading post 2 in this thread as it contains a link to a max-scene already containing many completed reference meshes for you.

`https://www.realitymod.com/forum/f18...ml#post2096455 <https://www.realitymod.com/forum/f189-modding-tutorials/134649-advanced-3dsmax-lightmapping.html#post2096455>`_

For my first example I'm going to fix up ``af_palmbush_01``. First we need to import the proper mesh so go to **Bf2 > Bf2 Utilities** and hit the **Mesh Import** button. Then browse to the location of the object and select its main ``.con`` file and it will import the mesh and its lods.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000064.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000065.jpg
   :width: 750px
   :height: 630px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000066.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000067.jpg

First thing to do is delete the unnecessary lods and helpers, just leaving the ``lod0`` mesh, which you need to convert to an Edible Polygon.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000068.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000069.jpg
   :width: 750px
   :height: 406px

Now we need to setup the materials. If you struggle with this next bit I would advise you to read `this tutorial <https://www.realitymod.com/forum/f189-modding-tutorials/117705-working-multi-sub-object-materials.html>`_ here as it will explain how to use Multi-Sub/Object Materials like I'm going to be using.

First we need to find out what textures this object is using so browse to the mesh and open it with BfMeshView, or a similar program, and we can see that this OG object only has one leaf material, which is what we are interested in here, and its uses the ``leaf_af_palmtree_b_de.dds`` texture.

Next select an unused material slot and click the "Standard" button in the top right, then select "Multi/Sub-Object" to change the material to that part. Click ok on the window that pops up and rename your new material to something like **Overgrowth**.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000074.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000075.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000077.jpg

Next in the first box right of 1 under name, put in the basic materiel name and this is going to be our bark material so call it "Bark" and give it a brownish colour so you can easily spot it.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000078.jpg

Go to parent and call this material the name of the texture its using, which in this case is ``leaf_af_palmtree_b_de`` and then in the diffuse slot, put that texture in like so.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000079.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000080.jpg
   :width: 750px
   :height: 630px

Now before we go any further we should just look at what Material IDs this object uses, go into face selection mode, scroll down to Polygon Properies on the right and open up the drop down box and you will see that it has two materials, 1 being bark and 2 being the left as we want so this doesn't need any changes.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000082.jpg
   :width: 750px
   :height: 406px

But if we apply the current material to this the leaves aren't transparent but we do have the texture on them.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000087.jpg
   :width: 750px
   :height: 406px

This is because we need to assign an **Opacity Map** by clicking the ``None`` Button next to **Opacity**, select bitmap and browse to the texture.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000083.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000084.jpg
   :width: 750px
   :height: 630px

At first, however, nothing will change since the texture is trying to read the RGB colour for its transparency and its not in there, its in the alpha channel. As such in the Bitmap Parameters we need switch the **Mono Channel Output** from RGB Intensity to ``Alpha`` and now the leaves should be transparent like so.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000086.jpg
   :width: 750px
   :height: 406px

Finally we need to give the leaves a backface since they currently don't have one, which you can see if we look up from underneath.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000096.jpg
   :width: 750px
   :height: 406px

This is because Overgrowth in BF2 draw their back faces but in Max we need to give them some manually in order to ensure they cast a shadow. Select all the leaf materials (in this case there is only one) faces and then click the **Detach** button, select **Detach to Element** and **Detach as Clone**, then hit the **Flip** button which will flip our cloned faces around, giving us the back faces we want.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000097.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000098.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000099.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000100.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000101.jpg
   :width: 750px
   :height: 406px

Then I would recommend renaming these fixed up OG objects to have a prefix of ``_REF_`` so you know its a reference geometry which you will replace all the others with later.

Then continue to do this for all your overgrowth object types and other objects with transparent materials etc you have in your map and if other objects use the same textures, assign them to both use the same materials to save you time setting them up.

Next object I'm going to fix up is the ``jungle_palm_small_01``.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000088.jpg
   :width: 750px
   :height: 525px

Just do the same as above with putting the new leaf material, in this case the ``nam_palmtreefrond_01_c`` texture in the next available slot and apply the material to the object. But in this case there is a small issue since not all the material IDs match and the other leaf texture is on the trunk of the tree:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000089.jpg
   :width: 750px
   :height: 406px

If we look at the face material IDs we can see that one of the bark textures is set to `MatID 2`, which is the leaf texture we did for the other one and we need to reassign it to our proper Bark Material, 1.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000090.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000092.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000091.jpg
   :width: 750px
   :height: 406px

Now for the ``kentia_palm_cluster01``, its materials are a little odder with its leaf being material 1, which is our bark material, and the trunk being material 2, which is one of our leaf textures but we need it to be 1, our bark. The import thing here is not to by mistake assign the bark first to 1 as then you wont be able to select the leaf though materials since they will both be mat ID 1. As such you want to assign the leaf first to in this case, MatID 5 from 1 and then assign the Bark to 1.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000094.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000095.jpg
   :width: 750px
   :height: 406px

For the Wire Fence series, which are not overgrowth objects but statics with transparent materials, the process is more or less the same but with a few differences. The biggest difference is that because its not an Overgrowth object, it already has the back faces for the transparent materials so we don't need to clone and flip the transparent faces like we needed to do for the OG Objects.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000102.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000103.jpg
   :width: 750px
   :height: 406px

First things we need to do like before is to import it, delete all the unnecessary helpers and LODs, leaving only the ``lod0`` mesh, then converting it to an edible poly and renaming it to have a ``_REF_`` Prefix. Then we need to go and find the transparent textures it uses, which is ``common_alpha_01_de``. Also its import to note that the alpha material in this case isn't the **Colour**, channel 1 material, but the **Detail**, channel 2 material, indicated by it being second on the list of materials.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000104.jpg
   :width: 750px
   :height: 525px

Before we get into that, assign the materials to our mesh and assign the non-transparent metal material to be the Bark material, and while yes it is not Bark, the Bark material is just a generic material that isn't transparent so light wont pass though it and as such, it serves the same purpose here.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000106.jpg
   :width: 750px
   :height: 406px

Now as you have probably noted in the above picture that even thou I have assigned the correct material to the wire, the UVs are not right for it and the wire texture is wrong.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000107.jpg
   :width: 750px
   :height: 406px

This is because as noted above, the texture is a detail, channel 2 material and is currently using the channel 1 UVs. As such we need to change the **Map Channel** to 2 so it uses the right UVs.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000108.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000109.jpg
   :width: 750px
   :height: 406px

Now its just a matter of applying the alpha and a small trick I forgot to mention above is that you can clone your **Diffuse Material** by dragging and dropping it onto the other slot and then telling it to be a copy of the above material. Then all you need to do is change it to use the alpha material.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000112.jpg
   :width: 750px
   :height: 406px

It is also worth noting that the Diffuse Material isn't actually necessary to apply for the rendering process, only the Opacity material but its easier to see what your working with and that the materials are correct with applying both.

One other thing you may want to consider is deleting the tiny bits of barb wire on the top, since these are so small they aren't going to cast any kinda shadow and are just going to slow down rendering time so its kinda worth deleting them and this can be applied to other objects that ONLY cast a shadow like these (if they also are meant to receive shadows and have a lightmap then you will be deleting faces that won't get shadows on them after its LMed) to speed up rendering time etc.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000113.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000114.jpg
   :width: 750px
   :height: 406px

For the Civi Car, for its reference I'm not going to bother applying any transparent materials to it since the only transparent materials it has on it, is the windows and for them, its simplest we just 100% delete them as the light difference passing though is marginal, but far easier to process no faces than a transparent material. But you may wish to make sure that all the faces on the object are using MatID1 so if you do apply the material to it, it will only be the Bark Material:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000115.jpg
   :width: 750px
   :height: 406px

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000116.jpg
   :width: 750px
   :height: 406px

Finally its worth pointing out that for overgrowth objects etc that have no transparent materials on them, or need no tweaks from their existing mesh to cast the right shadows, you don't need to import and fix up a Reference mesh to replace them with, since there is nothing to change. This is unless they have only be imported as a helper of course, as then you will need to replace them with a mesh but no need to fix up their materials if they have no transparent ones.

In total I have 45 Different Reference Objects required for my map.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000118.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000119.jpg
   :width: 750px
   :height: 406px
