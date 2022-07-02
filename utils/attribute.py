# https://developer.Mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*

# https://developer.Mozilla.org/en-US/docs/Web/JavaScript/Reference
# /Global_Objects/Array/some

from typing import Sequence
from re import compile
from js import document, Array

_PY_TAG = 'py-script'
_ATTRIBUTE = 'flavors'
_DELIMITERS = compile('\s*[;,\s]\s*')

arrayFrom: callable = getattr(Array, 'from')

def splitScriptData(attr = _ATTRIBUTE) -> tuple[str, ...]:
    return tuple( _DELIMITERS.split(getScriptData(attr).strip().lower()) )


def getScriptData(attr: str, data: str = ''):
    def matchAttr(script: object, *_):
        nonlocal data
        return (data := getattr(script.dataset, attr, data))

    scripts: Sequence[object] = arrayFrom(document.querySelectorAll(_PY_TAG))
    scripts.push(*document.scripts)
    scripts.some(matchAttr)

    return data
