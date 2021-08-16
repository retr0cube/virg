#_____The API Module____#

import neptune_lib

from neptune_lib.core import create_project

import os

#___________________________#

script_path = os.path.dirname(__file__)

#___________________________#

descr = "Hi! This is My add-on" # This is The Description Variable for your project
icon = open(f"{script_path}/src/pack_icon.png") # The "pack_icon.png" Path for your project

#_____Project Properties____#

add_on = create_project.CreateProject( "myaddon","mya")  #This Class Will create the project
add_on.create_dependencies(True, True) # This Method create the Behavior Pack/Ressource Pack

#_____Manifest Properties____#

add_on.project_version([1,7,1]) # The Project Version e.g('1.0.0','4.5.3')
add_on.project_properties(descr, icon) # Here You put a description & an icon for your project
