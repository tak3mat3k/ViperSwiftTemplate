from viper_class_base import *

class VIPERLoadModule_h(ViperClass):
	
	def fName(self):
		return "LoadModule.h"

	def cName(self):
		return "LoadModule"

	def folderPath(self):
		return self.folder.path_module_module


class VIPERLoadModule_m(ViperClass_Imp):
	
	def fName(self):
		return "LoadModule.m"

	def cName(self):
		return "LoadModule"

	def folderPath(self):
		return self.folder.path_module_module


class VIPERLoadModule(ViperClass):

	def create(self, interactor, presenter, wireframe):

		load_h = VIPERLoadModule_h(self.module_name, self.folder)

		interactor_class = interactor.interactor_h
		presenter_class = presenter.presenter_h
		wireframe_class = wireframe.wireframe_h

		load_h.addImports(interactor_class.fileName())
		load_h.addImports(presenter_class.fileName())
		load_h.addImports(wireframe_class.fileName())

		prt_interactor = Property.nonatomic_strong_class(interactor_class.className()) + "interactor;"
		prt_presenter = Property.nonatomic_strong_class(presenter_class.className()) + "presenter;"
		prt_wireframe = Property.nonatomic_strong_class(wireframe_class.className()) + "wireframe;"

		load_h.addProperty(prt_interactor)
		load_h.addProperty(prt_presenter)
		load_h.addProperty(prt_wireframe)

		load_h.create()

		load_m = VIPERLoadModule_m(self.module_name, self.folder, load_h)
		load_m.create()



