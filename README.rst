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

