class student:
	def setvalue(self,rollno,name,fee):
		self.sturoll=rollno
		self.stuname=name
		self.stufee=fee
	def display(self):
		print("student roll no= ",self.sturoll)
		print("student name= ",self.stuname)
		print("student fee= ",self.stufee)
		
stu=student()
stu.setvalue(170280159,'Shefali Bajaj',25000)
stu.display()

