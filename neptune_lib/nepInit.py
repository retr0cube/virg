#__________________________#
# nepInit.py - Contributors:
# -RetroCube ;
#
#
#__________________________#
# Necessary Modules For The File #
import os
import json
import neptune_lib

WKD = os.getcwd()

class init:

    def __init__(self, pr_idtfr, vers):

        self.pr_idtfr = pr_idtfr
        self.vers = vers

    class Item:

        def __init__(self, itm_name):
           self.itm_name = itm_name

           os.chdir(WKD)
           f = open("projectName.txt", "r")
           NAME = f.read()
