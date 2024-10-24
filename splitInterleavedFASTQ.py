#!/usr/bin/env python
#Benli Chai, July 9, 2014
#Used to separate paired-end read1 and read2 interleavely ordered in FASTQ file. Be aware: the order of the sequence reads in the file has to be strictly alternate beginning with read1 and then read2 for each pair.

import sys, string, os
if len(sys.argv) !=2:
	print "splitInterleaved.py FASTQfile"
	sys.exit()

f = open(sys.argv[1], 'r')
prefix = os.path.basename(sys.argv[1]).split('.fastq')[0]
outName1 = prefix + '_R1.fastq'
outName2 = prefix + '_R2.fastq'
out1 = open(outName1, 'w')
out2 = open(outName2, 'w')

while 1:
	try:
		for i in [1, 2, 3, 4]:
			out1.write(f.next())
		for j in [5, 6, 7, 8]:
			out2.write(f.next())
	except StopIteration:
		break
out1.close()
out2.close()
