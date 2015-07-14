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
		return "View.h"

	def cName(self):
		return "View"

	def folderPath(self):
		return self.folder.path_module_ui_view

	def inherit(self):
		return " : UIView"

	def baseImport(self):
		return "<UIKit/UIKit.h>"


class VIPERView_m(ViperClass_Imp):
	
	def fName(self):
		return "View.m"

	def cName(self):
		return "View"

	def folderPath(self):
		return self.folder.path_module_ui_view

class VIPERView(ViperClass):

	viperPresenter = None

	view_interface = None
	view_h = None
	
	def create(self, presenter):

		self.viperPresenter = presenter

		self.view_interface = VIPERView_Interface(self.module_name, self.folder)
		self.view_interface.create()

 		self.view_h = VIPERView_h(self.module_name, self.folder)

 		self.view_h.addProtocol(self.viperPresenter.presenter_interface.className())

		self.view_h.addImports(self.view_interface.fileName())

		self.view_h.addInterface(self.view_interface.className())

		prt_view_presenter = Property.nonatomic_weak_interface(self.viperPresenter.presenter_interface.className()) + "presenter;"
		self.view_h.addProperty(prt_view_presenter)

		self.view_h.create()

		view_m = VIPERView_m(self.module_name, self.folder, self.view_h) 
		view_m.create()



		