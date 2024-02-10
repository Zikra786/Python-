try:
 a=int(input("enter  the  first number:"))
 b=int(input("enter the second number:"))
 z=a/b
 print("the sum is=",z)
except ZeroDivisionError:
     print("invalid")