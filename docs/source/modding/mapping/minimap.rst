How To Make The "Perfect" MiniMap
=================================

In this tutorial I will explain how to make the "perfect" minimap for your map with all the objects, trees etc. drawing on it.

Requirements
------------

Tools
^^^^^

:BF2 Editor: :download:`BF2 Editor <http://files.ancientdev.com/prbf2/PREditor.zip>`
:Photoshop: :download:`https://www.adobe.com/products/photoshop.html`
:NVIDIA DDS Plugins: :download:`http://developer.nvidia.com/object/photoshop_dds_plugins.html`
:RAM: The bigger the map, the more RAM you are going to need.

Materials
^^^^^^^^^

- Map with the editor colormap or detailmap files etc.

   Needs to be finished for best results.

- Completion of `Setting Up The BF2 Editor for PR Mapping/Modding <https://www.realitymod.com/forum/f189-modding-tutorials/14468-setting-up-bf2-editor-pr-mapping-modding.html>`_

----

Getting Started
---------------

:download:`Download these files <https://files.realitymod.com/prbf2/perfectminimapfiles.zip>`. Once downloaded, you will need to install them into the correct places. You should have 2 folders with in that ``.zip`` file, a ``BF2`` and a ``Photoshop``, BF2 folder is BF2 files used by the editor, and Photoshop is Photoshop files used by Photoshop.

   Lets install the Photoshop files first.

   #. Open the Photoshop folder with in that ``.zip``, and you will see 2 files, ``MiniMap 1024x2.atn`` and ``MiniMap 1024x4.atn``
   #. Extract these files to ``C:\Program Files\Adobe\Adobe Photoshop CS3\Presets\Actions``

      Bare in mind that this path may be different if you have installed Photoshop in a different location, or have a different version and I'm not 100% sure if it will fully work with older versions but it should, if not, report back here (you will see what they are used for later on).

   #. Open up Photoshop and once its open, double click on both of these files to load them

      Should switch to Photoshop each time but at first it will probaly look that nothing has changed

   #. To check they are installed, go to your actions window, should be on the right hand side, if not go to :menuselection:`Windows --> Actions` :kbd:`Alt-F9`

      You should see afew folders in there, 2 of which called the same names as the files you double clicked on:

      - ``MiniMap 1024x2.atn``
      - ``MiniMap 1024x4.atn``

If they are there, they should be installed, if not, post below for help. Now we will install the BF2 Editor files:

   #. Browse to ``C:\Program Files (x86)\Project Reality\Project Reality BF2``

      This may be in a different location depending if you installed it on another hard drive or in the non-default location

   #. Go into the BF2 folder of the ``.zip`` and you will see 2 files in there:

      - ``makeMegaMap_1024x2.con``
      - ``makeMegaMap_1024x4.con``

   #. Extract them into the ``Project Reality BF2`` folder

Close Photoshop, we wont be needing it for abit and open up the BF2 Editor, loading your preferred mod etc. Once loaded,

   #. :menuselection:`Tools --> Options --> Miscellaneous`
   #. In there you will see a bunch of boxes you can fill in. Put:

      - ``CustomCommandFile1`` in ``C:\Program Files (x86)\Project Reality\Project Reality BF2makeMegaMap_1024x4.con``
      - ``CustomCommandFile2`` in ``C:\Program Files (x86)\Project Reality\Project Reality BF2makeMegaMap_1024x2.con``

Now, open up the BF2 Editor and your map with the Level Editor and we can get started.

Basic MiniMap (Temporary/Preview Use)
-------------------------------------

Just encase you do not know how to make a basic minimap already, I will go though how to do that now. It's normally a good idea to generate one of these for just a preview of what it will look like before you might go though a lot of work depending on your map size and its also good for just a temperate minimap used for Test builds etc and when your map is final you can replace it with your "perfect" final minimap. To do this, with your map open in the level editor and in the :menuselection:`Editor --> General` bar on the right.

If you click on the generate button, you will probaly have to wait a few seconds then will pop up a small preview in the top left corner of your main view of the minimap you have just generated.

