class A(object):

    def __init__(self, name):
        self.name = name
        print '%s is inited' % self.name

    def __del__(self):
        print '%s is killed' % self.name

a = A('A')
b = A('B')
c = A('C')
b.x = c
c.x = b
