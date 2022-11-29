from .typing import JSON

try:
    import orjson

    def read_json(data: str or bytes) -> JSON:
        """Reads json using most efficient JSON library available"""
        return orjson.loads(data)


    def dump_json(obj: dict or list, indent: bool = False) -> str:
        """Dumps json using most efficient JSON library available"""

        try:
            if indent:
                dump_text = orjson.dumps(obj, option=orjson.OPT_INDENT_2)
            else:
                dump_text = orjson.dumps(obj)
        except TypeError:
            # See: https://github.com/ijl/orjson#opt_non_str_keys
            dump_text = orjson.dumps(obj, option=orjson.OPT_NON_STR_KEYS)

        return dump_text.decode()

except ImportError:
    import json

    def read_json(data: str or bytes) -> JSON:
        """Reads json using most efficient JSON library available"""
        return json.loads(data)


    def dump_json(obj: dict or list, indent: bool = False) -> str:
        """Dumps json using most efficient JSON library available"""
        return json.dumps(obj, indent=2 if indent else None)


__all__ = ("dump_json", "read_json")
