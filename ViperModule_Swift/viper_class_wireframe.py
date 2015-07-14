from viper_class_base import *

class VIPERWireframe_h(ViperClass):
	
	def fName(self):
		return "Wireframe.swift"

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

		prt_wireframe_presenter = Property.var(viperPresenter.presenter_h.className(), "presenter")

		self.wireframe_h.addProperty(prt_wireframe_presenter)

		self.wireframe_h.create()

		
		







		