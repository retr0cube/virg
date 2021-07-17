#_________________________#
# nepMain.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#

# from __future__ import annotations
# from typing import List, Dict, Union, Optional
# import attr
# import cattr
import sys
import json
import uuid
import zipfile
import shutil
import time
import send2trash
import os
import logging

#______Logging Stuff_______#

try:
    apiLog = "logfile.nepLog"
    if os.path.exists(apiLog):
        os.remove(apiLog)
    for handler in logging.root.handlers[:]: # This will log Errors/Issues
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=apiLog,level=logging.DEBUG)
    logging.info(' nepMain.py started...')
    logging.debug(' loading components...\n')
except Exception:
       print("\033[1;31;40m /!\ Error #001 : Unable to Create A log File (Please try Again)\033[0m\n")

#__________________________#

mainPath = os.getcwd()
projectName = None

#__________________________#

class createProject:

    def __init__(createProject, name, identifier):
        global projectName
        global projectIdentifier
        projectName = createProject.name = name # The Project Name Variable =I
        projectIdentifier = createProject.identifier = identifier # The Identifier Name Variable

        #__________________________#

        print("\n\033[0;36;40m Info \033[0m Creating Project... \n")
        logging.debug(" projectName = {}".format(str(projectName)))
        logging.debug(" projectIdentifier = {}\n".format(str(projectIdentifier)))
        time.sleep(2)

        #__________________________#
        try:
            logging.info(" creating project...")
            if not os.path.exists('Project'):
                os.mkdir('Project')
            os.chdir('Project')
            if os.path.isdir(createProject.name):
                send2trash.send2trash(createProject.name)  # Here if the "Project" Folder Doesn't Exist It will Create it & Create The Project
                os.mkdir(createProject.name)
                os.chdir(createProject.name)
            elif not os.path.isfile(createProject.name):
                os.mkdir(createProject.name)
                os.chdir(createProject.name)
            logging.info(" task ended successfully!")
        except Exception :
            logging.info(" task ended with an Exception!")
            logging.error(" an error occured while creating the project, please try again!")
            logging.info(" exited with error #003")
            print("\033[1;31;40m /!\ Error #003 : Unable to Create The Project (Please try to delete it properly)\033[0m\n")
            quit()

    def projectVersion(createProject, v_f, v_s, v_t):
        createProject.v_f = v_f # The First Left Number
        createProject.v_s = v_s # The Second Center Number
        createProject.v_t = v_t # The Third Right Number
        logging.debug(" version = v{}.{}.{}".format(createProject.v_f,createProject.v_s,createProject.v_t))

        #__________________________#

    def createDependencies(createProject, beh=True, res=True):
        createProject.res = res
        createProject.beh = beh

        #__________________________#

        if res is True and beh is True:
            logging.info(' beh = True ; res = True') # Logging The Info into the .nepLog File #1
            folders = ['{}_res'.format(createProject.name), '{}_beh'.format(createProject.name)] # Sub-folders Stored in a List ;)
            for folder in folders: # A for Loop That will Make the Two Res & Beh Directories.
                os.mkdir(os.path.join(folder))
        elif res is True and beh is False:
            logging.info(' res = true')
            os.mkdir('{}_res'.format(createProject.name)) # Doing Pretty Much The same thing Twice
        elif res is False and beh is True:
            logging.info(' beh = True')
            os.mkdir('{}_beh'.format(createProject.name))

        else: # If None of the Conditions Occured The Following Error will Pop :)
            print(f"""\033[1;31;40m /!\ Error #002 : You Need to specify at least One Dependency (Ressource Pack or Behavior Pack)\033[0m
            """) # Printing The Error in the Terminal
            logging.error(' Unable to Create Dependency \nCAUSE:root: UNSPECIFIED_DEPENDENCY ') # Logging The Error into the .nepLog File #1
            quit() # This Will Quit The Program due to the Error #003

        #__________________________#


    def projectProperties(createProject, desc, icon):
            createProject.desc = desc # Descripcion Amigos !
            createProject.icon = icon # pack_icon.png

            #__________________________#

            # Manifest JSON Structure fo Ressource Packs
            mnifst_rp = {
                "format_version": 2,
                "header": {
                    "name": str(createProject.name),
                    "description": str(createProject.desc),
                    "uuid": str(uuid.uuid1()),
                    "version": [
                        int(createProject.v_f),
                        int(createProject.v_s),
                        int(createProject.v_t)
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
                                int(createProject.v_f),
                                int(createProject.v_s),
                                int(createProject.v_t)
                        ]
                    }
                ]
            }

            #__________________________#

            # Manifest JSON Structure fo Behavior Packs
            mnifst_bp = {
            	"format_version": 2,
            	"header": {
            		"name": str(createProject.name),
            		"description": str(createProject.desc),
            		"uuid": str(uuid.uuid4()),
            		"version": [
            			int(createProject.v_f),
            			int(createProject.v_s),
            			int(createProject.v_t)
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
            				int(createProject.v_f),
            				int(createProject.v_s),
            				int(createProject.v_t)
            			]
            		}
            	],
            	"dependencies": [
            		{
            			"version": [
            				int(createProject.v_f),
            				int(createProject.v_s),
            				int(createProject.v_t)
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
            		"name": str(createProject.name),
            		"description": str(createProject.desc),
            		"uuid": str(uuid.uuid4()),
            		"version": [
            			int(createProject.v_f),
            			int(createProject.v_s),
            			int(createProject.v_t)
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
            				int(createProject.v_f),
            				int(createProject.v_s),
            				int(createProject.v_t)
            			]
            		}
            	]
             }

            #__________________________#

            projectRoot = os.getcwd() # The Current Path Variable, Duh.

            #__________________________#

            if createProject.beh is True and createProject.res is True:
                os.chdir('{}_beh'.format(createProject.name)) # Changing Directory to the Ressource folder
                with open("manifest.json", "w") as manBP: # Creating & Dumping the .json with Data
                     json.dump(mnifst_bp, manBP, indent=4) #<-- Space Indentation
                     shutil.copy(createProject.icon, os.getcwd()) # Copying the pack_icon.png image to the destination
                os.chdir(projectRoot) # This Will Return To The Original Directory
                os.chdir('{}_res'.format(createProject.name))
                os.mkdir('textures')
                with open("blocks.json", "w") as manRP: # Creating & Dumping the blocks.json with Data
                     pass
                with open("manifest.json", "w") as manRP: # Doing The Same Thing again...
                     json.dump(mnifst_rp, manRP, indent=4)
                     shutil.copy(createProject.icon, os.getcwd()) # Copying the pack_icon.png image to the destination

            elif createProject.beh is False and createProject.res is True:
                os.chdir('{}_res'.format(createProject.name))
                os.mkdir('textures')
                with open("blocks.json", "w") as manRP: # Still Doing it...
                     pass
                with open("manifest.json", "w") as manRP: # Still Doing it...
                     json.dump(mnifst_rp, manRP, indent=4)

                shutil.copy(createProject.icon, os.getcwd()) # Copying the pack_icon.png image to the destination

            elif createProject.beh is True and createProject.res is False:
                os.chdir('{}_beh'.format(createProject.name))
                with open("manifest.json", "w") as manBP:
                     json.dump(mnifst, manBP, indent=4) # Finally! =)
                shutil.copy(createProject.icon, os.getcwd())

            logging.info(" created manifest files successfully!")

            #__________________________#

            os.chdir(mainPath) # This Will Return To The Original Directory

#__________________________#


if __name__ == "main":
    createProject() # This Will Make Sure That The Class Will Be Called once & Not twice <-- Bug Fixed YAY!
