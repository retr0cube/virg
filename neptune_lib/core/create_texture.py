#_________________________#
# create_texture.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#

import json
import os
import shutil
import logging



class createTexture:

    def __init__(self, texture_type):
        self.texture_type = texture_type

        if not self.texture_type:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.texture_type should have an argument type.\n")
