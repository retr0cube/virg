#__________________________#
# nepMain.py - Contributors:
# -RetroCube ;
#
#
#__________________________#
# Necessary Modules For The File #
import random
import neptune_lib
import uuid
import os
import sys
import time
import json
import shutil

print("\033[0;33;40m # You are using Python {}.{} #\033[0m \n".format(sys.version_info.major, sys.version_info.minor))

print("""\033[0;34;46m🪐 Neptune API - v0.0.1_alpha - By RetroCube
\033[0m""")

if not os.path.exists("Project"):
    os.mkdir("Project")
else:
    os.chdir("Project")

class createProject:

    def __init__(self, name, version, desc):

        self.name = name
        self.version = version
        self.desc = desc
        self.W_K_D = os.getcwd()

        if not os.path.exists("projectName.txt") :
           with open("projectName.txt","a+") as FILE:
                FILE.write(self.name)

        print(f"""\033[0;30;47m⏲ Loading Files...\033[0m""")
        time.sleep(0.75)
        self.if_check_dir_exist()
        print(f"""   \033[0;30;47m|_ ⏳ Creating Ressource Pack...\033[0m""")
        time.sleep(0.75)
        print(f"""   \033[0;30;47m|_ ⌛ Creating Behavior Pack...\033[0m
        """)

        try:
            os.mkdir(str(self.name))
            os.chdir(str(self.name))

        except Exception as e :
            print(f"""\033[1;31;40m /!\ Error : Unable to Overwrite Files (Try to Delete Them Manually)\033[0m
            """)

        print(f"""\033[1;32;40m√ Done - {random.randrange(-1000000,1000000)}\033[0m
        """)

    def if_check_dir_exist(self):
        if os.path.exists(str(self.name)):
            shutil.rmtree(str(self.name), ignore_errors=True)
        else:
            pass

    def projectVersion(self, v_f, v_s, v_t):
        self.v_f = v_f
        self.v_s = v_s
        self.v_t = v_t

    uuid1 = uuid.uuid1()
    uuid3 = uuid.uuid4()

    def createManifest_rp(self):

        mnifst_rp = {
            "format_version": 2,
            "header": {
                "name": str(self.name),
                "description": str(self.desc),
                "uuid": str(self.uuid1),
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
                    "uuid": str(self.uuid3),
                    "version": [
                            1,
                            0,
                            0
                    ]
                }
            ]
        }
        with open("manifest.json", "w") as manRP:
            json.dump(mnifst_rp, manRP, indent=4)

    def createManifest_bp(self):
        mnifst_bp = {
        	"format_version": 2,
        	"header": {
        		"name": str(self.name),
        		"description": str(self.desc),
        		"uuid": str(self.uuid1),
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
        			"uuid": str(uuid.uuid1()),
        			"version": [
        				1,
        				0,
        				0
        			]
        		}
        	],
        	"dependencies": [
        		{
        			"version": [
        				1,
        				0,
        				0
        			],
        			"uuid": str(self.uuid3)
        		}
        	]
        }
        with open("manifest.json", "w") as manBP:
             json.dump(mnifst_bp, manBP, indent=4)

    def Res(self, cls):
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
        if cls is True:
            os.mkdir("{}_RP".format(str(self.name)))
            os.chdir("{}_RP".format(str(self.name)))
            self.createManifest_rp()

    def Beh(self, cls):
        os.chdir(f"{self.W_K_D}/{self.name}")
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
        if cls is True:
            os.mkdir("{}_BP".format(str(self.name)))
            os.chdir("{}_BP".format(str(self.name)))
            self.createManifest_bp()



if __name__ == "main":
    createProject()
