# demonstrate single inhertance
class Student():
 def student(self):
  print("A method from class Student")
class Teacher(student):
 def  teacher(self):
  print("B method from class Teacher")
b=Teacher()
b.Student()
b.Teacher()

