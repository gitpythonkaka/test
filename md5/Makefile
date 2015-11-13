
all : test_32 test_64

test_32 : test.c md5c.c md5.h global.h 
	gcc -m32 md5c.c test.c -o test_32 -t

test_64 : test.c md5c.c md5.h global.h 
	gcc -m64 md5c.c test.c -o test_64 -t

test :
	./test_32 -x
	./test_64 -x

clean : 
	rm -f *~ test *.o

.PHONY: test clean

