
import sys
MAXINT = sys.maxint


def has_prefix(values):
    for index, value in enumerate(values):
        if index < len(values) - 1:
            for item in values[index+1:]:
                if item.startswith(value):
                    return True
    return False


def make_input(input_list):
    res = {}
    nodes = input_list.split(' ')
    for i, item in enumerate(nodes):
        if i % 2 == 0:
            res[item] = int(nodes[i+1])
    return res


def calc(input_list):
    haffman_tree = HaffmanTRee(input_list)
    return haffman_tree.weight


class HaffmanTRee(object):

    def __init__(self, nodes):
        self.tree = self.make_tree(nodes)

    def delete(self, heap):
        node = heap.pop(1)
        if len(heap) > 2:
            heap_1 = heap[1]
            heap_2 = heap[2]
            if heap_2['weight'] < heap_1['weight']:
                heap[1], heap[2] = heap[2], heap[1]
        return node

    def make_tree(self, nodes):
        weights = [{'left': {}, 'right': {}, 'weight': item} for item in nodes]
        heap = [{'weight': MAXINT}]
        self.make_heap(weights, heap)
        while len(heap) > 1:
            node = {}
            node_left = self.delete(heap)
            node_right = self.delete(heap)
            weight = node_left['weight'] + node_right['weight']
            node['left'] = node_left
            node['right'] = node_right
            node['weight'] = weight
            if len(heap) > 1:
                self._insert(node, heap)
        return node

    def make_heap(self, seqs, heap):
        for item in seqs:
            self._insert(item, heap)

    def _insert(self, item, heap):
        heap.append(item)
        heap_index = len(heap) - 1
        while heap_index:
            old_heap = heap_index
            if heap[heap_index/2]['weight'] > item['weight']:
                heap_index = heap_index/2
                if heap_index != 0:
                    heap[heap_index], heap[old_heap] = heap[old_heap], heap[heap_index]
            else:
                break

    @property
    def weight(self):
        tree = self.tree
        res = []
        res = self.get_all_leaves(tree, res)
        return sum(res)

    def get_all_leaves(self, tree, res, length=0):
        if not tree['left'] and not tree['right']:
            res.append(tree['weight'] * length)
        else:
            self.get_all_leaves(tree['left'], res, length+1)
            self.get_all_leaves(tree['right'], res, length+1)
        return res

num = int(raw_input())

input_list = make_input(raw_input())
# input_list = make_input(fake_input())

weight = calc(input_list.values())
students = int(raw_input())

for student in range(students):
    answer = 0
    paths = []
    for i in range(num):
        key, path = raw_input().split(' ')
        answer += input_list[key]*len(path)
        paths.insert(0, path)
    if answer == weight:
        if has_prefix(paths):
            print 'No'
        else:
            print 'Yes'
    else:
        print 'No'
