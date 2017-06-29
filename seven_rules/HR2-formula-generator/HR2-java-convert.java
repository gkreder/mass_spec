public class GlobalMembersProcess
{

//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execl(String path, String argv0, Object... ParamArray);
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: int execle(const char *path, const char *argv0, ... /*, char * const *envp */);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execle(String path, String argv0, Object... ParamArray);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execlp(String path, String argv0, Object... ParamArray);
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: int execlpe(const char *path, const char *argv0, ... /*, char * const *envp */);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execlpe(String path, String argv0, Object... ParamArray);

//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execv(String path, RefObject<String * const> argv);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execve(String path, RefObject<String * const> argv, RefObject<String * const> envp);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execvp(String path, RefObject<String * const> argv);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int execvpe(String path, RefObject<String * const> argv, RefObject<String * const> envp);

//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnl(int mode, String path, String argv0, Object... ParamArray);
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: int spawnle(int mode, const char *path, const char *argv0, ... /*, char * const *envp */);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnle(int mode, String path, String argv0, Object... ParamArray);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnlp(int mode, String path, String argv0, Object... ParamArray);
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: int spawnlpe(int mode, const char *path, const char *argv0, ... /*, char * const *envp */);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnlpe(int mode, String path, String argv0, Object... ParamArray);

//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnv(int mode, String path, RefObject<String const> argv);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnve(int mode, String path, RefObject<String const> argv, RefObject<String const> envp);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnvp(int mode, String path, RefObject<String const> argv);
//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int spawnvpe(int mode, String path, RefObject<String const> argv, RefObject<String const> envp);

//C++ TO JAVA CONVERTER TODO TASK: The implementation of the following method could not be found:
	//int cwait(int NamelessParameter1, int NamelessParameter2, int NamelessParameter3);

	//#define _P_WAIT 1
	//#define _P_NOWAIT 2
	//#define _P_OVERLAY 3
	//#define _P_NOWAITO 4
	//#define _P_DETACH 5

	//#define WAIT_CHILD 1

	//C++ TO JAVA CONVERTER TODO TASK: There is no preprocessor in Java:
	//#if __cplusplus
	}
	//#endif

	//#endif


	// --- atomic masses as published by IUPAC, 2002-10-02 ----------

	// array of the elements used here:
	//   Symbol, exact mass, dbe, keycode, number, default-min, default-max
	//
	public static Element[] el = { { "C", 12.000000000, +2.0, 'C', 0, 41, 0,0 }, { "13C", 13.0033548378, +2.0, '1', 0, 0, 0,0 }, { "H", 1.0078250321, -1.0, 'H', 0, 72, 0,0}, { "D", 2.0141017780, -1.0, 'D', 0, 0, 0,0}, { "N", 14.0030740052, +1.0, 'N', 0, 34, 0,0 }, { "15N", 15.0001088984, +1.0, 'M', 0, 0, 0,0 }, { "O", 15.9949146221, 0.0, 'O', 0, 30, 0,0}, { "F", 18.99840320, -1.0, 'F', 0, 0, 0,0}, { "Na", 22.98976967, -1.0, 'A', 0, 0, 0,0}, { "Si", 27.9769265327, +2.0, 'I', 0, 0, 0,0}, { "P", 30.97376151, +3.0, 'P', 0, 0, 0,0}, { "S", 31.97207069, +4.0, 'S', 0, 0, 0,0}, { "Cl", 34.96885271, -1.0, 'L', 0, 0, 0,0}, { "Br", 78.9183376, -1.0, 'B', 0, 0, 0,0}};

	public static final double electron = 0.000549; // mass of the electron in amu


	// --- global variables ---

	public static double charge; // mass tolerance in mmu
	public static double tol;
	public static String comment =""; // some text ;-)
	public static int single; // flag to indicate if we calculate only once and exit
	public static int nr_el; // number of elements in array (above)


	// --- some variables needed for reading the cmd line ---

	public static String optarg; // global: pointer to argument of current option
	static int optind = 1; // global: index of which argument is next. Is used

//**************************************************************************
//* INPUT:	reads a dataset in "dialog mode".			   *
//* Input: 	Pointer to comment text, pointer to mass.		   *
//* Returns:	Result of sscanf(), 0 if prog is to be finished. 	   *
//* Note:		This is a fairly primitive way to do it, but it works ;-)  *
//***************************************************************************
	//                as a global variable for collection of further
	//                arguments (= not options) via argv pointers.


	// --- function prototypes -------------------

	public static int input(RefObject<String> txt, RefObject<Double> zahl)
	{
	String buf = new String(new char[DefineConstantsProcess.MAXLEN]); // input line

//C++ TO JAVA CONVERTER TODO TASK: The following line could not be converted:
*zahl = 0.0;

	System.out.print("Comment             : "); // display prompt
	fgets(buf, DefineConstantsProcess.MAXLEN-1, stdin); // read line
	buf = StringHelper.changeCharacter(buf, DefineConstantsProcess.MAXLEN, 0x0); // terminate string
	RefObject<String> TempRefObject = new RefObject<String>(buf);
	clean (TempRefObject); // remove linefeed
	buf = TempRefObject.argvalue;
	txt.argvalue = buf; // copy text over

	System.out.print("Mass (ENTER to quit): "); // display prompt
	fgets(buf, DefineConstantsProcess.MAXLEN-1, stdin); // read line
	buf = StringHelper.changeCharacter(buf, DefineConstantsProcess.MAXLEN, 0x0); // terminate string
	if (clean (buf) == 0) // only a CR ? --> quit
		return 0;
	sscanf(buf,"%lf", zahl.argvalue); // scan string

	return 1;
	}

