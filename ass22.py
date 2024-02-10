class Bank:
	def Interest(self):
		return 0

class pnb(Bank):
	def Interest(self):
		return 2.5


class sbi(Bank):
	def Interest(self):
		return 3.4


a=Bank()
print(a.Interest())
b=pnb()
print(b.Interest())
c=sbi()
print(c.Interest())

