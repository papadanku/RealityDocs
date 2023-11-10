
Reloading Modules at Runtime
============================

Submitted by *King of Camelot*.

Problem
-------

You're sick of having to restart the server everytime you make a change to your Python code. Simple changes that should take all of two seconds end up taking minutes because you have to shutdown and start back up a server just to see the effects of your coding.

Solution
--------

The fact that Python is a `dynamic language <https://en.wikipedia.org/wiki/Dynamic_language>`_ allows us to reload a module while the main Python code is still running. To accomplish this, I've broken it down into two parts: first a header file to set up the reload function and other odd ends, and then the module where you put your code.

The Header File
---------------

The header file will contain the function code to reload your module. Unfortunately Battlefield 2 allows you to register for events in your code, but doesn't let you unregister for them. This creates a problem because even though you have reloaded the module, the old code that is registered to an event will still run when the event fires. This causes both your old code and your new code to run at the same time, which as you can imagine is a far form ideal situation. To get around this little problem I decided to set up the events in the header file under a different name, and then when the event fires the code in the header file will call your code(under the normal name) in your module. The commented code is provided below:

.. code-block:: python

   import host
   import sys
   import bf2.mymodule
   import inspect
   import re

   def init():
      # Set up any events you will use in your code
      # These can be changed later, but only if you restart the server
      # Note the extra _Header added to the end of the events
      # This suffix is needed for this to work correctly

      host.registerHandler('EnterVehicle', onEnterVehicle_Header)
      host.registerHandler('ExitVehicle', onExitVehicle_Header)

      # This event will be used by the header to know when to reload the module
      # If you want to use the ChatMessage event in your own code, I suggest you
      # Register it up above like the others, and leave this as is

      host.registerHandler('ChatMessage', onChatMessage)

   def onEnterVehicle_Header(player, vehicle, freeSoldier = False):
      # This event is acting as a wrapper of sorts, recieving the information
      # and then sending it off to the module

      bf2.mymodule.onEnterVehicle(player, vehicle, freeSoldier = False)

   def onExitVehicle_Header(player, vehicle):
      # This event is acting as a wrapper of sorts, recieving the information
      # and then sending it off to the module

      bf2.mymodule.onExitVehicle(player, vehicle)

   def onChatMessage(playerId, text, channel, flags):
      # Fairly simple usage here
      # Checks chat messages looking for one that says 'reset'
      # When found it reloads your module
      # For this to work as plan use 'Say All:'

      if text == 'reset':
         try:
               reload(bf2.mymodule)
         except:
               sys.stderr.write("\n" + "Couldn't reload module, an exception occured")
               ExceptionOutput()

   def ExceptionOutput():
      sys.stderr.write("\n" + "Exception Occured: " + str(sys.exc_info()[0]) + "\n")
      sys.stderr.write("Value: " + str(sys.exc_info()[1]) + "\n")
      sys.stderr.write("Line:" + str(readline(inspect.getfile(sys.exc_info()[2]),
                        sys.exc_info()[2].tb_lineno)) + "\n")
      sys.stderr.write("Line #: " + str(sys.exc_info()[2].tb_lineno) + "\n")
      sys.stderr.write("File: " + str(inspect.getfile(sys.exc_info()[2])) + "\n" + "\n")

   def readline(filename, lineno):
      filen = re.sub('\\\\', '/', filename)
      file = open(filen, 'rU')
      lines = file.readlines()
      file.close()
      linen = lineno - 1
      line = re.sub('\s+', ' ', lines[linen])
      return line

.. note::

   In light of writing my cookbook receipe on better error catching, I've decided to update the reload function to output an error message if an error occurs on load. (I ran into a few of these errors on load while writing my recipie on better error catching, and they are very annoying. Yes I see the irony in running into errors while making better error catching.) Since the reload fails, your old code will still execute until you get a succesful reload. For more information on the error catching implented, :doc:`click here <errorcatching>`

The Module File
---------------

Next comes the actual module, where you put your custom code. From the coding aspect, nothing has changed. The only difference is instead of registering for event callback in your module, you now do so in the header file. Otherwise all imports, functions, etc. should work fine in the module. For simplicity's sake, here is an example module named mymodule.py:

.. code-block:: python

   # Set up any imports you need for your module

   def onEnterVehicle(player, vehicle, freeSoldier = False):
      # Set up your events just like you normally would
      # For this example I will use a simple print command
      # To demonstrate that it works
      print "Entered:", vehicle.templateName

   def onExitVehicle(player, vehicle):
      # Set up your events just like you normally would
      # For this example I will use a simple print command
      # To demonstrate that it works
      print "Exited:", vehicle.templateName

Discussion
----------

Reloading files at runtime saves a lot of time. All you have to do is shrink the game, change and save your module, bring back up the game and type 'reset' in the public chat. I broke it up into a header and module file, but it might be doable as one file. I though it was simplest this way, as you can set up multiple modules to the same header file, it save on redundant coding. Also, I decided to use a chat message as the event for a reload for simplicity, you could set it up to work with any event you want.

This was a learning experience for me, so there may be some mistakes. Feel free to point out anything that is done wrong or could be done better. Remember, these are just examples for you to understand the theory behind reloading files, there are several other ways this could be done.
