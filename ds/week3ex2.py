from collections import deque
num = int(raw_input())
nodes = {}
none_roots = []
for i in range(num):
    node = raw_input().split(' ')
    nodes[i] = node
    none_roots.extend([int(j) for j in node if j != '-'])

root = set(none_roots) ^ set(range(num))
start = root.pop()
queue = deque()
queue.append(start)
leaves = []
while True:
    if queue:
        start = int(queue.popleft())
    else:
        break
    left = nodes[start][0]
    right = nodes[start][1]
    if left == right == '-':
        leaves.append(str(start))
    if left != '-':
        queue.append(left)
    if right != '-':
        queue.append(right)

print ' '.join(leaves)
