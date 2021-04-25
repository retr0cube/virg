# nepMain.py - Contributors:
# -RetroCube ;
#
#
#
import random
import os
import json # Necessary Modules For The File
import shutil

print("""
\033[0;34;46m🪐 Neptune API - v0.0.1_alpha - By RetroCube
\033[0m""")

class createProject:
    def __init__(self, name, version, project_subfolders):
        self.name = name
        self.version = version
        self.project_subfolders = project_subfolders
        os.chdir("Project")
        self.if_check_dir_exist()
        print(f"""\033[0;30;47m⏲ Loading...\033[0m
        """)
        try:
          os.mkdir(str(self.name))
          os.chdir(str(self.name))
          print(f"""\033[1;32;40m√ Done -  {random.randrange(-100000000,100000000)}\033[0m
          """)
        except:
            print(f"""\033[1;31;40m /!\ Error : Unable to Overwrite Files (Try to Delete Them Manually)\033[0m
            """)


    # def check_dir_exist(self):
    #     if os.path.exists(str(self.name)):
    #         proj_dir = Path(f"{str(self.name)}/{str(self.name)}_RP" if os.path.exists()
    #         proj_dir.rmdir()
    #     else:
    #         pass

    def if_check_dir_exist(self):
        if os.path.exists(str(self.name)):
           shutil.rmtree(str(self.name), ignore_errors= True)
        else:
           pass

    def Res(self, cls):
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
            # for subfolder_name in self.project_subfolders: # Creating Sub Folders For Ressource Pack
            #     print("hi")
            #     os.makedirs(os.path.join( '', subfolder_name))
        if cls == True:
            os.mkdir("{}_RP".format(str(self.name)))

    def Bes(self, cls):
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
        if cls == True:
            os.mkdir("{}_BP".format(str(self.name)))


if __name__ == "main":
    createProject()
