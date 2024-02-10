day=int(input("enter no of days: "))

year=int(day/365)
day=day-(365*year)
month=int(day/30)
week=int((day%365)/7)
days=(day%365)%7

print("years= ",year)
print("months= ",month)
print("weeks= ",week)
print("days= ",days)

# enter no of days: 390
# years=  1
# months=  0
# weeks=  3
# days=  4
