*****************************************************************************
Powerful Pipes - The power of UNIX Pipes
*****************************************************************************

.. image:: https://img.shields.io/badge/License-Apache2-SUCCESS
   :target: https://github.com/42crunch/powerful-pipes/blob/main/LICENSE
   :alt: License
.. image:: https://img.shields.io/pypi/v/powerful-pipes
   :alt: PyPI
.. image:: https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10-blue
   :alt: Python Versions

.. figure:: https://raw.githubusercontent.com/42Crunch/powerful-pipes/main/docs/logo-250x250.png
   :align: center

In a nutshell ``Powerful Pipes`` is a library for working with UNIX Pipes.

Install
-------

.. code-block:: bash

    > pip install powerful-pipes

Quick Start
-----------

Create a CLI tool that reads from the JSON from stdin and dumps to the stdout, after processing input data:

.. code-block:: python

    # File: pipe-example.py
    from powerful_pipes import read_json_from_stdin, eprint, write_json_to_stdout

    for error, input_json in read_json_from_stdin():

        if error:
            # Here you can manager the error. Most common error is that the
            # input is not a valid json.
            # eprint(...) function dumps the error message to the stderr
            eprint(message="Error processing input from stdin")
            continue

        try:
            input_json["myData"] = "data 1"

        except Exception as e:
            report_exception(input_json, e)

        finally:
            # THIS STEP IS CRITICAL. If you don't put again in the stdout the
            # input data, following tools in the pipe chain wouldn't receive
            # the data
            write_json_to_stdout(input_json)

Using in CLI:

.. code-block:: bash

    > echo '{}' | python pipe-example.py | jq
    {
        "myData": "data 1"
    }


Documentation
-------------

You can find the complete documentation at: `Documentation <https://powerful-pipes.pythonhosted.org>`_

Authors
-------

Powerful Pipes was made by 42Crunch Research Team:

- `jc42 <https://github.com/jc42c>`_
- `cr0hn <https://github.com/cr0hn>`_


License
-------

Powerful Pipes is Open Source and available under the `Apache 2 <https://github.com/42crunch/powerful-pipes/blob/main/LICENSE>`_.

Contributions
-------------

Contributions are very welcome. See `CONTRIBUTING.md <https://github.com/42crunch/powerful-pipes/blob/main/CONTRIBUTING.md>`_ or skim existing tickets to see where you could help out.

Acknowledgements
----------------

Special thanks to `Cesar Gallego <https://github.com/CesarGallego>`_ for his mentoring in data processing, that inspired this project.

Project logo thanks to `Pipe icons created by srip - Flaticon <https://www.flaticon.com/free-icons/pipe>`_
