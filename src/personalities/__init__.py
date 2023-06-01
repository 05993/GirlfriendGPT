from .luna import luna
from .sacha import sacha
from .sandra import sandra
from .angele import angele

__all__ = [
    "sacha",
    "luna",
    "sandra",
  "angele",
    "get_personality"
]


def get_personality(name: str):
    try:
        return {
            "luna": luna,
            "sacha": sacha,
            "sandra": sandra,
          "Angèle": angele
        }[name]
    except Exception:
        raise Exception("The personality you selected does not exist!")
