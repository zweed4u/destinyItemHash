from xml.dom import minidom
import urllib
import os
import sys
url = 'http://www.destinydb.com/sitemap.xml/items/1'
xml = urllib.urlopen(url).read()
xmldoc = minidom.parseString(xml)
loc_values = xmldoc.getElementsByTagName('loc')
f=open('itemHashCatalog.txt','w')
for loc_val in loc_values:
	item=(loc_val.firstChild.nodeValue)
	if len((str(item).split('items/')))==1:
		pass
	else:
		print (str(item).split('items/'))[1][:(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')]+' - '+(str(item).split('items/'))[1][(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')+1:].replace("-"," ").title()
		f.write((str(item).split('items/'))[1][:(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')]+' - '+(str(item).split('items/'))[1][(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')+1:].replace("-"," ").title()+'\n')
f.close()
print '\nComplete! File saved to:\n'+os.getcwd()+'/itemHashCatalog.txt\n'

print "For what do you want me to pull info for?"
item = raw_input('')
item = item.title()

#Keep track of multiple matches
count=0

#Declare array/list with 'null' in index0 for consistency in enumerations
matchArray=['null']

with open('itemHashCatalog.txt', 'r') as inF:
	for line in inF:
        	if str(item) in line:
			count+=1		
			print '\nMatch '+str(count)+":\n"+ line
			matchArray.append(str(line))
if count>1:
	print "Multiple intances found!\n"
	#sleep here to let user know
	print "Which match number is desired? (enter number from above)"
	itemSpecific = raw_input('')
	#print "\n"+matchArray[int(itemSpecific)]	

elif count==1:
	#Nothing only one match - set index to after 'null'
	itemSpecific=1
	pass

#No matches 			
else:
	print "\nNo matches found. Please check spelling and rerun.\n"
	sys.exit()

itemHash=str(matchArray[int(itemSpecific)].split(' - ')[0])
itemName=str(matchArray[int(itemSpecific)].split(' - ')[1])
itemUrl="http://www.bungie.net/platform/Destiny/Manifest/InventoryItem/"+itemHash+"/"

print "HASH:\n"+itemHash+"\n"
print "ITEM:\n"+itemName+"\n"
print "URL:\n"+itemUrl+"\n"

		
		


