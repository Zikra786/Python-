class Shape:
	def __init__(self):
		self.shape="this is shape"
		print("This is shape ")

class Circle(Shape):
	def __init__(self):
		super().__init__()
		# Shape.__init__(self)
		self.circle="this is circular"
		print("This is circular shape")

class Rectangle(Shape):
	def __init__(self):
		super().__init__()
		# Shape.__init__(self)
		self.rectangle="this is rectangular shape"
		print("This id Rectangular shape")

class Square(Rectangle):
	def __init__(self):
		super().__init__()
		# Rectangle.__init__(self)
		self.square="square is rectangle"
		print("Square is a rectangle")
		


s=Square()
# print(s.square)
# print(s.rectangle)
# print(s.circle)
# print(s.shape)


