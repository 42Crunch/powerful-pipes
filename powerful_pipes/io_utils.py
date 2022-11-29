import os
import sys
import select
import tempfile

from typing import Iterable, Tuple, Generator

from .typing import JSON
from .exceptions import NotConnectedToPipe
from .json_utils import read_json, dump_json
from .json_schema import validate_json_schema


def read_stdin_lines(read_timeout: int = 0) -> Iterable[str]:
    """
    Read stdin line by line and return the tuple:

    (IS_STDIN_PIPE, IS_STDOUT_PIPE, LINE)

    :param read_timeout: read timeout of stdin. 0 = infinite
    :type read_timeout: int
    """

    if sys.stdin.isatty():
        raise NotConnectedToPipe(
            "Input data must be entered as a UNIX pipeline. For example: "
            "'cat info.json | tool-name'")

    is_stdout_pipe = not sys.stdout.isatty()

    # -------------------------------------------------------------------------
    # Read info by stdin or parameter
    # -------------------------------------------------------------------------
    if read_timeout:
        if sys.stdin in select.select([sys.stdin], [], [], read_timeout)[0]:
            for line in sys.stdin.readlines():
                yield is_stdout_pipe, line

        else:
            yield is_stdout_pipe, None

    else:

        while 1:

            line = sys.stdin.readline()

            if not line:
                return

            yield is_stdout_pipe, line



def write_to_stdout(data: str, force_flush: bool = True):
    try:
        sys.stdout.write(f"{data}\n")
    except BrokenPipeError:
        print(
            f"[ERROR] when try to write data '{data}' in pipe",
            file=sys.stderr,
            flush=True
        )

    if force_flush:
        try:
            sys.stdout.flush()
        except BrokenPipeError:
            ...


def write_to_stderr(data: str):
    sys.stderr.write(f"{data}\n")

    try:
        sys.stderr.flush()
    except BrokenPipeError:
        ...


def read_json_from_stdin() -> Iterable[Tuple[Exception, JSON]]:
    # Read from the STDIN PIPE
    for _, line in read_stdin_lines():

        # noinspection PyBroadException
        try:
            # this var contains JSON data in our format
            yield None, read_json(line)

        except Exception as e:
            yield e, line


def write_json_to_stdout(
    data: JSON,
    force_flush: bool = True
):
    write_to_stdout(dump_json(data), force_flush=force_flush)


def write_json_to_stderr(data: JSON):
    write_to_stderr(dump_json(data))

def read_from_stdin_by_file_ref(auto_delete: bool = True) -> Iterable[Tuple[Exception, JSON]]:
    """
    Reads file references from stdin. Load file content and return the tuple:

    :return: (IS_ERROR, JSON)
    """
    for _, line in read_stdin_lines():

        # noinspection PyBroadException
        try:
            file_path = line.strip()

            with open(file_path, "r") as f:
                file_content = f.read()

            if auto_delete:
                os.remove(file_path)

            yield None, read_json(file_content)

        except Exception as e:
            yield e, line


def write_to_stdout_by_file_ref(
    data: JSON,
    force_flush: bool = True,
    file_prefix: str = "pwp-",
):
    name = tempfile.NamedTemporaryFile(prefix=file_prefix).name

    with open(name, "w") as f:
        f.write(dump_json(data))
        f.flush()

    write_to_stdout(name, force_flush=force_flush)


def read_and_validate_stdin(json_schema: dict) -> Generator[dict, None, None]:
    for error, json_message in read_json_from_stdin():
        if error:
            continue

        if json_schema and not validate_json_schema(json_message, json_schema):
            continue

        yield json_message

__all__ = ("read_json_from_stdin", "write_json_to_stdout", "write_to_stdout",
           "write_to_stderr", "write_json_to_stderr",
           "read_stdin_lines", "read_from_stdin_by_file_ref", "write_to_stdout_by_file_ref",
           "read_and_validate_stdin")
