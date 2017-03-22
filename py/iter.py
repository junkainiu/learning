class IterRator(object):

    def __init__(self, l, n):
        self.l = l
        self.n = n

    def __iter__(self):
        for i in range(0, len(self.l), 2):
            yield self.l[i: i+self.n]


it = IterRator([1,2,3,4,5], 2)
for item in it:
    print item
