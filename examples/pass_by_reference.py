import random
import datetime

from powerful_pipes import read_from_stdin_by_file_ref, eprint, write_to_stdout_by_file_ref, report_exception


def main():

    for error, input_json in read_from_stdin_by_file_ref(auto_delete=False):

        if error:
            # Here you can manager the error. Most common error is that the
            # input is not a valid json.
            # eprint(...) function dumps the error message to the stderr
            eprint(message=f"Error processing input from stdin: {error}")
            continue

        try:
            input_json[str(random.randint(10, 1000))] = datetime.datetime.now()

        except Exception as e:
            report_exception(input_json, e)

        finally:
            # THIS STEP IS CRITICAL. If you don't put again in the stdout the
            # input data, following tools in the pipe chain wouldn't receive
            # the data
            write_to_stdout_by_file_ref(input_json)


if __name__ == '__main__':
    main()
