"Rakesh Kumar Bajaj = R.K Bajaj"
name=input("enter the full name: ")
shortname=name.split(" ")
# print(shortname)
print("your short name is:" ,end=" ")
for n in range(len(shortname)-1):
	# print("hello",n)
	print(shortname[n][0]+".",end="")
print(shortname[len(shortname)-1])