string=input("enter a string: ")
print(string)

rstring="".join(reversed(string))
print(rstring)

if string==rstring:
	print("Plaindrome")
else:
	print("Not Palindrome")