//**************************************************************************
//* READFILE:	reads dataset from file.				   *
//* Input: 	Pointer to comment text, pointer to mass.		   *
//* Returns:	0 if OK, 1 if error.					   *
//***************************************************************************
	public static int readfile(RefObject<String> whatfile)
	{
	double mz; // measured mass
	String buf = new String(new char[DefineConstantsProcess.MAXLEN]); // input line
	FILE infile;

	infile = fopen(whatfile.argvalue, "r");
	if (null == infile)
		{
		fprintf (stderr, "Error: Cannot open %s.", whatfile.argvalue);
		return 1;
		}

	while (fgets(buf, DefineConstantsProcess.MAXLEN-1, infile))
		{
		buf = StringHelper.changeCharacter(buf, DefineConstantsProcess.MAXLEN, 0x0); // terminate string
		if (*buf.equals(';')) // comment line
			continue;
		if (clean (buf) == 0) // only a CR ? --> quit
			return 0;
		sscanf(buf, "%s %lf", comment, mz); // scan string
		do_calculations(mz, tol);
		mz = 0.0; // reset
		}
	return 0;
	}

//***********************************************************************
//* CALC_MASS:	Calculates mass of an ion from its composition.	  	*
//* Input: 	nothing (uses global variables) 	      		*
//* Returns. 	mass of the ion.	  				*
//* Note:		Takes care of charge and electron mass!   		*
//* 		(Positive charge means removal of electrons).	 	*
//************************************************************************
	public static double calc_mass()
	{
	int i;
	double sum = 0.0;

	for (i =0; i < nr_el; i++)
		sum += el[i].mass * el[i].cnt;

	return (sum - (charge * electron));
	}

//***********************************************************************
//* CALC_RDB:	Calculates rings & double bond equivalents.    		*
//* Input: 	nothing (uses global variables)			   	*
//* Returns. 	RDB.				       			*
//************************************************************************
	public static float calc_rdb()
	{
	int i;
	float sum = 2.0;

	for (i =0; i < nr_el; i++)
		sum += el[i].val * el[i].cnt;

	return (sum/2.0);
	}

