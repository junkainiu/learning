def fib():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a+b
        yield a

f = fib()
for i in f:
    print i
    import time
    time.sleep(1)
