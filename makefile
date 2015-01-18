all:
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
	cygstart thesis.pdf

clean:
	rm -rf *.aux *.bbl *.blg *.toc *.log *.lot *.lof *.out Body/*.aux

vim:
	vim -p makefile thesis.tex mybib.bib Preface/dedication.tex Preface/acknowl.tex Preface/abstract.tex Body/chapter1.tex Body/chapter2.tex Body/chapter3.tex Body/chapter4.tex Body/chapter5.tex Body/chapter6.tex Body/chapter7.tex Body/chapter8.tex Body/chapter9.tex
