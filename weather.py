#! /usr/bin/env python

import pycurl
from time import gmtime, strftime
from StringIO import StringIO


"""using pycurl, take all data from webpage and buffer it to a stringIO"""
buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://money.cnn.com/data/markets/sandp/') #url we need
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

"""store that buffer into a string called body"""
body = buffer.getvalue()

"""write that body to its own text file to search"""
with open ("body.txt","w+") as in_file:
	in_file.write(body)


"""this searches the file for the specific line that holds the S&P Value, once we find that line we search its index to find the value and store it in spVal"""

lines = [] # Declare an empty list named "lines"
with open ("body.txt","r+") as f:
	
	for line in f:
		lines.append(line)

	substr='streamFormat="ToHundredth" streamFeed="SunGard">' # Substring to search for
	
	for linenum, line in enumerate(lines): # For every line in lines, enumerated by linenum,
		index = 0 # Set the search index to the first character,"""
		str = lines[linenum] # and store the line in a string variable, str.
		while index < len(str): # While search index is less than the length of the string:
			index = str.find(substr, index) 
			if index == -1: # If nothing is found,
				break # break out of the while loop. Otherwise,
			
			#print(linenum,index)
			
			index += len(substr)
			find_val = lines[linenum]#stored the line in find_val
			spVal =""
			while find_val[index] != "<": #iterate through the index to and store the #
								
				spVal = spVal + find_val[index]
				index += 1
			
			#print (spVal) 


"""sets the date and time, then appends date plus our value in weather.txt"""

date = strftime("%Y-%m-%d %H:%M:%S:%Z", gmtime())
with open("weather.txt", "a+") as text_file:
	text_file.write(date)
	text_file.write(" ")
	text_file.write(spVal)
	text_file.write(" \r\n ")
	


