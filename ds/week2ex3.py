start, num, reverse_num = raw_input().split(' ')
lines = {}
res = []
for i in range(int(num)):
    node = raw_input().split(' ')
    lines[node[0]] = (node[1], node[2])

data, addr = lines.pop(start)
tmp = [(start, data ,addr)]
while lines:
    for i in range(int(reverse_num)):
        if len(tmp) == int(reverse_num):
            break
        if addr == '-1':
            break
        data, next_addr = lines.pop(addr)
        tmp.append((addr, data, next_addr))
        addr = next_addr
    if len(tmp) == int(reverse_num):
        res.append(reversed(tmp))
    else:
        res.append(tmp)
    tmp = []

for sub_res in res:
    for i in sub_res:
        print ' '.join(list(i))
