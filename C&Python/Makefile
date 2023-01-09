.SILENT:

all: compile clean

compile:
	gcc -o detect detect.c -lpython3.10
	./detect ./dataset

install:
	sudo apt-get install python${1}-dev

clean:
	rm -rf detect