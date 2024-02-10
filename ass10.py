def fact(num):
	if num==0 or num==1:
		return 1
	else:
		return num*fact(num-1)

x=int(input("enter a number : "))
factorial=fact(x)

print("factorial of: ",x," is ",factorial)
