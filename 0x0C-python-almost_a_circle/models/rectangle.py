#!/usr/bin/python3
""" Module for rectangle class """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__witdh

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__witdh = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.width * self.height

    def display(self):
        cont = 0
        cont2 = 0
        for i in range(0, self.height):
            while cont < self.y:
                print()
                cont += 1
            if i != 0:
                print()
            cont2 = 0
            for j in range(0, self.__witdh):
                while cont2 < self.x:
                    print(end=" ")
                    cont2 += 1
                print("#", end="")
        print()

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.x,
                                                self.y,
                                                self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for i, args in enumerate(args):
                if i == 0:
                    self.id = args
                if i == 1:
                    self.width = args
                if i == 2:
                    self.height = args
                if i == 3:
                    self.x = args
                if i == 4:
                    self.y = args
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return (
                {"id": self.id,
                 "width": self.width,
                 "height": self.height,
                 "x": self.x,
                 "y": self.y
                 }
               )
