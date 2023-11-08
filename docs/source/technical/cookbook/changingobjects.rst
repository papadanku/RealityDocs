
Changing Objects At Runtime
===========================

Submitted by *Woody*.

Problem
-------

You don't like how some of the standard Python code that comes with BF2 works, and want to change it. Maybe you want to add your own RCon commands; maybe you want to change the way scores are kept. You *could* just hack the default code and make whatever changes you wanted, but if you do very much of that it becomes a maintenance nightmare, and things really could get ugly when you try to apply the next game patch that EA will be releasing "soon", and all your changes get overwritten.

Solution
--------

Python is a `dynamic language <https://en.wikipedia.org/wiki/Dynamic_language>`__, which, among other things, means that programs can change themselves even while they are running. We can take advantage of Python's dynamic nature to write code that dynamically modifies the properties of standard BF2 objects.

Example: Adding A New Property To An Object
---------------------------------------------

Let's say you're working on a new mod for BF2 and need for :py:class:`bf2.PlayerManager.Player` to track a new property, called ``karma``. If you look in the :doc:`Object Reference <../python/reference/objects>`, you'll see that Player Objects don't have a ``karma`` property, and you want to add one.

In Python, if all you want to do is add a new attribute to an object, you can Just Do It:

.. code-block:: python

    playerObject.karma = 0

There--it's done! If :py:class:`playerObject` is an instance of class :py:class:`bf2.PlayerManager.Player`, then we just created a new attribute called ``karma`` within that instance, and assigned it the value "0". There really isn't anything else to it--we can read and change that attribute elsewhere in our code at will, just as though it had been defined as part of the class from the beginning.

.. note::

    We didn't add this attribute to the :py:class:`bf2.PlayerManager.Player` class--we added it to a specific instance of that class, so only that one player will have a karma attribute. If we want other players to have a karma attribute, then we need to find their playerObjects and do the same thing. Assuming we've imported :doc:`bf2 <../python/reference/bf2>`, we could loop through and assign a karma attribute to all players by doing something like

    .. code-block:: python

        for playerObject in bf2.playerManager.getPlayers():
            playerObject.karma = 0

Discussion
----------

This cookbook entry just scratches the surface of what you can do with dynamic code modification. Before you start hacking around in the BF2's default Python code, please consider whether it might be cleaner to use an approach like this!

It may have occured to you, though, that *something* needs to be running that will make these dynamic modifications--and how does that *something* get to run in the first place, without itself modifying some of the standard code? The short answer is that these dynamic programming tricks are only possible if there is a "hook" you can use to cause this and other code to be run, and DICE put no such hook in their Python code. So, no matter what, at least **one** modification needs to be made to the standard BF2 code: at a minimum, an "import" statement needs to be added to one of the main files that will cause your code to be read in and executed... but that's a subject for another time...
