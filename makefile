quick:
	pdflatex thesis
	cygstart thesis.pdf &

all: mybib2.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
	cygstart thesis.pdf &

mybib2.bib : mybib.bib RCLfull.bib
	cat IEEEfull.bib RCLfull.bib mybib.bib > mybib2.bib

clean:
	rm -rf *.aux *.bbl *.blg *.toc *.log *.lot *.lof *.out Body/*.aux Preface/*.aux Reference/*.aux mybib2.bib

vim:
	vim -p makefile thesis.tex mybib.bib Body/chapter4.tex Body/chapter_matrix_traversal.tex Body/chapter5.tex Body/chapter6.tex Body/chapter7.tex Body/chapter8.tex Body/chapter9.tex
