try:
    import jsonschema_rs

    class JsonSchemaCacheRust:
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

        def validate(self, schema_path: dict or str, data: dict) -> None:
            """
            Validate data against schema
            """
            return self.get_schema(schema_path).is_valid(data)

    json_schema_cache = JsonSchemaCacheRust()


except ImportError:
    from jsonschema import validate, ValidationError

    class JsonSchemaCacheSimple:

        def validate(self, schema_path: dict or str, data: dict) -> bool:
            """
            Validate data against schema
            """
            try:
                validate(data, schema_path)

                return True

            except ValidationError:
                return False


    json_schema_cache = JsonSchemaCacheSimple()


from .json_utils import read_json, dump_json

def validate_json_schema(json_data: dict, schema: dict | str) -> bool:
    """
    Validate json data against schema
    """
    return json_schema_cache.validate(schema, json_data)


__all__ = ("validate_json_schema", )
