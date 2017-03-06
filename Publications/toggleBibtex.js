// Toggle Display of BibTeX
function toggleBibtex(articleid) {
	var bib = document.getElementById('bib_'+articleid);
	if (bib) {
		if(bib.className.indexOf('bibtex') != -1) {
		bib.className.indexOf('noshow') == -1?bib.className = 'bibtex noshow':bib.className = 'bibtex';
		}
	} else {
		return;
	}
}