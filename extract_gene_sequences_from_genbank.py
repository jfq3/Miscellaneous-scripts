#!/bin/python

import argparse
import sys
# Biopython's SeqIO module handles sequence input/output
from Bio import SeqIO

# Create the parser
my_parser = argparse.ArgumentParser(description='Extract gene sequences from a GenBank file')

# Add the arguments
my_parser.add_argument('-f',
	metavar='gbk_file',
	type=str,
	help='Input GenBank file')

my_parser.add_argument('-l',
	metavar='gene_list',
	type=str,
	help='Input list of genes')

my_parser.add_argument('-g',
	metavar='single_gene',
	type=str,
	help='Input a single gene')

args = my_parser.parse_args()
gbk_file = args.f
gene_list = args.l
single_gene = args.g

if(gene_list is None and single_gene is None):
	sys.exit("Aborted\nMust supply single gene name or list of genes")

if(gene_list is None):
	genes = [single_gene]
else:
	# Read in list of genes
	genes = []
	with open(gene_list, 'r') as file:
		genes = [line.strip() for line in file]
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
	for gene in genes:
		print("Looking for " + gene)
		cds_feature = get_cds_feature_with_qualifier_value(genome_record, "gene", gene)
		if(cds_feature is None):
			print(gene + " not found")
		else:
			gene_sequence = cds_feature.extract(genome_record.seq)
			protein_sequence = gene_sequence.translate(table=11, cds=True)
		
			# This is asking Python to halt if the translation does not match:
			assert protein_sequence == cds_feature.qualifiers["translation"][0]
	 
			# Output FASTA records - note \n means insert a new line.
			# This is a little lazy as it won't line wrap the sequence:
			nt_output.write(">%s\n%s\n" % (gene, gene_sequence))
			aa_output.write(">%s\n%s\n" % (gene, protein_sequence))

print("Done")

