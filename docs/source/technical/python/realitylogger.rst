
Reality Logger
==============

The Reality Logger is used to easily log to a file.

Creating a logger
-----------------

.. code-block:: python

   realitylogger.createLogger(name, path, fileName, continous)

-  ``name``: a unique key used to select the logger
-  ``Path``: Diretory the log file gets created in
-  ``fileName``: Name of the file created. If not contionous should specify a date format (strftime format)
-  ``continous``: Whether to log to one file all the time or create new one every round

``createLogger`` may be called many times with the same key, repeating calls will be properly filtered out. It is not required to put it in an init() function.

Using a logger
--------------

.. code-block:: python
   :caption: To acquire a logger

      X = realitylogger.RealityLogger[key]

.. code-block:: python
   :caption: Basic logging commands

      X.logLine(line)
      X.logLines(lines)
