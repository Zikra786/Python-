try:
	x=int(input("enter first no: "))
	y=int(input("enter second no: "))
	z=x/y
	print("result = ",z)

except ValueError:
	print("enter numbers only")
except ZeroDivisionError:
	print("we cant divide with zero")
finally:
	print("bye bye")
