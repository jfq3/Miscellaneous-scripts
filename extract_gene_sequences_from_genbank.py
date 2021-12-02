#!/bin/python

import argparse
import textwrap
import sys
# Biopython's SeqIO module handles sequence input/output
from Bio import SeqIO

# Create the parser
my_parser = argparse.ArgumentParser(description='Extract gene sequences from a GenBank file')

# Add the arguments
my_parser.add_argument('-g',
	metavar='gbk_file',
	type=str,
	help='Input GenBank file')


my_parser.add_argument('-f',
	metavar='feature',
	type=str,
	help='Input feature [EC_number, gene_id, product, protein_id, locus_tag]. Not all features are present in all GenBank files.')

my_parser.add_argument('-l',
	metavar='feature_list',
	type=str,
	help='A text file listing feature values, one per line')

my_parser.add_argument('-s',
	metavar='single_feature',
	type=str,
	help='A single feature value; -l or -s, not both')

args = my_parser.parse_args()
gbk_file = args.g
feature_type = args.f
feature_list = args.l
single_feature = args.s

if(feature_list is None and single_feature is None):
	sys.exit("Aborted\nMust supply single feature name or list of feature names")

if(feature_list is None):
	feature_names = [single_feature]
else:
	# Read in list of  features [].
	feature_names = []
	with open(feature_list, 'r') as file:
		feature_names = [line.strip() for line in file]
	file.close()

def get_cds_feature_with_qualifier_value(seq_record, name, value):
	"""Function to look for CDS feature by annotation value in sequence record.

	e.g. You can use this for finding features by locus tag, gene ID, or protein ID.
	"""
	# Loop over the features
	for feature in genome_record.features:
		if feature.type == "CDS" and value in feature.qualifiers.get(name, []):
			return feature
	# Could not find it
	return None

genome_record = SeqIO.read(gbk_file, "genbank")

with open("nucleotides.fasta", "w") as nt_output, open("proteins.fasta", "w") as aa_output:
	for feature_name in feature_names:
		print("Looking for " + feature_name + " in " + feature_type)
		cds_feature = get_cds_feature_with_qualifier_value(genome_record, feature_type, feature_name)
		if(cds_feature is None):
			print(feature_name + " not found")
		else:
			print("found")
			gene_sequence = cds_feature.extract(genome_record.seq)
			protein_sequence = gene_sequence.translate(table=11, cds=True)

			# This is asking Python to halt if the translation does not match:
			assert protein_sequence == cds_feature.qualifiers["translation"][0]

			# Output FASTA records - note \n means insert a new line.
			# This is a little lazy as it won't line wrap the sequence:
			nt_output.write(">%s\n%s\n" % (feature_name, gene_sequence))
			aa_output.write(">%s\n%s\n" % (feature_name, protein_sequence))

print("Done")

