import abc


class Server(object):

    __metaclass = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self):
        pass
