#_________________________#
# create_texture.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#

from typing import Dict
import json
import os
import shutil
import logging

import cattr

import neptune_lib

from neptune_lib.components.textures import *

#_________________________#

class CreateBlockTexture:

    def __init__(self, obj_name, texture_props):
        self.texture_props = texture_props
        self.obj_name = obj_name

        if not self.texture_props:
            print("\033[1;30;40m-\033[0m\033[1;31;40m Error \033[0m\033[1;30;40m- \033[0m\n")
            raise ValueError(" self.texture_type should have an argument type.\n")

        with open("blocks.json", "w") as block_json_file:

            json_schema = Dict[str, Block]
            block_data = {"dnb:{}".format( self.obj_name): self.texture_props}

            json.dump(cattr.unstructure(block_data), block_json_file, indent=4)
