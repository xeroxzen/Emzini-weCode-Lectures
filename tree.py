#! python

##########
# Trees
##########

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
        return True


def is_leaf(tree):
    return not branches(tree)


### +++ === ABSTRACTION BARRIER === +++ ###
def fib_tree(n):
    """Construct a fibonacci tree.
    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    """Count the leaves of a tree.
    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(branch) for branch in branches(tree)]
        return sum(branch_counts)


def leaves(tree):
    """Return a list containing the leaf labels of a tree.
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        leaf_counts = [leaves(branch) for branch in branches(tree)]
        return sum(leaf_counts)


def increment_leaves(tree):
    """Return a tree like t but with leaf labels incremented. """
    if is_leaf(tree):
        return tree(label(tree) + 1)
    else:
        bs = [increment_leaves(branch) for branch in branches(tree)]
        return tree(label(tree), bs)


def increment(tree):
    """Return a tree like t but with all labels incremented. """
    return tree(label(tree) + 1, [increment(branch) for branch in branches(tree)])


def tree_map(tree, f):
    """Return a tree like t but with all labels having  f applied to them. """
    return tree(f(label(tree)), [tree_map(branch, f) for branch in branches(tree)])
