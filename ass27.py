def find(sentance,fw):
	sent=sentance.split(" ")
	# print(sent)
	for i in sent:
		if i==fw:
			return True
	return False

sent=input("enter a sentance: ")
fw=input("find what: ")
if (find(sent, fw)): 
    print("Yes! it is present") 
else: 
    print("No! its not") 

