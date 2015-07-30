from viper_class_base import *

class VIPERView_Interface(ViperClass_Interface):

	def fName(self):
		return "ViewInterface.swift"

	def cName(self):
		return "ViewInterface"

	def folderPath(self):
		return self.folder.path_module_module

class VIPERView_h(ViperClass):
	
	def fName(self):
		return "ViewController.swift"

	def cName(self):
		return "ViewController"

	def folderPath(self):
		return self.folder.path_module_ui_view

	def baseImport(self):
		return "UIKit"

class VIPERView(ViperClass):

	viperPresenter = None
	view_interface = None
	view_h = None
	
	def create(self, presenter):

		self.viperPresenter = presenter

		self.view_interface = VIPERView_Interface(self.module_name, self.folder)
		self.view_interface.create()

 		self.view_h = VIPERView_h(self.module_name, self.folder)

		self.view_h.addInterface("UIViewController")
		self.view_h.addInterface(self.view_interface.className())

		prt_view_presenter = Property.weakVar(self.viperPresenter.presenter_interface.className(), "presenter")
		self.view_h.addProperty(prt_view_presenter)

		self.view_h.create()



		