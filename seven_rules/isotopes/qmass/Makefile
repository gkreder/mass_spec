progs = qmass

objs = qmass.o parser.o formula.o getopt.o kiss_fft.o
headers = parser.h formula.h getopt.h kiss_fft.h

CXX = g++

libs = -lm 
#CXXFLAGS = -Wall -W -ansi -pedantic -g 
#CXXFLAGS = -O3 -g -pg
CXXFLAGS = -O3

LDFLAGS =

qmass : $(objs) $(headers)
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $(objs) -o $@ $(libs)

qmass.o : qmass.cpp $(headers)
	$(CXX) $(CXXFLAGS) -c $<

parser.o : parser.cpp $(headers)
	$(CXX) $(CXXFLAGS) -c $<

formula.o : formula.cpp $(headers)
	$(CXX) $(CXXFLAGS) -c $<

getopt.o : getopt.cpp $(headers)
	$(CXX) $(CXXFLAGS) -c $<

kiss_fft.o : kiss_fft.c $(headers)
	$(CXX) $(CXXFLAGS) -c $<


.PHONY: all
all: $(progs)

.PHONY: clean
clean:
	rm -f core *.o $(progs)

.PHONY: bare
bare: clean
	rm -f *~
