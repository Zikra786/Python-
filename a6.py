string=input("enter the string:")
print("string")
rstring="".join(reversed(string))
print(rstring)
if string==rstring:
 print("string is palindrome:")
else:
 print("string is not a palindrome:")

