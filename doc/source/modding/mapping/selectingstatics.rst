
Selecting Statics to Optimize Performance
=========================================

I've been finding quite a few mappers have been making this mistake quite a lot recently and finding myself explain this a few times over recently and so I feel its necessary to fully explain this as quickly and simply as possible so hopefully I won't have to re-explain this to another mapper in the future.

The Basics & vBF2 Statics
-------------------------

Basically how most statics in BF2 work is that they all share a series of textures between them all grouped up onto a few large texture sheets known as "texture palettes" and they generally look something like this:

.. image:: http://i.imgur.com/H5QH4.jpg

Now in vBF2, there are a 5 main "series" of texture palettes, these are:

- ``common``
- ``industry``
- ``military``
- ``_asia``
- ``_middle-east``

These all have there own set of around 15 texture palettes each, combining many different types of textures that are used on pretty much all the statics ingame. They are separated into different series other than the "common" texture palettes, since they do not interchange for reasons which I'll go into why later on. More info on each of the series:

``Common``
    ``\objects\staticobjects\common\textures\``

    **Common** texture palettes as the main well suggests, is basically used by everything and anything and houses a wide range of ``common`` textures, such as metal, wood, corrugated iron etc etc in a range of different texture palettes.

    There are some statics that "only" use common texture palettes and nothing else. These are called "common statics" and are located inside the ``\objects\staticobjects\common\`` folder (although some like the ``buddha_statue`` are not, they are just badly filed statics) and contain items such as wire fences, wheelie bins, wooden crates etc.

``Industry``
    ``\objects\staticobjects\industry\textures\``

    **Industry** is another somewhat common type of texture palette that is used on most maps, but that is because most maps use industry buildings such as warehouses, power stations etc. These textures are however, more about heavy duty concrete, tread plates etc and are only used on Industry statics in the ``\objects\staticobjects\industry\`` folder.

    .. note::

        This has a ``uniqueobjects`` folder, containing objects such as the "Kubra Dam", which not only use the Industry textures but also some unique textures that only they use such as the textures in ``\objects\staticobjects\industry\uniqueobjects\dam\textures\dam_01_c.dds``.

``Military``
    ``\objects\staticobjects\military\textures\``

    **Military** is also another type of somewhat common texture palette that is used on most maps, but that is because most maps use military buildings/objects such as sandbags, bunkers, vehicle shelters etc.

    .. note::

        This also has a uniqueobjects folder, containing objects such as the USS Essex Carrier, which not only use the Military textures but also some unique textures that only they use such as the textures in ``\objects\staticobjects\military\uniqueobjects\us_c arrier_wasp\textures\hull_de.dds``.

``_Asia``
    ``\objects\staticobjects\_asia\village\textures\``

    **_Asia** is all about Chinese texture palettes, however they have been known to be used on Vietnam maps etc. These texture palettes contain textures such as Chinese Roofing Tiles, brick work, Chinese signs and writing and are used on all the Chinese Statics.

``_Middle-East``
    ``\objects\staticobjects\_middle-east\city\textures\``

    **_Middle-East** is all about Middle Eastern texture palettes, however they have been known to be used on Chinese maps using the ``_woodland`` version of their textures to pass them off as Chinese Buildings (mainly for towns/cities, will go into this more later). These texture palettes contain textures such as concrete, brick work, tiles, flooring and Arabic signs/writing.

    .. note::

        This also has a uniqueobjects folder, but only containing the mouse which has a few of its own unique textures such as decorated tiles, as well as using the normal middle eastern textures.

PR Statics
----------

PR statics on the other hand are a little more tricky. Since we didn't think too much in the early days about our folder structures or what statics where loading what textures, or even how we where really using our own new textures, its all quite a mess. With our new statics we are making we are organising it a lot more but for the old statics, its not really worth the effort to fix the folder structure, which we can't really make anyways for the most part.

PR' Static Textures are also generally not "palettes" (ie, lots of textures grouped up into a single sheet to reduce materials / draw calls) but more lots of individual textures that can be tiled in all directions which is a lot easier for the Static Modeller, but not so good for ingame performance.

.. image:: http://i.imgur.com/MmzvF.jpg

This however means you can use an individual static without it loading a massive palette without 90% of the texture sheet not being used if that's just the only static from that "series" your using, like for vBF2 statics, but still means you shouldn't put down only one of a static that loads a, or a bunch of brand new textures in, as its still not worth it unless you use that static enough to justify it (will go more into that later).

Also many of PR's statics load vBF2 texture palettes, mainly our new Middle-East buildings etc but there are some statics in there you wouldn't expect to be loading them, that are.

For PR's statics you really are going to have to look up what textures the static is really using before you decide to use it.

Finding Out Exactly What Textures The Static Loads
--------------------------------------------------

This is mainly for finding out what textures a PR static uses since you can't tell from folder location, but this can be used for any vBf2 static, or in fact, any model ingame including weapons and vehicles.

There are a few tools that you can use to find out (and even edit) the texture paths of a mesh but the most user friendly one by far is BFMeshView. Download and install the latest version of this if you don't already have it.

Then when you want to find out what static uses what textures

    #. Browse to the static's ``.staticmesh`` which you can find in its ``Meshes`` folder. For example, if I wanted to find out what textures the ``citybuilding_4a`` located in ``\objects\staticobjects\pr\citybuildings\``
    #. I would go to ``\objects\staticobjects\pr\citybuildings\citybuilding_4a\Meshes\`` and in there you will find the ``citybuilding_4a.staticmesh`` file
    #. Open ``citybuilding_4a.staticmesh`` up with BFMeshView by:

      #. Dragging and dropping it into the BFMeshView window
      #. :kbd:`RMB` on it, go to open with then select the bfmeshview.exe in the :menuselection:`Choose Default Program` list (will need to manually browse to where you have installed it and select it).

