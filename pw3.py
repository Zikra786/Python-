file=open("anam.txt","w")
sname=input("Enter student name:")
sid=int(input("Enter the student id:"))
sfee=int(input("Enter the student fees:"))
file.write("student name:"+(sname)+"\n"+"student id:"+str(sid)+"\n"+"student fees:"+str(sfee)+"\n")
file.close()
print("Student details..!!")