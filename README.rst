Desugar
=======

Automatically translate python source using @decorator syntax to a form that
works on versions of python before 2.4.


For example, the following code:

.. code-block:: python

    class Foo(object):

        def __init__(self):
            self._x = 1

        @property
        def x(self):
            return self._x


Will be converted to this:

.. code-block:: python


    class Foo(object):

        def __init__(self):
            self._x = 1

        def x(self):
            return self._x
        x = property(x)


Usage
-----

Simply run:

.. code-block:: bash

    $ python desugar.py <source file>

The translated source will be written to stdout.

``desugar`` also has an ``--in-place`` option that, when used, overwrites the
source file instead of just writing to stdout.

Caveats
-------

* Formatting is lost in the translation from source to AST
  (The same goes for any comments in the module)

