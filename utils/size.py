# https://developer.Mozilla.org/en-US/docs/Web/API/Screen/availWidth

from typing import Sequence
from js import screen, Float32Array, Uint8Array, Uint16Array

_w: int = screen.availWidth
_h: int = screen.availHeight

SIZES: tuple[ Sequence[int | float] ] = ( # rows, cols, ver, hor
    Float32Array.of(1, 1, .779),          # 01 canvas
    Uint8Array.of(2, 1),                  # 02 canvases
    Uint8Array.of(1, 3),                  # 03 canvases
    Float32Array.of(2, 2, .848),          # 04 canvases
    Uint8Array.of(2, 3),                  # 05 canvases
    Uint8Array.of(3, 2),                  # 06 canvases
    Uint8Array.of(2, 4),                  # 07 canvases
    Uint8Array.of(4, 2),                  # 08 canvases
    Uint8Array.of(3, 3),                  # 09 canvases
    Uint8Array.of(5, 2),                  # 10 canvases
    Uint8Array.of(4, 3),                  # 11 canvases
    Uint8Array.of(3, 4)                   # 12 canvases
)

def canvasSize(rows = 1, cols = 1, ver = .845, hor = .976) -> Sequence[int]:
    return Uint16Array.of(_w / cols * hor, _h / rows * ver)

def canvasMappedToDimensions(num: int):
    return SIZES[ max(0, min(len(SIZES) - 1, int(num) - 1)) ]
