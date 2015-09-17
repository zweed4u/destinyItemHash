This is an xml parser that makes use of a sitemap to catalog item number hashes for Destiny. These numbers are ubiquitous when referencing items and are commonly used in URLs. The output is both displayed in terminal and output in a text file for further use. 
This will be expanded to make use of the item hashes in Bungie's API so that more information can be extracted for each item.  

eg. http://www.bungie.net/platform/Destiny/Manifest/InventoryItem/*  

Thus far the user is prompted for which item they wish to see more on. It displays the line from the text file for all matching substrings and outputs the format in:  

*ItemHash* - *ItemName*  

Item search is via substring so "gja" returns:  

"1274330687 - Gjallarhorn"  

==================================================  

~~In the near future, file checking will be implemented and if the hash cataog is already existant then the file creation will be skipped and only parsing the existant document will take place.~~

==================================================
Recently, Bungie has required an API Key header to view their '/Manifest/*' path. I migrated to urllib2 to allow header addition in the request. Image download is still available publicly without any headers so I stuck with urllib to download.   
#UPDATE
API Key is no longer needed in the request. API Key will still be implemented to ensure proper functionality.  
On the fly API Key generating maybe something to come in the future.  
##TTK - 2.0! (Where is the new stuff?!)
With the Taken King finally released, many new items have been hashed and indexed. The current text file catalogged all hashes available as of September 14th, 2015. To ensure the your hash catalog is synchronous with the current up to date database - remove all instances of 'itemHashCatalog.txt' from the local directory and run. The script will write the current catalog to file and continue the program with this table as the reference.  


Contact me with any questions: @ZWeed4U
