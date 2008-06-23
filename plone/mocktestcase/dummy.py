
class Dummy(object):
    """Dummy object with arbitrary attributes
    """
    
    def __init__(self, **kw):
        self.__dict__.update(kw)