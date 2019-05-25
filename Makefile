NAME:=template

$(NAME).fountain: $(wildcard scenes/*.md)
	python assemble.py $(NAME).fountain

$(NAME).pdf: $(NAME).fountain
	afterwriting --source $(NAME).fountain --pdf

.PHONY: clean pdf
clean:
	rm $(NAME).fountain $(NAME).pdf
pdf: $(NAME).pdf
