#_________________________#
# nepMain.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#

import sys
import json
import uuid
import shutil
import time
import os
import logging

#__________________________#

class nepCore:

    class createProject:

        projectName = None

        def __init__(self, name, version, identifier):
            self.name = self.projectName
            self.version = version
            self.identifier = identifier

        def projectVersion(self, v_f, v_s, v_t):
            self.v_f = v_f # The First Left Number
            self.v_s = v_s # The Second Center Number
            self.v_t = v_t # The Third Right Number

        def createDependencies(self, beh=True, res=True):

            print("\n\033[0;36;40m Info \033[0m Creating Project... \n")
            time.sleep(2)

            if res is True and beh is True:
                logging.info('Behavior & Ressource set to TRUE') # Logging The Info into the .nepLog File #1
                folders = ['{}_res'.format(self.name), '{}_beh'.format(self.name)] # Sub-folders Stored in a List ;)
                for folder in folders: # A for Loop That will Make the Two Res & Beh Directories.
                    os.mkdir(os.path.join(folder))
            elif res is True and beh is False:
                logging.info('Ressource set to TRUE')
                os.mkdir('{}_res'.format(self.name)) # Doing Pretty Much The same thing Twice
            elif res is False and beh is True:
                logging.info('Behavior set to TRUE')
                os.mkdir('{}_beh'.format(self.name))

            else: # If None of the Conditions Occured The Following Error will Pop :)
                print(f"""\033[1;31;40m /!\ Error #003 : You Need to specify at least One Dependency (Ressource Pack or Behavior Pack)\033[0m
                """) # Printing The Error in the Terminal
                logging.debug(' Unable to Create Dependency \nCAUSE:root: UNSPECIFIED_DEPENDENCY ') # Logging The Error into the .nepLog File #1
                quit() # This Will Quit The Program due to the Error #003


        def projectProperties(self, isBeh, isRes, desc, icon):
                self.desc = desc # Descripcion Amigos !
                self.icon = icon # pack_icon.png

                # Manifest JSON Structure fo Ressource Packs
                mnifst_rp = {
                    "format_version": 2,
                    "header": {
                        "name": str(self.name),
                        "description": str(self.desc),
                        "uuid": str(uuid.uuid1()),
                        "version": [
                            int(self.v_f),
                            int(self.v_s),
                            int(self.v_t)
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
                                    int(self.v_f),
                                    int(self.v_s),
                                    int(self.v_t)
                            ]
                        }
                    ]
                }

                # Manifest JSON Structure fo Behavior Packs
                mnifst_bp = {
                	"format_version": 2,
                	"header": {
                		"name": str(self.name),
                		"description": str(self.desc),
                		"uuid": str(uuid.uuid4()),
                		"version": [
                			int(self.v_f),
                			int(self.v_s),
                			int(self.v_t)
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
                				int(self.v_f),
                				int(self.v_s),
                				int(self.v_t)
                			]
                		}
                	],
                	"dependencies": [
                		{
                			"version": [
                				int(self.v_f),
                				int(self.v_s),
                				int(self.v_t)
                			],
                			"uuid": str(uuid.uuid1())
                		}
                	]
                }

                CURPATH = os.getcwd() # The Current Path Variable ! Duh.

                if isBeh is True and isRes is True:
                    os.chdir('{}_beh'.format(self.name)) # Changing Directory to the Ressource folder
                    with open("manifest.json", "w") as manBP: # Creating & Dumping the .json with Data
                         json.dump(mnifst_bp, manBP, indent=4) #<-- Space Indentation
                    os.chdir(CURPATH) # This Will Return To The Original Directory

                    os.chdir('{}_res'.format(self.name))
                    os.mkdir('textures')
                    shutil.copy(self.icon, CURPATH) # Copying the pack_icon.png image to the destination
                    with open("blocks.json", "w") as manRP: # # Creating & Dumping the blocks.json with Data
                         json.dump({}, manRP, indent=4)
                    with open("manifest.json", "w") as manRP: # Doing The Same Thing again...
                         json.dump(mnifst_rp, manRP, indent=4)

                    logging.info(' ManifestRP & BP set to TRUE')
                    os.chdir(CURPATH)

                elif isBeh is False and isRes is True:
                    os.chdir('{}_res'.format(self.name))
                    os.mkdir('textures')
                    shutil.copy(self.icon, CURPATH) # Copying the pack_icon.png image to the destination
                    with open("blocks.json", "w") as manRP: # Still Doing it...
                         json.dump({}, manRP, indent=4)
                    with open("manifest.json", "w") as manRP: # Still Doing it...
                         json.dump(mnifst_rp, manRP, indent=4)

                    logging.info(' ManifestRP set to TRUE')
                    os.chdir(CURPATH)

                elif isBeh is True and isRes is False:
                    os.chdir('{}_beh'.format(self.name))
                    with open("manifest.json", "w") as manBP:
                         json.dump(mnifst_rp, manBP, indent=4) # Finally! =)

                    logging.info(' ManifestBP set to TRUE')
                    os.chdir(CURPATH)

                elif isBeh is False and isRes is False: # If Both Conditions are False The Following Error will Pop :)
                    print(f"""\033[1;31;40m /!\ Error #004 : You Need to specify at least One Manifest file\033[0m
                    """) # Printing The Error in the Terminal
                    logging.debug(' Unable to Create Manifest files \nCAUSE:root: UNSPECIFIED_MANIFEST ') # Logging The Error into the .nepLog File
                    quit() # This Will Quit The Program due to the Error #004

    print(createProject.projectName)




if __name__ == "main":
    nepCore() # This Will Make Sure That The Class Will Be Called once & Not twice <-- Bug Fixed YAY!
