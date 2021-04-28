#__________________________#
# nepMain.py - Contributors:
# -RetroCube ;
#
#
#__________________________#
# Necessary Modules For The File
import random
import neptune_lib
import uuid
import os
import json
import shutil


print("""
\033[0;34;46m🪐 Neptune API - v0.0.1_alpha - By RetroCube
\033[0m""")


class createProject:
    W_K_D = os.getcwd()

    def __init__(self, name, version):
        self.name = name
        self.version = version
        os.chdir("Project")
        self.if_check_dir_exist()
        print(f"""\033[0;30;47m⏲ Loading...\033[0m
        """)
        try:
            os.mkdir(str(self.name))
            os.chdir(str(self.name))
            print(f"""\033[1;32;40m√ Done -  {random.randrange(-100000000,100000000)}\033[0m
          """)
        except Exception as e:
            print(f"""\033[1;31;40m /!\ Error : Unable to Overwrite Files (Try to Delete Them Manually)\033[0m
            """)

    def if_check_dir_exist(self):
        if os.path.exists(str(self.name)):
            shutil.rmtree(str(self.name), ignore_errors=True)
        else:
            pass

    uuid1 = uuid.uuid1()
    uuid3 = uuid.uuid4()

    def createManifest_rp(self):

        mnifst_rp = {
            "format_version": 2,
            "header": {
                "name": str(self.name),
                "description": "",
                "uuid": str(self.uuid1),
                "version": [
                    1,
                    0,
                    0
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

    def Res(self, cls):
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
            # for subfolder_name in self.project_subfolders: # Creating Sub Folders For Ressource Pack
            #     print("hi")
            #     os.makedirs(os.path.join( '', subfolder_name))
        if cls is True:
            os.mkdir("{}_RP".format(str(self.name)))
            os.chdir("{}_RP".format(str(self.name)))
            self.createManifest_rp()

    def Beh(self, cls):
        os.chdir(f"{self.W_K_D}/Project/{self.name}")
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
        if cls is True:
            os.mkdir("{}_BP".format(str(self.name)))


if __name__ == "main":
    createProject()
