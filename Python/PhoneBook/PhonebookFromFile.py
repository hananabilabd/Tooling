mydict={}

def phonebook(option ,*args):
	if ( option == 'a'):
		if not (open('phonebook.txt','r').read(1)) :#file is empty
			dictFile = {}
		else :
			dictFile = eval(open('phonebook.txt', 'r').read())
		mydict[args[0]]={'number':args[1],'mail':args[2],'work':args[3]}
		mydict.update(dictFile)
		file = open('phonebook.txt', 'w')
		file.write(str(mydict))
		file.close()
	elif (option == 'd') :#display
		dictFile = eval(open('phonebook.txt', 'r').read())
		if not dictFile :
			print ("PhoneBook is Empty")
		else :
			for k in dictFile:
				print k ,'::=>',"Number:",dictFile[k]['number'],",","Mail:",dictFile[k]['mail'],",","Work:",dictFile[k]['work']
	elif (option =='c'):#clear all
		mydict.clear()
		file = open('phonebook.txt', 'w')
		file.write(str(mydict))
		file.close()
	elif (option =='r'):#remove an item
		if not (open('phonebook.txt','r').read(1)) :#file is empty
			dictFile = {}
		else :
			dictFile = eval(open('phonebook.txt', 'r').read())
		mydict.update(dictFile) ##concatenate the 2 dictionary
		if [args[0] in mydict ]:
			mydict.__delitem__(args[0])
			file = open('phonebook.txt', 'w')
			file.write(str(mydict))
			file.close()
			print args[0],'Removed Successfully'
		else :
			print ("Not Found to delete")
	elif (option =='s'): #search for an item
		dictFile = eval(open('phonebook.txt', 'r').read())
		if not dictFile: ##return false if dictionary is empty
			print ("PhoneBook is Empty")
		else:
			if [args[0] in dictFile ]:
				print (dictFile[args[0]])
			else :
				print ("Not Found")
def loop():
	while True:
		print '-----------------------------------------------------------------------------------'
		print 'Enter a to add new Entry'
		print 'Enter d to display Entries'
		print 'Enter c to clear all Entries'
		print 'Enter r to remove an Item'
		print 'Enter s to search for an Item'
		print 'Enter x to Exit'
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
		elif (x=='s'):
			nameSearch = raw_input("What is name you wanna search for? ")
			phonebook('s',nameSearch)
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
