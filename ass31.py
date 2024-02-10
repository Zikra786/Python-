try:
	filen="student.txt"
	file=open(filen,"r")
	con=file.read()
	print(con)
	file.close()
	print("data successfully recieved from file")

except FileNotFoundError:
	print("type correct name of file pls")