
all : test_32 test_64

test_32 : test.c md5_file.c md5_file.h md5c.c md5.h global.h 
	gcc -m32 md5c.c test.c md5_file.c -o test_32 -t

test_64 : test.c md5_file.c md5_file.h md5c.c md5.h global.h 
	gcc -m64 md5c.c test.c md5_file.c -o test_64 -t

test :
	./test_32 -x
	./test_64 -x
	md5sum md5c.c

clean : 
	rm -f *~ test32 test_64 *.o

.PHONY: test clean

