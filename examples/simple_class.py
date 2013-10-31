
class Foo(object):

    def __init__(self):
        self._x = 1

    @property
    def x(self):
        return self._x
