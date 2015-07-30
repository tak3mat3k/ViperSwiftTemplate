from logs import *
from constants import *

class ClassType (object):

	@classmethod
	def begin(self):
		return "{"

	@classmethod
	def end(self):
		return "}"

	@classmethod
	def protocol(sef):
		return "protocol "

	@classmethod
	def classIdentifier(sef):
		return "class"

	@classmethod
	def interface(self):
		return "class"

	@classmethod
	def implementation(self):
		return "{no - implementation}"

class Property(object):
	
	@classmethod
	def var(self, interface_or_class, name, optional=False):
		optional = '?'
		return "\tvar %s:%s%s" % (name, interface_or_class, optional)

	@classmethod
	def weakVar(self, interface_or_class, name, optional=False):
		optional = '?'
		return "\tweak var %s:%s%s" % (name, interface_or_class, optional)

	@classmethod
	def let(self, interface_or_class, name, optional=False):
		optional = '?'
		return "\tlet %s:%s%s" % (name, interface_or_class, optional)

	@classmethod
	def nonatomic_weak_interface(self, interface_class):
		return " var potato1 %s " % interface_class

	@classmethod
	def nonatomic_assign_interface_view(self, interface_class):
		return " var potato2 %s " % interface_class

	@classmethod
	def nonatomic_strong_interface(self, interface_class):
		return " var potato3 %s " % interface_class

	@classmethod
	def nonatomic_strong_class(self, className):
		return " var potato4 %s " % className

	@classmethod
	def nonatomic_assign_class(self, className):
		return " var potato5 %s " % className


class ViperClass(object):
	
	module_name = ''
	file_name = ''
	folder = None
	class_file = None
	array_Interfaces = []
	array_Imports = []
	array_properties = []
	array_classes = []
	array_protocols = []
	array_methods = []

	def __init__(self, module_name, folder, class_file=None):
		super(ViperClass, self).__init__()
		self.module_name = module_name
		self.folder = folder
		self.class_file = class_file
		self.clear()
		self.addImports(self.baseImport())

	def clear(self):
		self.array_Interfaces = []
		self.array_Imports = []
		self.array_properties = []
		self.array_classes = []
		self.array_protocols = []

	def fName(sef):
		return "FileName.swift"

	def cName(self):
		return "ClassName"

	def cType(self):
		return ClassType.interface()

	def className(self):
		return self.module_name + "" + self.cName()

	def fileName(self):
		return self.module_name + "" + self.fName()

	def folderPath(self):
		pass

	def createFile(self):
		filepath = self.folderPath() + "/" + self.fileName()
		print filepath
		fh = open(filepath, "a")
		return fh
			
	def write(self, string):
		self.class_file.write(string)

	def closeFile(self):
		self.class_file.close()

	def copyRight(self):
		copyright = "//" + "\n" \
		"// " + self.fileName() + "\n" \
		"// Copyright (c) 2015 " + DEFAULT_COMPANY_NAME + " " + "(" + DEFAULT_COMPANY_URL  + ")" + "\n" \
		"// Creator " + DEFAULT_CREATOR + "\n" \
		"//" + "\n\n"
		return copyright

	def baseImport(self):
		return "Foundation"

	def imports(self):
		if len(self.array_Imports) > 0:
			imports_list = '\n'.join([str(x) for x in self.array_Imports])
			return imports_list + "\n"
		else:
			return ""

	def inherit(self):
		return ""

	def interfaces(self):
		if len(self.array_Interfaces) > 0:
			interfaces_list = ', '.join([str(x) for x in self.array_Interfaces])
			interfaces = ":" + " " + interfaces_list + ""
		else:
			interfaces = " "

		return interfaces

	def properties(self):
		if len(self.array_properties) > 0:
			properties_list = '\n'.join([str(x) for x in self.array_properties])
			return "\n" + properties_list + "\n"
		else:
			return ""

	def classes(self):
		if len(self.array_classes) > 0:
			class_list = '\n'.join([str(x) for x in self.array_classes])
			return class_list + "\n"
		else:
			return "" 

	def protocols(self):
		if len(self.array_protocols) > 0:
			protocol_list = '\n'.join([str(x) for x in self.array_protocols])
			return "\n" + protocol_list + "\n"
		else:
			return "" 

	def methods(self):
		if len(self.array_methods) > 0 : 
			methods = '\n'.join([str(x) for x in self.array_methods])
			return "\n" + methods + "\n"
		else:
			return ""

	def addInterface(self, interface):
		self.array_Interfaces.append(interface)

	def addImports(self, imports):
		if not "<" in imports: 
			self.array_Imports.append('import %s' % imports)
		else:
			self.array_Imports.append('import %s' % imports)

	def addProperty(self, properties):
		self.array_properties.append(properties)

	def addMethod(self, method):
		self.array_methods.append(method)

	def addClass(self, className):
		self.array_classes.append("class %s;" % className)

	def addProtocol(self, protocol):
		self.array_protocols.append("protocol %s;" % protocol)

	def beginClass(self):
		return "\n" + self.cType() + " " + self.className() + "" + self.inherit() + ""

	def beginClassBody(self):
		return " " + ClassType.begin() + "\n"

	def closeClass(self):
		return "\n" + ClassType.end() + "\n"

	def create(self):
		self.class_file = self.createFile()
		self.write(self.copyRight())
		self.write(self.imports())
		self.write(self.classes())
		self.write(self.protocols())
		self.write(self.beginClass())
		self.write(self.interfaces())
		self.write(self.beginClassBody())
		self.write(self.properties())
		self.write(self.methods())
		self.write(self.closeClass())
		self.closeFile()


class ViperClass_Imp(ViperClass):

	interface_class = None
	array_inner_properties = []

	def __init__(self, module_name, folder_path, interface):
		super(ViperClass_Imp, self).__init__(module_name, folder_path)
		self.interface_class = interface
		self.clear()
		self.addImports(interface.fileName())

	def clear(self):
		super(ViperClass_Imp, self).clear()
		self.array_inner_properties = []

	def cType(self):
		return ClassType.implementation()

	def beginClass(self):
		return "\n" + self.cType() + " " + self.className() + "\n"

	def beginClassInnerInterface(self):
		return "\n" + self.interface_class.cType() + " " + self.className() + "()" + "\n"

	def pragmas(self):
		if len(self.interface_class.array_Interfaces) > 0:
			pragma_list = ''.join([ "//MARK: - \n//MARK: " + str(x) + "\n\n" for x in self.interface_class.array_Interfaces])
			pragma = "\n" + pragma_list
			return pragma
		else:
			return ""

	def addInnerProperties(self, properties):
		self.array_inner_properties.append(properties)

	def innerProperties(self):
		if len(self.array_inner_properties) > 0:
			properties_list = '\n'.join([str(x) for x in self.array_inner_properties])
			return "\n" + properties_list + "\n"
		else:
			return ""

	def innerInterfaceClass(self):
		self.write("\n")
		self.write(self.beginClassInnerInterface())
		self.write(self.innerProperties())
		self.write(self.closeClass())
		self.write("\n")


	def prepare(self):
		pass

	def create(self):

		self.class_file = self.createFile()

		self.write(self.copyRight())
		self.write(self.imports())

		#Inner interface class
		self.innerInterfaceClass()

		#Create the class	
		self.write(self.beginClass())
		self.write(self.pragmas())
		self.write(self.closeClass())
		self.closeFile()

class ViperClass_Interface(ViperClass):

	def inherit(self):
		return ""

	def cType(self):
		return ClassType.protocol()





		