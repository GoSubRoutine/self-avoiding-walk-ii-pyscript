from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: from grid import Grid

from step import Step
from random import choice

AGE_THRESHOLD = 200
AGE_INCREASE = 5
MAX_STRAIGHT_REMOVALS = 200

SPACING = 10
HALF_SPACE = SPACING * .5
QUARTER_SPACE = SPACING * .25

PATH_STROKE = -1 # white
TRAIL_STROKE = 0xffFFA000 # orange

class Spot:
    def __init__(s, p: object, row: int, col: int):
        s.c = col
        s.r = row

        s.x = s.c * SPACING
        s.y = s.r * SPACING

        s.visited = False
        s.p = p
        s.age: int = p.frameCount

        s.options = Step.allDirections()
        s.dirs: list[Step] = []


    def clear(s):
        for step in s.options: step.tried = False
        s.visited = False
        s.age = s.p.frameCount
        return s


    def nextSpot(s, grid: Grid):
        rr = grid.rows
        cc = grid.cols
        sr = s.r
        sc = s.c

        spot2d = grid.grid
        valid = Step.isValidAlt

        dirs = s.dirs
        dirs.clear()

        for step in s.options:
            r = sr + step.y
            c = sc + step.x
            not step.tried and valid(spot2d, r, c, rr, cc) and dirs.append(step)

        if not len(dirs): return

        step = choice(dirs)
        step.tried = True

        return spot2d[sr + step.y][sc + step.x]
