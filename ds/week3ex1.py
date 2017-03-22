first_num = int(raw_input())
first_nodes = []
first_tree = {}
for i in range(first_num):
    node = raw_input()
    first_nodes.append(node.split(' '))

for node in first_nodes:
    first_tree[node[0]] = sorted([first_nodes[int(item)][0] for item in node[1:] if item != '-'])

second_num = int(raw_input())
second_nodes = []
second_tree = {}
for i in range(second_num):
    node = raw_input()
    second_nodes.append(node.split(' '))

for node in second_nodes:
    second_tree[node[0]] = sorted([second_nodes[int(item)][0] for item in node[1:] if item != '-'])
if first_tree == second_tree:
    print 'Yes'
else:
    print 'No'
