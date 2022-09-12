1.1.0
-----

- Changed signature for `read_json_from_stdin` and `read_from_stdin_by_file_ref`. Now it returns an exception as error, instead of a boolean.
- Added two new functions: `write_to_stdout_by_file_ref` and `read_from_stdin_by_file_ref`. They are similar to `read_json_from_stdin` and `write_to_stdout`, but they don't use `json` as intermediate format. They use file referencies instead.
- Added usage examples to the documentation.
- Improved how the `dump_json` and `read_json` choice the JSON library and improved error handling.

1.0.x
-----

First release
