#!/bin/sh

# generate publications per research topics that appear in the file ResearchTopics.txt
cd ResearchProjects

#remove previous files
rm pubs-*.*

bibfilename="../VadimIndelman"
while IFS= read -r line; do
    currentresearch=$line
    outputfile="pubs-$currentresearch"
    echo $outputfile
    #echo "START - $outputfile-Journals.html"
    
    # generate bib file that only contains bib-entries with the current research topic	
	python ../python/filter_bib_by_entry_type.py $bibfilename $outputfile researchtopic $currentresearch
	# generate journal and conference html pages, sort by date, just in case
	#java -jar ../JabRef-2.10.jar -m entrytype="incollection","$outputfile-Chapters.html",PubList -n true "$outputfile.bib"	
	#java -jar ../JabRef-2.10.jar -m entrytype="article","$outputfile-Journals.html",PubList -n true "$outputfile.bib"
	#python ../python/sort_html_entries_by_date.py "$outputfile-Journals"
	#java -jar ../JabRef-2.10.jar -m entrytype="InProceedings","$outputfile-Conferences.html",PubList -n true "$outputfile.bib"
	#python ../python/sort_html_entries_by_date.py "$outputfile-Conferences"
	#java -jar ../JabRef-2.10.jar -m entrytype="TechReport","$outputfile-TechReport.html",PubList -n true "$outputfile.bib"

	# generate single publication file
	#python ../python/generate_single_publication_html.py $outputfile h5

	
done <../ResearchTopics.txt		

# generate publications per year
#startyear=2008
#currentyear=$(date +"%Y")
#yeariterator=$startyear
#while [ "$yeariterator" -le $currentyear ]
#do
#  outputfile="Publications/pubs-$yeariterator.html"
#  java -jar JabRef-2.10.jar -m year=$yeariterator,$outputfile,PubList -n true VadimIndelman.bib   
#  yeariterator=$(($yeariterator+1))
#done


