str=input("enter a string: ")
# print(str)

newstr="".join(reversed(str))
# print(newstr)

if str==newstr:
	print("Plaindrome")
else:
	print("Not Palindrome")

