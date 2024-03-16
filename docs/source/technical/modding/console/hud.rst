
HUD
===

``hudBuilder``
--------------

``hudBuilder.addNodeAlphaShowEffect``
   -> bool

``hudBuilder.addNodeBlendEffect``
   int int -> bool

``hudBuilder.addNodeMoveShowEffect``
   float int -> bool

``hudBuilder.addNodeVariableMoveShowEffect``
   std::string std::string -> bool

``hudBuilder.addObjectMarkerNodeLockTextNode``
   std::string -> bool

``hudBuilder.addTransformListNode``
   std::string -> bool

``hudBuilder.createBarNode``
   std::string std::string int -> bool

``hudBuilder.createButtonNode``
   std::string std::string int -> bool

``hudBuilder.createCompassNode``
   std::string std::string int -> bool

``hudBuilder.createEditNode``
   std::string std::string int -> bool

``hudBuilder.createHoverNode``
   std::string std::string int -> bool

``hudBuilder.createListNode``
   std::string std::string int -> bool

``hudBuilder.createMapNode``
   std::string std::string -> bool

``hudBuilder.createMiniMapNode``
   std::string std::string int -> bool

``hudBuilder.createObjectMarkerNode``
   std::string std::string int -> bool

``hudBuilder.createObjectSelectionNode``
   std::string std::string int -> bool

``hudBuilder.createOccupiedNode``
   std::string std::string int -> bool

``hudBuilder.createPictureNode``
   std::string std::string int -> bool

``hudBuilder.createSliderNode``
   std::string std::string float -> bool

``hudBuilder.createSplitNode``
   std::string std::string -> bool

``hudBuilder.createTextNode``
   std::string std::string int -> bool

``hudBuilder.createTileNode``
   std::string std::string int -> bool

``hudBuilder.createTransformListNode``
   std::string std::string int -> bool

``hudBuilder.createTransformNode``
   std::string std::string int -> int

``hudBuilder.deleteNode``
   -> bool

``hudBuilder.newLayer``
   -> bool

``hudBuilder.searchNodes``
   std::string std::string -> meme::Node\*

``hudBuilder.setActiveObject``
   std::string std::string -> bool

``hudBuilder.setBarNodeBorder``
   int int int -> bool

``hudBuilder.setBarNodeSnap``
   int -> bool

``hudBuilder.setBarNodeSnapDir``
   bool -> bool

``hudBuilder.setBarNodeTexture``
   int std::string -> bool

``hudBuilder.setBarNodeValueVariable``
   std::string -> bool

``hudBuilder.setBarNodeVariableTexture``
   int std::string -> bool

``hudBuilder.setButtonNodeAltConCmd``
   std::string int -> bool

``hudBuilder.setButtonNodeConCmd``
   std::string int -> bool

``hudBuilder.setButtonNodeDebug``
   bool -> bool

``hudBuilder.setButtonNodeFunction``
   std::string int -> bool

``hudBuilder.setButtonNodeMouseArea``
   int int int -> bool

``hudBuilder.setButtonNodeMouseOverColor``
   float float float -> bool

``hudBuilder.setButtonNodeTexture``
   int std::string -> bool

``hudBuilder.setCommanderPos``
   Vec2 -> bool

``hudBuilder.setCommanderSize``
   Vec2 -> bool

``hudBuilder.setCompassNodeBorder``
   int int int -> bool

``hudBuilder.setCompassNodeOffset``
   int -> bool

``hudBuilder.setCompassNodeSnapOffset``
   int int int -> bool

``hudBuilder.setCompassNodeSnapTexture``
   bool std::string -> bool

``hudBuilder.setCompassNodeTexture``
   int std::string -> bool

``hudBuilder.setCompassNodeTextureSize``
   int int -> bool

``hudBuilder.setCompassNodeValueVariable``
   std::string -> bool

``hudBuilder.setCompassNodeVariableTexture``
   int std::string -> bool

``hudBuilder.setCPFont``
   std::string -> void

``hudBuilder.setCPFontColor``
   float float float -> void

``hudBuilder.setEditNodeColor``
   float float float -> bool

``hudBuilder.setEditNodeData``
   int -> bool

``hudBuilder.setEditNodeFont``
   std::string bool -> bool

``hudBuilder.setEditNodeMaxLength``
   int -> bool

``hudBuilder.setEditNodestd::string``
   int -> bool

``hudBuilder.setHoverInMiddlePos``
   int int -> bool

``hudBuilder.setHoverMaxValue``
   float -> bool

``hudBuilder.setHoverWidthLength``
   float float -> bool

``hudBuilder.setListNodeBackgroundColor``
   float float float -> bool

``hudBuilder.setListNodeBorder``
   int int int -> bool

``hudBuilder.setListNodeBorderColor``
   float float float -> bool

``hudBuilder.setListNodeConCmd``
   int std::string -> bool

``hudBuilder.setListNodeData``
   int -> bool

``hudBuilder.setListNodeFont``
   std::string int -> bool

``hudBuilder.setListNodeOutline``
   bool -> bool

``hudBuilder.setListNodeRowSpacing``
   int -> bool

``hudBuilder.setListNodeScrollbar``
   int int -> bool

``hudBuilder.setListNodeScrollbarBackgroundColor``
   float float float -> bool

``hudBuilder.setListNodeScrollbarColor``
   float float float -> bool

