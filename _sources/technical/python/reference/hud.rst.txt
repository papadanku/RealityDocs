
HudEvent
========

Detailed information about the :py:meth:`bf2.gameLogic.sendHudEvent <bf2.GameLogic.GameLogic.sendHudEvent>`

Event by Number
---------------

#. Close To Control Point
#. Hud State Changed
#. Hud Disable
#. Hud Enable
#. Init Loading Screen
#. Update Loading Screen
#. Set Loading Screen Debug
#. Remove Loading Screen
#. Map Zoom Changed
#. Map Static Changed
#. Squad Is Full
#. Squad Is Private
#. Squad Creation Failed
#. Squad Creation Success
#. Squad Invalid Name
#. Squad Invitation
#. Squad Join Request
#. Squad Join Request Denied

   - **Data:** 0 - 7
   - **Data name:** Squad ID
   - **Results:** This event causes a ``Your request to join #SQUADNAME# squad has been denied`` message. The squad name changes depending on the supplied Squad ID.

#. Squad Join Request Accepted

   - **Data:** 0 - 7
   - **Data name:** Squad ID
   - **Results:** This event causes a ``Your request to join #SQUADNAME# squad has been accepted message``. The squad name changes depending on the supplied Squad ID.

#. Kicked From Squad

   - **Data:** 0 - 255
   - **Data name:** Player ID
   - **Results:** This event causes a kicked from squad message, saying either ``... has been kicked from your squad.`` or ``You have been kicked from your squad``, depending on the player ID.

#. Left Squad

   - **Data:** 0 - 255
   - **Data name:** Player ID
   - **Results:** This event causes a player left squad message, saying ``... has left your squad``. This message will only work if the player it is sent to is in a squad. Nothing happens if the player ID is the player the message was sent to.

#. Joined Squad

   - **Data:** 0 - 255
   - **Data name:** Player ID
   - **Results:** This event causes a player joined squad message, saying ``... has joined your squad``. This message will only work if the player it is sent to is in a squad. Nothing happens if the player ID is the player the message was sent to.

#. Squad Orders Received

   - **Data:** 0 - 255
   - **Data name:** Player ID
   - **Results:** This event causes an order recieved message, saying ``You have recieved a new order from your squadleader``. Player ID seems to have no effect on the message. Does nothing if player message is sent to is the squad leader.

#. New Squad Leader

   - **Data:** 0 - 255
   - **Data name:** Player ID
   - **Results:** This event causes a new squad leader message, saying either ``... is your new squad leader`` or ``You are the new squad leader``, depending on the player ID.

#. Squad Leader Request
#. Commander Orders Received
#. Commander Orders Sent
#. Squad Orders Sent
#. Request Recieved
#. Request Sent
#. Update Hud
#. Weapon Changed
#. Commander Accept
#. Commander Decline
#. Commander Invitation
#. Squad LeaderInvitation
#. Commander Resign
#. Rank Change
#. Medal Reward
#. UAV
#. Satellite
#. Artillery
#. Unit Spotted
#. Missile Lock
#. New Unlock
#. Call For Medic
#. Call For Ammo
#. Call For Repair
#. Call For Revive
#. Auto Call For Revive
#. Radio Call
#. Was Hit
#. Possibly Not Used
#. Possibly Not Used
#. Possibly Not Used
#. Possibly Not Used
#. Is Close To Mine

   - **Data:** 0 - 255
   - **Data name:** Player ID

#. Not Close To Mine

   - **Data:** 0 - 255
   - **Data name:** Player ID

#. Muted By Remote
#. Possibly Not Used
#. TK Option
#. TK Response
#. Possibly Not Used
#. Control Point Taken
#. Control Point Lost
#. Enable Help Message

   - **Data:** 49
   - **Data name:** Exit To Capture Flag

#. Enable Help
#. Possibly Not Used
#. Possibly Not Used
#. Ticket Bleed
#. Ticket State Changed
#. Begin Round
#. Possibly Not Used
#. Possibly Not Used
#. Map Change Complete
#. Map Zoom Complete

.. note::

   Some hud events may cause informative messages to be sent to players in-game, but the hud event does not cause these events to happen, instead it only sends the message that would be sent if that event did happen.
