#_________________________#
# create_project.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#

import os
import shutil
import logging
import time
import json
import uuid

import send2trash

#__________________________#

main_path = os.getcwd()

#__________________________#

# TODO: Add Exceptions

#__________________________#

class CreateProject:

    def _get_project_name(self):
        return self.name

    def _get_project_version(self):
        return self.version

    #__________________________#

    def __init__(self, name: str, identifier: str):
        self.name = name
        self.identifier = identifier

        #__________________________#

        if type(self.name) != str:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.name should be a str type.\n")

        if type(self.identifier) != str:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.identifier should be a str type.\n")

        #__________________________#

        print("\n\033[0;36;40m Info \033[0m Creating Project... \n")
        logging.debug(" self.name = {}".format(str(self.name)))
        logging.debug(" self.identifier = {}\n".format(str(self.identifier)))
        time.sleep(2)

        #__________________________#

        logging.info(" Creating project...")
        try:
            if not os.path.exists('Project'):
                os.mkdir('Project')
            os.chdir('Project')
            if os.path.isdir(self.name):
                send2trash.send2trash(self.name)
                os.mkdir(self.name)
                os.chdir(self.name)
            elif not os.path.isfile(self.name):
                os.mkdir(self.name)
                os.chdir(self.name)
            logging.info(" Task ended successfully!")
        except Exception :
            logging.error(" Task ended with an Exception! An error occured while creating the project, please try again!")
            print("\033[1;31;40m Error #2 \033[0m\033[1;30;40m-\033[0m  Unable to Create the Project. (Please try to delete it manually) ")
            quit()

    def project_version(self, version: list):
        self.version = version

        if type(self.version) != list:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.version should be a list type.\n")

        logging.debug(" version = v{}".format(self.version))

        #__________________________#

    def create_dependencies(self, beh: bool, res: bool):
        self.res = res
        self.beh = beh

        if type(self.beh) != bool:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.beh should be a bool type.\n")

        if type(self.res) != bool:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.res should be a bool type.\n")

        #__________________________#

        if res is True and beh is True:
            logging.info(' beh = True ; res = True') # Logging The Info into the .nepLog File #1
            folders = ['{}_res'.format(self.name), '{}_beh'.format(self.name)] # Sub-folders Stored in a List ;)
            for folder in folders: # A for Loop That will Make the Two Res & Beh Directories.
                os.mkdir(os.path.join(folder))
        elif res is True and beh is False:
            logging.info(' res = true')
            os.mkdir('{}_res'.format(self.name)) # Doing Pretty Much The same thing Twice
        elif res is False and beh is True:
            logging.info(' beh = True')
            os.mkdir('{}_beh'.format(self.name))

        else: # If None of the Conditions Occured The Following Error will Pop :)
            print("\033[1;31;40m /!\ Error #002 : You Need to specify at least One Dependency (Ressource Pack or Behavior Pack)\033[0m") # Printing The Error in the Terminal
            logging.error(' Unable to Create Dependency \nCAUSE:root: UNSPECIFIED_DEPENDENCY ') # Logging The Error into the .nepLog File #1
            quit() # This Will Quit The Program due to the Error #003

        #__________________________#


    def project_properties(self, desc, icon):
            self.desc = desc # Descripcion Amigos !
            self.icon = icon # pack_icon.png

            #__________________________#

            # Manifest JSON Structure fo Ressource Packs
            mnifst_rp = {
                "format_version": 2,
                "header": {
                    "name": str(self.name),
                    "description": str(self.desc),
                    "uuid": str(uuid.uuid1()),
                    "version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
                    ],
                    "min_engine_version": [
                        1,
                        13,
                        0
                    ]
                },
                "modules": [
                    {
                        "type": "resources",
                        "uuid": str(uuid.uuid4()),
                        "version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
                        ]
                    }
                ]
            }

            #__________________________#

            # Manifest JSON Structure fo Behavior Packs
            mnifst_bp = {
            	"format_version": 2,
            	"header": {
            		"name": str(self.name),
            		"description": str(self.desc),
            		"uuid": str(uuid.uuid4()),
            		"version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
            		],
            		"min_engine_version": [
            			1,
            			13,
            			0
            		]
            	},
            	"modules": [
            		{
            			"type": "data",
            			"uuid": str(uuid.uuid4()),
            			"version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
            			]
            		}
            	],
            	"dependencies": [
            		{
            			"version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
            			],
            			"uuid": str(uuid.uuid1())
            		}
            	]
            }

            #__________________________#

            # Manifest JSON Structure fo Behavior Packs
            mnifst = {
            	"format_version": 2,
            	"header": {
            		"name": str(self.name),
            		"description": str(self.desc),
            		"uuid": str(uuid.uuid4()),
            		"version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
            		],
            		"min_engine_version": [
            			1,
            			13,
            			0
            		]
            	},
            	"modules": [
            		{
            			"type": "data",
            			"uuid": str(uuid.uuid4()),
            			"version": [
            				int(self.version[0]),
            				int(self.version[1]),
            				int(self.version[2])
            			]
            		}
            	]
             }

            #__________________________#

            project_root = os.getcwd() # The Current Path Variable, Duh.

            #__________________________#

            if self.beh is True and self.res is True:
                os.chdir('{}_beh'.format(self.name)) # Changing Directory to the Ressource folder
                with open("manifest.json", "w") as manBP: # Creating & Dumping the .json with Data
                     json.dump(mnifst_bp, manBP, indent=4) #<-- Space Indentation
                     shutil.copy(self.icon, os.getcwd()) # Copying the pack_icon.png image to the destination
                os.chdir(project_root) # This Will Return To The Original Directory
                os.chdir('{}_res'.format(self.name))
                os.mkdir('textures')
                with open("manifest.json", "w") as manRP: # Doing The Same Thing again...
                     json.dump(mnifst_rp, manRP, indent=4)
                     shutil.copy(self.icon, os.getcwd()) # Copying the pack_icon.png image to the destination

            elif self.beh is False and self.res is True:
                os.chdir('{}_res'.format(self.name))
                os.mkdir('textures')
                with open("manifest.json", "w") as manRP: # Still Doing it...
                     json.dump(mnifst_rp, manRP, indent=4)

                shutil.copy(self.icon, os.getcwd()) # Copying the pack_icon.png image to the destination

            elif self.beh is True and self.res is False:
                os.chdir('{}_beh'.format(self.name))
                with open("manifest.json", "w") as manBP:
                     json.dump(mnifst, manBP, indent=4) # Finally! =)
                shutil.copy(self.icon, os.getcwd())

            logging.info(" created manifest files successfully!\n")

            #__________________________#

            os.chdir(main_path) # This Will Return To The Original Directory


#__________________________#
