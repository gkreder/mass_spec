#!/usr/bin/env Rscript
library (mzmatch.R)
source('mzmatch.ipeak.sort.MetAssign.R')
mzmatch.init (version.1=FALSE)

baseDir <- "."

setwd (baseDir)

#
# Run the XCMS script first
#

mzXMLfiles <- dir("std1",recursive=TRUE,full.names=TRUE,pattern=".mzXML")
output <- sub (".mzXML",".peakml",mzXMLfiles)

for (i in 1:length(mzXMLfiles))
{
#	xset <- xcmsSet(mzXMLfiles[i], method='centWave', ppm=2.5, peakwidth=c(10,50), snthresh=3, prefilter=c(3,100), integrate=1, mzdiff=-0.00005, verbose.columns=TRUE,fitgauss=FALSE)
#	PeakML.xcms.write.SingleMeasurement( xset=xset, filename=output[i], ionisation="detect", addscans=2, writeRejected=FALSE, ApodisationFilter = TRUE)
}

# Combining
MainClasses <- dir ("std1",full.names=TRUE)
MainClasses.short <- dir ("std1")
dir.create ("combined")

for (i in 1:length(MainClasses))
{
	FILESf <- dir(MainClasses[i],full.names=TRUE,pattern="\\.peakml$",recursive=TRUE)
	OUTPUTf <- paste("combined/",MainClasses.short[i],".peakml",sep="")
#	mzmatch.ipeak.Combine(i=paste(FILESf, collapse=","), v=T, rtwindow=30, o=OUTPUTf, combination="set", ppm=5, label=paste(MainClasses[i], sep=""))
}

print('Filtering')
#mzmatch.ipeak.filter.SimpleFilter( i="combined/POS.peakml", o="combined_filtered.peakml",minintensity=5000, v=T)

print('Gap Filling')
#PeakML.GapFiller(filename="combined_filtered.peakml", ionisation = "detect", Rawpath = baseDir, outputfile="combined_filtered_gapfilled.peakml",ppm=0,rtwin=0)

ADDUCTS="M+2H,M+H+NH4,M+ACN+2H,M+2ACN+2H,M+H,M+NH4,M+Na,M+CH3OH+H,M+ACN+H,M+ACN+Na,M+2ACN+H,2M+H,2M+Na,2M+ACN+H"
#mzmatch.ipeak.sort.MetAssign(i="combined_filtered_gapfilled.peakml", o="final_identified.peakml", ppm=2.5, numDraws=200, burnIn=200, databases="std1_POS.filtered.xml,std1_POS_1000.xml", adducts=ADDUCTS, dbIdentOut="identified_metabolites.tsv", v=T)

mzmatch.ipeak.convert.ConvertToText( i="final_identified.peakml", o="identified_peaks.tsv", annotations="filteredIdentification" )
