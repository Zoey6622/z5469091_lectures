"""Docstring for the doc_example.py module.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

This example was adapted from Numpy's `example.py <https://numpydoc.readthedocs.io/en/latest/example.html#example>`_

"""

import os  # standard library imports first

# Do NOT import using *, e.g. from numpy import *
#
# Import the module using
#
#   import numpy
#
# instead or import individual functions as needed, e.g
#
#  from numpy import array, zeros
#
# If you prefer the use of abbreviated module names, we suggest the
# convention used by NumPy itself::

import numpy as np

# These abbreviated names are not to be used in docstrings; users must
# be able to paste and execute docstrings after importing only the
# numpy module itself, unabbreviated.


def foo(var1, var2, long_var_name='hi'):
    """Summarize the function in one line.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.

    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.

    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    """
    pass



# Explicitly setting the "read" and "text" modes
fobj = open('qan_stk_prc.csv', mode='rt')

# Using the default "text" mode
fobj = open('qan_stk_prc.csv', mode='r')

# Using the default "read" and "text" modes
fobj = open('qan_stk_prc.csv')