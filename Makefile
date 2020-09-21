LTX=pdflatex
SRC=main.tex

main.pdf: $(SRC) $(IMG)
	$(LTX) $(SRC)
	$(LTX) $(SRC)

.PHONY: clean
clean:
	-rm -f *.log *.snm *.out *.nav *.toc *.aux
	-rm -f main.pdf
