start, num, reverse_num = raw_input().split(' ')
reverse_num = int(reverse_num)

from collections import deque

def reverse(l, last_addr='-1'):
    for i in range(reverse_num - 1, -1, -1):
        start, data, _next = l[i]
        if i > 0:
            print start, data, l[i-1][0]
        else:
            print start, data, last_addr

lines = {}
tmp = deque()
next_tmp = deque()

for i in range(int(num)):
    node = raw_input().split(' ')
    lines[node[0]] = (node[1], node[2])

data, addr = lines[start]
tmp.append((start, data, addr))

for i in range(min(num, reverse_num - 1)):
    data, next_addr = lines[addr]
    tmp.append((addr, data, next_addr))
    addr = next_addr

while True:
    if addr == '-1':
        break

    for i in range(reverse_num):
        if addr == '-1':
            break
        data, next_addr = lines[addr]
        next_tmp.append((addr, data, next_addr))
        addr = next_addr
    if len(tmp) == reverse_num:
        if len(next_tmp) == reverse_num:
            reverse(tmp, last_addr=next_tmp[-1][0])
            tmp, next_tmp = next_tmp, deque()
        else:
            if next_tmp:
                reverse(tmp, last_addr=next_tmp[0][0])
                tmp, next_tmp = next_tmp, deque()

if tmp:
    if len(tmp) == reverse_num:
        reverse(tmp)
    else:
        for i in tmp:
            print ' '.join(i)

if next_tmp:
    if len(next_tmp) == reverse_num:
        reverse(next_tmp)
    else:
        for i in next_tmp:
            print ' '.join(i)
