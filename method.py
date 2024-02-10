class A:
	def m1(self):
		print("m1 method is from class A")
	def m2(self):
		print("m2 method is from class A")

class B(A):
	def m3(self):
		print("m3 method is from class B")
	def m1(self):
		print("m1 method is from class B")

b=B()
b.m3()
b.m2()
b.m1()
A().m1()