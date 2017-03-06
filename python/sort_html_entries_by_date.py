#!/usr/bin/env python

from datetime import date
import os
import sys
from sort_html_entries_engine import extract_entries_and_write_to_file

def sort_entries_in_html_file(filename):
	"""Function to sort html files that contains publications, according to year in bib entry. 
	   Designed to  sort html files produced by command-line jab-ref
	"""		

	if not os.path.isfile(filename+".html"):
		print "file ", filename, ".html does not exist"
		return

	# first, rename existing file 	
	os.rename(filename+".html", filename+"_original.html")

	f = open(filename+'_original.html')

	# new file
	f2 = open(filename+".html", 'w')

	Lines=f.readlines()

	# keep the first two rows from the original file
	f2.write(Lines[0])
	f2.write(Lines[1])

	startyear=1990
	currentyear=date.today().year+1

	years=range(currentyear,startyear,-1)
	# print years

	str_backwards = '<li ><p>'
	str_forward   = '</li>'
	take_next_row = 1

	# for each year in years, search for html entries, and store entries of the same year together
	for year in years:	
		searchfield = 'year = {'
		searchquery = str(year)
		# print searchquery
		extract_entries_and_write_to_file(Lines, searchfield, searchquery, f2, str_backwards, str_forward, take_next_row)		

	# write last line from the original files
	f2.write(Lines[len(Lines)-1])

	# remove original file
	os.remove(filename+"_original.html")

def main(argv):
	if len(sys.argv) != 2:
		print 'sort_html_entries_by_date.py <htmlname-without-extension>'
		sys.exit(2)

	filename = sys.argv[1]

	sort_entries_in_html_file(filename)	

if __name__ == "__main__":
   main(sys.argv[1:])

