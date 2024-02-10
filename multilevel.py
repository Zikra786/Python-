class A:
	def sayhello(self):
		print("sayhello method from class A")
	def sayhii(self):
		print("sayhii method from class A")

class B(A):
	def welcome(Self):
		print("welcome methodfrom class B ")

class C(B):
	def hello(self):
		print("hello method from class C")


c=C()
c.hello()
c.welcome()
c.sayhii()
c.sayhello()