As you can see, it looks pretty crap in its current state, lots of objects missing and just a load of shadows on the ground. You can also use this for navigation as you can see, there is a little green box on the map with the location of your camera, click on a diffrent location on the MiniMap and your camera will warp strait too there. I tbh don't use it much as a navigation tool as it blocks too much of your view, need to generate a :guilabel:`2048x2048` image and keep it loaded which kinda defeats the point, but its up to you, there if you need it.

After this MiniMap is generated, it saves it (and overwrite any previous MiniMaps you have unless backed up) to the editor folder of your map.

Advanced Tweaks
---------------

The following steps we are about to take will make your minimap look that little bit nicer. Most of them I have added to the scripts you have installed so you do not have to type them in each time, but there are a few that you need to do manually before generating the final minimap.

.. note::

   Do Not save any of these map changes made from this point, they are only made to make the minimap look better, and will not necessarily make your map look better.

First tweak that needs to be made is with your roads.
   Switch to the Roads Tool and then in the Editor bar too the right, click on the :guilabel:`Build All Final Roads` Button.

   This will "snap" your road texture dead onto the terrain without effecting the splines, and how the road will look in-game. It is just much slower for the editor to edit the splines when its like this, why it doesn't do it by default. This basically means that none of your roads on the minimap will be going under the terrain, and will always be on top.

   After that's done come out of the road tool, back into something like the move tool.

Second tweak we need to make is to the water.
   For some reason when rendering the minimap the water virtually rises by :guilabel:`1m` (or about), so to keep the same water level on the minimap as it is in-game, we need to move all the water down by :guilabel:`1m`.

   #. Go to your :menuselection:`Tweaker Bar --> Map Settings --> Water Settings``
   #. Lower your :guilabel:`Sea Water Level` by :guilabel:`1m`

   So my :guilabel:`Sea Level` after that will be :guilabel:`25.8`

   Bare in mind we are not going to be saving these changes on exit, this is only to make the minimap look correct.

   Now if you have any waterplanes in your map, you need to move these down by :guilabel:`1m` as well. Best way to do this is to select all your water planes on the map, then in the tweaker bar check what the :guilabel:`y` position is (as in x, y and z cordints) and just drag it as close as you can get to :guilabel:`1m` below where it was.

Third tweak we must do is to make all the overgrowth show up on the map as static objects.
   This means they will draw on your minimap in the positions they really are, tweaking your overgrowth draw distance will rearrange the positions of all your overgrowth, and then your overgrowth wont line up with the shadows on the terrain.

   To do this, all we need to do is lightmap one object in the map. This does not work for all users, but I think what you need is some sample files in your mod path which if you have the PR lightmap samples installed, it wont be a problem.

   - Best thing to do is pick a really simple, small object to relightmap.

      I always choose the :guilabel:`1m` crate where ever possible, just select it, and go :guilabel:`Trace Selected Item(s)`, and lightmap at the quility it was before (ie, should be final unless there is some reason why not).

   - After that objects lightmaps are done, you should now notice all the overgrowth on your map has turned to static overgrowth, turn your overgrowth off thou you should have not had it on before to check.

      Good way to check is to drag a selection box around it, if you can select it and you did not place it before, then thats good news and you are all set

Forth thing we need to do depending on your map is too run its texture mode.
   - Lots of statics like tents have Desert and Woodland textures and maybe others that you will want to show on your minimap as it will in game
   - Some maps may also use there own custom textures which if they are for big objects that will show on the minimap and will make a difference you will want to load

      Muttrah for example has its own textures to make all the buildings nice and white like they are in the real muttrah, which I am going to need to load for this

   - So all you need to do is load the correct Texture Suffix and then you're set

Final thing you need to do is switch to the :guilabel:`Detail Texture Mode` (if you are not already in it) by going to :menuselection:`Render --> Detail Texture Mode`, or press :kbd:`Ctrl-F4` (not :kbd:`Alt-F4`, that will close the editor)

