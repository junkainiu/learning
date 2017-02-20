class Tmeta(type):

    def __init__(self, *args, **kwargs):
        print 'yeal'
        print self.name
        super(Tmeta, self).__init__(*args, **kwargs)

class T(object):

    __metaclass__ = Tmeta
    name = 'h'
    def __init__(self, n):
        print '%s is me' % n


T('a')
