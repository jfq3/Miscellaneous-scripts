#!/usr/bin/python

# seq_id_2_file_name.py
# John Quensen
# 24 May 2021

import sys, os
from Bio import SeqIO

infiles = [fn for fn in os.listdir('.') if fn.endswith(('.fasta', '.fa', '.fastq'))]

for infile in infiles:
	# Get file type
	if infile.endswith("q"):
		file_type = "fastq"
	else:
		file_type = "fasta"
	count = 0

	for record in SeqIO.parse(open(infile, "r"), file_type):
		count = count + 1
		record.id = infile.split(".")[0] + "." + str(count)
		record.description = ""
		out_file_name = record.id + "." + "fasta"
		out_file = open(out_file_name, 'w')
		SeqIO.write(record, out_file, file_type)

	backup_file = infile + ".bak"
	os.rename(infile, backup_file)

