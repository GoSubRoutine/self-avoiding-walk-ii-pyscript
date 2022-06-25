###
 # Self Avoiding Walk II [with Backtracking]
 # Coding Challenge #162
 # by The Coding Train / Daniel Shiffman
 #
 # https://TheCodingTrain.com/CodingChallenges/162-self-avoiding-walk.html
 #
 # PyScript conversion by GoToLoop (2022/Jun/24) (v1.1.0)
 #
 # https://Discourse.Processing.org/t/
 # converting-coding-challenge-self-avoiding-walk-backtracing-
 # from-p5-js-to-processing-java/35047/21
 #
 # https://Glitch.com/~self-avoiding-walk-ii-pyscript
###

from grid import Grid, REMOVED, PAUSED, FINISHED, BG
from spot import MAX_STRAIGHT_REMOVALS

from discover import whichProcessingFlavor, PJS, P5JS
from color import randomColor

from types import MethodType
from pyodide import create_proxy

import js
from js import document

_SCREENSHOT, _EXT = 'screen-', '.png'

p5 = object

def sketch(p: p5):
    p.flavor = whichProcessingFlavor(p)

    p.grid = None
    p.removals = 0

    p.setup = MethodType(_setup, p)
    p.draw  = MethodType(_draw, p)

    if p.flavor != P5JS: p.mousePressed = MethodType(_mousePressed, p)


def _setup(p: p5, MAIN = 'main'):
    dims = js._p5CanvasDims
    p.flavor != PJS and p.createCanvas(*dims) or p.size(*dims)

    p.noFill()

    p.grid = Grid(p)
    p.grid.states[BG] = randomColor(p)

    if p.flavor != PJS: p.canvas.oncontextmenu = lambda _: False

    if p.flavor == P5JS:
        mouseCallback = create_proxy(MethodType(_mousePressed, p))
        p._renderer.mousePressed(mouseCallback)
        document.body.insertBefore(p.canvas, p.select(MAIN).elt)


def _draw(p: p5):
    grid: Grid = p.grid
    states = grid.states

    if states[FINISHED]: return

    states[REMOVED] and grid.removeTailSpotIfTooOld()
    states[REMOVED] or  grid.getNextSpot()

    p.removals += states[REMOVED] and 1 or -p.removals
    p.removals == MAX_STRAIGHT_REMOVALS and grid.resetAllSpotsAges()

    grid.drawGridPath().drawTrailPoint()


def _mousePressed(p: p5, *_):
    btn: int = p.mouseButton
    grid: Grid = p.grid
    states = grid.states

    if btn == p.LEFT:
        states[PAUSED] ^= True
        p.noLoop() if states[PAUSED] else p.loop()

    elif btn == p.RIGHT:  states[BG] = randomColor(p)
    elif btn == p.CENTER: grid.createGrid()
    elif p.flavor == PJS: p.saveFrame()
    else: p.saveCanvas(p, _SCREENSHOT + str(p.frameCount) + _EXT)
