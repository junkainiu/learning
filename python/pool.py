from multiprocessing import Pool

def f(x):
    return x*3

p = Pool(processes=5)
print p.apply_async(f, (3,))
