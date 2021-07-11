#_____The API Module____#
import neptune_lib as Neptune

descr = "Hi! This is a Dummy " # This is The Description Variable for your project
icon = "pack_icon.png" # The "pack_icon.png" Path for your project

add_on = Neptune.nepCore.createProject('MYADDON',"1.13.4",'mya')

#_____Project Properties____#

# add_on.createDependencies(True, True) # This Method create the Behavior Pack/Ressource Pack

#_____Manifest Properties____#
#
# add_on.projectVersion(0,1,1) # The Project Version e.g('1.0.0','4.5.3')
# add_on.projectProperties(descr, icon) # Here You put a description & an icon for your project

#_____Object Creation____#

# Neptune.createObject("ITEM","myItem","1.17.0") Soon™
