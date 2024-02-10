class interest:
	def simpleintrest(self,p,n,r):
		return (p*n*r)/100

x=float(input("enter principal value: "))
y=float(input("enter no of years: "))
z=float(input("enter rate of interest: "))

inte=interest()
print(inte.simpleintrest(x,y,z))