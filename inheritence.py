class A:
	def showA(self):
		print("this message from base class")
class B(A):
	def showB(self):
		print("This mesgae from derived class")

b=B()
# object with refrence variable
b.showA()
b.showB()

