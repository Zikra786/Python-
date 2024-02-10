try:
	filename=input("enter file name: (with extension)")
	file=open(filename,"r")
	content=file.read()
	print(content)
	file.close()
	print("data successfully recieved from file")

except FileNotFoundError:
	print("type correct name of file pls")