//***********************************************************************
//* DO_CALCULATIONS: Does the actual calculation loop.			*
//* Input: 	   measured mass (in amu), tolerance (in mmu)	    	*
//* Returns. 	   number of hits.	       				*
//************************************************************************
	public static int do_calculations(double measured_mass, double tolerance)
	{
	time_t start;
	time_t finish;
	double elapsed_time;

	double mass; // calc'd mass
	double limit_lo; // mass limits
	double limit_hi;
	float rdb; // Rings & double bonds
	float lewis;
	int i;
	long hit; // counts the hits, with long declaration, overflow after 25h with all formulas < 2000 Da
	//							    long = FFFFFFFFh = 4,294,967,295d
	long counter;
	boolean elementcheck;
	boolean set_break;


	time(start); // start time
	System.out.print("\n"); // linefeed

	// calculate limits

	limit_lo = measured_mass - (tolerance / 1000.0);
	limit_hi = measured_mass + (tolerance / 1000.0);

	if (comment.length()) // print only if there is some text to print
		System.out.printf ("Text      \t%s\n", comment);

	System.out.print ("Composition\t");
	for (i =0; i < nr_el; i++)
		if (el[i].max > 0)
			System.out.printf("%s:%d-%d ", el[i].sym, el[i].min, el[i].max);
	System.out.print ("\n");

	System.out.printf ("Tol (mmu)\t%.1f\n",tolerance);
	System.out.printf ("Measured\t%.4lf\n", measured_mass);
	System.out.printf ("Charge  \t%+.1lf\n", charge);

	hit = 0; // Reset counter
	counter = 0;
	set_break = false; // set breaker for element counts to false

	// Now let's run the big big loop ... I'd like to do that
	//   recursively but did not yet figure out how ;-)
	//   TK Adds: the loop is just fine.
	//

	// now comes the "COOL trick" for calculating all formulae:
	//sorting the high mass elements to the outer loops, the small weights (H)
	//to the inner loops;
	//
	//This will reduce the computational time by factor ~10-60-1000
	//OLD HR: Cangrelor at 1ppm  4465 formulas found in   5866 seconds.
	//NEW HR2: Cangrelor at 1ppm 4465 formulas found in     96 seconds.
	//NEW2 HR2: Cangrelor at 1ppm 4465 formulas found in     60 seconds.
	//NEW3 HR2: Cangrelor at 1ppm 4465 formulas found in     59 seconds.
	//HR2 Fast: Cangrelor at 1ppm 4465 formulas found in     41 seconds by evaluating 2,003,436,894 formulae.
	//hr2 -c "Cangrelor" -m  774.948 -t 0.77 -C 1-64 -H 1-112 -N 0-30 -O 0-80 -P 0-12 -S 0-9 -F 0-10 -L 0-10
	//
	//Another additional trick is to end the 2nd.. 3rd.. 4th.. xth innermost loop
	//to prevent loops which are just higher and higher in mass.
	//

	el[13].cnt = el[13].min - 1;
	el[13].save = el[13].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[13].cnt++ < el[13].max) /* "Br"*/ {
	while (el[13].cnt++ < el[13].max)
	{

	el[12].cnt = el[12].min - 1;
	el[12].save = el[12].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[12].cnt++ < el[12].max) /*"Cl"*/ {
	while (el[12].cnt++ < el[12].max)
	{

	el[11].cnt = el[11].min - 1;
	el[11].save = el[11].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[11].cnt++ < el[11].max) /*"S"*/ {
	while (el[11].cnt++ < el[11].max)
	{

	el[10].cnt = el[10].min - 1;
	el[10].save = el[10].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[10].cnt++ < el[10].max) /*"P"*/ {
	while (el[10].cnt++ < el[10].max)
	{

	el[9].cnt = el[9].min - 1;
	el[9].save = el[9].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[9].cnt++ < el[9].max) /*"Si"*/ {
	while (el[9].cnt++ < el[9].max)
	{

	el[8].cnt = el[8].min - 1;
	el[8].save = el[8].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[8].cnt++ < el[8].max) /*"Na"*/{
	while (el[8].cnt++ < el[8].max)
	{

	el[7].cnt = el[7].min - 1;
	el[7].save = el[7].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[7].cnt++ < el[7].max) /*"F"*/ {
	while (el[7].cnt++ < el[7].max)
	{

	el[6].cnt = el[6].min - 1;
	el[6].save = el[6].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[6].cnt++ < el[6].max) /*"O"*/ {
	while (el[6].cnt++ < el[6].max)
	{

	el[5].cnt = el[5].min - 1;
	el[5].save = el[5].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[5].cnt++ < el[5].max) /*"15N"*/{
	while (el[5].cnt++ < el[5].max)
	{

	el[4].cnt = el[4].min - 1;
	el[4].save = el[4].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[4].cnt++ < el[4].max) /*"N"*/{
	while (el[4].cnt++ < el[4].max)
	{

	el[1].cnt = el[1].min - 1;
	el[1].save = el[1].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[1].cnt++ < el[1].max) /*"13C"*/ {
	while (el[1].cnt++ < el[1].max)
	{

	el[0].cnt = el[0].min - 1;
	el[0].save = el[0].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[0].cnt++ < el[0].max) /* "C"*/ {
	while (el[0].cnt++ < el[0].max)
	{

	el[3].cnt = el[3].min - 1;
	el[3].save = el[3].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[3].cnt++ < el[3].max) /*"D"*/{
	while (el[3].cnt++ < el[3].max)
	{

	el[2].cnt = el[2].min - 1;
	el[2].save = el[2].cnt;
	//C++ TO JAVA CONVERTER NOTE: Embedded comments are not maintained by C++ to Java Converter
	//ORIGINAL LINE: while (el[2].cnt++ < el[2].max) /*"H"*/{
	while (el[2].cnt++ < el[2].max)
	{

		mass = calc_mass();
		counter++;

		//just for debug purposes
		//if (mass > limit_hi)
		//printf("mass: %f\tC: %d  H: %d  N: %d O: %d P: %d S: %d Cl: %d Br: %d\n",mass,el[0].cnt,el[2].cnt,el[4].cnt,el[6].cnt,el[10].cnt,el[11].cnt,el[12].cnt,el[13].cnt);

	//     if we exceed the upper limit, we can stop the calculation
	//       for this particular element (JHa 20050227). <-- comment TK that will only bust the innermost while loop, which is "H"

		// break H loop
		if (mass > limit_hi)
			break;

		//************************************************************************************************************/
		//Calculus loop with print out
		//************************************************************************************************************/

		if ((mass >= limit_lo) && (mass <= limit_hi)) // within limits?
		{
			// element check will be performed always, if variable bool element_probability is true also probabilities will be calculated
			// not an elegant implementation, but fast.
			 elementcheck = calc_element_ratios(true);
			 if (elementcheck)
		{
		rdb = calc_rdb(); // get RDB
		lewis = (float)(Math.IEEEremainder(rdb, 1)); //calc reminder
		if ((rdb >= 0) && (lewis != 0.5) && (lewis !=-0.5)) // less than -0.5 RDB does not make sense
			{ // NO(!) CH3F10NS2 exists , RDB = -4.0 M= 282.9547
			hit ++;
			for (i = 0; i < nr_el; i++) // print composition
				if (el[i].cnt > 0) // but only if useful

				 //! comment the following two printlines and add a single ; in a free line for the counting version

				  System.out.printf("%s%d.", el[i].sym, el[i].cnt); // print formula
				  System.out.printf("\t\t%.1f\t%.4lf\t%+.1lf mmu \n", rdb, mass, 1000.0 * (measured_mass - mass));

			} // end of 'rdb' loop
		} // end of elementcheck loop

		} // end of 'limit' loop
		//************************************************************************************************************/


	//
	//	TK: if the current mass is larger than the limit the loop can be exited.
	//	Each element must point to the element which is in use and before.
	//	This is a static implementation which can be enhanced with a pointer chain to the lower element.
	//	Actually now its only allowed for CHNSOP-Fl-Cl-Br-Si !!! Brute-force <> elegance :-)
	//
			} //"H"

			} //"D"

			if ((mass >= limit_lo) && (el[2].save == el[2].cnt-1))
				break;
			} // "C"

			} //"13C"

			if ((mass >= limit_lo) && (el[0].save == el[0].cnt-1))
				break;
			} //"N"

			} //"15N"

			if ((mass >= limit_lo) && (el[4].save == el[4].cnt-1))
				break;
			} //"O"

			if ((mass >= limit_lo) && (el[6].save == el[6].cnt-1))
				break;
			} //"F"

			} //"Na"

			if ((mass >= limit_lo) && (el[7].save == el[7].cnt-1))
				break;
			} //"Si"

			if ((mass >= limit_lo) && (el[9].save == el[9].cnt-1))
				break;
			} //"P"

			if ((mass >= limit_lo) && (el[10].save == el[10].cnt-1))
				break;
			} //"S"

			if ((mass >= limit_lo) && (el[11].save == el[11].cnt-1))
				break;
			} //"Cl"

			if ((mass >= limit_lo) && (el[12].save == el[12].cnt-1))
				break;
			} //"Br" ends
	// close that giant loop thing started above




	time(finish); // stop timer
	elapsed_time = difftime(finish, start); // calulate time difference

	if (hit == 0)
		System.out.printf("No matching combination found in %6.0f seconds.\n", elapsed_time);
	else
		System.out.printf("\n%llu formulas found in %6.0f seconds by evaluating %llu formulae.\n",hit,elapsed_time,counter);
		System.out.print("RDBs are overloaded to maximum valence values (N=3,P=5,S=6).\n");

	return hit;
	}

