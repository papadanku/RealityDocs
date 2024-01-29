
Running The Debugger in PR:BF2 v1.X
===================================

The BF2/PR debugger is extremely helpful in tracking down bugs that don't give error messages, but it does require a bit of knowledge on how to read the log messages.

#. :download:`Debugger files <https://files.realitymod.com/resources/Debugger_files.zip>` and :download:`menu files <https://drive.google.com/file/d/1ZWQdh90h0eTIO9okBuOxm7SRyMxavCNS/view?usp=sharing>` modified to work with the debugger (they are quite outdated compared to the release version but it doesn't really matter).
#. Extract Debugger files into your root Project Reality folder (i.e. ``C:\Program Files (x86)\Project Reality\Project Reality BF2\``) and modified menu files into ``mods/pr_edit/content``.

    Do it AFTER you have completed step 4 from the editor setup tutorial.

#. Run the normal PR launcher

    :menuselection:`Right-click PLAY --> Launch Debugger`

#. Next you'll need to make a profile that will function properly in the debugger

    :menuselection:`Manage Profiles --> Create a New Offline Profile`

#. Convert to a debuffer profile

    :menuselection:`Your profile --> Convert Profile`

#. Depending on what you want to do, you may want to go back to the :guilabel:`Options` menu through the launcher, select debugger profile in order to lower resolution and disable fullscreen. That's because fullscreen only produces logs while windowed mode also shows error windows for more important errors.
#. Go back to the debugger screen :menuselection:`Right-click PLAY --> Launch debugger --> Select your new profile --> log in`

When you're running the debugger in windowed mode, you'll get error messages popping up all the time when loading. Generally, these are messages about texture coordinates, which can be ignored. Simply press Continue through them all.

Log messages are output to ``mods/pr/logs``.

    You'll get 2 log messages, a BFLog and a Debug log. The Debug log is lots of stuff about what it's currently doing, and the BFLog is more similar to the standard error messages that pop up, and is more about errors rather than notifications.

.. note::

    Generally, any errors and crashes will be the last thing in the log, but not all the time. We have found that errors relating to collisionmeshes won't be the last error, and sometimes some other things. So, go back through the Debug log looking for "Error" or "Warning" messages (you'll notice things start with Debug, Warning, Error, Assert, etc), and see if it's anything about something you've just modified. That'll generally be the problem there Good luck and if something doesn't work out then come to the community modding forums and make a thread about your issue.