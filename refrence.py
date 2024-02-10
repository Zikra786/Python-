class employee:
	def setemp(self,empid,empname,empsalary):
		self.eid=empid
		self.ename=empname
		self.esalary=empsalary
	def viewemp(self):
		print("employee id= ",self.eid)
		print("employee name= ",self.ename)
		print("employee salary= ",self.esalary)
		
emp=employee()
emp.setemp(1,'shefali',70000)
emp.viewemp()

