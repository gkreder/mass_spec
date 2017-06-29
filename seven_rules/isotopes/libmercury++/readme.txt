libmercury++ [download][svn]

http://klimt.iwr.uni-heidelberg.de/mip/proteomics/

This is an ANSI-C++ re-implementation of Rockwood's Mercury7 algorithm, in parts based on the emass code of Perttu Haimi.

libmercury++ produces exactly the same results as emass, however, as it uses simpler data structures, it is easier and straightforward to use. Most importantly, it is available as a library and does not read from standard input. As for documentation, the source documentation and the demo.cpp file should be sufficient. Elements are still limited to H, C, N, O, S. This is no limitation to the program, but merely a question of entering all isotope data into the static tables.
libmercury++ is the main building block of the amsmercury R package (see above).

libmercury++ is licensed under LGPL. 