from collections import deque
num = int(raw_input())
seqs = map(int, raw_input().split(' '))


def make_tree(seq):
    tree = {}
    for item in seq:
        tree, revert = _make_tree(item, tree, deque(), {})
        if revert:
            tree = tree_transform(tree, revert)
            tree = recalc_balance(tree)
    print tree['data']


def recalc_balance(tree):
    seq = gen_seq_from_tree(tree, [])
    tree = {}
    for item in seq:
        tree, _ = _make_tree(item, tree, deque(), {}, calc_revert=False)
    return tree


def gen_seq_from_tree(tree, stack):
    stack.append(tree['data'])
    if tree['left']:
        gen_seq_from_tree(tree['left'], stack)
    if tree['right']:
        gen_seq_from_tree(tree['right'], stack)
    return stack


def find_tree(item, tree):
    if item == tree['data']:
        return tree
    else:
        if tree['left']:
            value = find_tree(item, tree['left'])
            if value:
                return value
        if tree['right']:
            value = find_tree(item, tree['right'])
            if value:
                return value


def _transform(sub_tree, mode, stack):
    if mode.startswith('leftleft'):
        data = sub_tree.pop('data')
        right = sub_tree.pop('right')
        left = sub_tree['left'].pop('right', {})
        sub_tree['left']['right'] = {}
        sub_tree['data'] = sub_tree['left']['data']
        sub_tree['left'] = sub_tree['left']['left']
        sub_tree['right'] = {'left': left, 'right': right, 'data': data, 'balance': 0}
    elif mode.startswith('rightright'):
        data = sub_tree.pop('data')
        left = sub_tree.pop('left')
        right = sub_tree['right'].pop('left', {})
        sub_tree['right']['left'] = {}
        sub_tree['data'] = sub_tree['right']['data']
        sub_tree['right'] = sub_tree['right']['right']
        sub_tree['left'] = {'left': left, 'right': right, 'data': data, 'balance': 0}
    elif mode.startswith('leftright'):
        data = sub_tree.pop('data')
        left = sub_tree.pop('left')
        right = sub_tree.pop('right')
        left_right = left.pop('right')
        left['right'] = {}
        sub_tree['data'] = left_right['data']
        if left_right['left']:
            left['right'] = left_right['left']
        elif left_right['right']:
            left['right'] = left_right['right']
        sub_tree['right'] = {"data": data, 'left': {}, 'right': right, 'balance': 0}
        sub_tree['left'] = left
    elif mode.startswith('rightleft'):
        data = sub_tree.pop('data')
        left = sub_tree.pop('left')
        right = sub_tree.pop('right')
        right_left = right.pop('left')
        right['left'] = {}
        sub_tree['data'] = right_left['data']
        if right_left['left']:
            right['left'] = right_left['left']
        elif right_left['right']:
            right['left'] = right_left['right']
        sub_tree['left'] = {"data": data, 'right': {}, 'left': left, 'balance': 0}
        sub_tree['right'] = right
    return sub_tree


def tree_transform(tree, revert):
    mode = revert['mode']
    stack = revert['nodes']
    sub_tree = find_tree(stack[0], tree)
    sub_tree = _transform(sub_tree, mode, stack)
    return tree


def _make_tree(item, tree, stack, revert, calc_revert=True):
    if not tree:
        tree = {'left': {}, 'right': {}, 'balance': 0, "data": item}
    else:
        if item > tree["data"]:
            stack.appendleft(tree)
            if tree['right']:
                _make_tree(item, tree['right'], stack, revert, calc_revert)
            else:
                for i, v in enumerate(stack):
                    if i == 0:
                        old = abs(v['balance'])
                        v['balance'] += 1
                        if abs(v['balance']) < old:
                            taller = False
                        else:
                            taller = True
                    else:
                        if taller is False:
                            continue
                        else:
                            old = abs(v['balance'])
                            if v['left'] == stack[i-1]:
                                v['balance'] -= 1
                            else:
                                v['balance'] += 1
                            if abs(v['balance']) < old:
                                taller = False
                            else:
                                taller = True
                if calc_revert:
                    r_stack = deque(reversed(stack))
                    for i, v in enumerate(r_stack):
                        if abs(v['balance']) == 2:
                            if v['left'] == r_stack[i+1]:
                                revert['nodes'] = [r_stack[i]['data']]
                                revert['mode'] = 'left'
                            elif v['right'] == r_stack[i+1]:
                                revert['nodes'] = [r_stack[i]['data']]
                                revert['mode'] = 'right'
                        elif revert:
                            if i < len(stack) - 1:
                                if v['left'] == r_stack[i+1]:
                                    revert['nodes'].append(r_stack[i]['data'])
                                    revert['mode'] += 'left'
                                elif v['right'] == r_stack[i+1]:
                                    revert['nodes'].append(r_stack[i]['data'])
                                    revert['mode'] += 'right'
                                else:
                                    revert['mode'] += 'right'
                            else:
                                revert['mode'] += 'right'
                tree['right'] = {'left': {}, 'right': {}, 'balance': 0, "data": item}
        else:
            stack.appendleft(tree)
            if tree['left']:
                _make_tree(item, tree['left'], stack, revert, calc_revert)
            else:
                for i, v in enumerate(stack):
                    if i == 0:
                        old = abs(v['balance'])
                        v['balance'] -= 1
                        if abs(v['balance']) < old:
                            taller = False
                        else:
                            taller = True
                    else:
                        if taller is False:
                            continue
                        else:
                            old = abs(v['balance'])
                            if v['left'] == stack[i-1]:
                                v['balance'] -= 1
                            else:
                                v['balance'] += 1
                            if abs(v['balance']) < old:
                                taller = False
                            else:
                                taller = True
                if calc_revert:
                    r_stack = deque(reversed(stack))
                    for i, v in enumerate(r_stack):
                        if abs(v['balance']) == 2:
                            if v['left'] == r_stack[i+1]:
                                revert['nodes'] = [r_stack[i]['data']]
                                revert['mode'] = 'left'
                            elif v['right'] == r_stack[i+1]:
                                revert['nodes'] = [r_stack[i]['data']]
                                revert['mode'] = 'right'
                        elif revert:
                            if i < len(r_stack) - 1:
                                if v['left'] == r_stack[i+1]:
                                    revert['nodes'].append(r_stack[i]['data'])
                                    revert['mode'] += 'left'
                                elif v['right'] == r_stack[i+1]:
                                    revert['nodes'].append(r_stack[i]['data'])
                                    revert['mode'] += 'right'
                                else:
                                    revert['mode'] += 'left'
                            else:
                                revert['mode'] += 'left'
                tree['left'] = {'left': {}, 'right': {}, 'balance': 0, "data": item}
    return tree, revert

make_tree(seqs)
