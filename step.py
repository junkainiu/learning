l = [0,1,2,3,4,5,6,7,8,9]
n = 2
def doublestep(l, n):
    result = []
    for i in range(0, len(l),n):
        if i == 0:
            tmp = l[-2:]
        else:
            tmp = l[-(i+n):-i]
        result.append(tmp)
    print result

doublestep(l, n)
