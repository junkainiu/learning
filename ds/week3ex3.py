from collections import deque
num = int(raw_input())
opers = []
for i in range(num*2):
    opers = raw_input()
    oper = opers[0]
    num = opers[-1]
    if oper == 'push':
        opers.append(num)
    elif oper == 'pop':
        opers.append('pop')
