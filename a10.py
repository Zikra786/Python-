file=open("student.txt","w") 
sname=input("enter student name:")
srn=int(input("enter thestudent rollno.:"))
scnt=int(input("Enter the student contact:"))
sadr=input("Enter the student adress:")
file.write("Enter the student name:"+(sname)+"\n"+"enter the student rollno.:"+str(srn)+"\n"+"enter the student contact:"+str(scnt)+"\n"+"enter the student adress:"+(sadr)+"\n")
file.close()
print("record saved")