try:
	x=int(input("enter first no: "))
	y=int(input("enter second no: "))
	z=x*y
	print("multiplication = ",z)

except ValueError:
	print("Multiply can be done with numbers only ...sorry")
finally:
	print("thank you :) bye bye")
