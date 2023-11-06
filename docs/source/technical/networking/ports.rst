
BF2 Porting
===========

Preface
-------

Here is a list of common Project Reality Server Ports

======== =========== ===================================================
Protocol Ports       Function
======== =========== ===================================================
TCP      80,443      Battle Recorder
TCP      22          SSH
TCP      4712        PRISM RCON
UDP      29901       Server status (GameSpy)
UDP      16567       Server Game Port
TCP      64740       Mumble (Block UDP, TCP works better for PR Mumble)
======== =========== ===================================================

Firewalling Your Server
-----------------------

This is from the ``readmeserver.txt``

::

   FIREWALL

   The use of a software firewall on the server is not recommended,
   as it can adversely affect server performance and the overall
   gameplay experience.

How to firewall your server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. External firewall

   You have a machine that all traffic has to pass through to get to your server (my favourite)

2. Local Firewall

   You are running a firewall on the same server as you have the server (uses local CPU,so not the best way)

We will NOT go into the rigamole on HOW to set up a firewall for your system here, lots of other sites cover this. What we will attempt to cover here is the specific rulesets that are needed for a BF2 server to work properly.

External Firewall
~~~~~~~~~~~~~~~~~

We need more info here, folks!

Local Firewall
~~~~~~~~~~~~~~

Linux Iptables
^^^^^^^^^^^^^^

This ruleset allows my server to be seen in the server browser list, people can join it AND use VOIP, game admins can connect through PRISM and sysadmins can connect to SSH.

Note that this is a standard server, only one BF2 server on the machine, and no hank panky with ports used and such. Battlerecorder is recommended to be hosted on a separate box.

::

   iptables -A INPUT -m udp -p udp -m multiport --dports 29901,16567 -j ACCEPT
   iptables -A INPUT -m tcp -p tcp -m multiport --dports 22,4711,64740 -j ACCEPT
