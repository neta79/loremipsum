"""Test plugin.


def load(*args, **kwargs): pass


def dump(*args, **kwargs): pass


def plugin():
    return (__name__.split('.')[-1], sys.modules.get(__name__))

"""
