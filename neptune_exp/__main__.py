#_________________________#
# __main__.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#

import os
import logging
import sys
import neptune_exp
import atexit

#__________________________#

api_version = 'Experimental v2' # API's Version

print("\033[1;33;40m Python Info \033[0m\033[1;30;40m- \033[0mYou are Using Python {}.{} \n".format(sys.version_info.major, sys.version_info.minor))

print("\033[0;36;40m Info \033[0m\033[1;30;40m- \033[0m 🌚 Neptune API by Retr0cube")

print("\033[1;35;40m Version \033[0m\033[1;30;40m- \033[0m {}\n".format(api_version))

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
       print("\033[0;36;40m Error #1 \033[0m\033[1;30;40m- \033[0m\033[91m Unable to Create A log File (Please try Again) \033[0m")

#___Exit Handling Stuff____#

def exit_handler():
    logging.info(' Done !')
    print("\033[0;36;40m Info \033[0m\033[1;30;40m- \033[0m\033[92m √ Done!\033[0m")

atexit.register(exit_handler)

if __name__ == '__main__':
    neptune_exp.create_project.CreateProject()
