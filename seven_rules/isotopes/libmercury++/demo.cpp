/*
 * $Id: demo.cpp 27 2006-05-26 20:56:29Z mkirchner $
 */
#include <iostream>
#include <iomanip>
#include <vector>
#include "libmercury++.h"

int main(void) {
	std::vector<unsigned int> composition(5,500000);
	std::vector<double> mz, ab;
	mercury::mercury(mz, ab, composition, 0, 0);
	std::cout.setf(std::ios::fixed);
  	std::cout.precision(12);
	std::cout << "Isotope distribution for (CHNOS)500000:" << std::endl;
	for (size_t i = 0; i < mz.size(); i++) {
		std::cout << mz[i] << "\t" << ab[i] << std::endl;
	}
	return(0);
}

