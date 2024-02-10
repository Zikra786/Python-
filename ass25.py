try:
	x=int(input("enter first no: "))
	y=int(input("enter second no: "))
	z=x*y
	print("multiplication = ",z)
	print("If 'a' found then value of will be printed ")
	print("but if not then except part will print")
	print("variable = ",a)

except NameError:
	print("sorry not found: variable 'a' is not found in local or global scope")
finally:
	print("thank you :) bye bye")
