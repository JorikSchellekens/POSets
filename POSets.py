class POSET(object):
    def __init__(self):
        self.RELATIONS = {}
        discrete_node = node()
        self.RELATIONS[discrete_node] = discrete_node


class node(object):
    """This is an empty noncomparable empty object representing the items in a poset.
    I've left it empty so that it can be modified for later implementations."""
    pass
