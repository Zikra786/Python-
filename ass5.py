x=int(input("enter the x cordinate: "))
y=int(input("enter the y cordinate: "))

if x>=0 and y>=0:
	print("Ist quadrant")
elif x>0 and y<0:
	print("IVth quadrant")
elif x<0 and y>0:
	print("IInd quadrant")
else:
	print("IIIrd quadrant")