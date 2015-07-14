import os

from constants import *
from defines import *
from logs import *
from model_helpers import exit

def createFolder(folder_path):
	if not os.path.exists(folder_path): 
		os.makedirs(folder_path, 0777)
	else:
		LOG_ERROR("FOLDER EXIST"+folder_path)
		exit()

class ViperFolder(object):

	module_name = ''

	path = ''
	path_module = ''
	path_module_module = ''
	path_module_logic = ''
	path_module_logic_interactor = ''
	path_module_ui = ''
	path_module_ui_presenter = ''
	path_module_ui_view = ''
	path_module_ui_wireframe = ''

	def __init__(self, module_name, path_module):
		super(ViperFolder, self).__init__()
		self.module_name = module_name
		self.path = path_module

	def create_folders(self):

		self.path_module = self.path + "/" + self.module_name
		createFolder(self.path_module)
		
		self.path_module_module = self.path_module + "/" + FOLDER_MODULE_MODULE_NAME
		createFolder(self.path_module_module)
		
		self.path_module_logic = self.path_module + "/" + FOLDER_MODULE_LOGIC_NAME
		createFolder(self.path_module_logic)

		self.path_module_logic_interactor = self.path_module_logic + "/" + FOLDER_MODULE_LOGIC_INTERACTOR_NAME
		createFolder(self.path_module_logic_interactor)

		self.path_module_ui = self.path_module + "/" + FOLDER_MODULE_UI
		createFolder(self.path_module_ui)

		self.path_module_ui_presenter = self.path_module_ui + "/" + FOLDER_MODULE_UI_PRESENTER
		createFolder(self.path_module_ui_presenter)

		self.path_module_ui_view = self.path_module_ui + "/" + FOLDER_MODULE_UI_VIEW
		createFolder(self.path_module_ui_view)

		self.path_module_ui_wireframe = self.path_module_ui + "/" + FOLDER_MODULE_UI_WIREFRAME
		createFolder(self.path_module_ui_wireframe)




