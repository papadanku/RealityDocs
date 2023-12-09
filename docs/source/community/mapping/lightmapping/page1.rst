
Introduction
============

I have been experimenting and refining Lightmapping with 3DsMax for BF2, for quite a few years now and I have been meaning to write up a tutorial on them for some time but never gotten round to it. After a few requests from fellow mappers and with the old 3DsMax lightmapping tutorial lost with BFEditor.org, I've decided its time to put down all my techniques on paper for any future mappers who might be able to benefit from them.

First of all I want to state the advantages of 3DsMax Lightmapping for anyone unsure if its worth it, including the advantages that are new in this tutorial.

   - 3DsMax Lightmapping is generally a lot faster than Lightmapping in the BF2 Editor (depending on the type of lighting you use), with multi-core processing and 64bit support, especially for large complex maps, even after you take into account the extra time for importing your terrain and all the objects etc.

      I have also managed to make this process even faster than the traditional method of 3DsMax lightmapping shown in previous tutorials, with generating all three types of light together at once instead of individually as before with max.

   - For Object Lightmapping the BF2 Editor generally takes around 3 and a 1/2 minutes to generate all the LODs of a single, complex static, where 3DsMax with Adv. Ray Traced Shadows takes around 2 and a 1/2 minutes for the same object and all its lod, saving a whole minute per object and in all taking around 70% of the time BF2 Editor takes.

      It should be noted thou that in full Ray Traced Shadows, which gives the best quality lighting, the lightmapping process dose take quite a bit longer at around 6 minutes per object and its lods.

   - For Terrain Lightmaps the savings are even larger, depending on the complexity of your map of course, since the BF2 Editor really struggles to render lots of overgrowth on the terrain, like the example map in this tutorial.

      For a single patch that was 2/3 sea water and didn't have that many trees on it, the BF2 Editor took 11mins and 41secs, where 3DsMax with Adv. Ray Traced Shadows only took 2mins and 38secs, which is a massive saving of around 23% of the time the BF2 Editor took on the same patch. Even when it came to Full Ray Traced Shadows in 3DsMax it took quite a bit less time than the Editor, taking 8mins and 20secs for the same patch which really says it all.

   - The Quality of the Lightmaps is far superior, depending on the settings and lighting method you use of-course, especially when it comes to overgrowth when setup with transparent leaves (as per in this tutorial).
   - The Lightmap Sizes are far more optimized than standard BF2 Lightmap Samples since many small vBF2, and even PR Custom Statics, have super large lightmap samples for tiny objects, resulting in a 512x512 texture for a small detached house which can easily be lightmapped in 256x256 without much loss of quality and being the same light pixel ratio as the other statics on your map.
   - You have far more control over your lighting and how objects have an impact on your map and the end result of your lightmaps as well than with the BF2Editor.
   - "Point Light" (Man Made Light such as light bulbs in buildings) can be done far easier, with much more flexibility and with better quality than in the BF2Editor.
   - No requirement of "Lightmap Samples" for all your statics to be present in order to lightmap them, which also allows for lightmapping xpack objects etc (although it is now possible to generate samples for most statics using Bf2MeshView, but doing this, especially for a lot of objects, is very time consuming).
   - Full Lightmap Padding (with new scripts) which helps cut down lighting errors in the mipmaps and is something the BF2 Editor doesn't have (although dose have a little padding).

.. list-table::
   :header-rows: 1
   :widths: auto
   :align: center

   * - BF2 Editor (Final Quality)
     - 3DsMax (Ray-Traced Shadows)
     - 3DsMax (Advanced Ray-Traced)
   * - |image1|
     - |image2|
     - |image3|
   * - |image4|
     - |image5|
     - |image6|
   * - |image7|
     - |image8|
     - |image9|

.. |image1| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg15_terrain_BF2Editor.jpg
.. |image2| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg15_terrain_RayTracedShadows.jpg
.. |image3| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg15_terrain_AdvRayTraced.jpg
.. |image4| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg17_terrain_BF2Editor.jpg
.. |image5| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg17_terrain_RayTracedShadows.jpg
.. |image6| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg17_terrain_AdvRayTraced.jpg
.. |image7| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg14_terrain_BF2Editor_LM.jpg
.. |image8| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg14_terrain_RayTracedShadows_LM.jpg
.. |image9| image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/method_examples/Adv_3DsMax_LMing_eg14_terrain_AdvRayTraced_LM.jpg

