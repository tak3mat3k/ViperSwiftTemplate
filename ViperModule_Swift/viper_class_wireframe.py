from viper_class_base import *

class VIPERWireframe_h(ViperClass):
	
	def fName(self):
		return "Wireframe.h"

	def cName(self):
		return "Wireframe"

	def folderPath(self):
		return self.folder.path_module_ui_wireframe


class VIPERWireframe_m(ViperClass_Imp):
	
	def fName(self):
		return "Wireframe.m"

	def cName(self):
		return "Wireframe"

	def folderPath(self):
		return self.folder.path_module_ui_wireframe

class VIPERWireframe(ViperClass):

	viperView = None

	wireframe_h = None

	def create(self, view):

		self.viperView = view
		viperPresenter = view.viperPresenter

		self.wireframe_h = VIPERWireframe_h(self.module_name, self.folder)

		self.wireframe_h.addClass(viperPresenter.presenter_h.className())

		prt_wireframe_presenter = Property.nonatomic_strong_class(viperPresenter.presenter_h.className()) + "presenter;"
		self.wireframe_h.addProperty(prt_wireframe_presenter)

		self.wireframe_h.create()

		wireframe_m = VIPERWireframe_m(self.module_name, self.folder, self.wireframe_h)

		wireframe_m.addImports(viperPresenter.presenter_h.fileName())
		wireframe_m.addImports(self.viperView.view_h.fileName())

		prt_wireframe_view = Property.nonatomic_strong_class(self.viperView.view_h.className()) + "view;"
		wireframe_m.addInnerProperties(prt_wireframe_view)


		wireframe_m.create()







		