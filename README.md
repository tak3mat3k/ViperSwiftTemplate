## Python Template Swift Viper Module

Template script in python, for create a Viper Module in Swift

# Steps

- Download the Folder
- cd /ViperModule_Swift
- Takeshi$ python Viper.py -n YourModuleName
- And Thats it

# Folder Structure

It Create a Folder With the bellow Structure
- YourModuleName
	- Logic
    	- Interactor
        	- YourModuleNameInteractor.swift
    - Module
    	- YourModuleNameInteractorInputInterface.swift
        - YourModuleNameInteractorOutputInterface.swift
        - LanesLoadModule.swift
        - LanesPresenterInterface.swift
        - LanesViewInterface.swift
    - UI
    	- Presenter
        	- YourModuleNamePresenter.swift
        - View
        	- YourModuleNameViewController.swift
        - Wireframe
        	- YourModuleNameWireframe.swift
            
   # Configurations 
   
   Inside the Folder ther are one file called **constants.py** 
`  
			"""
			Constants
			"""
			DEFAULT_CREATOR = "Takeshi Kajino Morales"
			DEFAULT_MODEL_PATH = ".."
			DEFAULT_COMPANY_NAME = "Tak3mat3"
			DEFAULT_COMPANY_URL = "https://github.com/tak3mat3k"
			"""
			End Constants
			"""
`
   
            
         
