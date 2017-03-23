num = int(raw_input())
oper_seq = []
for i in range(num*2):
    opers = raw_input().split(' ')
    if oper_seq:
        if oper_seq[-1][-1][0] == opers[0]:
            oper_seq[-1].append(opers)
        else:
            oper_seq.append([opers])

    else:
        oper_seq.append([opers])

stack = []
tree = {}
for index, opers in enumerate(oper_seq):
    for i, item in enumerate(opers):
        if item[0] == "Push":
            stack.append(item[1])
            tree[item[1]] = {"left": None, "right": None, "visit": 0}
            if i < len(opers) - 1:
                tree[item[1]]["left"] = opers[i+1][1]
        elif item[0] == "Pop":
            node = stack.pop()
            if index < len(oper_seq) - 1 and i == len(opers) - 1:
                tree[node]["right"] = oper_seq[index+1][0][1]

node_name = oper_seq[0][0][1]
tmp = []
res = []
while tree or tmp:
    while node_name:
        node = tree.pop(node_name)
        node["visit"] += 1
        tmp.append({node_name: node})
        node_name = node["left"]
    if tmp:
        node = tmp.pop()
        name = node.keys()[0]
        if node[name]['visit'] < 2:
            node[name]['visit'] += 1
            node_name = node[name]['right']
            tmp.append(node)
        else:
            if node[name]['visit'] == 2:
                res.append(name)
                node_name = None

print ' '.join(res)
