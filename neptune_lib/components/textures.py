#_________________________#
# textures.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#


from __future__ import annotations
# from typing import List, Dict, Union, Optional
import json

import attr
# import cattr

@attr.dataclass
class Block:
    brightness_gamma: int
    carried_textures: Union[CarriedTexture, str]

@attr.dataclass
class CarriedTexture:
    down: Optional[str] = None
    east: Optional[str] = None
    north: Optional[str] = None
    south: Optional[str] = None
    west: Optional[str] = None
    up: Optional[str] = None

@attr.dataclass
class Textures:
    down: Optional[str] = None
    east: Optional[str] = None
    north: Optional[str] = None
    south: Optional[str] = None
    west: Optional[str] = None
    up: Optional[str] = None

@attr.dataclass
class Sound:
    type: str


# BlockJsonSchema = Dict[str, Block]
# data = {"project:block": Block(brightness_gamma=2,
#                                carried_textures=CarriedTexture(down="grass_carried_top"))}
#
# print(json.dumps(cattr.unstructure(data), indent=4))
