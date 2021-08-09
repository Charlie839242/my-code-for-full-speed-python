# code:utf-8

# 1.
#     Use the Python documentation on classes at https://docs.python.org/3/tutorial/classes.
#     html to solve the following exercises.
#     1. Implement a class named “Rectangle” to store the coordinates of a rectangle given
#     by (x1, y1) and (x2, y2).
#     2. Implement the class constructor with the parameters (x1, y1, x2, y2) and store them
#     in the class instances using the “self” keyword.
#     3. Implement the “width()” and “height()” methods which return, respectively, the
#     width and height of a rectangle. Create two objects, instances of “Rectangle” to
#     test the calculations.
#     4. Implement the method “area” to return the area of the rectangle (width*height).
#     5. Implement the method “circumference” to return the perimeter of the rectangle
#     (2*width + 2*height).
#     6. Do a print of one of the objects created to test the class. Implement the “__str__”
#     method such that when you print one of the objects it print the coordinates as (x1,
#     y1)(x2, y2).
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def width(self):
        return abs(self.y2 - self.y1)
    def length(self):
        return abs(self.x2 - self.x1)
    def area(self):
        return self.width()*self.length()
    def circumference(self):
        return 2*self.width()+2*self.length()
    def __str__(self):
        return '(%d,%d) (%d,%d)'%(self.x1, self.y1, self.x2, self.y2)
rectangle = Rectangle(1,2,3,4)
print(rectangle.length())
print(rectangle)



# 2.
#     Use the “Rectangle” class as implemented above for the following exercises:
#         1. Create a “Square” class as subclass of “Rectangle”
#         2. Implement the “Square” constructor. The constructor should have only the x1, y1
#         coordinates and the size of the square. Notice which arguments you’ll have to use
#         when you invoke the “Rectangle” constructor when you use “super”.
#         3. Instantiate two objects of “Square”, invoke the area method and print the objects.
#         Make sure that all calculations are returning correct numbers and that the coordinates
#         of the squares are consistent with the size of the square used as argument.
class Square(Rectangle):
    def __init__(self, x1, y1, size):
        # 第一种继承方式
        Rectangle.__init__(self, x1, y1, x1 + size, y1 + size)      # 先继承父类
        self.size = size                                            # 再继承新的
        # 第二种继承方式
        # super().__init__(x1, y1, x1 + size, y1 + size)
square = Square(1,2,3)
print(square.area())
print(square)

