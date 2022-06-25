# https://developer.Mozilla.org/en-US/docs/Web/API/Screen/availWidth

from typing import Sequence
from js import screen, Float32Array, Uint8Array, Uint16Array

_w: int = screen.availWidth
_h: int = screen.availHeight

SIZES: tuple[ Sequence[int | float] ] = ( # rows, cols, ver, hor
    Float32Array.of(1, 1, .85),   # 01 canvas
    Uint8Array.of(2, 1),          # 02 canvas
    Uint8Array.of(1, 3),          # 03 canvas
    Uint8Array.of(2, 2),          # 04 canvas
    Uint8Array.of(2, 2),          # 05 canvas
    Uint8Array.of(3, 2),          # 06 canvas
    Uint8Array.of(2, 3),          # 07 canvas
    Uint8Array.of(4, 2),          # 08 canvas
    Uint8Array.of(3, 3),          # 09 canvas
    Uint8Array.of(5, 2),          # 10 canvas
    Uint8Array.of(2, 5),          # 11 canvas
    Uint8Array.of(3, 4)           # 12 canvas
)

def canvasSize(rows = 1, cols = 1, ver = .9, hor = .98) -> Sequence[int]:
    return Uint16Array.of(_w / cols * hor, _h / rows * ver)

def canvasMappedToDimensions(num: int):
    return SIZES[ max(0, min(len(SIZES) - 1, int(num) - 1)) ]
