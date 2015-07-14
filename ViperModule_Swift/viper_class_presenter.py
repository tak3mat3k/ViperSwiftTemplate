from viper_class_base import *

class VIPERPresenter_Interface(ViperClass_Interface):

	def fName(self):
		return "Presenter_Interface.h"

	def cName(self):
		return "Presenter_Interface"

	def folderPath(self):
		return self.folder.path_module_module

class VIPERPresenter_h(ViperClass):
	
	def fName(self):
		return "Presenter.h"

	def cName(self):
		return "Presenter"

	def folderPath(self):
		return self.folder.path_module_ui_presenter


class VIPERPresenter_m(ViperClass_Imp):
	
	def fName(self):
		return "Presenter.m"

	def cName(self):
		return "Presenter"

	def folderPath(self):
		return self.folder.path_module_ui_presenter


class VIPERPresenter(ViperClass):

	viperInteractor = None
	viperWireframe = None

	presenter_interface = None
	presenter_h = None
	presenter_m = None


	def prepare(self, interactor=None, wireframe=None):

		if self.viperInteractor == None:
			self.viperInteractor = interactor

			self.presenter_interface = VIPERPresenter_Interface(self.module_name, self.folder)

			self.presenter_h = VIPERPresenter_h(self.module_name, self.folder)

			self.presenter_h.addImports(self.viperInteractor.interactor_Input.fileName())
			self.presenter_h.addImports(self.presenter_interface.fileName())

			self.presenter_h.addInterface(self.viperInteractor.interactor_Output.className())
			self.presenter_h.addInterface(self.presenter_interface.className())

			prt_presenter_interactor = Property.nonatomic_strong_interface(self.viperInteractor.interactor_Input.className()) + "interactor;"
			self.presenter_h.addProperty(prt_presenter_interactor)

			self.presenter_m = VIPERPresenter_m(self.module_name, self.folder, self.presenter_h)

		if self.viperWireframe == None and wireframe != None:
			self.viperWireframe = wireframe

			self.presenter_h.addImports(self.viperWireframe.wireframe_h.fileName())

			self.presenter_h.addProtocol(self.viperWireframe.viperView.view_interface.className())

			prt_presenter_wireframe = Property.nonatomic_assign_class(self.viperWireframe.wireframe_h.className()) + "wireframe;"
			prt_presenter_view_interface = Property.nonatomic_assign_interface_view(self.viperWireframe.viperView.view_interface.className()) + "userInterface;"

			self.presenter_h.addProperty(prt_presenter_wireframe)
			self.presenter_h.addProperty(prt_presenter_view_interface)

			self.presenter_m.addImports(self.viperWireframe.viperView.view_interface.fileName())


	def create(self):
		self.presenter_interface.create()
		self.presenter_h.create()
		self.presenter_m.create()

		