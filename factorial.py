num=int(input("enter a number: "))
fact=1
for i in range (0,num):
	fact=fact*(num-i)

print(fact)

num=int(input("enter a number: "))
fact=1
while num>0:
	fact=fact*num
	num=num-1

print(fact)

# i=0
# fact=1*(5-0)=5
# i=1
# fact=5*(5-1)=20
# i=2
# fact=20*(5-2)=60
# i=3
# fact=60*(5-3)=120
# i=4
# fact=120*(5-4)=120