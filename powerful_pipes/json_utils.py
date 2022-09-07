try:
    import json as js
    import orjson as json

    JSON_LIBRARY = "orjson"

except ImportError:
    import json

    JSON_LIBRARY = "json"

from .typing import JSON

def dump_json(obj: dict or list) -> str:
    """Dumps json using most efficient JSON library available"""
    try:
        dump_text = json.dumps(obj)
    except TypeError:
        global JSON_LIBRARY
        JSON_LIBRARY = "json"
        dump_text = js.dumps(obj)

    if JSON_LIBRARY == "orjson":
        dump_text = dump_text.decode()

    return dump_text

def read_json(data: str or bytes) -> JSON:
    """Reads json using most efficient JSON library available"""
    if JSON_LIBRARY != "orjson" and hasattr(data, "decode"):
        data = data.decode()

    return json.loads(data)


__all__ = ("dump_json", "read_json")
