#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# The following lab has modifications over the original google's lab
 
import sys
import re
from fileinput import filename

from scipy.io.matlab.mio5_params import mat_struct

"""Baby Names exercise

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h1>Popular Names by Birth Year</h1>September 12, 2007</td>
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
"""

def extractFemaleNames(filename,letter):
  """
  Given a html file name, extract all female names that start with
  the passed letter and return a list with the 'extracted names and their rank'
  in alphabetical order.    
  for e.x. ['Amina 70','Anita 100','Aya 61',...]
  """
  pattern=r'<tr align=\"right\"><td>(\d*)</td><td>(\w*)</td><td>(' +str(letter)+ r'\w*)</td>'
  html_file = open(filename, 'r')
  matches=re.findall(pattern,html_file.read())
  extracted_list=[]
  for tuple in matches:
      extracted=str(tuple[2])+str(' ') + str (tuple[0])
      extracted_list.append(extracted)
  html_file.close()


  # +++your code here+++
  return sorted(extracted_list)
  
    
def extractMaleNames(filename,letter):
  """
  Given a html file name, extract all male names that start with
  the passed letter and return a list with the 'extracted names and their rank'
  in reverse alphabetical order.    
  for e.x. ['Muhamed 91', Morgan 57', 'Mahdy 895', ...]
  """
  pattern = r'<tr align=\"right\"><td>(\d*)</td><td>('+ str(letter)+r'\w*)</td><td>(\w*)</td>'
  html_file = open(filename, 'r')
  matches = re.findall(pattern, html_file.read())
  extracted_list = []
  for tuple in matches:
      extracted = str(tuple[1]) + str(' ') + str(tuple[0])
      extracted_list.append(extracted)
  html_file.close()

  return sorted(extracted_list,reverse=True)

def extractDocAndPopularityDate(filename):
  """
  Given a html file name, extract the document date and Popularity date and return them.
  e.x if the following headers are:
  <h1>Popular Names by Birth Year</h1>September 12, 2007</td>
  <h3 align="center">Popularity in 1990</h3>
  then the extracted string should be is "September 12, 2007 and Popularity in 1990"   
  """
  # +++your code here+++

  pattern_popularNames=r'<h1>Popular Names by Birth Year</h1>(\w*\s.*)</td>'
  pattern_popularity=r'<h3 align=\"center\">(\w*\s.*)</h3>'
  html_file = open(filename, 'r')
  content=html_file.read()
  matches_popularNames = re.findall(pattern_popularNames,content )
  matches_popularity = re.findall(pattern_popularity, content)
  html_file.close()

  extractedString=str(matches_popularNames[0]) + ' and ' + str (matches_popularity[0])
  #print (extractedString)
  return extractedString
   
