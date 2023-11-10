
Adding New RCon Commands
========================

Submitted by *Woody*.

Problem
-------

You want to create your own RCon command(s) to add administrative features to BF2. You really don't want to change the code for standard BF2 administration module, though, because you know modifying the standard code is a Bad Idea™.

Solution
--------

Use the dynamic object modification technique explained in :doc:`this recipe <changingobjects>`. Just import the following function from one of the main modules:

.. py:function:: registerRConCommand(command, function)

   Register a custom RCon command by dynamically adding a function that implements the new command as a new method of the default.AdminServer class.

   :param str command: The name of the new RCon command
   :param function: The function that implements the command

   .. code-block:: python

      import new, default

      def registerRConCommand(command, function):
         # Put the function into a new instancemethod object bound to the AdminServer
         newMethod = new.instancemethod(function, default.server, default.AdminServer)

         # Create a new class attribute in AdminServer that's wired to our function
         setattr(default.AdminServer, command, newMethod)

         # Add the new command into the rcon dispatch table, pointing to our function
         default.server.rcon_cmds[command] = newMethod

:py:func:`registerRConCommand` takes care of everything you need to do to create a new RCon command; to use it, you just need to define the Python function you want your new RCon command to execute, and then call :py:func:`registerRConCommand` to register your new command and link it to your function:

.. code-block:: python

   '''
   Create a function that executes our desired new RCon command; note that since this is going to be a method within a class, the first argument to the function MUST be "self", even if we don't use it. The admin module also passes "ctx" (command context) and "cmd" (the rest of the RCon command line) to our function.
   '''

   def rcmd_mycmd(self, ctx, cmd):
      # We can make our new command do anything we want here
      ctx.write("We're now executing mycmd.\n")

   # Now register the new RCon command
   registerRConCommand('mycmd', rcmd_mycmd)

After this code is imported, your new RCon command will be active; once you authenticate (``rcon login``) you can execute your command from the server console, or an in-game player console, by typing ``rcon mycmd``.

If you want to execute it from an RCon TCP connection, you just need to type ``mycmd`` (without the "rcon").

Discussion
----------

You can add as many commands as you want, each of which can implement any function you want--and they will behave exactly as though they were coded in the ``Battlefield 2 Server/admin/default.py`` file--even though you never had to change that file!

The reason this is so useful, and the reason why it's such a bad idea to just hack around with the standard files, is that doing so makes it very difficult to upgrade to a new version of BF2 later, plus, if you have multiple mods or add-ons that want to add their own RCon commands, they will very quickly start tripping over and breaking each other if they're all modifying the original code. This approach is much cleaner; in fact, you can have multiple scripts like this that are all developed separately by different people, but when they're imported, they behave gracefully with each other, with no problem at all (unless two developers choose identical names for their new commands).
