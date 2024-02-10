import tempconvmodule


ch=input("enter your choice celcius or fahrenhit(C or F): ")
if ch=='C':
	t=float(input("enter the temprature in celcius"))
	print(tempconvmodule.ctof(t))
else:
	t=float(input("enter the temprature in fahrenhit"))
	print(tempconvmodule.ftoc(t))