#!/usr/bin/python3
'''Square module'''


class Square:
    '''A class to create squares'''

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """[property to get size]

        Returns:
            [int]: [square size]
        """
        return self.__size

    def area(self):
        """[Calculate area]

        Returns:
            [int]: [square area]
        """
        return self.__size*self.__size

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value (int): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print a graphical representation
        """
        if self.__size != 0:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__size + self.position[0]):
                    if j >= self.position[0]:
                        print("#", end="")
                    else:
                        print(" ", end="")
                print()
        else:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or value:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value
