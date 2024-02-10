n=int(input("enter how many no of values you want to enter: "))
list=[]
for i in range(0,n):
	li=eval(input())
	list.insert(i,li)
print("display all elemnts: ",list)
for li in list:
	print(li)