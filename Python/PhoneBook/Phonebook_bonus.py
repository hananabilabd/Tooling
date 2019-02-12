mydict={}
def phonebook(option ,*args):
	if ( option == 'a'):
		mydict[args[0]]={'number':args[1],'mail':args[2],'work':args[3]}
	elif (option == 'd') :#display
		for k in mydict:
			print k ,'::=>',"Number:",mydict[k]['number'],",","Mail:",mydict[k]['mail'],",","Work:",mydict[k]['work']
	elif (option =='c'):#clear all
		mydict.clear()
	elif (option =='r'):#remove an item
		if [args[0] in mydict ]:
			mydict.__delitem__(args[0])
			print args[0],'Removed Successfully'
		else :
			print ("Not Found to delete")
	elif (option =='s'): #search for an item
		if [args[0] in mydict ]:
			print (mydict[args[0]])
		else :
			print ("Not Found")
def loop():
	while True:
		print 'Enter a to add new Entry'
		print 'Enter d to display Entries'
		print 'Enter c to clear all Entries'
		print 'Enter r to remove an Item'
		print 'Enter x to remove an Item'
		x = raw_input('Enter a value:')
		if (x=='a'):
			name = raw_input("What is your name? ")
			phone = raw_input("What is your phone? ")
			mail = raw_input("What is your mail? ")
			work = raw_input("What is your work? ")
			phonebook('a',name,phone,mail,work)
			print 'Dictionary after update'
			phonebook('d')
			print '----------------------------------------------------------------'
		elif (x=='d'):
			phonebook('d')
		elif(x=='c'):
			phonebook('c')
			print 'Dictionary after update'
			phonebook('d')
			print '----------------------------------------------------------------'
		elif(x=='r'):
			nameDelete = raw_input("What is name you wanna delete? ")
			phonebook('r',nameDelete)
			print 'Dictionary after update'
			phonebook('d')
			print '----------------------------------------------------------------'
		elif (x == 'x'):
			break
		else:
			break

if __name__ == '__main__':
	loop()
	#phonebook('a','omar','01112111807','hana','valeo')
	#phonebook('a', 'hannon', '01112111807', 'hananabil@gmail.com', 'valeo')
	#phonebook('d')
	#print(mydict['omar'])
	#phonebook('r','omar')
	#print(mydict)
