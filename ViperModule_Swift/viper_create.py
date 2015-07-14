from viper_folders import *
from viper_class_interactor import VIPERInteractor
from viper_class_presenter import VIPERPresenter
from viper_class_view import VIPERView
from viper_class_wireframe import VIPERWireframe
from viper_class_LoadModule import VIPERLoadModule

"""
Create the viper model
"""
def create_Model_Viper(module_name, model_creator, path):
	folders = ViperFolder(module_name, path)
	folders.create_folders()

	viperInteractor = VIPERInteractor(module_name, folders)
	viperInteractor.create()

	viperPresenter = VIPERPresenter(module_name, folders)
	viperPresenter.prepare(viperInteractor)

	viperView = VIPERView(module_name, folders)
	viperView.create(viperPresenter)

	viperWireframe = VIPERWireframe(module_name, folders)
	viperWireframe.create(viperView)

	viperPresenter.prepare(viperInteractor, viperWireframe)
	viperPresenter.create()

	viperLoadModule = VIPERLoadModule(module_name, folders)
	viperLoadModule.create(viperInteractor, viperPresenter, viperWireframe)



"""
End Create the viper model
"""