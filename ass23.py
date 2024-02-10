try:
	x=int(input("enter first no: "))
	y=int(input("enter second no: "))
	z=x/y
	print("division = ",z)

except ZeroDivisionError:
	print("we cant divide with zero")
finally:
	print("Thank you :) bye bye")
