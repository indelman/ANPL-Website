#!/usr/bin/env python

from datetime import date
import os
import sys

def search_backwards(Lines, searchquery, i): 
    """Search for a string backwards in Lines starting from line i"""        
    result = []
    while i>0:    	
    	if searchquery in Lines[i]:    		
    		result = i
    		break
    	i = i - 1    	
    return result		

def search_forward(Lines, searchquery, i): 
    """Search for a string forward in Lines starting from line i"""    
    
    result = []
    while i<len(Lines):              
       if searchquery in Lines[i]:
          result = i
          # print "found!!"
          break
       i = i + 1     
    return result           

def extract_entries_and_write_to_file(Lines, searchfield, searchquery, fid, str_backwards, str_forward, take_next_row):
	"""Search for entries in Lines that include a searchfield with searchquery and write to the file fid 
	   the corresponding block of lines
	"""    
	i=1	
	# print "searchquery=<", searchquery, ">"	
	while i < len(Lines)-1:			
		if searchfield in Lines[i]:
			# print Lines[i]
			if searchquery in Lines[i]:
			   # print Lines[i], ">>>>>>>>"
			   block_start = search_backwards(Lines, str_backwards, i)
			   block_end   = search_forward(Lines, str_forward, i)											
			   #print "block_start, block_end: ", block_start, ",", block_end 
			   if not block_end:
				   block_end = len(Lines)
				   #print "reached eof??"
				   # print Lines[block_start-1:block_end]
			   elif take_next_row:
			      block_end = block_end + 1

			   # write entry Lines[block_start-1:block_end+1] into file
			   # print block_start, ", ", block_end
			   line_indices=range(block_start-1,block_end)
			   # print "i, line_indices: ", i, line_indices
			   for ind in line_indices:
				   fid.write(Lines[ind])
			   fid.write("\n\n")   

		i = i + 1	


# def main(argv):
# 	if len(sys.argv) != 4:
# 		print 'sort-html-entries-by-date.py <htmlname-without-extension>'
# 		sys.exit(2)

# 	Lines = sys.argv[1]
# 	searchquery = sys.argv[2]
# 	fid = sys.argv[3]
	
# 	extract_entries_and_write_to_file(Lines, searchquery, fid)

# if __name__ == "__main__":
#    main(sys.argv[1:])