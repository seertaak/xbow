from typing import *
from contextlib import contextmanager

from dataclasses import dataclass, fields
from textwrap import dedent


def record(*args, **kwargs):
    result = dataclass(*args, **kwargs)

    result.__cpp_code__ = f"def_record({result.__name__},\n" + ",\n".join(
        f"    ({f.type.__metadata__[0]}, {f.name})"
        for f
        in fields(result)
    ) + "\n);"

    return result


int8_t = Annotated[int, "int8_t"]
int16_t = Annotated[int, "int16_t"]
int32_t = Annotated[int, "int32_t"]
int64_t = Annotated[int, "int64_t"]
uint8_t = Annotated[int, "uint8_t"]
uint16_t = Annotated[int, "uint16_t"]
uint32_t = Annotated[int, "uint32_t"]
uint64_t = Annotated[int, "uint64_t"]


def cpp_code(T: type):
    return T.__cpp_code__



double = Annotated[float, "double"]
float = Annotated[float, "float"]


@record
class point:
    x: float
    y: float


@contextmanager
def namespace(module):
    s = f"using namespace {module.__name__};"
    try:
        yield "{" + s + "}"
    finally:
        pass


print(cpp_code(point))

