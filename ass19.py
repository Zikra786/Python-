class A:
	def base(self):
		print("this message from base class")
class B(A):
	def derived(self):
		print("This mesgae from derived class")

obj=B()
obj.base()
obj.derived()

