class Node:

    def __init__(self):
        print 'Create class node'

    def print_out(self):
        print type(self).__name__

# if __name__ == '__main__':
#     node = Node()
#     node.print_out()
#     print type(node).__name__



class Base(object):

    def __init__(self, node):
        self.node = node


class Child(Base):

    def __init__(self, node):
        super(Child, Base).__init__(node)


class Node(object):

    def __init__(self):
        self.name = 'node'


if __name__ == '__main__':
    node = Node()

