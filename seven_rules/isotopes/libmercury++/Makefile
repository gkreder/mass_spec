#
# $Id: Makefile 27 2006-05-26 20:56:29Z mkirchner $
#
LIB_SHARED=libmercury++.so
DEFS=
CXXFLAGS=-Wall -pedantic -O3
CXX=g++
LIBS=
OBJS=libmercury++.o
LD=g++
LD_SHFLAGS=-shared

all: shared

shared: objclean
	make $(LIB_SHARED)

objclean:
	rm -f *.o

%.o: %.cpp
	$(CXX) -o $@ $(CXXFLAGS) $(INCLUDES) $(DEFS) -c $<

$(LIB_SHARED): $(OBJS)
	$(LD) $(LD_SHFLAGS) -o $@ $(OBJS) $(LIBS)

clean: objclean
	rm -f $(LIB_SHARED) demo

demo:	shared demo.cpp
	$(CXX) -o demo $(CXXFLAGS) -L. -lmercury++ demo.cpp
	echo "Please make sure you set LD_LIBRARY_PATH correctly."
	echo "Check 'ldd demo' prior to running it."
