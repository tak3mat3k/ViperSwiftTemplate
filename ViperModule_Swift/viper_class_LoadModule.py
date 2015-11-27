from viper_class_base import *

class VIPERLoadModule_h(ViperClass):

	def fName(self):
		return "LoadModule.swift"

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

		str_interactor = "interactor"
		str_presenter = "presenter"
		str_wireframe = "wireframe"

		prt_interactor = Property.var(interactor_class.className(), str_interactor, False)
		prt_presenter = Property.var(presenter_class.className(), str_presenter, False)
		prt_wireframe = Property.var(wireframe_class.className(), str_wireframe, False)

		load_h.addProperty(prt_interactor)
		load_h.addProperty(prt_presenter)
		load_h.addProperty(prt_wireframe)

		hardCodedMethodLoadModule = "\tclass func loadModule() -> " + load_h.className() + " {\n\n" \
		"\t\tlet " + str_interactor + " = " + interactor_class.className() + "()\n" \
		"\t\tlet " + str_presenter + " = " + presenter_class.className() + "()\n" \
		"\t\tlet " + str_wireframe + " = " + wireframe_class.className() + "()\n" \
		"\n" \
		"\t\t" + str_interactor + ".output = " + str_presenter + "\n\n" \
		"\t\t" + str_presenter + ".interactor = " + str_interactor + "\n" \
		"\t\t" + str_presenter + ".wireframe = " + str_wireframe + "\n\n" \
		"\t\t" + str_wireframe + ".presenter = " + str_presenter + "\n\n" \
		"\t\tlet module = " + load_h.className() + "()" + "\n\n" \
		"\t\tmodule." + str_interactor + " = " + str_interactor + "\n" \
		"\t\tmodule." + str_presenter + " = " + str_presenter + "\n" \
		"\t\tmodule." + str_wireframe + " = " + str_wireframe + "\n\n" \
		"\t\treturn module" + "\n" \
		"\t}"+"\n" \




		load_h.addMethod(hardCodedMethodLoadModule)

		load_h.create()
