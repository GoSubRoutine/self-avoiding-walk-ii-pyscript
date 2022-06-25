PJS, Q5JS, P5JS = 'pjs', 'q5js', 'p5js'
FLAVORS = PJS, Q5JS, P5JS

def whichProcessingFlavor(p: object):
    if hasattr(p, 'param') and callable(p.param): return PJS
    elif hasattr(p, 'MAGIC') and isinstance(p.MAGIC, int): return Q5JS
    else: return P5JS
