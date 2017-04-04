import sys
from itertools import imap
MAXINT = sys.maxint
num, count = map(int, raw_input().split(' '))
seqs = imap(int, raw_input().split(' '))
heap = [MAXINT]

def make_heap(seqs, heap):
    for item in seqs:
        heap.append(item)
        heap_index = len(heap) - 1
        while heap_index:
            old_heap = heap_index
            if heap[heap_index/2] > item:
                heap_index = heap_index/2
                if heap_index != 0:
                    heap[heap_index], heap[old_heap] = heap[old_heap], heap[heap_index]
            else:
                break

make_heap(seqs, heap)

stack = map(int, raw_input().split(' '))
for i in stack:
    res = []
    while i:
        res.append(str(heap[i]))
        i = i/2
    print ' '.join(res)
