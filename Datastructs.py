

from config import DATAMAXRANGE
from Algorithms import selectionsort
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
        print(node.value)
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


class Heap:
    def __init__(self) -> None:
        self.data = list()

    def root_node(self):
        return self.data[0]

    def __last_node(self):
        return self.data[-1]

    def __left_child(self, index: int) -> int:
        return (index * 2) + 1

    def __right_child(self, index: int) -> int:
        return (index * 2) + 2

    def __parent_node(self, index: int) -> int:
        return (index - 1) // 2

    def get_heap(self):
        return self.data

    def delete(self) -> int:
        """ Delete the root node and init the trickle down of the last node """
        # TODO: Delete the root node
        return root  

    def insert(self, val:int):
        self.data.append(val)

        #  Keeping track of the new node index
        new_index = len(self.data) - 1

        # Move the new node up the tree
        while new_index > 0 and self.data[self.__parent_node(new_index)] < self.data[new_index]:
            tmp = self.data[self.__parent_node(new_index)]
            self.data[self.__parent_node(new_index)] = self.data[new_index]
            self.data[new_index] = tmp
            new_index = self.__parent_node(new_index)