//***********************************************************************
//* CLEAN:	"cleans" a buffer obtained by fgets() 			*
//* Input: 	Pointer to text buffer					*
//* Returns:	strlen of buffer.   					*
//************************************************************************
	public static int clean(RefObject<String> buf)
	{
	int i;

	for(i = 0; i < buf.argvalue.length(); i++) // search for CR/LF
		{
		if(buf.argvalue.charAt(i) == '\n' || buf.argvalue.charAt(i) == '\r')
			{
			buf.argvalue = buf.argvalue.substring(0, i); // stop at CR or LF
			break;
			}
		}
	return (buf.argvalue.length());
	}

//**************************************************************************
//* GETOPT: Command line parser, system V style.
//*
//*  This routine is widely (and wildly) adapted from code that was
//*  made available by Borland International Inc.
//*
//*  Standard option syntax is:
//*
//*    option ::= SW [optLetter]* [argLetter space* argument]
//*
//*  where
//*    - SW is '-'
//*    - there is no space before any optLetter or argLetter.
//*    - opt/arg letters are alphabetic, not punctuation characters.
//*    - optLetters, if present, must be matched in optionS.
//*    - argLetters, if present, are found in optionS followed by ':'.
//*    - argument is any white-space delimited string.  Note that it
//*      can include the SW character.
//*    - upper and lower case letters are distinct.
//*
//*  There may be multiple option clusters on a command line, each
//*  beginning with a SW, but all must appear before any non-option
//*  arguments (arguments not introduced by SW).  Opt/arg letters may
//*  be repeated: it is up to the caller to decide if that is an error.
//*
//*  The character SW appearing alone as the last argument is an error.
//*  The lead-in sequence SWSW ("--") causes itself and all the rest
//*  of the line to be ignored (allowing non-options which begin
//*  with the switch char).
//*
//*  The string *optionS allows valid opt/arg letters to be recognized.
//*  argLetters are followed with ':'.  Getopt () returns the value of
//*  the option character found, or EOF if no more options are in the
//*  command line. If option is an argLetter then the global optarg is
//*  set to point to the argument string (having skipped any white-space).
//*
//*  The global optind is initially 1 and is always left as the index
//*  of the next argument of argv[] which getopt has not taken.  Note
//*  that if "--" or "//" are used then optind is stepped to the next
//*  argument before getopt() returns EOF.
//*
//*  If an error occurs, that is an SW char precedes an unknown letter,
//*  then getopt() will return a '~' character and normally prints an
//*  error message via perror().  If the global variable opterr is set
//*  to false (zero) before calling getopt() then the error message is
//*  not printed.
//*
//*  For example, if
//*
//*    *optionS == "A:F:PuU:wXZ:"
//*
//*  then 'P', 'u', 'w', and 'X' are option letters and 'A', 'F',
//*  'U', 'Z' are followed by arguments. A valid command line may be:
//*
//*    aCommand  -uPFPi -X -A L someFile
//*
//*  where:
//*    - 'u' and 'P' will be returned as isolated option letters.
//*    - 'F' will return with "Pi" as its argument string.
//*    - 'X' is an isolated option.
//*    - 'A' will return with "L" as its argument.
//*    - "someFile" is not an option, and terminates getOpt.  The
//*      caller may collect remaining arguments using argv pointers.
//**************************************************************************
//C++ TO JAVA CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Java):
private String letP = null;
//C++ TO JAVA CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Java):
private char SW = '-';
	public static int getopt(int argc, RefObject<String[]> argv, RefObject<String> optionS)
	{
	//C++ TO JAVA CONVERTER NOTE: This static local variable declaration (not allowed in Java) has been moved just prior to the method:
	//static char *letP = null; // remember next option char's location
	//C++ TO JAVA CONVERTER NOTE: This static local variable declaration (not allowed in Java) has been moved just prior to the method:
	//static char SW = '-'; // switch character

	int opterr = 1; // allow error message
	byte ch;
//C++ TO JAVA CONVERTER TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged.
	char *optP;

	if (argc > optind)
		{
		if (letP.equals(null))
			{
			if ((letP = argv.argvalue.charAt(optind)) == null || *(letP++) != SW)
//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
				goto gopEOF;

			if ( letP.equals(SW))
				{
				optind++;
//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
				goto gopEOF;
				}
			}
		if (0 == (ch = *(letP++)))
			{
			optind++;
//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
			goto gopEOF;
			}
		if (':' == ch || (optP = SimulateStringFunctions.strChr(optionS.argvalue, ch)) == null)
//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
			goto gopError;
		if (':' == *(++optP))
			{
			optind++;
			if (0 == letP)
				{
				if (argc <= optind)
//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
					goto gopError;
				letP = argv.argvalue.charAt(optind++);
				}
			optarg = letP;
			letP = null;
		}
		else
		{
		if (0 == letP)
			{
			optind++;
			letP = null;
			}
		optarg = null;
		}
		return ch;
	}

//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
	gopEOF:
		optarg = letP = null;
		return EOF;

//C++ TO JAVA CONVERTER TODO TASK: There are no gotos or labels in Java:
	gopError:
		optarg = null;
		errno = EINVAL;
		if (opterr != 0)
			perror ("Command line option");
		return ('~');
	}
