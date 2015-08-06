from xml.dom import minidom
from PIL import Image                                                                                
import urllib2
import urllib
import os
import sys
import json


		 
print "\nChecking local disk in current directory..."
if (os.path.exists('itemHashCatalog.txt')==False):
	print "Catalog needed."
	print "\nWriting itemHash text file to local disk..."
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
			#print (str(item).split('items/'))[1][:(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')]+' - '+(str(item).split('items/'))[1][(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')+1:].replace("-"," ").title()
			f.write((str(item).split('items/'))[1][:(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')]+' - '+(str(item).split('items/'))[1][(str(item).split('items/'))[1].replace('-', ' ' ,1).index(' ')+1:].replace("-"," ").title()+'\n')
	f.close()
	print '\nComplete! File saved to:\n'+os.getcwd()+'/itemHashCatalog.txt\n'
else:
	print "\nHash Catalog already exists in current directory!\n"

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
	#BOLD HERE
	print "Multiple intances found! ("+str(count)+")\n"
	#sleep here to let user know
	print "Which match number is desired? (enter number from above)"
	itemSpecific = raw_input('')
	#Catch out of bound input here	

elif count==1:
	#Nothing only one match - set index to after 'null'
	itemSpecific=1
	pass

#No matches 			
else:
	print "\nNo matches found. Please check spelling and rerun.\n"
	sys.exit()

#Last verification with info from hash catalog
itemHash=str(matchArray[int(itemSpecific)].split(' - ')[0])
itemName=str(matchArray[int(itemSpecific)].split(' - ')[1])
itemUrl="http://www.bungie.net/platform/Destiny/Manifest/InventoryItem/"+itemHash+"/"

print "\nITEM:\n"+itemName.split('\n')[0]+"\n"
print "HASH:\n"+itemHash+"\n"
print "URL:\n"+itemUrl+"\n"

############## ADDED
while 1:
	if (os.path.exists('myKey.txt')==False):
		print "***API Key needed!***\nPlease create a text file called 'myKey' containing your API key in the same directory as this file and rerun or press any key to enter manually."

		#Any Key press to continue here.
		raw_input('')
		
		#Exception handling needed for incorrect input
		print "\nPlease enter your API Key: (Retrieved here: https://www.bungie.net/en/User/API)"
		API_Key = raw_input('')
		print "\n"
		break;

	else:
		print "API key txt file found! Parsing..."
		f=open('myKey.txt','r')
		textContents=f.read()

		#Omitting spaces and newlines
		#Also check string length - might be fixed number of characters - verify with another key
		#Going to have to parse txt file for spaces at end (Only take the 30+ alphanumeric string)
		#Also omit myKey.txt from gitignore
		API_Key=textContents.replace(' ','').replace('\n','')
		print "Your API_KEY: " + str(API_Key)
		print "\n"

		#Chance to correct/man enter here
		break;

#Migrated to urllib2 for header capability
req = urllib2.Request(itemUrl)

#Bungie making it harder to reference without dev capability -_-
req.add_header('X-API-Key', str(API_Key))
resp = urllib2.urlopen(req)
data = json.loads(resp.read())
itemInfoDict = data.values()[4]

#Text class here for prettiness
print "Name: "+itemInfoDict[u'data'][u'inventoryItem'][u'itemName']
print "Description: "+itemInfoDict[u'data'][u'inventoryItem'][u'itemDescription']
print "Type of weapon: "+itemInfoDict[u'data'][u'inventoryItem'][u'itemTypeName']
print "Tier: " +itemInfoDict[u'data'][u'inventoryItem'][u'tierTypeName']
iconUrl='http://www.bungie.net'+itemInfoDict[u'data'][u'inventoryItem'][u'icon']
print "Icon: "+iconUrl

print "\nSaving icon to "+os.path.dirname(os.path.realpath(__file__))+"/icons/" +itemName.split('\n')[0]+".jpg\n"

#Use requests to download image -- below this comment needs fixing
#UPDATE_COMMENT: just going to use both libraries - screw it
urllib.urlretrieve(iconUrl, 'icons/'+itemName.split('\n')[0]+".jpg")

print "Opening image...\n"
img = Image.open(os.path.dirname(os.path.realpath(__file__))+"/icons/" +itemName.split('\n')[0]+".jpg")
img.show()

#If myKey.txt path = false Write entered API to a created file...

