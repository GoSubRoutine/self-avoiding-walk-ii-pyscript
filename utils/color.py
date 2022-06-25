# https://developer.Mozilla.org/en-US/docs/Web/JavaScript/Reference
# /Global_Objects/Uint8Array

# https://developer.Mozilla.org/en-US/docs/Web/JavaScript/Reference
# /Global_Objects/DataView/setInt32

from typing import Sequence
from js import Uint8Array, Int32Array, DataView

ALL_COLORS: int = Int32Array.of(0xff << 0o30)[0] # signed 32-bit (4-byte)

_arr8Bit: Sequence[int] = Uint8Array.new(Int32Array.BYTES_PER_ELEMENT)
_bufView: object = DataView.new(_arr8Bit.buffer)

def colorFrom32bitTo8Bits(p: object, c: int) -> object | int:
    _bufView.setInt32(0, c)
    return p.color(*_arr8Bit.subarray(1), _arr8Bit[0])


def randomColor(p: object):
    return colorFrom32bitTo8Bits(p, p.random(ALL_COLORS))
