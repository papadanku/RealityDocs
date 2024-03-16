
Squad
=====

``squad``
---------

``squad.leaveSquad``
   -> void

``squadInterface``
------------------

``squadInterface.selectOrder``
   std::string -> bool

``squadInterface.setstd::stringMap``
   std::string std::string std::string -> void

``squadLeaderInterface``
------------------------

``squadLeaderInterface.selectOrder``
   std::string -> bool

``squadLeaderInterface.setstd::stringMap``
   std::string std::string std::string -> void

``squadLeader``
---------------

``squadLeader.sendOrder``
   int bool -> void

``squadLeader.sendRequest``
   int bool -> void

``squadLeader.sendRequestForOrder``
   -> void

``squadManager``
----------------

``squadManager.changeSquadName``
   std::string bool -> void

``squadManager.joinSquad``
   int -> void

``squadManager.leaveSquad``
   int -> void

``squadManager.listSquadMembers``
   int int -> std::string

``squadManager.listSquads``
   int -> std::string

``squadManager.makeMeCommander``
   -> void

``squadManager.popNextCommanderApplicant``
   int -> void

``squadMenu``
-------------

``squadMenu.applyInviteList``
   -> void

``squadMenu.createSquad``
   -> void

``squadMenu.doubleClickInvite``
   -> void

``squadMenu.doubleClickNew``
   -> void

``squadMenu.setShowInviteList``
   bool -> void

``squadMenu.setSquadCreateSelect``
   bool -> void

``squadMenu.setSquadNameSelect``
   -> void

``squadMenu.singleClickInvite``
   -> void

``squadMenu.singleClickNew``
   -> void

``squadMenu.squadCreateLockToggle``
   -> void