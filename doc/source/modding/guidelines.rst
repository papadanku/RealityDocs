
Guidelines for Community Assets
===============================

By *Z-trooper*

.. warning::

   **NO RENDERS**, they are fine when you want to show off your models friends, but if you want feedback and want them to go into PR then we need to see stuff that we can give feedback on. Simply take a screenshot of the viewport.

   You may use point light sources to help you show the model. 

Posting for Feedback
--------------------

We need the following type of shots below in able for us and other users to give you as much feedback on your model as possible. Keep in mind the more good shots you can give us of your model the more feedback someone can give you but dont go about taking lots of crappy shots as too many rubbish shots will more likley put someone off from giving you feedback rather than help them giving you feedback, so take what shots you need to and make sure they all show vital parts of the model that you need feedback on and are clear and use as much space on the shot as possible.

Wireframe screenshot :kbd:`F3`
   So we can see if the model has errors in the mesh. **These are best taken from the top, side and front views**... though sometimes a perspective view is good too.

Edged faces screenshot :kbd:`F4`
   So we can see if the model has errors in the mesh.

Screenshot without wireframe or edged faces
   So we can see if there are smoothing errors and to get an idea of how its going to look ingame.

.. note::

   When taking wireframe and edged faces screenshots, its clearest to see where the lines are when they are a solid black or solid white colour rather than a light green. To get your lines a solid black like the example shots of the harrier above, all you need to do is select all the models in your scene, and then assign them a black colour which you can either do in the objects properties, next to the name, or in the modifier tab at the top, next to the name.

   If you don't have any materials applied to your object it will now turn a solid black like. To get rid of this, apply a material to your object(s), if you have a texture you can apply to it good, if not a simple black standard material will do just fine.

References
~~~~~~~~~~

- Does your object look like what you are trying to make or does it just resemble it?
- Does your object have the necessary details to mirror its real world equivalent?
- Does your object have the correct proportions?

You need to be certain that your model (and textures) match the real thing, because we will have enough to do to look at your models quality and integrity alone. We don?t want to spend all of our time finding references and comparing it.

Frequently Asked Questions
--------------------------

"What Version of 3DsMax"?
~~~~~~~~~~~~~~~~~~~~~~~~~

Autodesk 3D Studio Max v9 or newer.

"Modeling, Poly & Triangle Counts?"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, around here we only deal in triangle counts (tris) since all polys etc are converted to tris on export into BF2 so dealing in polys when a poly could be 2, 3, or even 20 tris is not an accurate measure to go by when tris is. Always provide a triangle count for your models so we can get a good idea on how optimized the model is, with of course the screenshots with it.

"Triangle (Poly) Limits"
~~~~~~~~~~~~~~~~~~~~~~~~

Limits are hard to set, so we won?t. This is due to many reasons, the most obvious one being: it depends on what you are making!

A grenade and a jet fighter have vastly different levels of details.

In short you are your own master of the tri count if you work by the following guidelines:

- A vertex is good as long as it either adds shape or smoothness to a model, if it does not then it should be removed.
- Proximity to the player

   If something is right up in the face of the users face then it needs more detail than something that is further away or at a place where the player only views in rare circumstances.

- Silhouette

   As long as the silhouette of your object not jagged or look too low poly it is good.

- Keep in mind that the model (if weapon) will be animated and check that parts of the model does not suddenly become invisible when you pull back the charging handle or remove the magazine.
- Turn back face culling on to check that your object is not invisible in places.
- If you are making a vehicle make sure that all details on the hull, turret or whatever are a part of the main mesh, and not a separate element as this will cause Z-fighting.

The tri count of an object really depends on what the object is. For example one tank design may have smooth, flat surfaces all over it and hardly anything else, where anouther tank design may have something like reactive armour blocks all over it and lots of jagged edges. The tank with smooth flat surfaces would be most likley stupid to spend 8k tris on something that didn't need it where its tris would be probably spent on a really ultra smooth barrel since the body of the tank didn't need squat, and then the tank with reactive armour blocks and jagged edges all over it would maybe struggle to get all the detail with only 8k tris to work with so like said above, the tri count of an object really depends on what the object is and its design. You can always ask what sort of tri count you should be working towards but don't expect any good answers since no one can really give you an exact amount unless they are working on it.

"UV-mapping/Unwrapping?"
~~~~~~~~~~~~~~~~~~~~~~~~

You need to have your objects UV mapped before we will consider using it.

UV Mapping Guidelines
^^^^^^^^^^^^^^^^^^^^^

Use an appropriate aspect.
   For instance, if you are making a RPG tube it might not be wise using a 1:1 aspect map, but more suitable to use a 1:2 aspect (1024x2048 instead of 2048x2048) since the tube is very long and very thin and as such, will take up more width than height when UVing it but you also need to account for all the points on the model, if its a rifle a 1:1 aspect ratio may be required to fit on all the other bits like the magazine etc.

Maximize the space used on the sheets.
   In principle, every pixel you do not use on the UV map is wasted memory and also wasted detail. Maximize the UVs so that you can put more detail into the textures. Beware of grouping the UV groups too close together so that it causes pixel bleeding.

Proximity to the player.
   Be mindful of which parts of the object are close to the player. A scope is closer to the player than a barrel. Or a cockpit texture where you need detail on the instruments and screens is more important than having nice frames around them. Scale your UV groups accordingly to their function and proximity.

When UVing an object, use as few texture sheets as possible as the more texture sheets are used, the bigger impact the textures have on performance.
   For example, 4x 1024x1024 sheets (adding upto 2048x2048 pixels) has a much larger overhead on the engine than one single 2048x2048 texture sheet.

   The only time when you will want to consider using other texture sheets is if its such a large object that you can not fit all of the detail onto a single 2048x2048 sheet without it impacting on the look drastically (such as the Chinook) or when a common object is made for the object like a weapon scope like the ACOG which is used on (and can be used on in the future) many other objects that are not using the main textures of the weapon or w/e your UVing, so having the ACOG on its own texture sheet helps when the ACOG is placed onto anouther rifle other than a M16 or M4 and instead say an L85A2, so that when playing on the British Faction with a L85A2 with an ACOG, the player dose not need to load all the M16 and M4 textures that wouldn't be used anywhere in order to have that ACOG on his rifle. Another example would be the M203 UGL which is also used on many other weapons and as such, is best on its own texture sheet.
   But don't start putting every scope or small object onto its own sheet. For example if its a unique scope only for that Sniper rifle, put the UVs for that scope onto the main sniper rifle texture sheet.

   If you are unsure if your object is a common object that should go onto its own texture sheet or not, ask a developer in the forums or over PM.

"Texturing?"
~~~~~~~~~~~~

When working with your texture you should be working in a high quality format that dose not distort your texture on save such as ``.psd``

When you texture is final and is ready to be used ingame only then do you save it to a format for game use but keep in mind that you should always keep your ``.psd`` handy and upto date not only as a backup but for any changes needed to be done to the texture in future, its far better to work strait off the ``.psd`` so there is no loss of quality from resaving which ``.dds``, like ``.jpg``, has.
