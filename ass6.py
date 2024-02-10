basic=float(input("Enter your basic pay: "))
if basic>=1 and basic<=4000:
	hra=basic*0.10
	da=basic*0.50
elif basic>4000 and basic<=8000:
	hra=basic*0.20
	da=basic*0.60
elif basic>8000 and basic<=12000:
	hra=basic*0.25
	da=basic*0.70
else:
	hra=basic*0.30
	da=basic*0.80

salary=basic+hra+da
print(salary)