However there are a few disadvantages that you should be aware of:

   - Its a very complex process that for someone without any knowledge of 3DsMax and Rendering etc may struggle with but I aim to make this tutorial as straight forward as possible for any novices out there.
   - The setup process prior to lightmapping can be pretty time consuming with having to import all the static meshes of your map etc, especially if your going to setup all your overgrowth etc with transparent leaves etc as per this tutorial.
   - You need to manually set the lightmap sizes for each object, however pretty much all the statics in PR have been defined previously by other PR mappers and its only objects that aren't on the "Master Lightmap Sizes" List you will need to define.
   - Child Objects such as Ladders will not be imported with their parent meshes and will need to be added manually into Max in order to cast a shadow *(and to lightmap them if they require that but you can't lightmap Children in the BF2Editor either and Ladders shouldn't be ladders)*
   - Destroyable Objects can not be lightmapped in 3DsMax, at least not without a big complex work around and its best to generate them in the BF2 Editor with settings similar to those of 3DsMax.

      If a Destroyable Object has been made "non-destroyable" by code, then it will import the geom0 lods into Max and will lightmap them fine, but it will not import the geom1, wreck lods in and you will need to make 8x8px dummy lightmaps for the wreck lods which are required in order for the geom0 lod lightmaps to load ingame and will save quite a lot of lightmap space from generating them at full rez.

Before You Begin
----------------

Before you start the complex process of lightmapping your map in 3DsMax, you should ensure your map is truly final and has been tested as thoroughly as you can get it, with ideally having it looked over by other PR Mappers for issues you may have missed since any changes to your map after you've done all the work of importing your map into 3DsMax are very hard to replicate in 3DsMax and I will not be covering this side of things in this tutorial either and your probably best of starting this whole, complex process again from scratch to ensure there are no issues, unless you know excatly what you are doing.

Its also worth noting that it isn't really worth doing 3DsMax lightmaps (Lightmaps) for a test build of your map either, unless lightmapping with the BF2Editor on Medium/Low settings for the test, or not having any lightmaps for the test, is really not an option since the work involved to get your map in a state to be Lightmapped in 3DsMax, probably isn't worth it if your going to have to do it all again from scratch a few weeks/months later, but I will leave that up to you to decide. You could always skip a few steps like making all the leaves of the trees transparent for just a test build and do Adv. Ray Traced shadows rather than Ray Traced Shadows, both of which will also speed up rendering time, but having non-transparent leaves will look really, really bad and worse than BF2Editor lightmaps in many cases.

As such, just be aware of what your getting yourself into before you start this process.

Requirements & Tools
--------------------

- Battlefield 2 v1.5
- `BF2 Editor v1.3 <http://files.ancientdev.com/prbf2/PREditor.zip>`_
- The latest version of `Project Reality: BF2 <https://www.realitymod.com/downloads>`_ with a `pr_edit <https://www.realitymod.com/forum/f189-modding-tutorials/14468-setting-up-bf2-editor-pr-mapping-modding.html>`_ (or equivalent) working mod setup and working.
- 3DsMax9 (version 9 or later)
- `PR:BF2 3DsMax9 Tools <https://www.realitymod.com/forum/showthread.php?t=145720>`_
- `Adobe Photoshop <https://www.adobe.com/products/photoshop.html>`_
- A text editor such as Notepad.
- A decent computer

   The better the system, the faster the lightmap generation will be and the more RAM you have, the stabler it will be and will allow you to generate the super large terrain lightmaps.

- A finalised map ready for lightmapping

Make sure all of the above are installed and working before you start this tutorial.

.. note::

   Firstly I am going to be working with a ``pr_repo``, mod which is linked to our `SVN Repository <https://en.wikipedia.org/wiki/Apache_Subversion>`_ which is why you might see funny symbols on my folder icons etc but just ignore them and I will also be referring to the working mod as ``pr_edit`` in this tutorial for anyone not working our of the Developer SVN Server and if you see any reference to "pr_repo" in the screenshots etc just take note that is my working mod and just replace it with w/e your working mod it, be it ``pr_edit`` or whatever.

*Made by Rhino*
