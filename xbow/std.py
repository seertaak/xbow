from typing import *
from dataclasses import dataclass

string = Annotated[str, "std::string"]
vector = Annotated[list, "std::vector"]
array = Annotated[list, "std::vector"]
