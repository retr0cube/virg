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


def createProject(name, identifier):
    global projectName
    global projectIdentifier
    projectIdentifier = identifier
    projectName = name
    #__________________________#

    if not os.path.exists('Project'):
        os.mkdir('Project')
    os.chdir('Project')
    if os.path.isdir(name):
        try:
          # Here if the "Project" Folder Doesn't Exist It will Create it & Create The Project
          shutil.rmtree(name, ignore_errors=True)
          time.sleep(1)
        except Exception:
           print(
               "\033[1;31;40m /!\ Error #003 : Unable to Create The Project Files (Please try to delete them properly)\033[0m\n")
        os.mkdir(name)
        os.chdir(name)
    elif not os.path.isdir(name):
        os.mkdir(name)
        os.chdir(name)

    #__________________________#

    print("\n\033[0;36;40m Info \033[0m Creating Project... \n")
    time.sleep(2)

    #__________________________#


def projectVersion( v_f, v_s, v_t):
    global vf, vs, vt
    vf = v_f
    vs = v_s
    vt = v_t


    #__________________________#

def createDependencies(beh=True, res=True):
    global isBeh
    global isRes
    isBeh = beh
    isRes = res

    if res is True and beh is True:
        folders = ['{}_res'.format(projectName), '{}_beh'.format(projectName)] # Sub-folders Stored in a List ;)
        for folder in folders: # A for Loop That will Make the Two Res & Beh Directories.
            os.mkdir(os.path.join(folder))
    elif res is True and beh is False:
        os.mkdir('{}_res'.format(projectName)) # Doing Pretty Much The same thing Twice
    elif res is False and beh is True:
        os.mkdir('{}_beh'.format(projectName))

    else: # If None of the Conditions Occured The Following Error will Pop :)
        print(f"""\033[1;31;40m /!\ Error #002 : You Need to specify at least One Dependency (Ressource Pack or Behavior Pack)\033[0m
        """) # Printing The Error in the Terminal
        logging.error(' Unable to Create Dependency \nCAUSE:root: UNSPECIFIED_DEPENDENCY ') # Logging The Error into the .nepLog File #1
        quit() # This Will Quit The Program due to the Error #003

    #__________________________#


def projectProperties( desc, icon):
        desc = desc # Descripcion Amigos !
        icon = icon # pack_icon.png

        #__________________________#

        # Manifest JSON Structure fo Ressource Packs
        mnifst_rp = {
            "format_version": 2,
            "header": {
                "name": str(projectName),
                "description": str(desc),
                "uuid": str(uuid.uuid1()),
                "version": [
                    int(vf),
                    int(vs),
                    int(vt)
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
                            int(vf),
                            int(vs),
                            int(vt)
                    ]
                }
            ]
        }

        #__________________________#

        # Manifest JSON Structure fo Behavior Packs
        mnifst_bp = {
        	"format_version": 2,
        	"header": {
        		"name": str(projectName),
        		"description": str(desc),
        		"uuid": str(uuid.uuid4()),
        		"version": [
        			int(vf),
        			int(vs),
        			int(vt)
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
        				int(vf),
        				int(vs),
        				int(vt)
        			]
        		}
        	],
        	"dependencies": [
        		{
        			"version": [
        				int(vf),
        				int(vs),
        				int(vt)
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
        		"name": str(projectName),
        		"description": str(desc),
        		"uuid": str(uuid.uuid4()),
        		"version": [
        			int(vf),
        			int(vs),
        			int(vt)
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
        				int(vf),
        				int(vs),
        				int(vt)
        			]
        		}
        	]
         }

        #__________________________#

        curPath = os.getcwd() # The Current Path Variable, Duh.

        #__________________________#

        if isBeh is True and isRes is True:
            os.chdir('{}_beh'.format(projectName)) # Changing Directory to the Ressource folder
            with open("manifest.json", "w") as manBP: # Creating & Dumping the .json with Data
                 json.dump(mnifst_bp, manBP, indent=4) #<-- Space Indentation
            os.chdir(curPath) # This Will Return To The Original Directory
            os.chdir('{}_res'.format(projectName))
            os.mkdir('textures')
            shutil.copy(icon, curPath) # Copying the pack_icon.png image to the destination
            with open("blocks.json", "w") as manRP: # Creating & Dumping the blocks.json with Data
                 json.dump({}, manRP, indent=4)
            with open("manifest.json", "w") as manRP: # Doing The Same Thing again...
                 json.dump(mnifst_rp, manRP, indent=4)

        elif isBeh is False and isRes is True:
            os.chdir('{}_res'.format(projectName))
            os.mkdir('textures')
            shutil.copy(icon, curPath) # Copying the pack_icon.png image to the destination
            with open("blocks.json", "w") as manRP: # Still Doing it...
                 json.dump({}, manRP, indent=4)
            with open("manifest.json", "w") as manRP: # Still Doing it...
                 json.dump(mnifst_rp, manRP, indent=4)

        elif isBeh is True and isRes is False:
            os.chdir('{}_beh'.format(projectName))
            with open("manifest.json", "w") as manBP:
                 json.dump(mnifst, manBP, indent=4) # Finally! =)

        #__________________________#

        os.chdir(curPath) # This Will Return To The Original Directory

        #__________________________#


if __name__ == "main":
    createProject() # This Will Make Sure That The Class Will Be Called once & Not twice <-- Bug Fixed YAY!
