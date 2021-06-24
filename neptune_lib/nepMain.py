#__________________________#
# nepMain.py - Contributors:
# -RetroCube ;
#
#
#__________________________#
# Necessary Modules For The File #
import neptune_lib
import os
import sys
import json
import uuid
import logging

VERS = 'v0.0.1-Alpha'

try:
    apiLog = "logfile.nepLog"
    if os.path.exists(apiLog):
        os.remove(apiLog)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=apiLog,level=logging.DEBUG)
    logging.info('API Started...')
    logging.debug('Init Class started...\n')
except Exception:
       print(f"""\033[1;31;40m /!\ Error #002 : Unable to Create A log File (Please try Again)\033[0m
       """)

print("\033[0;33;40m # You are using Python {}.{} #\033[0m \n".format(sys.version_info.major, sys.version_info.minor))

print("""\033[0;34;46m🪐 Neptune API - v0.0.1_alpha - By RetroCube
\033[0m""")

# Legacy Files :)
# class createProject:
#
#     def __init__(self, name, version, desc):
#
#         self.name = name
#         self.version = version
#         self.desc = desc
#         self.W_K_D = os.getcwd()
#         print(f"""\033[0;30;47m⏲ Loading Files...\033[0m""")
#         time.sleep(0.75)
#         self.if_check_dir_exist()
#         print(f"""   \033[0;30;47m|_ ⏳ Creating Ressource Pack...\033[0m""")
#         time.sleep(0.75)
#         print(f"""   \033[0;30;47m|_ ⌛ Creating Behavior Pack...\033[0m
#         """)
#         print(f"""\033[1;32;40m√ Done - {random.randrange(-1000000,1000000)}\033[0m
#         """)
#

class Init:

    def __init__(self, name):
        self.name = name

        if not os.path.exists("Project"):
           os.mkdir("Project")
           os.chdir("Project")
           os.mkdir(self.name)
        else:
           os.chdir("Project")
           if not os.path.exists(self.name):
              os.mkdir(self.name)
           else:
              os.chdir(self.name)


    def projectVersion(self, v_f, v_s, v_t):
        self.v_f = v_f
        self.v_s = v_s
        self.v_t = v_t

    def createDependencies(self, res=True, beh=True):

        if not os.getcwd() is str(self.name):
            try:
              os.chdir(str(self.name))
            except Exception:
              print(f"""\033[1;31;40m /!\ Error : Unable to Modify Files (Try to Delete Them Manually)\033[0m
              """)
              logging.debug(' Failed To Modify Files ')

        if res is True and beh is True:
            logging.info('Behavior & Ressource set to TRUE')
            folders = ['{}_res'.format(self.name), '{}_beh'.format(self.name)]
            for folder in folders:
                os.mkdir(os.path.join(folder))
        elif res is True and beh is False:
            logging.info('Ressource set to TRUE')
            os.mkdir('{}_res'.format(self.name))
        elif res is False and beh is True:
            logging.info('Behavior set to TRUE')
            os.mkdir('{}_beh'.format(self.name))
        else:
            print(f"""\033[1;31;40m /!\ Error #003 : You Need to specify at least One Dependency (Ressource Pack or Behavior Pack)\033[0m
            """)
            logging.debug(' Unable to Create Dependency \nCAUSE:root: UNSPECIFIED_DEPENDENCY ')
            quit()

        os.getcwd()

    def createManifest(self, isBeh, isRes, desc):
            self.desc = desc # Déscription Amigos !

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
                os.chdir('{}_beh'.format(self.name)) # Changing Directory to the Ressource folder #0
                with open("manifest.json", "w") as manBP: # Creating & Dumping the .json with Data #0
                     json.dump(mnifst_bp, manBP, indent=4) #<-- Space Indentation #0
                os.chdir(CURPATH) # This Will Return To The Original Directory #0
                os.chdir('{}_res'.format(self.name))  # Changing Directory to the Ressource folder #1
                with open("manifest.json", "w") as manRP: # Creating & Dumping the .json with Data #1
                     json.dump(mnifst_rp, manRP, indent=4) #<-- Space Indentation #1

                logging.info(' ManifestRP & BP set to TRUE') # Logging The Info into the .nepLog File #1
                os.chdir(CURPATH) # This Will Return To The Original Directory #1

            elif isBeh is False and isRes is True:
                os.chdir('{}_res'.format(self.name))  # Changing Directory to the Ressource folder #2
                with open("manifest.json", "w") as manRP: # Creating & Dumping the .json with Data #2
                     json.dump(mnifst_rp, manRP, indent=4) #<-- Space Indentation #2

                logging.info(' ManifestRP set to TRUE') # Logging The Info into the .nepLog File #2
                os.chdir(CURPATH) # This Will Return To The Original Directory #2

            elif isBeh is True and isRes is False:
                os.chdir('{}_beh'.format(self.name)) # Changing Directory to the Behavior folder #3
                with open("manifest.json", "w") as manBP: # Creating & Dumping the .json with Data #3
                     json.dump(mnifst_rp, manBP, indent=4) #<-- Space Indentation :) #3

                logging.info(' ManifestBP set to TRUE') # Logging The Info into the .nepLog File #3
                os.chdir(CURPATH) # This Will Return To The Original Directory ;) MAGIC! #3

            elif isBeh is False and isRes is False: # If Both Conditions are False The Following Error will Pop :)
                print(f"""\033[1;31;40m /!\ Error #004 : You Need to specify at least One Manifest file\033[0m
                """) # Printing The Error in the Terminal
                logging.debug(' Unable to Create Manifest files \nCAUSE:root: UNSPECIFIED_MANIFEST ') # Logging The Error into the .nepLog File
                quit() # This Will Quit The Program due to the Erro #004


if __name__ == "main":
    Init() # This Will Make Sure That The Class Will Be Called once & Not twice <-- Bug Fixed YAY!
