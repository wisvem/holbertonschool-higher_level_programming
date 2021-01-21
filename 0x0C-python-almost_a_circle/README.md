# 0x0C. Python - Almost a circle

### [0. If it's not tested it doesn't work](./tests/)
- All your files, classes and methods must be unit tested and be PEP 8 validated.
### [1. Base class](./models(base.py))
- Write the first class Base. Create a folder named models with an empty file [__init__.py](./models/__init__.py) inside - with this file, the folder will become a Python package
Create a file named models/base.py:
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
### [2. First Rectangle](./models/rectangle.py)
- Write the class Rectangle that inherits from Base.
In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
### [3. Validate attributes](./models/rectangle.py)
- Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
### [4. Area first](./models/rectangle.py)
- Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
### [5. Display #0 ](./models/rectangle.py)
- Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
### [6. __str__ ](./models/rectangle.py)
- Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
### [7. Display #1](./models/rectangle.py)
- Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
### [8. Update #0](./models/rectangle.py)
- Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.
### [9. Update #1](./models/rectangle.py)
- Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.
### [10. And now, the Square!](./models/sqaure.py)
- Write the class Square that inherits from Rectangle
### [11. Square size](./models/square.py)
- 
### [12. Square update](./models/square.py)
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:
-- args is the list of arguments - no-keyworded arguments
1st argument should be the id attribute
2nd argument should be the size attribute
3rd argument should be the x attribute
4th argument should be the y attribute
-- kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
-- kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance
### [13. Rectangle instance to dictionary representation](./models/square.py)
- Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
### [14. Square instance to dictionary representation](./models/square.py)
- Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square