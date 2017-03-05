def t():
    for i in range(10):
	print 'a'
	yield i

def x(a):
    for i in a:
	print 'b'
	yield i

t = t()
y = x(t)
for i in y:
    print i
