class IterRator(object):

    def __init__(self, l, n):
        self.l = l
        self.n = n
        self.i = 0

    def __iter__(self):
        for i in range(len(self.l)):
            yield self.l[i: i+self.n]


it = IterRator([1,2,3], 2)
for item in it:
    print item
