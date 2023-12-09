Terrain Sea Water Depth/Transparency Lightmap
=============================================

As mentioned above the, red channel in the terrain lightmap is used to control the water transparency depending on the depth of the water, unlike statics where the red channel is used for point lighting. This is a pretty quick thing to generate since there is no shadowing required.

First load your lightmapping scene back up in 3DsMax\ **9** and then download and merge this **\_WaterLight** into your scene the same way you did for your sky lights: `https://media.realitymod.com/tutoria...t_Template.max <https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Lightmaps_Water_Light_Template.max>`_


This is a **Target Direct** Light, like your Sun Light, but its placed in the centre of your map and points directly downwards. By default the light is at ``0, 0, 50`` (X, Y, Z) and you should change the Z Axis value, i.e., the highest this light is placed at to be the same level as your sea water level, which in my case is 5m, or 50 units, which it is already *(Ignore that I have the light switched off, forgot to turn it on, the one in the template above is on by default)*

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000453.jpg

This light is already setup not to cast any shadows and to case the correct red light etc. The only change you may want to make is the ``Near Attenuation`` settings, which basically controls the start and end of the transparency, with the end being when the water is totally opaque, ie, once the water is very deep. When the terrain is lightmapped with the BF2 Editor the water becomes opaque at around 3.5m, which is what the ``End`` setting in the ``Near Attenuation`` is set to currently. If, however, you want your sea water to be more transparent increase this value and if you want it to be less, decrease this value. Since my map is a sunny tropical map with crystal blue water and with some coral reefs around the island, I want my water to be pretty transparent so I'm going to increase my ``Near Attenuation``, ``End`` values to 45 units *(4.5m and again, ignore that the light is turned off in the pics below)*.

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000454.jpg

Next, turn off all other lights in your map. Your map will turn black from there being no lighting and if you want to see your map again, right click on **Perspective** in the top left of your viewport and select **Configure...**, then in the **Rendering Method**, tab check **Default Lighting** and hit **ok** and your map will be back to normal again:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000455.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000456.jpg

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000457.jpg

Lastly select your ``_TERRAIN`` and turn off the ``Edit Poly`` and ``Vol. Select`` modifiers by clicking on the lightbulb icons to the left of both of these modifiers until they become grey and you should see your sea bed restored from the flat water surface they applied for the sun and sky lighting:

.. image:: https://media.realitymod.com/tutorials/Adv_3DsMax_LMing/Adv_3DsMax_LMing_000458.jpg

Now we just need to render this water light, hit ``0`` to bring up the **Render to Texture** window and **MAKE SURE YOU CHANGE THE NAME OF THE TEXTURE** as the last thing you want to do is overwrite your sun and sky terrain lightmap, which you should probably back up before generating the water lightmap just encase too. Other than the output file's name, the render to texture settings are all the same as before and you can probably render this fine in 3DsMax9 since its easy to process, unless it's an 8192x8192 texture, then you will need to do it in a later, 64bit version of max since Max9 wont have enough memory to save the texture.

.. note::

   It's worth noting that your overgrowth should be hidden and you may also want to hide your staticobjects too to speed things up a little but having them in view otherwise should not affect the render since the water light isn't casting any shadows.

