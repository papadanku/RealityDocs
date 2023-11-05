
BF2 Porting
===========

Preface
-------

EA says the following ports are used by BF2, But the list is suspect for several reasons. The original list was published in a community news letter on EA's official BF2 page, and was a hode podge of ports, now I can't seem to find that community update again, if anyone bookmarked it please let us know the url.

Here is a tentative list:

======== =========== ====== ============================
Protocol Ports       In/Out Function
======== =========== ====== ============================
TCP      80          ?      Battle Recorder / PunkBuster
TCP      4711        IN     Remote console
?        4712        ?      BF2 CC Daemon
UDP      27901       IN     Stats port
UDP      1500-4999   ?      “General use”
UDP/TCP  1024-1124   ?      “General use”
UDP      29900       ?      Server status (Gamespy)
UDP/TCP  27900       ?      Stats port
UDP      16567       IN     PunkBuster
UDP      55123-55125 IN/OUT VoIP
======== =========== ====== ============================

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

This ruleset allows my server to be seen in the server browser list, people can join it AND use VOIP.

Note that this is a stander server, only one BF2 server on the machine, and no hank panky with ports used and such.

::

   iptables -A <ChainName> -m udp -p udp -m multiport --dports 29900,29901,29902,29903,29904,16567,55125 -j ACCEPT
   iptables -A <ChainName> -m tcp -p tcp -m multiport --dports 4711 -j ACCEPT
   iptables -A <ChainName> -m udp -p udp --sport 29910 -s 207.38.8.27 -j ACCEPT
   iptables -A <ChainName> -m udp -p udp --sport 29910 -s 207.38.8.28 -j ACCEPT
