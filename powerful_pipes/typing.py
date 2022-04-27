from typing import Union

# -------------------------------------------------------------------------
# Custom definition for JSON data typing.
#
# Found at: https://github.com/python/typing/issues/182#issuecomment-1076984118
# -------------------------------------------------------------------------
class JSONArray(list[JSON], Protocol):  # type: ignore
    __class__: Type[list[JSON]]  # type: ignore

class JSONObject(dict[str, JSON], Protocol):  # type: ignore
    __class__: Type[dict[str, JSON]]  # type: ignore

JSON = Union[None, float, str, JSONArray, JSONObject]
