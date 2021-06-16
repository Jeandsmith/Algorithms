

from abc import abstractproperty
from typing import List


class Node:

    def __init__(self, val: int = None, left=None, right=None) -> None:
        self.__value = val
        self.right = right
        self.left = left

    @property
    def value(self):
        return self.__value

    @value.getter
    def value(self):
        return self.__value

    @value.setter
    def value(self, valuePassed):
        self._value = valuePassed

# Types of tree
class BinarySearchTree:

    def __init__(self) -> None:
        self.__root = None

    def insert(self, value: int = None) -> None:
        if value is None:
            return None

        self.__root = self.__insert_in_place(value, self.__root)

    def __insert_in_place(self, val, node: Node):
        if node is None:
            return Node(val)
        
        if val < node.value:
            node.left = self.__insert_in_place(val, node.left)
        elif val >= node.value:
            node.right = self.__insert_in_place(val, node.right)

        #  Return the root node
        return node 

    def print_nodes(self, node: Node):
        if node is None:
            return

        # In order
        self.print_nodes(node.left)
        print (node.value)
        self.print_nodes(node.right)

        # Post order
        # self.print_nodes(node.left)
        # self.print_nodes(node.right)
        # print (node.value)

        # Pre order
        # print(node.value)
        # self.print_nodes(node.left)
        # self.print_nodes(node.right)


    def print_all(self):
        self.print_nodes(self.__root)

    def max_value(self):
        return self.__get_max_value(self.__root, 0)

    def __get_max_value(self, node: Node, current_max: int) -> int:

        if node is None:
            return current_max

        if current_max < node.value:
            current_max = node.value
        
        return self.__get_max_value(node.right, current_max)

class HeapBinaryTree:
    