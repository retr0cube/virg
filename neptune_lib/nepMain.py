from pathlib import Path
import os
import json
import shutil, stat

print("""
\033[0;34;46m🪐 Neptune API - v0.0.1_alpha - By RetroCube
\033[0m""")

class createProject:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        os.chdir("Project")
        self.check_dir_exist()
        os.mkdir(str(self.name))
        os.chdir(str(self.name))

    def check_dir_exist(self):
        if os.path.exists(str(self.name)):
            proj_dir = Path(f"{str(self.name)}/{str(self.name)}_RP" if os.path.exists()
            proj_dir.rmdir()
        else:
            pass

    def Res(self, cls):
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
        if cls == True:
            os.mkdir("{}_RP".format(str(self.name)))

    def Bes(self, cls):
        if os.getcwd() == str(self.name):
            os.chdir(str(self.name))
        if cls == True:
            os.mkdir("{}_BP".format(str(self.name)))
