file=open("student.txt","w")
sroll=int(input("enter student roll no: "))
sname=input("enter student name:")
sadd=input("enter student address: ")

file.write("student roll no: "+str(sroll)+"\n"+"student name: "+sname+"\n"+"student address: "+sadd+"\n")
file.close()
print("student details saved !!!")