from viper_class_base import *

class VIPERPresenter_Interface(ViperClass_Interface):

	def fName(self):
		return "PresenterInterface.swift"

	def cName(self):
		return "PresenterInterface"

	def folderPath(self):
		return self.folder.path_module_module

class VIPERPresenter_h(ViperClass):
	
	def fName(self):
		return "Presenter.swift"

	def cName(self):
		return "Presenter"

	def folderPath(self):
		return self.folder.path_module_ui_presenter


class VIPERPresenter(ViperClass):

	viperInteractor = None
	viperWireframe = None

	presenter_interface = None
	presenter_h = None

	def prepare(self, interactor=None, wireframe=None):

		if self.viperInteractor == None:

			self.viperInteractor = interactor

			self.presenter_interface = VIPERPresenter_Interface(self.module_name, self.folder)

			self.presenter_h = VIPERPresenter_h(self.module_name, self.folder)

			self.presenter_h.addInterface(self.viperInteractor.interactor_Output.className())
			self.presenter_h.addInterface(self.presenter_interface.className())

			prt_presenter_interactor = Property.var(self.viperInteractor.interactor_Input.className(), "interactor")
			self.presenter_h.addProperty(prt_presenter_interactor)

		if self.viperWireframe == None and wireframe != None:

			self.viperWireframe = wireframe

			prt_presenter_wireframe = Property.var(self.viperWireframe.wireframe_h.className(), "wireframe")
			prt_presenter_view_interface = Property.weakVar(self.viperWireframe.viperView.view_interface.className(), "userInterface")

			self.presenter_h.addProperty(prt_presenter_wireframe)
			self.presenter_h.addProperty(prt_presenter_view_interface)


	def create(self):
		self.presenter_interface.create()
		self.presenter_h.create()
	

		