class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("data must be an integer")
        self.data = value

    @property
    def next_node(self):
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None or isinstance(value, Node) is False):
            raise TypeError("next_node must be a Node object")
        self.next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        Node = Node(value)