//***********************************************************************
//* Calculates element ratios , CH2 (more than 8 electrons needed is not handled)
//* Calculations element probabilities if element_probability = true
//* Input: 	nothing (uses global variables)
//* Returns. true/false.
//************************************************************************
	//you have to compile with C++ or define yourself this bool type (C99 compiler definition)
	public static boolean calc_element_ratios(boolean element_probability)
	{
	boolean CHNOPS_ok;
	float HC_ratio;
	float NC_ratio;
	float OC_ratio;
	float PC_ratio;
	float SC_ratio;

	float C_count = (float)el[0].cnt;
	float H_count = (float)el[2].cnt;
	float N_count = (float)el[4].cnt;
	float O_count = (float)el[6].cnt;
	float P_count = (float)el[10].cnt;
	float S_count = (float)el[11].cnt;


	//         ELEMENT RATIOS allowed
	//			MIN		MAX (99.99%)
	//		H/C	0.07	6.00
	//		N/C	0.00	4.00
	//		O/C	0.00	3.00
	//		P/C	0.00	2.00
	//		S/C	0.00	6.00
	//

		// set CHNOPS_ok = true and assume all ratios are ok
		CHNOPS_ok = true;


		if (C_count && H_count >0) // C and H must have one count anyway (remove for non-organics//
		{
			HC_ratio = H_count/C_count;
			if (element_probability)
			{
				if ((HC_ratio < 0.2) || (HC_ratio > 3.0)) // this is the H/C probability check ;
				CHNOPS_ok = false;
			}
			else if (HC_ratio > 6.0) // this is the normal H/C ratio check - type cast from int to float is important
				CHNOPS_ok = false;
		}

		if (N_count >0) // if positive number of nitrogens then thes N/C ratio else just calc normal
		{
			NC_ratio = N_count/C_count;
			if (element_probability)
			{
				if (NC_ratio > 2.0) // this is the N/C probability check ;
				CHNOPS_ok = false;
			}
			else if (NC_ratio > 4.0)
				CHNOPS_ok = false;
		}

		if (O_count >0) // if positive number of O then thes O/C ratio else just calc normal
		{
			OC_ratio = O_count/C_count;
			if (element_probability)
			{
				if (OC_ratio > 1.2) // this is the O/C probability check ;
				CHNOPS_ok = false;
			}
			else if (OC_ratio > 3.0)
					CHNOPS_ok = false;
		}


		if (P_count >0) // if positive number of P then thes P/C ratio else just calc normal
		{
			PC_ratio = P_count/C_count;
			if (element_probability)
			{
				if (PC_ratio > 0.32) // this is the P/C probability check ;
				CHNOPS_ok = false;

			}
			else if (PC_ratio > 6.0)
				CHNOPS_ok = false;
		}

		if (S_count >0) // if positive number of S then thes S/C ratio else just calc normal
		{
			SC_ratio = S_count/C_count;
			if (element_probability)
			{
				if (SC_ratio > 0.65) // this is the S/C probability check ;
				CHNOPS_ok = false;
			}
			else if (SC_ratio > 2.0)
				CHNOPS_ok = false;
		}

	//-----------------------------------------------------------------------------

		// check for multiple element ratios together with probability check
		//if N<10, O<20, P<4, S<3 then true
		if (element_probability && (N_count > 10) && (O_count > 20) && (P_count > 4) && (S_count > 1))
			CHNOPS_ok = false;

		// NOP check for multiple element ratios together with probability check
		// NOP all > 3 and (N<11, O <22, P<6 then true)
		if (element_probability && (N_count > 3) && (O_count > 3) && (P_count > 3))
			{
			if (element_probability && (N_count > 11) && (O_count > 22) && (P_count > 6))
				CHNOPS_ok = false;
			}

		// OPS check for multiple element ratios together with probability check
		// O<14, P<3, S<3 then true
		if (element_probability && (O_count > 14) && (P_count > 3) && (S_count > 3))
			CHNOPS_ok = false;

		// PSN check for multiple element ratios together with probability check
		// P<3, S<3, N<4 then true
		if (element_probability && (P_count > 3) && (S_count > 3) && (N_count >4))
			CHNOPS_ok = false;


		// NOS check for multiple element ratios together with probability check
		// NOS all > 6 and (N<19 O<14 S<8 then true)
		if (element_probability && (N_count >6) && (O_count >6) && (S_count >6))
		{
			if (element_probability && (N_count >19) && (O_count >14) && (S_count >8))
				CHNOPS_ok = false;
		}


		// function return value;
		if (CHNOPS_ok == true)
			return true;
		else
			return false;
	}

	// --- threading -------------------
	// mass and RDB calculation could be in several other threads
	//however the loop is very fast, context switching takes longer and
	//slows down the whole process. Single-Thread multiprocessor (cluster) implementation
	//seems superior here.
	//
	public static HANDLE hThread2;
	public static HANDLE hThread3;
	public static int threadID2;
	public static int threadID3;
