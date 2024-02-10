num=int(input("enter a number"))
temp=num
sum=0
while num>0:
	rem=num%10
	sum=sum+(rem*rem*rem)
	num=int(num/10)

if temp==sum:
	print("no. is armstrong")
else:
	print("no is not armstrong")

