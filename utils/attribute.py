# https://developer.Mozilla.org/en-US/docs/Web/HTML/Global_attributes/data-*

# https://developer.Mozilla.org/en-US/docs/Web/JavaScript/Reference
# /Global_Objects/Array/some

from typing import Sequence
from re import compile
from js import document, Array

_PY_TAG = 'py-script'
_ATTRIBUTE = 'flavors'
_PATTERN = compile('\s*[;,\s]\s*')

def splitScriptData(attr = _ATTRIBUTE, pattern = _PATTERN) -> tuple[str, ...]:
    return tuple( _PATTERN.split(getScriptData(attr).strip().lower()) )


def getScriptData(attr = _ATTRIBUTE, _data: str = ''):
    def matchAttr(script: object, *_):
        nonlocal _data
        return (_data := getattr(script.dataset, attr, _data))

    scripts: Sequence[object] = Array.from_(document.querySelectorAll(_PY_TAG))
    scripts.push(*document.scripts)
    scripts.some(matchAttr)

    return _data
