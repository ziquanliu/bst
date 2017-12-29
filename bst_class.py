class bst_node(object):
    def __init__(self,parent,k):
        self.key=k
        self.p=parent
        self.left=None
        self.right=None
