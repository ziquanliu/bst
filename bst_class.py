class bst_node(object):
    def __init__(self,parent,k):
        self.key=k
        self.parent=parent
        self.left=None
        self.right=None

    def _str(self):
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.p is not None and \
           self is self.p.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width



    def __str__(self):
        return '\n'.join(self._str()[0])


    def insert(self,x):
        if x is None: return
        if x.key>self.key:
            if self.right is None:
                x.parent=self
                self.right=x
            else:
                self.right.insert(x)
        else:
            if self.left is None:
                x.parent=self
                self.left=x
            else:
                self.left.insert(x)

    def find(self,x):
        if x is None: return None
        if self is None or self.key is x.key:
            return self
        if x.key>self.key:
            if self.right is None: return None
            else:
                #print 'go right'
                return self.right.find(x)
        else:
            if self.left is None: return None
            else:
                #print 'go left'
                return self.left.find(x)

    def maximum(self):
        x=self
        while not (x.right is None):
            x=x.right
        return x

    def minimum(self):
        x=self
        while not (x.left is None):
            x=x.left
        return x

    def successor(self):
        if not self.right is None: return self.right.minimum()
        x=self
        y=self.parent
        #print x
        #print y
        while not (y is None) and (x is y.right):
            x=y
            y=y.parent
        return y

    def predecessor(self):
        if not self.left is None: return self.left.maximum()
        x=self
        y=self.parent
        while not (y is None) and (x is y.left):
            x=y
            y=y.parent
        return y



class bst(object):
    def __init__(self,bst_class=bst_node):
        self.root=None
        self.klass=bst_class

    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)

    def insert(self,x):
        node_x=self.klass(None,x)
        if self.root is None:
            self.root=node_x
        else:
            self.root.insert(node_x)

    def find(self,x):
        node_x=self.klass(None,x)
        if self.root is None:
            return  None
        if self.root.key is node_x.key:
            return self.root
        else:
            return self.root.find(node_x)

    def max_t(self):
        if self.root is None: return None
        else:
            return self.root.maximum()

    def min_t(self):
        if self.root is None: return None
        else:
            return self.root.minimum()


    def find_suc(self,x):
        node_in_t=self.find(x)
        if node_in_t is None: print 'No such node!'
        else:
            return self.find(x).successor()

    def find_pre(self,x):
        node_in_t=self.find(x)
        if node_in_t is None: print 'No such node!'
        else:
            return self.find(x).predecessor()

