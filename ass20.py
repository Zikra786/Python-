class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

class Square(Rectangle):
    def __init__(self,length,breadth):
        super().__init__(length,breadth)

    # def area(self):
    #     return self.length*self.length

    # def perimeter(self):
    #     return 2*(self.length+self.length)

    

s=Square(5,5)
print("area of square is: ",s.area())
print("Perimeter of square is: ",s.perimeter())

s=Square(3,5)
print("area of Rectangle is: ",s.area())
print("Perimeter of Rectangle is: ",s.perimeter())
