import os
import json          #Necessary Modules For The File
import time
import shutil

print("""
\033[0;34;46m🪐 Neptune API - v0.0.1_alpha - By RetroCube
\033[0m""")
class Name:
    proj_name = None
    def __init__(self,project_name):
        self.project_name = self.proj_name
        self.Work_Dir()   
        time.sleep(0.5)
        self.Dir_Exists() 
 
           
class createProject: # The Main Class That Creates The Directory
    def __init__(self,version): # Initializing The Class
        self.version = version
        print('⏳ Loading...')
        time.sleep(1.5)
        self.Work_Dir()
        self.Dir_Exists()
        print('\n\033[1;32;40m√ Done!\033[0m')
    
    def Work_Dir(self): # Check The Working Directory
        wkd = str(os.getcwd())
        if wkd != 'Project':
           os.chdir('Project')
           os.path.join("Project")
        else:
          pass
    def Dir_Exists(self): # Checks if your Project Exists & Deletes It & Recreate it again with the new stuff
       if not os.path.exists(f"{str(Name.proj_name)}"):
           os.mkdir(str(Name.proj_name))
           os.chdir(str(Name.proj_name))
       elif os.path.exists(str(Name.proj_name)):
           shutil.rmtree(f"{str(Name.proj_name)}/{str(Name.proj_name)}_RP" and f"{str(Name.proj_name)}/{str(Name.proj_name)}_BP" and str(Name.proj_name))
           quit

    def Res(self, cls): # The Function Creates The Ressource Pack
        if os.getcwd() != str(Name.proj_name):
            os.path.join(str(Name.proj_name))
        else:
            quit
        if cls == True:
           os.mkdir(f"{str(Name.proj_name)}_RP")
        else:
            pass

    def Beh(self, cls): # The Function Creates The Behavior Pack
        if os.getcwd() != str(Name.proj_name):
            os.path.join(str(Name.proj_name))
        else:
            quit
        if cls == True:
           os.mkdir(f"{str(Name.proj_name)}_BP")
        else:
            pass


if __name__ == "__main__": # Preventing The File from Repeating In Something Weird Happened ^_~
    createProject()