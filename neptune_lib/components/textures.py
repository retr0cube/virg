#_________________________#
# textures.py - Contributors:
# -RetroCube ;
#
#
#________Modules__________#


from typing import List, Dict, Union, Optional
import attr

@attr.dataclass
class Block:
    brightness_gamma: int = None
    textures: Union[Textures, str] = None
    sound: Union[Sound, str] = None
    carried_textures: Union[CarriedTexture, str] = None

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
