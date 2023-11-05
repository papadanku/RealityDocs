
``.con`` File Grammar
=====================

Con files are the core of how Battlefield 2 (and 1942 before it) configures its weapons, maps, objects, players and other game assets. These files can be run by the engine or from within the in-game console. The in-game console uses the exact same syntax with the notable difference that multi-line commands like ``beginRem`` do not work. With Battlefield 2, the console grammar has extended into a rudimentry scripting language, with loops and full conditionals. Battlefield 1942 had only very rudimentry conditionals.

Comments
--------

There exist two classes of comments

``title="Block rem" beginRem this text is ignored endRem``

``title="Line rem" rem this text is ignored``

Statements
----------

Statements are a command followed by a number of optionally “quoted”, whitespace-seperated arguments.

``title="Statement command" commandClass.commandMethod argument1 "argument2"``

The number and type of the arguments depends on the command being used. The available commands is beyond the scope of this page, but a good portion of them are included with the editor.

A full list is available by running GNU ``strings`` against your bf2.exe

CRD Argument Type
~~~~~~~~~~~~~~~~~

Many arguments are a CRD type of argument, which stands for *Continuous Random Distribution*, and is used to calculate a random number based on the specify properties.

``title="A CRD always has four sub-arguments" CRD_NONE/3/0/0``

The first argument says what type of distribution should be used, the second and third depend on the type and the latter is called symmetry, and can affect any of the distributions; it will be explained later.

The meaning of the second and third arguments, which are always '''numbers''', varies depending on the type of distribution property specified. The four types for this first argument are:

-  ``CRD_NONE``

   Do not vary the argument at all, just return the first number.

-  ``CRD_UNIFORM``

   Uniform random distribution, between the two numbers specified.

-  ``CRD_EXPONENTIAL``

   Exponential drop off, first number specifies the mean (average).

-  ``CRD_NORMAL``

   Normal distribution, the first number is the mean, the second the variance.

We just need the first three arguments to compute a random number, the final, fourth argument is a boolean and can affect the sign of this computed number: If this argument is 1 (true), then there is a 50/50 chance that the computed number will be negated. If 0 (false), no negation “coin-flip” takes place.

Some examples:

-  ``ObjectTemplate.TimeToLive CRD_NONE/240/0/0``

   ``TimeToLive`` will be set to 240: no computation was performed we just returned the first argument. This sort of CRD can be directly replaced by the number itself.

-  ``ObjectTemplate.TimeToLive CRD_UNIFORM/2/7/0``

   ``TimeToLive`` can be one of [2, 3, 4, 5, 6, 7] and they have all the same chance.

-  ``ObjectTemplate.rotationalSpeedInDof CRD_EXPONENTIAL/-20/0/1``

   The exponential distribution basically gives a distribution curve that drops off sharply and then levels out. It is computed by ``-mean*ln(random(0,1))``. In other words, a random number between 0 and 1 (not including 0 or 1) is generated, the natural logarithm of this number is computed, and the result is multiplied by the negative of the mean (the average), the second argument (and first number) passed in. For example, if the random number generated was 0.1, the natural log is -2.3, so since the mean was -20, the final number returned would be -(-20)\*-2.3 = -46. Since the symmetric flag, the last argument, is set to 1 (true), there is a 50/50 chance that this result will be negated, i.e. be returned as 46 instead of -46.

   NOTE: this distribution is often misused in the Battlefield code, e.g.

   ``ObjectTemplate.initRotation CRD_EXPONENTIAL/0/180/1``

   is a common use. However, this setting actually always returns a value of 0, since that is the mean specified. The “180” argument is ignored.

-  ``ObjectTemplate.timeToLive CRD_NORMAL/2/3.5/0``

   A normal distribution is a classic bell curve shape. The second argument is the mean, the average value, and the third argument is the variance, how fast the distribution curve drops off into its bell shape. The fourth argument again acts to force symmetry if set, though the bell curve has its own symmetry when the mean is 0.

   Variance specifies the range in which about 4/5ths of the numbers generated will fall. In our example, the 2 is the average time to live desired, and a variance of 3.5 means that this value can vary fairly widely; about 4/5ths of the numbers generated will be in the range +3.5 to -3.5 from the mean of 2, i.e. -1.5 to 5.5, with 1/5th of the numbers appearing above and below this range.

`Source <https://bfmods.com/mdt/scripting/CRD.html>`__

Variables
---------

Variables must be predefined, and have a strict naming system. All mutable variables must begin with ``v_`` whereas all immutable variables or *constants* must begin with ``c_``. It's a simple form of `Hungarian Notation <https://en.wikipedia.org/wiki/Hungarian_notation>`_.

Mutable Variables
~~~~~~~~~~~~~~~~~

``var v_dongs = test``

Defines a new variable called ``dongs`` or ``v_dongs`` depending on your point of view with the value “test”. When defining a variable you can omit the default value however:

``var v_dongs``

is a value construct for example.

Immutable Variables
~~~~~~~~~~~~~~~~~~~

``const c_butts = test``

Defines a constant called, again, ``butts`` or ``c_butts`` with the value “test”. Obviously, this variable cannot be changed.

``const`` vs. ``var`` and assignments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assigning to a variable is as simple as appending ``-> v_varname`` to any command. However, many commands do not return a value. The ones that do generally return either a boolean value (``0`` or ``1``) or a simple string.

Clearly, trying to assign to a ``const`` variable is an error and will not work.

Conditionals
------------

Conditionals include the standard constructs. These evaluate an ''expression''

-  ``if ... endIf``
-  ``if ... elseIf ... endIf``
-  ``while ... endWhile``

Expressions
~~~~~~~~~~~

The grammar of an expression is roughly:

``<variable> <comparator> <value>``

-  ``variable``

   Any variable name beginning with ``v_`` or ``c_``.

-  ``comparator``

   One of ``==``, ``!=``, ``>``, ``>=``, ``<`` or ``<=`` or their textual equivalents: ``lessOrEqualThan``, ``lessThan``, ``greaterOrEqualThan``, ``greaterThan``, ``notEquals``, ``equals``.

-  ``value``

   Any literal string, quoted if neccessary.

``Return``
----------

You may cease interpretation of the current .con file by using the command ``return``. This resumes interpretation from the calling file. It is an error to use this unless the file was called with…

``include`` and ``run``
-----------------------

Both ``include`` and ``run`` trigger the interpretation of another .con file.

They also have the ability to set ``arguments``, which are a special type of mutable variable. For example:

``run test.con 1 2 3``

Runs ``test.con``. In ``test.con``, the variables ``v_arg1``, ``v_arg2`` and ``v_arg3`` are set to ``1``, ``2`` and ``3``, respectively.

Typically this is used along with a conditional to do something for the editor mode, or to do something different for single player mode (a common use in BF1942, where this method also existed).

As for differences, ``run`` seems to create a new scope, while ``include`` does not.

An Example
----------

::

   var v_tst
   fileManager.fileExists movies/menu.bik -> v_tst
   if v_tst == 0
   fileManager.copyFile ../../mods/bf2/movies/menu.bik movies/menu.bik
   fileManager.copyFile ../../mods/bf2/movies/menu_loggedin.bik movies/menu_loggedin.bik
   endIf

This example checks if ``movies/menu.bik`` exists, and if it doesn't copies two files from the ``bf2`` mod to the current mod.
