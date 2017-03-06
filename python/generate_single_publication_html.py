#!/usr/bin/env python

from datetime import date
import os
import sys

def write_html_block_pub_type(f_new, filename, title_txt, title_level_str):
	"""Function to write to f_new publications from filename"""

	if os.path.isfile(filename):
		str_pub_type = "<" + title_level_str + ">" + title_txt + "</" + title_level_str + ">"
		print str_pub_type
		f_new.write(str_pub_type)
		f = open(filename)
		Lines=f.readlines()	
		# print "Lines: ", Lines
		for line in Lines:
			f_new.write(line)

def generate_single_publication_html(basename, title_level_str):
	"""Function to create a single html containing Journal, conference etc publications
	   title_level_str should be h1, h2, etc.
	"""
	
	# new html file
	f_new = open(basename+".html", 'w')	

	# journals	
	filename = basename+"-Chapters.html"	
	title_txt = "Book Chapters"
	write_html_block_pub_type(f_new, filename, title_txt, title_level_str)

    # journals	
	filename = basename+"-Journals.html"	
	title_txt = "Journal publications"
	write_html_block_pub_type(f_new, filename, title_txt, title_level_str)

	# conference
	filename = basename+"-Conferences.html"	
	title_txt = "Conference publications"
	write_html_block_pub_type(f_new, filename, title_txt, title_level_str)

	# Technical Reports
	filename = basename+"-TechReport.html"	
	title_txt = "Technical Reports"
	write_html_block_pub_type(f_new, filename, title_txt, title_level_str)




def main(argv):
	if len(sys.argv) != 3:
		print 'generate_single_publication_html <basename>  <title_level_str>'
		sys.exit(2)

	basename = sys.argv[1]
	title_level_str = sys.argv[2]

	generate_single_publication_html(basename, title_level_str)

if __name__ == "__main__":
   main(sys.argv[1:])

