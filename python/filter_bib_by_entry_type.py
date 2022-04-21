#!/usr/bin/env python

from datetime import date
import os
import sys
from sort_html_entries_engine import extract_entries_and_write_to_file

def sort_entries_in_html_file(bibfilename, newbibfilename, fieldname, query_string):
	"""Function to create new bib file from bibfilename, that contains only block-entries 
	   that contain query_string in the field fieldname
	   Use this to filter bib file according to some criteria, e.g. 
	   Designed to  sort bib files produced by command-line jab-ref
	"""
	
	# first, rename existing file 		
	f = open(bibfilename+'.bib')

	# new file
	f2 = open(newbibfilename+".bib", 'w')

	Lines=f.readlines()
	
	str_backwards = '@'
	str_forward   = '@'
	take_next_row = False # True

	# for each year in years, search for bib entries, and store entries of the same year together	
	searchfield = fieldname + ' = {'
	searchquery = query_string
	# print "searchquery=<", searchquery, ">"
	# print searchquery
	extract_entries_and_write_to_file(Lines, searchfield, searchquery, f2, str_backwards, str_forward, take_next_row)		

	# write last line from the original files
	f2.write(Lines[len(Lines)-1])	

def main(argv):
	if len(sys.argv) != 5:
		print('filter_html_by_entry_type.py <htmlname-without-extension> <newbibfilename> <fieldname> <query_string>')
		sys.exit(2)

	bibfilename = sys.argv[1]
	newbibfilename = sys.argv[2]
	fieldname = sys.argv[3]
	query_string = sys.argv[4]

	sort_entries_in_html_file(bibfilename, newbibfilename, fieldname, query_string)	

if __name__ == "__main__":
   main(sys.argv[1:])

