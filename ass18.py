class rectangle:
	def __init__(self,leng,wid):
		self.leng=leng
		self.wid=wid

	def recarea(self):
		return self.leng*self.wid
	def recperi(self):
		return 2*(self.leng+self.wid)

l=float(input("enter the length: "))
b=float(input("enter the width: "))
rec=rectangle(l,b)
print("area = ",rec.recarea())
print("perimeter = ",rec.recperi())
