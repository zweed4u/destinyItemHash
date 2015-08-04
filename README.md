This is an xml parser that makes use of a sitemap to catalog item number hashes for Destiny. These numbers are ubiquitous when referencing items and are commonly used in URLs. The output is both displayed in terminal and output in a text file for further use. 
This will be expanded to make use of the item hashes in Bungie's API so that more information can be extracted for each item.  

eg. http://www.bungie.net/platform/Destiny/Manifest/InventoryItem/*  

Thus far the user is prompted for which item they wish to see more on. It displays the line from the text file for all matching substrings and outputs the format in:  

*ItemHash* - *ItemName*  

Item search is via substring so "gja" returns:  

"1274330687 - Gjallarhorn"  

==================================================
In the near future, file checking will be implemented and if the hash cataog is already existant then the file creation will be skipped and only parsing the existant document will take place. 



Contact me with any questions: @ZWeed4U
