from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spot import Spot
    spot2d = tuple[tuple[Spot, ...], ...]

class Step:
    def __init__(s, x: int, y: int):
        s.x = x
        s.y = y
        s.tried = False


    @staticmethod
    def allDirections():
        return Step(1, 0), Step(-1, 0), Step(0, 1), Step(0, -1)


    @staticmethod
    def isValid(grid: spot2d, r: int, c: int): return\
        0 <= r < len(grid) and 0 <= c < len(grid[r]) and not grid[r][c].visited


    @staticmethod
    def isValidAlt(grid: spot2d, r: int, c: int, rows: int, cols: int):
        return 0 <= r < rows and 0 <= c < cols and not grid[r][c].visited
