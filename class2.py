class calculator:
	def sum(self,x,y):
		return(x+y)
	def sub(self,x,y):
		print("subtraction is: ",x-y)
	def mul(self,x,y):
		return(x*y)
	def div(sef,x,y):
		return(x/y)

a=int(input())
b=int(input())
obj=calculator()
print("Sum = ",obj.sum(10,2))
obj.sub(10,2)
print("Multiplication = ",obj.mul(10,2))
print("Division = ",obj.div(10,2))