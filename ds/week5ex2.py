num = int(raw_input())
_set = {}

def find_root(num):
    root = _set.get(num)
    if not root:
        return 0
    while True:
        root = _set[num]
        num = root['data']
        parent = root['parent']
        if parent <= 0:
            break
        else:
            num = parent
            root = _set[num]
    return num

def connect(num1, num2):
    root1 = find_root(num1)
    if not root1:
        _set[num1] = {'data': num1, 'parent': -1}
        root1 = num1
    root2 = find_root(num2)
    if not root2:
        _set[num2] = {'data': num2, 'parent': -1}
        root2 = num2
    parent1 = _set[root1]['parent']
    parent2 = _set[root2]['parent']
    if abs(parent1) < abs(parent2):
        _set[root2]["parent"] += _set[root1]["parent"]
        _set[root1]["parent"] = root2
    else:
        _set[root1]["parent"] += _set[root2]["parent"]
        _set[root2]["parent"] = root1


def print_res():
    res = [v['parent'] for v in _set.itervalues() if v['parent'] < 0]
    _sum = sum(res)
    _len = len(res)
    if abs(_sum) == num:
        if _len == 1:
            print "The network is connected."
        else:
            print "There are %s components." % _len
    else:
        print "There are %s components." % (_len + num - abs(_sum))

while True:
    opers = raw_input()
    if opers == 'S':
        break
    oper, num1, num2 = opers.split(' ')
    if oper == 'C':
        root1 = find_root(num1)
        root2 = find_root(num2)
        if root1 and root2 and root1 == root2:
            print "yes"
        else:
            print "no"
    elif oper == 'I':
        connect(num1, num2)

print_res()
