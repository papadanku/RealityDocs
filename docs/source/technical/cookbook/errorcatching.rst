
Better Error Catching
=====================

Submitted by *King of Camelot*.

Problem
-------

Normal Python interpreters will abort when an uncaught exception (programming error) occurs, printing a "traceback" message to help you track the problem down. The built-in error catching on the Python host embedded in Battlefield 2, however, only catches some errors, but not all of them--and when it doesn't catch a problem, the module in which it occurs will generally just quietly discontinue execution, while execution continues with other modules. This can make life for programmers very tough; troubleshooting bad code can be a problem without error messages, and putting ``print`` statements everywhere to try and pinpoint where something is failing is far from desirable.

Solution
--------

Python has ``Try`` statements that allow you to catch and output errors that would otherwise wouldn't show error messages. Specifically we will use the ``Try...Except`` statement, which has two clauses. The first clause is the ``Try`` portion which is where you put your code. The next clause, the ``Except`` portion, is where you put the code to be executed when an exception(error) occurs. A simple example of this is:

.. code-block:: python

   Try:
      # Put code that you want executed here
   Except:
      # Put code that should execute on an error here

In the example I use the plain old ``Except``, which should catch all exceptions. You can be more specific if you know what kind of error might occur during this code, such as ``Except ImportError``. For a list of specific exceptions, go here: `Python Exceptions <https://docs.python.org/release/2.3.4/lib/module-exceptions.html>`_.

Next comes the code we want to execute when an exception occurs. When an exception occurs, three different values are put into ``sys.exc_info()``. The first value is the type of exception that occured, the second value tells you specifics of the exception, and the third value gives you a reference to a traceback object for the exception. This makes it easy for us to learn about specifics of an exception when it occurs. In the following example, I also use functions from both the `Inspect Module <https://docs.python.org/release/2.3.4/lib/module-inspect.html>`_ (to get the source code file name) and the `Re Module <https://docs.python.org/release/2.3.4/lib/module-re.html>`_ (to format strings):

.. code-block:: python

   import inspect
   import re

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

Time to explain the two functions we've just defined.

- The function ``readline`` takes two arguments, a file name and a line number.

   - The file name is gotten using the ``inspect.getfile(object)``, which takes an object and returns the name of the source code file that it is from.
   - The line number is gotten by using ``object.tb_lineno``. The tb in the ``tb_lineno`` refers to a trace back object.
   - In both of the above cases the object is the third value stored in ``sys.exc_info()``
   - Getting to the actual meat of the function, the first line take the file name argument and formats it to reverse all backslashes to frontslashes. The reasoning for this will be explained in a moment.
   - The next line opens the file pointed to by the file name we just formatted. The file name had to be formatted first because although ``inspect.getfile(object)`` returns a name with backslashes, the open method needs a file name with frontslashes.
   - Now that we have the source code file open, we spit out all the lines using ``file.readlines()``.
   - Next we close the file, because we are done with it.
   - We now take the line number and subtract one from it, because while source code file line numbers run 1,2,3...etc the list(aka array) in which the lines are stored is numbered 0,1,2,3..
   - Normally the returned line would have a lot of extra white space in front due to Python's use of white space in its source code files. Since this doesn't look good in an error log, we use a substitution function to remove all the excess white space.
   - Finally we return the source code line at the line number that was inputed.

- The function ``ExceptionOutput`` takes no arguments, but instead outputs some nice little error text for us.

   - The first line outputs the first value in ``sys.exc_info()``, the type of exception.
   - The next line outputs the second value of ``sys.exc_info()``, the specifics of the exception.
   - Next we output the source code line at which the exception occured, using the ``readline`` function.
   - Just to make things easier to find, we also output the line number at which the exception occured.
   - The last thing we output is the name of the source code file in which the exception occured.

Now lets see an example where we implement these functions:

.. code-block:: python

   def onEnterVehicle(player, vehicle, freeSoldier = False):
      try:
         print "Entered: ", vehicle.templateName
         print vehicle.getDamage()
         print vehicle.hasArmor
         print vehicle.getName()
      except:
         ExceptionOutput()

In this example, an error would occur at ``print vehicle.getName()`` and we will get a nice little error message from ``ExceptionOutput()``. The ``Try...Except`` statement stops processing code in the ``try`` section once an exception occurs, so that even if multiple exceptions exist inside the ``try`` section, you will only see the first one that Python finds. Once you fix the exception, and re-execute your code it should continue on and catch any other errors you have in your code.

Discussion
----------

When I wrote this code, I was writing it dealing specificially with the `BF2 Python Log <http://wikihost.org/wikis/bf2modding/>`_. The code should work with other forms of logging, but may need slight modifying. I suggest using `BF2 Python Log <http://wikihost.org/wikis/bf2modding/>`_, that way you can see errors in real-time, and the error messages show up in pretty red text.

Please remember that this is just an example, and there are other ways you can do things. For one, in my code I used one big ``Try...Except`` statement and put all the code in the ``try`` section. You can break it up into several ``Try...Except`` statements if you would like, with only a little code in each statement. This can be useful when being more specific with the type of exception. You could also use a ``Try...Except...Else`` statement. In a ``Try...Except...Else`` statement the ``else`` section is executed if no exception occurs in the ``try`` section, but no checking for exceptions occurs in the ``else`` section. More information on ``try`` statements can be found here: `Try Statements <https://docs.python.org/release/2.3.4/ref/try.html>`_.
