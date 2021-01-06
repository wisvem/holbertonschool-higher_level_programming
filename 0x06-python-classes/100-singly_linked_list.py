#!/usr/bin/python3
'''Linked list module'''


class Node:
    '''class to create Nodes'''

    def __init__(self, data, next_node=None):
        """[summary]

        Args:
            data ([type]): [description]
            next_node ([type], optional): [description]. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__data

    @property
    def next_node(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class to create single linked list"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        pass

    def sorted_insert(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        curr = self.__head
        newNode = Node(value)
        if not self.__head:
            self.__head = newNode
            return
        if curr.data >= value:
            newNode.next_node = curr
            self.__head = newNode
            return
        while curr.next_node is not None:
            if curr.next_node.data >= value:
                break
            curr = curr.next_node
        newNode.next_node = curr.next_node
        curr.next_node = newNode
        return

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        list = ""
        if self.__head is None:
            return list
        curr = self.__head
        while curr.next_node is not None:
            list += f'{curr.data}'
            list += "\n"
            curr = curr.next_node
        list += f'{curr.data}'
        return list