//C++ TO JAVA CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Java):
private static char *id = "hr version %s. Copyright (C) by Joerg Hau 2001...2005 & Tobias Kind 2006 :-).\n";
//C++ TO JAVA CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Java):
private static char *disclaimer = "\nThis program is free software; you can redistribute it and/or modify it under\n" + "the terms of version 2 of the GNU General Public License as published by the\n" + "Free Software Foundation.\n\n" + "This program is distributed in the hope that it will be useful, but WITHOUT ANY\n" + "WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A\n" + "PARTICULAR PURPOSE. See the GNU General Public License for details.\n";
//C++ TO JAVA CONVERTER NOTE: This was formerly a static local variable declaration (not allowed in Java):
private static char *msg = "Calculates possible elemental compositions for a given mass.\n\n" + "usage: hr [options] file\n\nValid command line options are:\n" + "-h      This Help screen.\n" + "-v      Display version information.\n" + "-t tol  Set tolerance to 'tol' mmu (default 5).\n" + "-m mz   Set mass to 'mz'.\n" + "-c txt  Set comment to 'txt' (only useful together with '-m').\n" + "-p      Positive ions; electron mass is removed from the formula.\n" + "-n      Negative ions; electron mass is added to the formula.\n" + "-X a-b  For element X, use atom range a to b. List of valid atoms:\n\n" + "           X    key   mass (6 decimals shown)\n" + "        -------------------------------------\n";


	// --- main ---

	static int Main(int argc, RefObject<String[]> argv)
	{
	double mz; // mass
	String buf = new String(new char[DefineConstantsProcess.MAXLEN]);
	int i;
	int tmp;

	//C++ TO JAVA CONVERTER NOTE: This static local variable declaration (not allowed in Java) has been moved just prior to the method:
	//static char *id = "hr version %s. Copyright (C) by Joerg Hau 2001...2005 & Tobias Kind 2006 :-).\n";

	//C++ TO JAVA CONVERTER NOTE: This static local variable declaration (not allowed in Java) has been moved just prior to the method:
	//static char *disclaimer = "\nThis program is free software; you can redistribute it and/or modify it under\n" + "the terms of version 2 of the GNU General Public License as published by the\n" + "Free Software Foundation.\n\n" + "This program is distributed in the hope that it will be useful, but WITHOUT ANY\n" + "WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A\n" + "PARTICULAR PURPOSE. See the GNU General Public License for details.\n";

	//C++ TO JAVA CONVERTER NOTE: This static local variable declaration (not allowed in Java) has been moved just prior to the method:
	//static char *msg = "Calculates possible elemental compositions for a given mass.\n\n" + "usage: hr [options] file\n\nValid command line options are:\n" + "-h      This Help screen.\n" + "-v      Display version information.\n" + "-t tol  Set tolerance to 'tol' mmu (default 5).\n" + "-m mz   Set mass to 'mz'.\n" + "-c txt  Set comment to 'txt' (only useful together with '-m').\n" + "-p      Positive ions; electron mass is removed from the formula.\n" + "-n      Negative ions; electron mass is added to the formula.\n" + "-X a-b  For element X, use atom range a to b. List of valid atoms:\n\n" + "           X    key   mass (6 decimals shown)\n" + "        -------------------------------------\n";

	// initialise variables

	single = DefineConstantsProcess.FALSE; // run continuously
	charge = 0.0; // default charge is neutral
	tol = 5.0; // default tolerance in mmu
//C++ TO JAVA CONVERTER TODO TASK: There is no Java equivalent to 'sizeof':
	nr_el = sizeof(el)/sizeof(el[0]); // calculate array size


	// decode and read the command line

	while ((tmp = getopt(argc, argv, "hvpnt:m:c:C:H:N:M:O:D:1:S:F:L:B:P:I:A:")) != EOF)
		switch (tmp)
			{
			case 'h': // help me
				printf (id, DefineConstantsProcess.VERSION);
				System.out.print (msg);
				for (i =0; i < nr_el; i++)
					System.out.printf ("        %4s     -%c %15.6lf\n", el[i].sym, el[i].key, el[i].mass);
				printf(disclaimer, "\n");
				return 0;
			case 'v': // version
				printf (id, DefineConstantsProcess.VERSION);
				return 0;
			case 'p': // positive charge
				charge = +1.0;
				continue;
			case 'n': // negative carge
				charge = -1.0;
				continue;
			case 't': // tolerance
				buf = optarg;
				sscanf(buf, "%lf", tol);
				continue;
			case 'm': // single mass
				buf = optarg;
					sscanf(buf, "%lf", mz);
					single = DefineConstantsProcess.TRUE;
					continue;
			case 'c': // comment for single mass
				   comment = optarg;
					continue;
			case 'C': // C12
			 case 'H': // 1H
			case 'N': // 14N
			case 'M': // 15N
			case 'O': // 16O
			 case 'D': // 2H
			 case '1': // 13C
			case 'A': // Na ('N' is taken for Nitrogen!)
			case 'S': // 32S
			case 'F': // 19F
			case 'L': // 35Cl ('C' is taken!)
			case 'B': // 79Br
			case 'P': // 31P
			case 'I': // 28Si ('S' is taken!)
				i = 0;
				// compare keys until found
				while ((i < nr_el) && (el[i].key != tmp))
					i++;
				buf = optarg;
				sscanf(buf, "%d-%d", el[i].min, el[i].max); // copy over
				if (el[i].min > el[i].max) // swap them
					{
					tmp = el[i].min;
					el[i].min = el[i].max;
					el[i].max = tmp;
					}

	//             printf ("\n %c = %c ... %s (%d-%d)", \
	//			tmp, el[i].key, el[i].sym, el[i].min, el[i].max);
				continue;
			case '~': // invalid arg
			default:
				System.out.printf ("'%s -h' for help.\n", argv.argvalue.charAt(0));
				return 1;
			}

	if (argv.argvalue.charAt(optind) != null) // remaining parameter on cmd line?
		// must be a file -- treat it line by line
		return readfile (argv.argvalue.charAt(optind));

	if (single == DefineConstantsProcess.TRUE) // only one calculation requested?
		do_calculations(mz, tol); // do it, then exit ...
	else
		{ // otherwise run a loop
		while input(comment, mz)
			{
			tmp = do_calculations(mz, tol);
			System.out.print("\n");
			}
		}

	return 0;
	}
}
//
//
// HR2.C
// V1.02
//
// A program to calculate elemental compositions for a given mass.
// See the file README for details.
//
//--------------------------------------------------------------------
// Copyright (c) 2001...2005 Joerg Hau <joerg.hau(at)dplanet.ch>.
//
// mail: joerg.hau@dplanet.ch
// www:  http://www.mysunrise.ch/users/joerg.hau/
//
// *changed version by Tobias Kind (TK), 2006 , Fiehnlab,
// *added extended valencies, added implementation of
//  seven golden rules of molecular formula filtering
//
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of version 2 of the GNU General Public
// License as published by the Free Software Foundation. See the
// file LICENSE for details.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//--------------------------------------------------------------------
//
// Creation:	somewhere in 1992 by JHa.
// Revision:  2001-04-18, GPL'd, first public release (JHa)
//            2001-04-21, improved help text (JHa)
//            2002-06-27, added sodium (JHa)
//            2002-10-09, added 15N (JHa)
//            2005-02-25, added -v option; license now GPL *v2* (JHa)
//            2005-02-27, optimised code in calc loop (JHa)
//            2005-02-28, verified and updated atomic masses (JHa)
//            2005-06-17, added GPL text when "-h" is used (JHa)
//			2006-01-01, extended version for BMC Bioinformatics publication - HR2 (TK)
//			2006-03-03, added element ratio checks, extended valencies, only even electrons - HR2 (TK)
//			2006-09-09,	1000x-10000x speedup hand optimized hehe. - HR2 (TK)
//						-->special version for CHNSOP-F-Cl-Br-Si
//
// This is ANSI C and should compile with any C compiler; use
// something along the lines of "gcc -Wall -O3 -o hr hr.c".
// Optimize for speed, you may gain factor 3!
// NOW compiled under Visual C++ Express (faster than GCC) in C++ mode for boolean type.
//
//
// ---------------------------------------------------------------------
// Example arguments:
// 1) -m 1 -t 100000 -C 1-100 -H 1-220 -N 0-10 -O 0-10 -P 0-10 -S 0-10 -L 0-10 -B 0-10
// 2) -m 500 -t 1 -C 50-100 -H 10-220 -N 0-10 -O 0-10 -P 0-10 -S 0-10 -L 0-10 -B 0-10
// 3) hr2-all-res -c "Hexaflumuron_459.982882Da_3ppm" -m 459.982882 -t 1.37995 -C 0-39 -H 0-98 -N 0-34 -O 0-30 -P 0-12 -S 0-12 -F 0-12 -L 0-14 -B 0-7 -I 0-0
//	945 formulas found in    253 seconds. (now 4 seconds, before eternal)
// 4) hr2 -m 459.982882 -t 1.37995 -C 10-39 -H 28-98 -N 4-34 -O 0-30 -P 1-12 -S 1-12 -F 0-12 -L 1-14 -B 2-6 -I 0-0
//	1 formula in 0 seconds (former eternal time)
//

