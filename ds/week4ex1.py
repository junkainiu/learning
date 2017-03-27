def make_tree(seq):
    tree = {}
    for item in seq:
        tree = _make_tree(item, tree)
    return tree


def _make_tree(item, tree):
    if not tree:
        tree[item] = {'left': {}, 'right': {}}
    else:
        last_key = tree.keys()[0]
        if item > last_key:
            _make_tree(item, tree[last_key]['right'])
        else:
            _make_tree(item, tree[last_key]['left'])
    return tree


def do(seqs):
    tree = make_tree(seqs[0])
    for seq in seqs[1:]:
        test_tree = make_tree(seq)
        if test_tree != tree:
            print 'No'
        else:
            print 'Yes'

while True:
    _input = raw_input()
    if _input != '0':
        seqs = []
        seq_len, seq_num = _input.split(' ')
        for i in range(int(seq_num) + 1):
            seq = raw_input()
            seqs.append(map(int, seq.split(' ')))
        do(seqs)
    else:
        break
