
def deco(f):
    def wrapped(*args, **kwargs):
        print 'before'
        r = f(*args, **kwargs)
        print 'after'
        return r
    return wrapped


@deco
def add(a, b):
    return a + b
