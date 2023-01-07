from utils.color import colorFrom32bitTo8Bits

from modules.spot import (
    Spot,
    SPACING, HALF_SPACE, QUARTER_SPACE,
    PATH_STROKE, TRAIL_STROKE,
    AGE_THRESHOLD, AGE_INCREASE
)

REMOVED, PAUSED, FINISHED, BG = 'removed', 'paused', 'finished', 'bg'
STATES = REMOVED, PAUSED, FINISHED, BG

class Grid:
    _DONE = 'Solved!'

    def __init__(g, p: object):
        g.p = p

        g.states: dict[ str, bool | int | object ] = {
            REMOVED: False, PAUSED: False, FINISHED: False, BG: 0
        }

        g.path: list[Spot] = []

        g.pathStroke  = colorFrom32bitTo8Bits(p, PATH_STROKE)
        g.trailStroke = colorFrom32bitTo8Bits(p, TRAIL_STROKE)

        g.createGrid()


    def createGrid(g):
        p = g.p

        g.rows: int = p.height // SPACING
        g.cols: int = p.width  // SPACING
        g.matrix = g.rows * g.cols

        g.states[FINISHED] = g.states[REMOVED] = False

        rows, cols = tuple( range(g.rows) ), tuple( range(g.cols) )
        g.grid = tuple( tuple( Spot(p, r, c) for c in cols ) for r in rows )

        g.spot = g.grid[g.rows >> 1][g.cols >> 1]
        g.spot.visited = True

        g.path.clear()
        g.path.append(g.spot)

        return g


    def getNextSpot(g):
        g.spot = g.spot.nextSpot(g)

        if g.spot:
            g.path.append(g.spot)
            g.spot.visited = True
            g.states[REMOVED] = False

        else: g.removeTailSpot()

        if len(g.path) == g.matrix:
            print(g._DONE)
            g.states[FINISHED] = True

        return g


    def removeTailSpotIfTooOld(g):
        g.states[REMOVED] = g.p.frameCount - g.spot.age >= AGE_THRESHOLD
        g.states[REMOVED] and g.removeTailSpot().adjustAllSpotsAges()
        return g


    def removeTailSpot(g):
        g.states[REMOVED] = (length := len(g.path)) >= 2

        if g.states[REMOVED]:
            g.path.pop().clear()
            g.spot = g.path[length - 2]

        else: g.spot = g.path[0]

        return g


    def adjustAllSpotsAges(g):
        p5map = g.p.map

        if length := len(g.path) - 1:
            for i, spot in enumerate(g.path):
                spot.age += round(p5map(i, 0, length, 1, AGE_INCREASE))

        return g


    def resetAllSpotsAges(g):
        count: int = g.p.frameCount
        for spot in g.path: spot.age = count
        return g


    def drawGridPath(g):
        p = g.p

        p.background(g.states[BG])
        p.translate(HALF_SPACE, HALF_SPACE)

        p.strokeWeight(QUARTER_SPACE)
        p.stroke(g.pathStroke)

        p.beginShape()
        for spot in g.path: p.vertex(spot.x, spot.y)
        p.endShape()

        return g


    def drawTrailPoint(g):
        p = g.p

        p.strokeWeight(HALF_SPACE)
        p.stroke(g.trailStroke)
        p.point(g.spot.x, g.spot.y)

        return g
