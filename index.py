from sketch import sketch, p5, p5Sketch

from attribute import splitScriptData
from size import canvasSize, canvasMappedToDimensions
from discover import PJS, Q5JS, P5JS, FLAVORS

from random import choice

import js
from js import document

def instantiateFlavor(flavor: str, app: p5Sketch) -> p5:
    if flavor == PJS: return pjs(app)
    elif flavor == Q5JS: return q5js(app)
    elif flavor == P5JS: return p5js(app)
    else: return randomFlavor(app)


def randomFlavor(app: p5Sketch):
    mode = choice(FLAVORS)
    hasattr(js, 'flavor') and setattr(js.flavor, 'textContent', mode)
    return instantiateFlavor(mode, app)


def pjs(app: p5Sketch) -> p5:
    if hasattr(js, 'Processing'):
        canvas = document.body.appendChild(document.createElement('canvas'))
        return js.Processing.new(canvas, app)


def q5js(app: p5Sketch) -> p5:
    p: p5 = hasattr(js, 'Q5') and js.Q5.new()
    app(p)
    return p


def p5js(app: p5Sketch) -> p5: return hasattr(js, 'p5') and js.p5.new(app)

_flavors = splitScriptData()
js._p5CanvasDims = canvasSize(*canvasMappedToDimensions(len(_flavors)))

for mode in _flavors: instantiateFlavor(mode, sketch)
