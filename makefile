quick:
	pdflatex thesis
	SumatraPDF thesis.pdf &

all: mybib2.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
	SumatraPDF thesis.pdf &

mybib2.bib : mybib.bib RCLfull.bib
	cat IEEEfull.bib RCLfull.bib mybib.bib > mybib2.bib

clean:
	rm -rf *.aux *.bbl *.blg *.toc *.log *.lot *.lof *.out Body/*.aux Preface/*.aux Reference/*.aux mybib2.bib

vim:
	vim -p makefile thesis.tex mybib.bib Preface/dedication.tex Preface/acknowl.tex Preface/abstract.tex Body/chapter1.tex Body/chapter2.tex Body/chapter3.tex Body/chapter4.tex Body/chapter5.tex Body/chapter6.tex Body/chapter7.tex Body/chapter8.tex Body/chapter9.tex
