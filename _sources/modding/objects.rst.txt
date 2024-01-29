
Steps to Making Objects for BF2
===============================

By *Z-trooper*

Creation of Geometry
   Make the 3D model

UV Mapping
   The process of mapping all of the surfaces of the model onto a single ""picture"" where you can paint each surface.

Texturing
   Painting these surfaces. Texturing also depends on what kind of game engine you are making it for. BF2 and newer engines have a "minimum" of 3 types of texture maps

   Diffuse Map
      Collor of the texture itself.
   Color Map
      Simply painting all the surfaces the way you want.
   Specular map
      This map controls how shiney/matte the object is, and where. For instance, you probably want it to be shinier where you painted metal on the diffuse map, and darker where you painted wood or paint. A specular map is critical to giving the object material definition. This is usually a greyscale image (but newer engines handle 24bit color spec maps).
   Normal map
      This can be explained as a way to make the object seem more detailed. What it does is using an image as displacement vectors, the red and blue channels control the two side axis displacement where the green channel controls the 'up's and 'down's. A normal map is basically an optical illusion. Its predecessor, the 'bump' map only had the info of the green channel, up/down. This was a greyscale image. Some people still call normal maps for bump maps for some reason.

#. **Preperation for export to game engine**

   So you've made a sniper rifle, but how do the game know how to use it and what parts are movable? Or you've made a building, how does the engine know when it hits it without killing all of the computing power?

   Some terms you may hear used in releation to BF2 (and various other engines)

      lod
         "Level of detail" model. When you are 100m away it is a massive waste of computation power to 'render' a gun or building with all of its details since you can't see them any way. So we make different versions of the same model depending on distance, and in case of weapons (and vehicles); 1st person and 3rd person versions along with scoped in versions.
      col
         "collision" model. To figure out if a vehicle collides with a massive detailed building does not require to know all of the details of the window and door frames and whatever ornament there is. It only needs an outline of the building. The player needs more resolution to the model, for instance holes where there are doors and the inside of the building. Bullets need almost full resolution so it can determine if you hit the wooden frame of the door or the concrete of the roof on the 2nd floor.

#. **Export**

   All of these elements are now grouped and organized into a hierarchy inside the modeling environment, so that the particular game engine may recognize which models are for colision, level of detail or which parts of the guns are movable.

#. **Animation**

   If it is a weapon then all of the movement of the arms, gun ect needs to be defined. Here you manipulate the so called 'bones' inside dynamic geometry (like soldiers) that then moves the model.

#. **Coding**

   Here you tell the model which parts are made of what materials, what reload time, fire rate, mag size, what sound files to use, speed, place where shell casings come out, where the muzzle flash and many many other things.

#. **Testing**

   Testing often reveals issues which require you to go back through several of these steps to fix stuff, but it is vital to ensure good quality and game experience.
