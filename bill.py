unit=int(input("enter units: "))
if unit>=0 and unit<=150:
	bill=unit*2.4
elif unit>150 and unit<=300:
	bill=150*2.40+(unit-150)*3.00
else:
	bill=150*2.40+150*3.00+(unit-300)*3.20

print("total payable amount is: ",bill)

arifrizvi07@gmail.com