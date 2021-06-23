#__________________________#
# nepInit.py - Contributors:
# -RetroCube ;
#
#
#__________________________#
# Necessary Modules For The File #
import os
import json
import time
import neptune_lib

#
# class init(neptune_lib.createProject):
#
#     def __init__(self, pr_idtfr, vers):
#
#         self.pr_idtfr = pr_idtfr
#         self.vers = vers
#         neptune_lib.createProject.__init__(self)
#         self.name = name
#         print(self.name)
#
#     class Item(neptune_lib.createProject):
#
#         def __init__(self, itm_name):
#
#            self.itm_name = itm_name
#            time.sleep(0.75)
#            print(f"""   \033[0;30;47m|_ ⌛ Creating Items...\033[0m
#            """)
#            with open("{}.json".format(self.itm_name),"w") as ITEM:
#                pass
