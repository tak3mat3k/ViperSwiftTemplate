from viper_class_base import *

class VIPERInteractor_Interface_Input(ViperClass_Interface):

	def fName(self):
		return "InteractorInputInterface.swift"

	def cName(self):
		return "InteractorInputInterface"

	def folderPath(self):
		return self.folder.path_module_module


class VIPERInteractor_Interface_Output(ViperClass_Interface):

	def fName(self):
		return "InteractorOutputInterface.swift"

	def cName(self):
		return "InteractorOutputInterface"

	def folderPath(self):
		return self.folder.path_module_module
		

class VIPERInteractor_h(ViperClass):
	
	def fName(self):
		return "Interactor.swift"

	def cName(self):
		return "Interactor"

	def folderPath(self):
		return self.folder.path_module_logic_interactor



class VIPERInteractor(ViperClass):

	interactor_Input = None
	interactor_Output = None
	interactor_h = None
	interactor_m = None

 	def create(self):

 		self.interactor_Input = VIPERInteractor_Interface_Input(self.module_name, self.folder)
 		self.interactor_Input.create()

 		self.interactor_Output = VIPERInteractor_Interface_Output(self.module_name, self.folder)
 		self.interactor_Output.create()

 		self.interactor_h = VIPERInteractor_h(self.module_name, self.folder)

 		self.interactor_h.addInterface(self.interactor_Input.className())

 		prt_int_output = Property.var(self.interactor_Output.className(), "output")
 		self.interactor_h.addProperty(prt_int_output)

 		self.interactor_h.create()