``hudBuilder.setListNodeSelectColor``
   float float float -> bool

``hudBuilder.setMaxiPos``
   Vec2 -> bool

``hudBuilder.setMaxiSize``
   Vec2 -> bool

``hudBuilder.setMiniPos``
   Vec2 -> bool

``hudBuilder.setMiniSize``
   Vec2 -> bool

``hudBuilder.setModifyer``
   float -> void

``hudBuilder.setNodeAlphaVariable``
   std::string -> bool

``hudBuilder.setNodeColor``
   float float float -> bool

``hudBuilder.setNodeInTime``
   float -> bool

``hudBuilder.setNodeLogicShowVariable``
   std::string std::string int -> bool

``hudBuilder.setNodeOffset``
   int int -> bool

``hudBuilder.setNodeOutTime``
   float -> bool

``hudBuilder.setNodePos``
   int int -> bool

``hudBuilder.setNodePosVariable``
   int std::string -> bool

``hudBuilder.setNodeRGBVariables``
   std::string std::string std::string -> bool

``hudBuilder.setNodeShowVariable``
   std::string -> bool

``hudBuilder.setNodeSize``
   int int -> bool

``hudBuilder.setObjectMarkerNodeLockOnType``
   int -> bool

``hudBuilder.setObjectMarkerNodeLockText``
   bool std::string -> bool

``hudBuilder.setObjectMarkerNodeLockTextOffset``
   int int -> bool

``hudBuilder.setObjectMarkerNodeObjects``
   int -> bool

``hudBuilder.setObjectMarkerNodeTexture``
   int std::string -> bool

``hudBuilder.setObjectMarkerNodeTextureSize``
   int int int -> bool

``hudBuilder.setObjectMarkerNodeWeapon``
   int -> bool

``hudBuilder.setObjectSelectionNodePointerSize``
   int int -> bool

``hudBuilder.setOccupiedNodeData``
   int -> bool

``hudBuilder.setOccupiedNodePosVariable``
   int std::string -> bool

``hudBuilder.setPictureNodeAlphaMask``
   std::string -> bool

``hudBuilder.setPictureNodeBorder``
   int int int -> bool

``hudBuilder.setPictureNodeBorderColor``
   float float float -> bool

``hudBuilder.setPictureNodeCenterPoint``
   int int -> bool

``hudBuilder.setPictureNodeRotateVariable``
   std::string -> bool

``hudBuilder.setPictureNodeRotation``
   int -> bool

``hudBuilder.setPictureNodeTexture``
   std::string -> bool

``hudBuilder.setPictureNodeVariableTexture``
   std::string -> bool

``hudBuilder.setSliderNodeChild``
   std::string -> bool

``hudBuilder.setSliderNodeData``
   std::string -> bool

``hudBuilder.setTextNodeOutLine``
   std::string -> bool

``hudBuilder.setTextNodeOutLineOffset``
   float float -> bool

``hudBuilder.setTextNodestd::string``
   std::string -> bool

``hudBuilder.setTextNodestd::stringVariable``
   std::string -> bool

``hudBuilder.setTextNodeStyle``
   std::string int -> bool

``hudBuilder.setTileNodeOptions``
   int int int -> bool

``hudBuilder.setTranformListNodeOffset``
   int int -> bool

``hudBuilder.setTranformListNodePosVariable``
   int std::string -> bool

``hudBuilder.setZoomIcons``
   bool -> bool

``hudItems``
------------

``hudItems.setBool``
   std::string bool -> void

``hudItems.setFloat``
   std::string float -> void

``hudItems.setstd::string``
   std::string std::string -> void

``hudManager``
--------------

``hudManager.addFavouriteServer``
   bool -> void

``hudManager.addTextureAtlas``
   std::string -> void

``hudManager.enableSayAllChatBox``
   bool -> void

``hudManager.enableSaySquadChatBox``
   bool -> void

``hudManager.enableSayTeamChatBox``
   bool -> void

``hudManager.refresh``
   -> bool

``hudManager.setCommMousePos``
   int int -> bool

``hudManager.setCommMouseSensitivity``
   int -> bool

``hudManager.setCommPos``
   int int -> bool

``hudManager.setCommSize``
   int int -> bool

``hudManager.setDisplayControlpoints``
   bool -> void

``hudManager.setDisplayTickets``
   bool -> void

``hudManager.setDone``
   bool -> void

``hudManager.setMapStatic``
   bool -> void

``hudManager.setMaximumNrOfCPs``
   int -> void

``hudManager.setMouseTextureArtillery``
   std::string -> bool

``hudManager.setMouseTextureCancel``
   std::string -> bool

``hudManager.setMouseTextureEmpty``
   std::string -> bool

``hudManager.setMouseTextureFull``
   std::string -> bool

``hudManager.setMouseTextureSupply``
   std::string -> bool

``hudManager.setMouseTextureUAV``
   std::string -> bool

``hudManager.setPaint``
   bool -> void

``hudManager.setPointerMouseSensitivity``
   int -> bool

``hudManager.setPointerSize``
   int int -> bool

``hudManager.setSpottedAngle``
   float -> void

``hudManager.setSpottedMenuPos``
   int int -> bool

``hudManager.setSpottedMenuSize``
   int int -> bool

``hudManager.setSpottedMousePos``
   int int -> bool

``hudManager.setTargetTop``
   float -> void

``hudManager.setUpdate``
   bool -> void