// process.h.  This file comes with MSDOS and WIN32 systems.

//C++ TO JAVA CONVERTER TODO TASK: There is no preprocessor in Java:
//#if ! __PROCESS_H_
//#define __PROCESS_H_

//C++ TO JAVA CONVERTER TODO TASK: There is no preprocessor in Java:
//#if __cplusplus
//C++ TO JAVA CONVERTER TODO TASK: Extern blocks are not supported in Java.
extern "C"
{
//#endif



//#define VERSION "20050617"
//#define TRUE 1
//#define FALSE 0
//#define MAXLEN 181

//#define _CRT_SECURE_NO_DEPRECATE 1

public class Element
{
		public String sym; // symbol
		public static final double mass; // accurate mass
		public static final float val; // to calculate unsaturations
		public static final int key; // used for decoding cmd line
		public int min; // atom count old - for loop exiting
		public int max;
		public int cnt;
		public int save;
}

//
//List of elements sorted according to mass
//_______________________
//INo#	El	Mass
//2		H	1.007825032
//3		D	2.014101778
//0		C	12
//1		13C	13.00335484
//4		N	14.00307401
//5		15N	15.0001089
//6		O	15.99491462
//7		F	18.9984032
//8		Na	22.98976967
//9		Si	27.97692653
//10		P	30.97376151
//11		S	31.97207069
//12		Cl	34.96885271
//13		Br	78.9183376
//------------------------
//

final class DefineConstantsProcess
{
	public static final int _P_WAIT = 1;
	public static final int _P_NOWAIT = 2;
	public static final int _P_OVERLAY = 3;
	public static final int _P_NOWAITO = 4;
	public static final int _P_DETACH = 5;
	public static final int WAIT_CHILD = 1;
	public static final String VERSION = "20050617";
	public static final int TRUE = 1;
	public static final int FALSE = 0;
	public static final int MAXLEN = 181;
	public static final int _CRT_SECURE_NO_DEPRECATE = 1;
}
//----------------------------------------------------------------------------------------
//	Copyright © 2006 - 2008 Tangible Software Solutions Inc.
//
//	This class provides the ability to simulate various classic C string functions
//	which don't have exact equivalents in the Java framework.
//----------------------------------------------------------------------------------------
final class SimulateStringFunctions
{
	//------------------------------------------------------------------------------------
	//	This method simulates the classic C string function 'isxdigit' (and 'iswxdigit').
	//------------------------------------------------------------------------------------
	static boolean isXDigit(char character)
	{
		if (Character.isDigit(character))
			return true;
		else if ("ABCDEFabcdef".indexOf(character) > -1)
			return true;
		else
			return false;
	}

	//------------------------------------------------------------------------------------
	//	This method simulates the classic C string function 'strchr' (and 'wcschr').
	//------------------------------------------------------------------------------------
	static String strChr(String stringtosearch, char chartofind)
	{
		int index = stringtosearch.indexOf(chartofind);
		if (index > -1)
			return stringtosearch.substring(index);
		else
			return null;
	}

	//------------------------------------------------------------------------------------
	//	This method simulates the classic C string function 'strrchr' (and 'wcsrchr').
	//------------------------------------------------------------------------------------
	static String strRChr(String stringtosearch, char chartofind)
	{
		int index = stringtosearch.lastIndexOf(chartofind);
		if (index > -1)
			return stringtosearch.substring(index);
		else
			return null;
	}

	//------------------------------------------------------------------------------------
	//	This method simulates the classic C string function 'strstr' (and 'wcsstr').
	//------------------------------------------------------------------------------------
	static String strStr(String stringtosearch, String stringtofind)
	{
		int index = stringtosearch.indexOf(stringtofind);
		if (index > -1)
			return stringtosearch.substring(index);
		else
			return null;
	}

	//------------------------------------------------------------------------------------
	//	This method simulates the classic C string function 'strtok' (and 'wcstok').
	//------------------------------------------------------------------------------------
	private static String activestring;
	private static int activeposition;
	static String strTok(String stringtotokenize, String delimiters)
	{
		if (stringtotokenize != null)
		{
			activestring = stringtotokenize;
			activeposition = -1;
		}

		//the stringtotokenize was never set:
		if (activestring == null)
			return null;

		//all tokens have already been extracted:
		if (activeposition == activestring.length())
			return null;

		//bypass delimiters:
		activeposition++;
		while (activeposition < activestring.length() && delimiters.indexOf(activestring[activeposition]) > -1)
		{
			activeposition++;
		}

		//only delimiters were left, so return null:
		if (activeposition == activestring.length())
			return null;

		//get starting position of string to return:
		int startingposition = activeposition;

		//read until next delimiter:
		do
		{
			activeposition++;
		} while (activeposition < activestring.length() && delimiters.indexOf(activestring[activeposition]) == -1);

		return activestring.substring(startingposition, activeposition - startingposition);
	}
}
//----------------------------------------------------------------------------------------
//	Copyright © 2006 - 2008 Tangible Software Solutions Inc.
//
//	This class provides miscellaneous helper methods for strings.
//----------------------------------------------------------------------------------------
final class StringHelper
{
	//------------------------------------------------------------------------------------
	//	This method allows replacing a single character in a string, to help convert
	//	C++ code where a single character in a character array is replaced.
	//------------------------------------------------------------------------------------
	static String changeCharacter(String sourcestring, int charindex, char changechar)
	{
		return (charindex > 0 ? sourcestring.substring(0, charindex) : "")
			+ Character.toString(changechar) + (charindex < sourcestring.length() - 1 ? sourcestring.substring(charindex + 1) : "");
	}
}
//----------------------------------------------------------------------------------------
//	Copyright © 2006 - 2008 Tangible Software Solutions Inc.
//
//	This class is used to simulate the ability to pass arguments by reference in Java.
//----------------------------------------------------------------------------------------
final class RefObject<T>
{
	T argvalue;
	RefObject(T refarg)
	{
		argvalue = refarg;
	}
}
