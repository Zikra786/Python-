file=open("shefali.doc","a")
eid=int(input("enter employee id: "))
ename=input("enter employee name:")
esal=int(input("enter employee salary: "))

file.write("employee id: "+str(eid)+"\n"+"employee name: "+ename+"\n"+"employee salary: "+str(esal)+"\n")
file.close()
print("employee details saved !!!")