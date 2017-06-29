/*
qmass.cpp: Calculation of isotopic compositions and 
           accurate masses of isotopic peaks

Algorithm published in 

Rockwood, A.L.; Van Orman, J.R.; Dearden, D.V. 
Isotopic Composition and Exact Masses of Single Isotopic 
Peaks. J. Am. Soc. Mass Spectrom. 2003, 15, 12-21

Copyright (c) 2000, 2005 Alan Rockwood, Steve van Orden, 
                         Perttu Haimi

All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, are permitted provided
that the following conditions are met:

    * Redistributions of source code must retain the
      above copyright notice, this list of conditions
      and the following disclaimer.
    * Redistributions in binary form must reproduce
      the above copyright notice, this list of conditions
      and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the author nor the names of any contributors
      may be used to endorse or promote products derived
      from this software without specific prior written
      permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>
#include <cwchar>
#include <cfloat>

#include "parser.h"
#include "formula.h"
#include "getopt.h"
#include "kiss_fft.h"

using std::wcin;
using std::wcout;
using std::wcerr;
using std::endl;
using std::wifstream;
using std::wistringstream;
using std::ios;

using std::string;
using std::wstring;

using std::getline;
using std::swap;

using std::abs;

// composition
struct iso_abundancy
{
  size_t elem_index;
  size_t iso_index;
  double weight;
};

typedef std::vector<iso_abundancy> Composition;

struct peak
{
  double mass;
  int int_mass;
  double rel_area;
  Composition comp;
};

typedef std::vector<peak> Pattern;   
typedef std::vector<Pattern> AtomData;

typedef std::vector<double> FreqData;

typedef std::vector<wstring> AtomList;

const double PI = 3.14159265358979323846;
const double TWOPI = 6.28318530717958647;
const double HALFPI = 1.57079632679489666;
const double ELECTRON_MASS = 0.00054858;

AtomData ad;
ElemMap em;
AtomList al;

void init_data(string filename, AtomData & ad, ElemMap & em)
{
  wifstream f(filename.c_str());
  
  ad.clear();
  em.clear();

  wstring line;
  ulong elemindex = 0;
  int state = 0;
  while(getline(f, line)) {
    wistringstream ist(line);
    wstring element;
    switch(state) {
    case 0: // new element
      ist >> element;
      em[element] = elemindex;
      ad.push_back(Pattern());
      al.push_back(element);
      elemindex++;
      state = 1;
      break;
    case 1: // isotope
      peak p;
      Pattern & idist = ad.back();
      if(ist >> p.mass >> p.rel_area) {
	p.int_mass = (int)(p.mass + 0.5);
	idist.push_back(p); // insert the peak
      } else  
	state = 0; // no more isotope data
      break;
    }
  }  
  f.close();
}

void print_pattern(Pattern & result, int digits)
{
  // find the maximum
  double max_area = 0;
  for(Pattern::iterator i = result.begin(); i != result.end(); ++i) {
    if(max_area < (*i).rel_area)
      max_area = (*i).rel_area;
  }
  if(max_area == 0)
    return; // empty pattern

  wcout.setf(ios::fixed);
  wcout.precision(digits);
  double print_limit = pow(10, -digits) / 2;
  for(Pattern::iterator i = result.begin(); i != result.end(); ++i) {
    peak & p = (*i);
    double mass = p.mass;
    int int_mass = p.int_mass;
    double rel_area = p.rel_area;
    double val = rel_area / max_area * 100;
    if(val >= print_limit) {
      wcout << int_mass << L" " << mass << L" " << val << L" ";
      
      // print the isotopic composition
      Composition c = p.comp;
      for(Composition::iterator j = c.begin(); j != c.end(); ++j) {
	iso_abundancy ia = *j;
	wcout << al[ia.elem_index];
	wcout << ad[ia.elem_index][ia.iso_index].int_mass << L":";
	wcout << ia.weight << L" ";
      }
      wcout << endl;
    }
  }
}

// Calculate integer average molecular weight
long calc_intMW(FormMap & fm)
{
  double tempMW = 0;

  for(FormMap::iterator i = fm.begin(); i != fm.end(); i++) {
    size_t elem_index = (*i).first;
    ulong n = abs((*i).second);
    Pattern elem_data = ad[elem_index];

    for(Pattern::iterator j = elem_data.begin(); 
	j != elem_data.end(); ++j) {
      tempMW += n * (*j).mass * (*j).rel_area;
    }
  }
  return (long)(tempMW + 0.5);
}


double calc_variance(FormMap & fm)
{
  double molvar = 0;

  for(FormMap::iterator i = fm.begin(); i != fm.end(); i++) {
    size_t elem_index = (*i).first;
    ulong n = abs((*i).second);
    Pattern elem_data = ad[elem_index];
    
    double avemass = 0;
    for(Pattern::iterator j = elem_data.begin(); 
	j != elem_data.end(); ++j) {
      avemass += (*j).mass * (*j).rel_area;
    }

    double var = 0;
    for(Pattern::iterator j = elem_data.begin();
	j != elem_data.end(); ++j) {
      var += ((*j).mass - avemass) * 
             ((*j).mass - avemass) * (*j).rel_area;
    }

    molvar += n * var;
  }

  return molvar; // the sum of variances of atoms
}

int calc_massrange(double molvar)
{
  int tmp = (int)(sqrt(1 + molvar) * 20);
  
  if((tmp & (tmp - 1)) == 0)
    return tmp; // already a power of 2
  
  // round up to the nearest power of 2
  int result;
  for(result = 1; tmp != 0; tmp >>= 1)
    result <<= 1;

  return result;
}

void calc_freq(kiss_fft_cpx data[], long npoints, 
	       int mass_range, long mass_shift,
	       FormMap & fm)
{  
  for (int i = 0; i < npoints; i++) {
    
    double freq;
    if(i <= npoints / 2)
      // first half of Frequency Domain (+)masses
      freq = (double)i / mass_range;
    else
      // second half of Frequency Domain (-)masses
      freq = (double)(i - npoints) / mass_range;

    double r = 1;
    double theta = 0;
    
    for(FormMap::iterator j = fm.begin(); j != fm.end(); ++j) {
      
      size_t elem_index = (*j).first;
      ulong n = abs((*j).second);
      Pattern & elem_data = ad[elem_index];
      
      double real = 0, imag = 0;
      for(Pattern::iterator k = elem_data.begin(); 
	  k != elem_data.end(); ++k) {
	peak & p = *k;
	double X = TWOPI * p.int_mass * freq;
	real += p.rel_area * cos(X);
	imag += p.rel_area * sin(X);
      }
      
      // Convert to polar coordinates, r then theta
      double tempr = sqrt(real * real + imag * imag);
      r *= pow(tempr, n);
      if (real > 0) theta += n * atan(imag / real);
      else if (real < 0) theta += n * (atan(imag / real) + PI);
      else if (imag > 0) theta += n * HALFPI;
      else 	         theta += n * -HALFPI;
    }
    
    // Convert back to real:imag coordinates and store
    double a = r * cos(theta);
    double b = r * sin(theta);
    double c = cos(TWOPI * mass_shift * freq);
    double d = sin(TWOPI * mass_shift * freq);
    data[i].r = a * c - b * d;
    data[i].i = b * c + a * d;
  }
}

// TODO: check whether the data sums to one,
// it would be enough to normalize once.
void filter_data(kiss_fft_cpx data[], long npoints, long intMW,
		 double limit, Pattern & result)
{
   // Normalize the intensity to a probability distribution
   double sumarea = 0;
   for (int i = 0; i < npoints; ++i)
     if (data[i].r < 0)
       data[i].r = 0; // get rid of negative values
     else
       sumarea += data[i].r;
   for (int i = 0; i < npoints; ++i)
     data[i].r = data[i].r / sumarea;

   // Find out which values can be discarded as too small
   int start, end;
   for (start = npoints / 2 + 1; start < npoints; start++)
     if(data[start].r >= limit)
       break;
   for (end = npoints / 2; end >= 0; end--)
     if(data[end].r >= limit)
       break;
   
   result.clear();

   peak p;
   for (int i = start + 1; i < npoints; i++) {
     p.int_mass = i - npoints + intMW; // integer masses are enough
     p.mass = 0;
     p.rel_area = data[i].r;
     result.push_back(p);
   }
   for (int i = 0; i < end; i++) {
     p.int_mass = i + intMW;
     p.mass = 0;
     p.rel_area = data[i].r;
     result.push_back(p);
   }
   
   // renormalize
   sumarea = 0;
   for(Pattern::iterator i = result.begin(); i != result.end(); ++i) {
     sumarea += (*i).rel_area;
   }
   for(Pattern::iterator i = result.begin(); i != result.end(); ++i) {
     (*i).rel_area = (*i).rel_area / sumarea;
   }
}
 
void calc_pattern(Pattern & result, FormMap & fm, double limit)
{
  int ptsperamu = 1;

  long intMW = calc_intMW(fm);
  double molvar = calc_variance(fm);
  int mass_range = calc_massrange(molvar);

  long npoints = mass_range * ptsperamu;
  kiss_fft_cpx * freq_data = new kiss_fft_cpx[npoints];
  kiss_fft_cpx * peak_data = new kiss_fft_cpx[npoints];

  calc_freq(freq_data, npoints, mass_range, -intMW, fm);
  
  kiss_fft_cfg cfg = kiss_fft_alloc(npoints, 0, NULL, NULL);
  kiss_fft(cfg, freq_data, peak_data);

  filter_data(peak_data, npoints, intMW,
	      limit, result);
  
  kiss_fft_cleanup();
  delete [] peak_data;
  delete [] freq_data;
}

// this is an O(n + m) algo, where n is product size
// and m is parent size
void calc_composition(Pattern & product, Pattern & parent,
		      size_t elem_index, size_t iso_index,
		      double weight)
{
  Pattern::iterator i = product.begin();
  Pattern::iterator j = parent.begin();

  while(1) {
    if(i == product.end() || j == parent.end())
      break;
    int prod_mass = (*i).int_mass;
    int par_mass = (*j).int_mass;
    if(prod_mass < par_mass)
      i++;
    else if(prod_mass > par_mass)
      j++;
    else {
      iso_abundancy ia;
      ia.elem_index = elem_index;
      ia.iso_index = iso_index;
      // steps 4, 5 and 6. divide by parent peaks and multiply
      ia.weight = (*i).rel_area / (*j).rel_area * weight;
      (*j).comp.push_back(ia);
      j++;
    }
  }
}


void calculate(Pattern & parent, FormMap & fm,
	       long charge, double limit)
{

  // calculate the elemental compositions
  calc_pattern(parent, fm, limit);     // step 1. compute the parent
  Pattern product;
  for(FormMap::iterator i = fm.begin(); i != fm.end(); i++) {
    size_t elem_index = (*i).first;
    ulong n = abs((*i).second);
    fm[elem_index]--;                
    calc_pattern(product, fm, limit);  // step 2. compute the product 
    fm[elem_index]++;
    Pattern elem_data = ad[elem_index];
    for(size_t j = 0; j < elem_data.size(); j++) {
      peak p = elem_data[j];
      Pattern tmp = product;
      for(Pattern::iterator k = tmp.begin(); k != tmp.end(); k++)
	(*k).int_mass += p.int_mass;  // step 3. add mass of the isotope
      calc_composition(tmp, parent, elem_index, j, p.rel_area * n);
    }
  }

  // calculate the accurate mass and use
  // error correction method 2
  for(Pattern::iterator i = parent.begin(); i != parent.end(); i++) {
    peak & p = (*i);
    p.mass = 0;
    double int_mass = 0;
    for(Composition::iterator j = p.comp.begin(); 
	j != p.comp.end(); j++) {
      iso_abundancy ia = *j;
      int_mass += ad[ia.elem_index][ia.iso_index].int_mass * ia.weight;
      p.mass += ad[ia.elem_index][ia.iso_index].mass * ia.weight;
    }
    p.mass *= p.int_mass;
    p.mass /= int_mass;
    if(charge > 0)
      p.mass = p.mass / abs(charge) - ELECTRON_MASS;
    else if(charge < 0)
      p.mass = p.mass / abs(charge) + ELECTRON_MASS;
  }
}


int main(int argc, char * argv[])
{
  init_data("ISOTOPE.DAT", ad, em);
  
  int digits = 6;
  double limit = 0.0;
  int opt;
  while((opt = getopt(argc, argv, "d:l:")) != -1) {
    if(opt == 'd') {
      digits = atoi(optarg);
      if(digits < 1)
	digits = 1;
      if(digits > 30)
	digits = 30;
    } else if(opt == 'l') {
      limit = atof(optarg);
      if(limit < 0)
	limit = 0;
    }
    else
      return 2;
  }

  Parser p(em);

  FormMap fm;

  Pattern result;

  wstring line;
  while(getline(wcin, line)) {

    size_t sep_pos = line.find(L',');
    long charge = 0;
    if(sep_pos < line.size() - 1) {
      wstring charge_str = wstring(line, sep_pos + 1, line.size());
      charge = wcstol(charge_str.c_str(), NULL, 0);
    }

    wstring formula(line, 0, sep_pos);
    wcout << L"formula: " << formula 
	  << L" charge : " << charge 
	  << L" limit: " << limit
	  << endl;

    // parse the formula
    fm.clear();
    try {
      p.write_compound(formula, fm);
    } catch (Parser::Error e) {
      wcerr << e._message;
      continue; // skip to next compound
    }
    if(!isRealFormula(fm)) {
      wcerr << L"Bad formula: " << formula << endl;
      continue; // skip to next compound
    }

    calculate(result, fm, charge, limit);
    print_pattern(result, digits);   
  }

  return 0;
}
