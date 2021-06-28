#__________________________#
# nepMain.py - Contributors:
# -RetroCube ;
#
#
#__________________________#
# Necessary Modules For The Project #
import sys
import json
import uuid
import shutil
import os
import logging
#__________________________#

VERS = 'v0.0.1-Alpha:02' # API's Version

try:
    apiLog = "logfile.nepLog"
    if os.path.exists(apiLog):
        os.remove(apiLog)
    for handler in logging.root.handlers[:]: # Logging stuff for Errors/Issues
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=apiLog,level=logging.DEBUG)
    logging.info('API Started...')
    logging.debug('Init Class started...\n')
except Exception:
       print("\033[1;31;40m /!\ Error #002 : Unable to Create A log File (Please try Again)\033[0m\n")

print("\033[1;33;40m Warning \033[0m\033[1;30;40m- \033[0mYou are Using Python {}.{} \n".format(sys.version_info.major, sys.version_info.minor))

print("\033[0;36;40m Info \033[0m\033[1;30;40m- \033[0m 🌚 Neptune API by Retr0cube")

print("\033[1;35;40m Version \033[0m\033[1;30;40m- \033[0m v0.0.1_p:alpha:01\n")


# Legacy Codes :)
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
        self.name = name # The "Project" Name Variable =I

        if not os.path.exists('Project'):
            os.mkdir('Project')
            os.chdir('Project')
        elif os.path.exists('Project'):      # W.I.P Work in Progress
            os.chdir('Project')
            if os.path.isdir(self.name):
                shutil.rmtree(self.name, ignore_errors= True)
                os.mkdir(self.name)
                os.chdir(self.name)
            elif not os.path.isfile(self.name):
                os.mkdir(self.name)
                os.chdir(self.name)
        print("\n\033[0;36;40m Info \033[0m Creating Project... \n")




            # Here if the "Project" Folder Doesn't Exist It will Create it & Create The Project
            # If it exists then it will create the Project Folder [if it exists]

    def projectVersion(self, v_f, v_s, v_t):
        self.v_f = v_f # The First Left Number
        self.v_s = v_s # The Second Center Number
        self.v_t = v_t # The Third Right Number

    def createDependencies(self, res=True, beh=True):

        # if not os.getcwd() is str(self.name):
        #     try: # Here this Exception Will try to change the Working Directory or an error will pop
        #       os.chdir(str(self.name))
        #     except Exception:
        #       # print(f"""\033[1;31;40m /!\ Error #001 : Unable to Modify Files (Try to Delete Them Manually)\033[0m
        #       # """) # Printing The Error in the Terminal
        #       # logging.debug(' Failed To Modify Files ') # Logging The Error into the .nepLog File #1
        #       # quit() # This Will Quit The Program due to the Error #003


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


    def createManifest(self, isBeh, isRes, desc, icon):
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
                shutil.copy(self.icon, CURPATH) # Copying the pack_icon.png image to the destination
                with open("blocks.json", "w") as manRP: # # Creating & Dumping the blocks.json with Data
                     json.dump('{}', manRP, indent=4)
                with open("manifest.json", "w") as manRP: # Doing The Same Thing again...
                     json.dump(mnifst_rp, manRP, indent=4)

                logging.info(' ManifestRP & BP set to TRUE')
                os.chdir(CURPATH)

            elif isBeh is False and isRes is True:
                os.chdir('{}_res'.format(self.name))

                shutil.copy(self.icon, CURPATH) # Copying the pack_icon.png image to the destination
                with open("blocks.json", "w") as manRP: # Still Doing it...
                     json.dump('{}', manRP, indent=4)
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


if __name__ == "main":
    Init() # This Will Make Sure That The Class Will Be Called once & Not twice <-- Bug Fixed YAY!