#Provided function to test your solution.  
def testAll():
  print 'Testing baby1990.html'
  if extractFemaleNames('baby1990.html','A') == ['Abbey 482', 
  'Abbie 685', 'Abby 222', 'Abigail 90', 'Adrian 603', 'Adriana 144',
  'Adrianna 325', 'Adrianne 783', 'Adrienne 233', 'Aileen 851', 
  'Aimee 272', 'Aisha 568', 'Aja 940', 'Alaina 441', 'Alana 368',
  'Alanna 474', 'Alannah 936', 'Alecia 678', 'Alejandra 211', 
  'Alesha 695', 'Alessandra 829', 'Alex 802', 'Alexa 146', 
  'Alexander 873', 'Alexandra 37', 'Alexandrea 653', 'Alexandria 95', 
  'Alexia 557', 'Alexis 66', 'Ali 687', 'Alice 347', 'Alicia 53', 'Alina 664',
  'Alisa 460', 'Alisha 135', 'Alison 133', 'Alissa 276', 'Allie 579', 
  'Allison 48', 'Allyson 236', 'Allyssa 709', 'Alma 386', 'Alycia 524', 
  'Alysa 900', 'Alyse 816', 'Alysha 410', 'Alysia 643', 'Alyson 358', 
  'Alyssa 27', 'Amanda 4', 'Amber 15', 'Amelia 194', 'Amie 698', 'Amy 38',
  'Ana 124', 'Anabel 746', 'Anastasia 382', 'Andrea 40', 'Andria 870', 
  'Angel 174', 'Angela 52', 'Angelia 501', 'Angelica 119', 'Angelina 261', 
  'Angelique 631', 'Angie 586', 'Anita 405', 'Anjelica 923', 'Ann 251',
  'Anna 45', 'Anne 155', 'Annemarie 996', 'Annette 513', 'Annie 334', 
  'Annmarie 973', 'Antoinette 354', 'Antonia 661', 'April 73', 'Araceli 556',
  'Ariana 227', 'Arianna 411', 'Ariel 94', 'Arielle 186', 'Arlene 682', 
  'Asha 997', 'Ashely 632','Ashlee 154', 'Ashleigh 178', 'Ashley 2', 
  'Ashli 722', 'Ashlie 476', 'Ashly 535', 'Ashlyn 559', 'Ashton 331', 
  'Asia 299', 'Athena 731', 'Aubrey 298', 'Audra 673', 'Audrey 161', 
  'Aurora 716', 'Autumn 177', 'Ava 953', 'Avery 797', 'Ayla 818']:
    print '\t extractFemaleNames => OK'
  else:
    print '\t extractFemaleNames => NOK'
  if extractMaleNames('baby1990.html','M') == ['Myron 679',
  'Myles 428', 'Mykel 869', 'Mychal 825', 'Moshe 702', 'Moses 588',
  'Morris 761', 'Morgan 277', 'Monte 901', 'Moises 467', 'Mohammed 678',
  'Mohammad 604', 'Mohamed 740', 'Mitchell 93', 'Mitchel 572', 
  'Misael 999', 'Milton 566', 'Miles 269', 'Mikhail 967', 'Mikel 757',
  'Mike 507', 'Miguel 101', 'Mickey 836','Michel 894', 'Micheal 175', 
  'Michael 1', 'Micah 238', 'Melvin 278', 'Maxwell 188', 'Maximilian 684',
  'Max 172', 'Mauricio 547', 'Maurice 205', 'Matthew 3', 'Mathew 148', 
  'Mason 208', 'Marvin 237', 'Marty 781', 'Martin 113', 'Martez 785',
  'Martell 975', 'Marshall 280', 'Marquise 555', 'Marquis 258', 'Marquez 874',
  'Marques 813', 'Marlon 458', 'Marlin 966', 'Markus 501', 'Mark 46', 
  'Marion 883', 'Mario 119', 'Marcus 72', 'Marcos 273', 'Marco 226', 
  'Marcelo 974', 'Marcel 560','Marc 163', 'Manuel 134', 'Malik 557', 
  'Male 701', 'Malcom 873', 'Malcolm 241','Malachi 959', 'Madison 847', 
  'Mackenzie 524']:
    print '\t extractMaleNames => OK'
  else:
    print '\t extractMaleNames => NOK'
  if extractDocAndPopularityDate('baby1990.html') == \
  'September 12, 2007 and Popularity in 1990':
    print '\t extractDocAndPopularityDate => OK'
  else:
    print '\t extractDocAndPopularityDate => NOK'
  
  print    
  print 'Testing baby2006.html'
  if extractFemaleNames('baby2006.html','K') == ['Kadence 391',
  'Kaelyn 367', 'Kaia 694', 'Kaila 772', 'Kailee 583', 'Kailey 257', 
  'Kailyn 492', 'Kaitlin 344', 'Kaitlyn 41', 'Kaitlynn 525', 'Kaiya 851', 
  'Kaleigh 488', 'Kaley 670', 'Kali 542', 'Kaliyah 755', 'Kallie 821', 'Kamila 873',
  'Kamryn 275', 'Kara 279', 'Karen 173', 'Karina 227', 'Karis 942', 'Karissa 618',
  'Karla 209', 'Karlee 649', 'Karley 916', 'Karli 865', 'Karlie 764', 'Karma 852',
  'Kasey 565', 'Kassandra 421', 'Kassidy 457', 'Kate 142', 'Katelyn 61', 'Katelynn 270',
  'Katharine 906', 'Katherine 36', 'Kathleen 371', 'Kathryn 144', 'Kathy 907', 
  'Katie 107', 'Katlyn 787', 'Katrina 382', 'Kaya 640', 'Kayden 624', 'Kaydence 356',
  'Kayla 26', 'Kaylah 951', 'Kaylee 42', 'Kayleigh 266', 'Kaylen 866', 'Kayley 729', 
  'Kayli 887', 'Kaylie 278', 'Kaylin 399', 'Kaylyn 686', 'Kaylynn 621','Keely 698', 
  'Keira 109', 'Kelly 212', 'Kelsey 184', 'Kelsie 766', 'Kendal 814', 'Kendall 148', 
  'Kendra 243', 'Kenia 874', 'Kenna 924', 'Kennedi 622', 'Kennedy 115', 'Kenya 523', 
  'Kenzie 557', 'Keyla 841', 'Khloe 963', 'Kiana 401', 'Kianna 773', 'Kiara 185', 
  'Kiera 301', 'Kierra 601', 'Kiersten 509', 'Kiley 429', 'Kimberly 58', 'Kimora 422',
  'Kinley 904', 'Kinsey 898', 'Kinsley 876', 'Kira 249','Kirsten 407', 'Krista 701', 
  'Kristen 374', 'Kristin 574', 'Kristina 404', 'Krystal 505', 'Kya 943', 'Kyla 204',
  'Kylee 146', 'Kyleigh 360', 'Kylie 66', 'Kyra 195']:
    print '\t extractFemaleNames => OK'
  else:
    print '\t extractFemaleNames => NOK'
  if extractMaleNames('baby2006.html','J') == ['Justus 743',
  'Justin 45', 'Justice 411', 'Junior 627', 'Julius 319', 'Julio 240', 
  'Julien 596', 'Julian 65', 'Jude 330', 'Judah 493', 'Juan 61', 
  'Jovany 833','Jovanny 805', 'Jovanni 776', 'Jovani 694', 'Jovan 840',
  'Josue 193', 'Josiah 117', 'Joshua 3', 'Josh 714', 'Joseph 11', 'Josef 972',
  'Jose 32', 'Jorge 120', 'Jordyn 780', 'Jordy 677', 'Jordon 739', 'Jorden 759',
  'Jordan 46', 'Jonathon 376', 'Jonathan 22', 'Jonas 357', 'Jonah 170', 'Jon 455',
  'Johnpaul 979', 'Johnny 237', 'Johnathon 542', 'Johnathan 177', 'John 20',
  'Johan 528', 'Joey 537', 'Joel 124', 'Joe 370', 'Joaquin 286', 'Joan 978', 
  'Jimmy 325', 'Jett 535', 'Jesus 74', 'Jessie 485', 'Jesse 102', 'Jerry 318', 
  'Jerome 577', 'Jermaine 474', 'Jerimiah 931', 'Jeremy 123', 'Jeremiah 71', 
  'Jeramiah 926', 'Jeffrey 180', 'Jeffery 432', 'Jefferson 642', 'Jean 721', 
  'Jayson 353', 'Jaylon 479', 'Jaylin 441', 'Jaylen 191', 'Jaylan 692', 'Jaydon 416',
  'Jaydin 971', 'Jayden 50', 'Jayce 427', 'Jay 351', 'Jaxson 391', 'Jaxon 211', 
  'Jax 995', 'Javon 410', 'Javion 644', 'Javier 162', 'Javen 954', 'Jasper 568', 
  'Jason 55', 'Jasiah 933', 'Jase 565', 'Jarvis 1000', 'Jarrett 659', 'Jaron 819', 
  'Jared 137', 'Jaquan 656', 'Jan 751', 'Jamison 534', 'Jamir 768', 'Jamie 583', 
  'Jameson 424', 'James 16', 'Jamel 970', 'Jamarion 459', 'Jamari 444', 'Jamarcus 914',
  'Jamar 649', 'Jamal 504', 'Jalen 228', 'Jakob 293', 'Jake 107', 'Jairo 564', 
  'Jair 726', 'Jaime 279', 'Jaiden 214', 'Jaheim 977', 'Jaeden 666', 'Jadyn 757',
  'Jadon 398', 'Jaden 88', 'Jacoby 909', 'Jacob 1', 'Jackson 36', 'Jack 35', 
  'Jace 187', 'Jabari 609']:
    print '\t extractMaleNames => OK'
  else:
    print '\t extractMaleNames => NOK'
  if extractDocAndPopularityDate('baby2006.html') == \
  'December 06, 2007 and Popularity in 2006':
    print '\t extractDocAndPopularityDate => OK'
  else:
    print '\t extractDocAndPopularityDate => NOK'

#Provided function to print the proper usage of this module      
def printUsage():
  print 'usage: babynames.py {--extractFemaleNames |--extractMaleNames} Filename Letter'
  print '       babynames.py  --extractDocAndPopularityDate Filename'
  print '       babynames.py --testAll to test your solution'
      
def main():
  if len(sys.argv) >= 2:
    if sys.argv[1] == '--testAll' or sys.argv[1] == '--extractDocAndPopularityDate' or sys.argv[1] == '--extractFemaleNames' or sys.argv[1] == '--extractMaleNames' :
      option = sys.argv[1]
      try:
        filename = sys.argv[2]
        Letter = sys.argv[3]
      except:
        None
      if option == '--extractFemaleNames':
        print extractFemaleNames(filename,Letter)
      elif option == '--extractMaleNames':
        print extractMaleNames(filename,Letter)
      elif option == '--extractDocAndPopularityDate':
        print extractDocAndPopularityDate(filename)
      elif option == '--testAll':
        testAll()
      else:
        print 'unknown option: ' + option
        sys.exit(1)
    else:
      printUsage()
      sys.exit(1)
  else:
    printUsage()
    sys.exit(1)
  
'''
There is something missing Here :)
'''
if __name__ == '__main__':
	main()