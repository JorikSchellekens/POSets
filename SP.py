# I'm going to use ordered tuples to represent the operations (po1, operation, po2)
# after this I will try to implement everything in dictionaries as an actual graph.

# Note since these are binary operators these 'meta graphs' are binary trees.
# For generating any SPn you just need to go through all binary trees of size n - 1
# And the generate the 2n permutations operation of those (Doesn't hold for non-cummutative
# and can create duplicates.)

# This is called generating topologies. We can implement it such that leaves represent
# the nodes of a hasse and the nodes the operators.
# This would literaly just be generating the binary trees.

# The number of partial orders of size n is

from functools import reduce

COMMUTATIVE = 'commutative'
SERIES = 's'
PARALLEL = 'p'
NODE = 'n'
OPERATORS = [[SERIES], [PARALLEL, COMMUTATIVE]]

# Dynamic programming memo
MEMO = {}

#pylint: disable = w0622, c0103
class frozenset(frozenset):
    '''Check normal frozenset. This just makes it look like any old set.
    Nothing to see here. Move along.'''
    def __repr__(self):
        return '{{{}}}'.format(', '.join(map(repr, self)))

def combine(SPn1_Collection, SPn2_Collection):
    operations = frozenset()
    for operator in OPERATORS:
        #Duplicate code her for time / memory reasons
        if COMMUTATIVE in operator:
            operations = operations.union(frozenset(frozenset([SPn1, operator[0], SPn2])
                                                          for SPn1 in SPn1_Collection
                                                          for SPn2 in SPn2_Collection))
        else:
            operations = operations.union(frozenset((SPn1, operator[0], SPn2)
                                                          for SPn1 in SPn1_Collection
                                                          for SPn2 in SPn2_Collection))
    return operations

def SPn(size):
    if size == 1:
        return set(NODE)
    elif not size in MEMO:
        combinations = map(lambda i: combine(SPn(i), SPn(size - i)), range(1, size))
        MEMO[size] = reduce(lambda x, y: x.union(y), combinations)
    return MEMO[size]

# Since I'm using the same base node value and the sets are not unique
# some look smaller because the second occurence of n in SPn(2) is not there.
# Think of {n, s} as {n, s, n}
print(*list(SPn(4)), sep='\n')