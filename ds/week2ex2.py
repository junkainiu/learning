from collections import defaultdict


def _convert(l):
    l = [int(i) for i in l if i]
    return l


def analyze_input(polynomial):
    polynomial = polynomial.split(' ')
    if polynomial[0]:
        return int(polynomial[0]), _convert(polynomial[1:])
    else:
        return 0, []


def _print(res):
    if not any(res.values()):
        print 0, 0
    res_len = len(res)
    count = 0
    for k, v in sorted(res.iteritems(), key=lambda x: x[0], reverse=True):
        count += 1
        if v:
            if count == res_len:
                print v, k
            else:
                print v, k,


def print_product(p1_len, p1, p2_len, p2):
    res = defaultdict(int)
    for i in range(0, p1_len*2, 2):
        for j in range(0, p2_len*2, 2):
            k = p1[i+1] + p2[j+1]
            v = p1[i]*p2[j]
            res[k] += v
    if res:
        _print(res)
    else:
        print 0, 0


def print_sum(p1_len, p1, p2_len, p2):
    p = p1 + p2
    p_len = p1_len + p2_len
    res = defaultdict(int)
    for i in range(0, p_len*2, 2):
        k = p[i+1]
        v = p[i]
        res[k] += v
    if res:
        _print(res)
    else:
        print 0, 0


p1_len, polynomial_1 = analyze_input(raw_input())
p2_len, polynomial_2 = analyze_input(raw_input())

print_product(p1_len, polynomial_1, p2_len, polynomial_2)
print_sum(p1_len, polynomial_1, p2_len, polynomial_2)
