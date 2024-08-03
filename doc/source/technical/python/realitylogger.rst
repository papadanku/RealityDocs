
Reality Logger
==============

The Reality Logger is used to easily log to a file.

Creating a logger
-----------------

.. py:function:: realitylogger.createLogger(name, path, fileName, continous)

   :param name: A unique key used to select the logger
   :param path: Directory the log file gets created in
   :param fileName: Name of the file created. If not contionous should specify a date format (strftime format)
   :param continous: Whether to log to one file all the time or create new one every round

   May be called many times with the same key, repeating calls will be properly filtered out. It is not required to put it in an init() function.

Using a logger
--------------

.. code-block:: python

   # Aquire a logger
   X = realitylogger.RealityLogger[key]

   # Basic logging commands
   X.logLine(line)
   X.logLines(lines)
