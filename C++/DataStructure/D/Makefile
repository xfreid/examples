CFLAGS =

ex14 : ex14.o Cartesian.o Polar.o
	g++ $(CFLAGS) -o ex14 ex14.o Cartesian.o Polar.o 

Cartesian.o : Cartesian.cc Cartesian.h Coordinate.h
	g++ $(CFLAGS) -c Cartesian.cc 

Cartesian.o : Cartesian.cc Cartesian.h Coordinate.h
	g++ $(CFLAGS) -c Cartesian.cc 

ex14.o : ex14.cc Cartesian.h Polar.h
	g++ $(CFLAGS) -c ex14.cc 

clean:
	rm *.o *~ ex14

