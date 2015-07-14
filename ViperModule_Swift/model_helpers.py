import sys

from constants import *
from logs import *

"""
Helpers
"""
def module_help():
	print 'HELP: viper_model.py -n <model_name>'
	exit()
	
def exit():
	print "EXIT"
	sys.exit(2)

def validateModelName(model_name):
	if not model_name:
		LOG_ERROR("Undefined module name")
		module_help()

def validateCreatroName(creator_name):
	if not creator_name:
		return DEFAULT_CREATOR
	else:
		return creator_name

"""
End Helpers
"""