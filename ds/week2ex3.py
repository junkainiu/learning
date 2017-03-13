start, num, reverse_num = raw_input().split(' ')
reverse_num = int(reverse_num)
lines = {}
res = []
for i in range(int(num)):
    node = raw_input().split(' ')
    lines[node[0]] = (node[1], node[2])
data, addr = lines.pop(start)
tmp = [(start, data ,addr)]
while lines:
    for i in range(reverse_num):
        if len(tmp) == reverse_num:
            break
        if addr == '-1':
            break
        data, next_addr = lines.pop(addr)
        tmp.append((addr, data, next_addr))
        addr = next_addr
    if len(tmp) == reverse_num:
        res.append(list(reversed(tmp)))
    else:
        res.append(tmp)
    tmp = []
if not res:
    res.append(tmp)
for index, sub_res in enumerate(res):
    if len(sub_res) == reverse_num:
        for i, item in enumerate(sub_res):
            start, data, _next = item
            if i < len(sub_res) - 1:
                sub_res[i] = (start, data, sub_res[i+1][0])
            else:
                if index == len(res) - 1:
                    sub_res[i] = (start, data, '-1')
                else:
                    sub_res[i] = (start, data, res[index+1][0][0])

for sub_res in res:
    for i in sub_res:
        print ' '.join(list(i))
