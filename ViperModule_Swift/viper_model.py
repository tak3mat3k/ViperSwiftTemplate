import sys, getopt
from constants import *
from defines import *
from model_helpers import *
from viper_create import *
 	
"""
Viper Model
"""
class ViperModel(object):
	model_name = ''
	author_name = ''
	path_model = DEFAULT_MODEL_PATH

	def __init__(self):
		super(ViperModel, self).__init__()

	def validate_vars(self):
		validateModelName(self.model_name)
		self.author_name = validateCreatroName(self.author_name)

	def inputs(self, args, opts):
		for opt, arg in opts:
			self.input(opt, arg)

	def input(self, opt, arg):
		if opt == '-h':
			module_help()
		elif opt == '-n': 
			self.model_name = arg
		elif opt == '-a':
			self.author_name = arg

	def create(self, argv):
   		try:
   			opts, args = getopt.getopt(argv,"h:n:a:")
   			self.inputs(args, opts)
   			self.validate_vars()
   			create_Model_Viper(self.model_name, self.author_name, self.path_model)
   		except getopt.GetoptError:
   			module_help()
"""
Viper Model
"""