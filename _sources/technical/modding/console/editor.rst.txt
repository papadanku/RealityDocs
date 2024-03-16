
``Editor``
==========

``Editor.createNewLayer``
   std::string -> void

``Editor.deleteAllLayers``
   -> void

``Editor.deleteAllObjects``
   -> std::string

``Editor.deleteObject``
   world::IObject_ptrproxy -> void

``Editor.deleteTemplate``
   world::IObjectTemplate_ptrproxy -> void

``Editor.getActiveLayer``
   -> std::string

``Editor.getActiveLayerId``
   -> int

``Editor.getActiveObject``
   -> world::IObject_ptrproxy

``Editor.getActiveObjectTemplate``
   -> world::IObjectTemplate_ptrproxy

``Editor.hideLayer``
   std::string -> void

``Editor.listAllVehicles``
   -> std::string

``Editor.listLayers``
   -> std::string

``Editor.listMeshes``
   -> std::string

``Editor.listObjects``
   -> std::string

``Editor.listObjectsOfTemplate``
   world::IObjectTemplate_ptrproxy -> std::string

``Editor.listTemplates``
   std::string -> std::string

``Editor.listTextures``
   -> std::string

``Editor.loadAllObjects``
   std::string -> bool

``Editor.loadAllTemplatesAndObjects``
   -> bool

``Editor.printObjectCreationScript``
   world::IObject_ptrproxy -> std::string

``Editor.printTemplateCreationScript``
   world::IObjectTemplate_ptrproxy -> std::string

``Editor.quickReloadActiveTemplate``
   -> void

``Editor.quickReloadTemplate``
   world::IObjectTemplate_ptrproxy -> void

``Editor.removeLayer``
   std::string -> void

``Editor.renameLayer``
   std::string std::string -> void

``Editor.saveAllEffects``
   -> void

``Editor.saveAllObjects``
   std::string -> bool

``Editor.saveAllSpawners``
   -> bool

``Editor.saveAllTemplates``
   -> bool

``Editor.saveAllTemplatesAndObjects``
   -> bool

``Editor.saveAllUsedTemplates``
   std::string -> bool

``Editor.saveFolderToArchive``
   std::string bool bool -> int

``Editor.saveSpawners``
   bool bool bool -> void

``Editor.saveTemplateToFile``
   std::string std::string -> bool

``Editor.saveTemplateTreeStructure``
   std::string std::string -> int

``Editor.saveVehicles``
   bool -> bool

``Editor.setActiveLayer``
   std::string -> void

``Editor.setActiveLayerId``
   int -> void

``Editor.setActiveObject``
   world::IObject_ptrproxy -> world::IObject_ptrproxy

``Editor.setActiveObjectTemplate``
   world::IObjectTemplate_ptrproxy -> world::IObjectTemplate_ptrproxy

``Editor.ShowEntryPoints``
   bool -> bool

``Editor.showLayer``
   std::string -> void

``Editor.start``
   world::IObject_ptrproxy -> void

``Editor.stop``
   world::IObject_ptrproxy -> void

``Editor.updateAllTemplates``
   -> void

``Editor.updateTemplate``
   world::IObjectTemplate_ptrproxy -> void