.. note::

   *AFsoccer*: If you have problems after lightmapping an object (like the crate that Rhino mentions), then another option is to lightmap the closest terrain grid. So if you lightmap an object and your cursor turns into a hundred move arrows or you can't move your screen afterwards, then try lightmapping the terrain, using :guilabel:`terrain/primary/closest/final` as your settings. You'll want to have a backup of your terrain lightmaps so you can swap an old one for the one you're about to do, but it will accomplish this task and the new terrain shadows won't show up until you re-open the map (so the minimap will look the way it should). Hope that helps.

Generating The Minimaps
-----------------------

Now depending on what size map you have, you will have some different paths to take:

:A: 256x2 (0.5km²) and 512x2 (1km²) sized maps
:B: 1024x2 (2km²) sized maps
:C: 1024x4 (4km²) sized maps

256x2 (0.5km²) and 512x2 (1km²) Sized Maps
   This Step is for :guilabel:`256x2 (0.5km²)` and :guilabel:`512x2 (1km²)` sized maps, do it on maps bigger than this size and objects will be missed out in the minimap generation but it is still possible and a good alternative if you do not have enough RAM to generate very large minimaps that you need to in.

      Now this way I can't put in a bunch of commands automatically for you just before the minimap generation like I have for options :guilabel:`B` and :guilabel:`C` as we are going to go off the editors normal creation, but with a few tweaks. So first you will want to put in these extra commands into the conceal to make the objects draw and look nicer.

         - ``renderer.minCullDistance 2000``
         - ``staticMeshRenderer.noLods 1``

      Then after that, generate your minimap with the normal editor script by clicking the :guilabel:`Show` button in the minimap editor bar.

   Now skip to **Editing The MiniMaps**.

1024x2 (2km²) Sized Maps
   This step is for :guilabel:`1024x2 (2km²)` sized maps, do it on maps bigger or smaller than this size and it will probably not turn out very well, ain't tested but in theory it will miss out some of the map, or will capture the surrounding terrain but overall, will not be accurate.

   This step is pretty much the same as B apart from 1 small difference where you need to run a different minimap generation script.

   .. note::

      This is where you require the ram as here you are in fact generating **4** different minimaps.

      All you need to do (providing you have set them up already which you should have in Step 1):
      
      :menuselection:`Tools --> Custom Action --> Execute Custom Command File 2 [C:\bla bla bla\makeMegaMap_1024_2.con]`

1024x4 (4km²) Sized Maps
   This Step is for :guilabel:`1024x4 (4km²)` sized maps, do it on maps bigger or smaller than this size and it will probably not turn out very well, ain't tested but in theory it will miss out some of the map, or will capture the surrounding terrain but overall, will not be accurate. This step is pretty much the same as :guilabel:`C` apart from 1 small difference where you need to run a different minimap generation script.

   .. note::

      This is where you require the RAM as here you are in fact generating **16** different minimaps.

      All you need to do (providing you have set them up already which you should have in Step 1):
      
      :menuselection:`Tools --> Custom Action --> Execute Custom Command File 1 [C:\bla bla bla\makeMegaMap_1024_4.con]`

Editing The MiniMaps
--------------------

Here we are going to do some editing of the minimaps to make them look as nice and possible.

First of all, its best you exit the BF2 editor at this point, and if you have done a 4km map is is probably a good idea you also have a restart before going on.
Going to have to split this up into a a, b and c again due to different map sizes.

:A: 256x2 (0.5km²) and 512x2 (1km²) sized maps
:B: 1024x2 (2km²) sized maps
:C: 1024x4 (4km²) sized maps

