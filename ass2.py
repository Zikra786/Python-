class bank:
 def interest(self):
  print("bank interest is 0")
class sbi(bank):
 def interest(self):
  print("value of interest is as per norm of bank")
class pnb(bank):
 def interest(self):
  print("value of interest is as per norm of bank")
c=bank()
c.sbi()
c.pnb()

