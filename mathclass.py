class mymath:
	def greatest(self,a,b):
		if a>b:
			print("greatest number = ",a)
		else:
			print("greatest number = ",b)

	def evenodd(self,n):
		if n%2==0:
			print("even no = ",n)
		else:
			print("odd no = ",n)

mymath().greatest(15,5)
mymath().evenodd(8)
