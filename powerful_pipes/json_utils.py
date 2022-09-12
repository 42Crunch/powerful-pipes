import json

try:
    import orjson
except ImportError:
    ...

from .typing import JSON

def dump_json(obj: dict or list) -> str:
    """Dumps json using most efficient JSON library available"""
    try:
        json_lib = globals()["orjson"]
    except KeyError:
        json_lib = json

    try:
        dump_text = json_lib.dumps(obj)
    except TypeError as e:
        if "Dict" in str(e):
            # See: https://github.com/ijl/orjson#opt_non_str_keys
            dump_text = json_lib.dumps(obj, option=orjson.OPT_NON_STR_KEYS)
        else:
            dump_text = json.dumps(obj)

    if hasattr(dump_text, "decode"):
        dump_text = dump_text.decode()

    return dump_text

def read_json(data: str or bytes) -> JSON:
    """Reads json using most efficient JSON library available"""
    try:
        json_lib = globals()["orjson"]
    except KeyError:
        json_lib = json

    return json_lib.loads(data)


__all__ = ("dump_json", "read_json")
