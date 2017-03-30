from __future__ import print_function
import math
from collections import deque
num = int(raw_input())
seqs = sorted(map(int, raw_input().split(' ')))
# num = 1000
# seqs = [i for i in range(1000)]

def get_root(num, seqs, stack):
    while True:
        if stack:
            num, seqs = stack.popleft()
        if num == 1:
            if stack:
                print(seqs[0], end=' ')
            else:
                print (seqs[0], end='')
        else:
            complete_height = int(math.log(num, 2))
            last_line_count = num - (math.pow(2, complete_height)-1)
            if last_line_count == 0:
                height = complete_height
                left_last_line_count = math.pow(2, height - 2)
                right_last_line_count = math.pow(2, height - 2)
            else:
                height = complete_height + 1
                left_last_line_count = min(math.pow(2, height - 2), last_line_count)
                right_last_line_count = last_line_count - left_last_line_count
            left_tree_num = int(math.pow(2, height-2) - 1 + left_last_line_count)
            left_tree_seq = seqs[:left_tree_num]
            right_tree_num = int(math.pow(2, height-2) - 1 + right_last_line_count)
            right_tree_seq = seqs[left_tree_num+1:]
            print(seqs[left_tree_num], end=' ')
            if left_tree_num:
                stack.append(
                        [left_tree_num, left_tree_seq]
                )
            if right_tree_num:
                stack.append(
                        [right_tree_num, right_tree_seq]
                )
        if not stack:
            break
get_root(num, seqs, deque())
