from xml.dom import minidom
import urllib
import os
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
print '\nComplete! File saved to:\n'+os.getcwd()+'/itemHashCatalog.txt'

