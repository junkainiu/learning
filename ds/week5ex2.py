num = int(raw_input())
_set = [-1]*(num+1)


def find_root(num):
    if _set[num] < 0:
        return num
    else:
        _set[num] = find_root(_set[num])
        return _set[num]


def connect(num1, num2):
    root1 = find_root(num1)
    root2 = find_root(num2)
    parent1 = _set[root1]
    parent2 = _set[root2]
    if abs(parent1) < abs(parent2):
        _set[root2] += _set[root1]
        _set[root1] = root2
    else:
        _set[root1] += _set[root2]
        _set[root2] = root1


def print_res():
    res = [v for v in _set[1:] if v < 0]
    _len = len(res)
    if _len == 1:
        print "The network is connected."
    else:
        print "There are %s components." % _len


while True:
    opers = raw_input()
    if opers == 'S':
        break
    oper, num1, num2 = opers.split(' ')
    if oper == 'C':
        root1 = find_root(int(num1))
        root2 = find_root(int(num2))
        if root1 == root2:
            print "yes"
        else:
            print "no"
    elif oper == 'I':
        connect(int(num1), int(num2))

print_res()
