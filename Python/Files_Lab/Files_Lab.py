import sys,os

#Write a function named countEndWrd that takes 2 arguments filename and word.
#Count how many times the given word appears at the end of a line, 
#Then append the following string to the passed file : 
#'The word => '+"'"+word+"'"+' appears => '+count+' times' .
'''
Write your function Here
'''
def countEndWrd(filename , word):
  counter =0
  with open (filename,'r') as f :
    lines=f.readlines()
  f.close()
  for i in lines:
      if i[-4:-1] ==word:
          counter+=1
  sentence="The word => "+"'"+word+"'"+" appears => "+str(counter)+" times"
  #print sentence
  ##append the sentence in the file
  a=open(filename,'a')
  a.write(str(sentence))
  a.close()
  return sentence
  

#Write a function named copyWrdToFile that takes 2 arguments source_file and word.
#It should copy all lines that contain the passed word from the file source_file 
#to a new file named 'new_file.txt'. 
'''
Write your function Here
'''
def copyWrdToFile(source_file ,word):
  file=open(source_file,'r')
  lines=file.readlines()
  file.close()
  ##append
  file_new=open('new_file.txt','a')

  for i in lines:
      if (i.find(word)) is not -1 :
          print i
          file_new.write(str(i))
  file_new.close()

  return 0
  
    
#Provided function to test your solution.  
def testAll():
  f=open('countEndWrd.txt','r')
  temp_list=f.readlines()
  if temp_list[len(temp_list)-1] == "The word => 'END' appears => 2 times":
    print 'countEndWrd=OK'
  else:
    print 'countEndWrd=NOK'
  f.close()
  
  if os.path.exists('new_file.txt'):
    f=open('new_file.txt','r')
    temp_list=f.readlines()
    f.close()
    if len(temp_list) == 3:
      if temp_list[0] =='A person can live without food for about a'\
      +' month, but only about a week without water.\n' and temp_list[1]\
      == 'Gopher snakes in Arizona are not poisonous, but when frightened'\
      +' they may hiss and shake their tails like rattlesnakes.\n' and temp_list[2]\
      == 'Cats sleep up to eighteen hours a day, but never'\
      +' quite as deep as humans. Instead, they fall asleep quickly and '\
      +'wake up intermittently to check to see if their environment is still safe.\n': 
        print 'copyWrdToFile=OK'
      else:
        print 'copyWrdToFile=NOK'
    else:
      print 'copyWrdToFile=NOK'
  else:
    print 'copyWrdToFile=NOK'
    

  
def main():
  if len(sys.argv) ==2:
      if (sys.argv[1])=='countEndWrd' :
        countEndWrd("countEndWrd.txt" ,'END')

      elif (sys.argv[1])=='copyWrdToFile' :
        copyWrdToFile('copyWrdToFile.txt','but')
      elif (sys.argv[1])=='testAll':
        testAll()
  else :
    print 'usage: Files_Lab.py {--countEndWrd | --copyWrdToFile} Filename'
    print '       Use Files_Lab.py --testAll N/A to test your solution' 
    sys.exit(1)
  '''
  Inside the main function, check on the passed option and call the proper function.
  If the passed option is unknown print: 'unknown option: ' + option 
  and then exit with failure.
  
  
  In case option is countEndWrd search for the word 'END'.
  In case option is copyWrdToFile search for the word 'but'.
  In case option is testAll then call function testAll.
  '''



if __name__ == '__main__':
  main()  