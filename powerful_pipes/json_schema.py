import jsonschema_rs

from .json_utils import read_json, dump_json

class JsonSchemaCache:
    def __init__(self):
        self._cache = {}

    def get_schema(self, schema_path: dict or str) -> jsonschema_rs.JSONSchema:
        """
        Get schema from cache or load it from file
        """
        if type(schema_path) == str:
            schema = read_json(schema_path)
            schema_key = schema_path
        else:
            schema = schema_path
            schema_key = dump_json(schema_path)

        if schema_key not in self._cache:
            validator = jsonschema_rs.JSONSchema(schema)
            self._cache[schema_key] = validator

        return self._cache[schema_key]


json_schema_cache = JsonSchemaCache()


def validate_json_schema(json_data: dict, schema: dict | str) -> bool:
    """
    Validate json data against schema
    """
    return json_schema_cache.get_schema(schema).is_valid(json_data)


__all__ = ("validate_json_schema", )