Once you have the static open in BFMeshView, you should have a list of geoms, lods and materials on the left hand side, right click, expand all to expand all the materials and geoms and then it should look something like this:

.. image:: http://i.imgur.com/J2PlG.jpg

For a staticobject, your mainly interested in ``geom0``, ``lod0`` but its worth looking though all the other lods just to check they don't load any new textures not loaded by ``lod0``, but generally, all the textures that will be loaded by a static, will be in its ``lod0``.

For the ``citybuilding_4a``'s ``geom0``, ``lod0`` we have a total of 7 materials (including ``material 0`` on the list):

.. code-block::

    geom0
     lod0

      Material 0
      Technique: BaseDetailDirtCrackNDetailNCrack
      Type: 0
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_c.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_obj_01_de.dds
       Texture: objects/staticobjects/pr/textures/null_di.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_cr.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_obj_01_deb.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_crb.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

      Material 1
      Technique: BaseDetail
      Type: 0
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_c.dds
       Texture: objects/staticobjects/common/textures/city_paving_de.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

      Material 2
      Technique: BaseDetailDirtCrackNDetailNCrack
      Type: 0
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_c.dds
       Texture: objects/staticobjects/common/textures/common_01_de.dds
       Texture: objects/staticobjects/pr/textures/null_di.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_cr.dds
       Texture: objects/staticobjects/common/textures/common_01_deb.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_crb.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

      Material 3
      Technique: BaseDetail
      Type: 0
       Texture: objects/staticobjects/common/textures/aircon.dds
       Texture: objects/staticobjects/pr/textures/null_de.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

      Material 4
      Technique: BaseDetailDirtCrackNDetailNCrack
      Type: 0
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_c.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_03_de.dds
       Texture: objects/staticobjects/pr/textures/null_di.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_cr.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_03_deb.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_crb.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

      Material 5
      Technique: BaseDetailDirtCrackNDetailNCrack
      Type: 0
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_c.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_de.dds
       Texture: objects/staticobjects/pr/textures/null_di.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_cr.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_deb.dds
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_crb.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

      Material 6
      Technique: BaseDetail
      Type: 0
       Texture: objects/staticobjects/_middle-east/city/textures/mecity_01_c.dds
       Texture: objects/staticobjects/common/textures/conc_256_de.dds
       Texture: Common\Textures\SpecularLUT_pow36.dds

As we can see this static mainly loading the ``_middle-east`` texture palettes with the odd common texture in there too. If we also look over the lods we can see its not loading anything different from ``lod0``, just fewer materials with some of the ``lod0`` materials/textures missing.

.. note::

    ``null`` textures such as ``objects/staticobjects/pr/textures/null_di.dds`` are tiny dummy textures that are loaded by many objects just so the object exports without issues, don't worry about them if you see them.

Using this method you can find out exactly what textures your static is loading and then make an informed decision on if it should be used on your map.

What Statics/Textures You Should & Should Not Be Using
------------------------------------------------------

This is the bit that confuses most mappers and really what this entire info post leads up to but you need to read all of the stuff before to fully understand this bit.

Basically if a static should or shouldn't be on your map isn't just about dose it look right and fit in with all the other statics from an artistic POV. Its also very much about how much this static "costs" in terms of client resources and the biggest cost is always in textures, since in BF2 these are loaded directly into the RAM and since we only have a max of around 2GBs to 3GBs to play with depending on what type of OS the client has and how they have it set up, even if they have physically more RAM in there system. This may sound like a lot, but when you stack everything up, we are very much on the limit in PR and in the past we have had clients CTDing on map load/mid game from running out of RAM and had to do major optimizations to our vehicle/weapon textures because of this. With the mod always getting more and more weapons/vehicles in it, and more different types of these weapons/vehicles being stashed onto maps, its VERY important that mappers optimize there map usage as much as possible, otherwise people may very well end up CTDing on map load / mid game on your map, due to running out of RAM. Also its worth noting these CTDs can happen after loading two+, highly demanding maps in a row, since BF2 isn't very good at flushing the memory before a new map load.

The biggest way you can cut back on this is by not using the odd static in your map that loads a wide range of texture palettes, 90% of which the texture space isn't even used by that single static and doesn't really do much for your map to justify all that RAM being used.

For example, if your making a map based in China/Asia, and are mainly using a bunch of Chinese Village statics and only making the odd small village with them, you then should NOT shove in a Middle Eastern city static into the middle of them, not because it doesn't fit because the colours, textures look more or less the same and even the writing on them is in Chinese (since they use the "_woodland" textures on a woodland map), but because that static, lets say that ``citybuilding_4a`` building we looked at above, is loading a whole load of ``_middle-east`` texture palettes which have so far not been loaded in the map. In all talking around 6.3mbs for this one building (which might not sound like a lot but its a huge amount for a single static), which around at a guess, 1/2 of that isn't even being used physically on this static and since this usage isn't repeated like the Chinese Village buildings over and over, its even more of a waste.

If on the other hand your making the same map above, but you have or planning to have a large town/city made out of ``_middle-east`` statics like on Shijia Valley, because there are no Chinese city statics and do look somewhat Chinese with their ``_woodland`` textures, then that is fine because your using a whole range of these statics in your map and its even now ok to shove that single, ME static into that village if you feel it fits.

Conclusion
----------

At the end of the day, if that static loading those textures is something you, the mapper are going to have to work out for yourself, or if you need help, post on the forums in your mapping topic asking if you should or shouldn't use this static in your map. But from now on, before placing down a static in your map, first ask yourself, what textures is this static loading and is it worth the cost?

I hope this helps,
Cheers!

*Made by Rhino*
