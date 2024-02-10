try:
 filename=input("enter the file to open:")
 file=open("student.txt","r")
 content=file.read()
 print(content)
except NameError:
 print("validated!!!")