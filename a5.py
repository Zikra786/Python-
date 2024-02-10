num=int(input("enter the numer:"))
sum = 0
while num>0:
  rem=num%10
  sum=sum+rem
  num=int(num/10)
print("sum of digits=",sum)