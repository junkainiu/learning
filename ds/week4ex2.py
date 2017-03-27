num = int(raw_input())
seqs = map(int, raw_input().split(' '))


def make_tree(seq):
    tree = {}
    for item in seq:
        tree = _make_tree(item, tree)
    print tree


def _make_tree(item, tree):
    if not tree:
        tree = {'left': {}, 'right': {}, 'balance': 0, "data": item}
    else:
        if item > tree["data"]:
            _make_tree(item, tree["right"])
        else:
            _make_tree(item, tree['left'])
    return tree

make_tree(seqs)