256x2 (0.5km²) and 512x2 (1km²) Sized Maps
   For these sizes you only need to do some very basic edits to the minimap if you want to make the water look better, but this is really more Photoshop skills.

   Open the ``minimap.dds`` in ``/levels/*yourmap*/editor/minimap.dds`` with Photoshop, then do any Photoshop edits you want on-top with only to make it look better (don't use any filters) and then that's really it, you can skip to Step 6.

1024x2 (2km²) Sized Maps
   For this size you need to combined the **4** minimaps you have generated with my Photoshop batch files (or you can do it by hand) and then any water on the map you will need to blend in.

   With Photoshop open (with also the Action files installed which you should have done in step 1). Open up or crate a small file. Any file will do as long as its open and then you need to do is go to :menuselection:`File --> Automate --> Batch`. After that, you should save up what you have done and go onto Step 6.

   Then once that is all set, click :menuselection:`Ok` and let it run its magic

1024x4 (4km²) Sized Maps
   For this size, you need to combined the **16** minimaps you have generated with my Photoshop batch files (or you can do it by hand) and then any water on the map you will need to blend in.

   With Photoshop open (with also the Action files installed which you should have done in step 1). Open up or crate a small file. Any file will do as long as its open and then you need to do is go to :menuselection:`File --> Automate --> Batch`. After that, you should save up what you have done and go onto Step 6.

Saving The MiniMaps To Be Used In-Game
--------------------------------------

Now we are going to be saving our MiniMaps in the best format to minimize there impact on performance while still keeping them looking as nice as possible.

   While playing in-game, like any other texture the minimap has to be also be loaded and stored in the ram, just like a tank texture etc and there has been noticeable performance drop when saving the minimap in the wrong format or too high rez.

   Now EA's Minimaps are really low rez, saved in DXT1 and only ``512x512`` but they have also for some reason saved it with 10MipMaps which are not used and decrease performance. Still there MiniMap is only 170kbs which is nothing.

   We are going to be saving in DXT1, ``1024x1024` and with No MipMaps, and for ``1024x4`` maps it is maybe a idea to save with the same settings, but at ``2048x2048`` which will make the minimap 2mbs, but will be the same detail as a ``1024x2`` minimap. That bit is up to you and how much the extra detail means to you, but really when a user has over 1024mbs of ram normally 2mbs of that is not much, thou (``1`` / ``2``) the size cuts it down to (``1`` / ``4``) of the file size (512kbs). What ever you decrease you minimap too it MUST be a power of ``2``, otherwise there is a bug with ATI cards that it cant handle textures out of that rez and will screw up. so the texture must be either ``16``, ``32``, ``64``, ``128``, ``256``, ``512``, ``1024``, ``2048`` etc, etc.

So first thing we need to do is decrease the size of our MiniMap to ``1024x1024`` or ``2048x2048``.

   #. Go to :menuselection:`Image --> Image Size` at the top, this will open a new window
   #. In that window, put in your new :guilabel:`Width` and :guilabel:`Height` Pixel Dimensions and let it do its work
   #. Now its time to save this minimap. Go to :menuselection:`File --> Save As`
   #. Browse to ``/levels/*your map*/Hud/Minimap/`` and in there you will see 3 ``.dds`` files

      If you cant see them, switch the format to D3D/DDS ``*.DDS``:

         ingameMap.dds
            The main MiniMap seen by all players in there minimap view.
         commanderMicromap.dds
            - An unused minimap DICE was going to use for the commander view
            - DICE must have decided against it later on in the development stage and couldn't be asked to fully get rid of it
            - Like many other things in BF2. Best not to delete it, it "may" cause a CTD but tbh, ain't bothered testing
         commanderMap.dds
            - Another unused minimap DICE was going to use for the commander view.
            - DICE must have decided against it later on in the development stage and couldn't be asked to fully get rid of it
            - Like many other things in BF2. Best not to delete it, it "may" cause a CTD but tbh, ain't bothered testing

Anyways back to saving!

   #. Save up the ``ingameMap.dds``

      Double click on it to save over the old file, and match the DDS settings below.

      Now you can just leave the other 2 minimaps, but the best idea is too just resize to 32x32pixels, keeping the same DDS settings as above and save over the top of them to keep the overall size of your map down as that makes them only **1kb** each and keeps them there encase it will CTD if you deleted them, thou I don't think it would but this is just as good as deleting them.

   #. Pack it up with your map

And then you are done, you should now have a "perfect" MiniMap for your map

`Here you can find the Grid overlay used on PR maps <https://www.realitymod.com/forum/f354-community-maps/133780-map-grid-overlay-template.html>`_
