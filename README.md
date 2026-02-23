# Miscellaneous-scripts
As the name suggest, these are miscellaneous scripts I have written to help with certain tasks encountered when working with sequencing data.

**miga_completeness.py** - Use this script to extract a report on genome completeness, contamination and quality from a MiGA project directory to a tab-delimited text file.

**miga_sumdb.sh** - Use this script to summarize the taxonomy information for all of the genomes in your MiGA project. Run it from the directory <project_name>/data/09.distances/05.taxonomy. 

**rename_sra_files.py** - Given a tab-delimited file associating SRA run names with sample names, this script renames downloaded files by their sample names.

**test_figaro.sh** - Use this script to test your installation of FIGARO after following the installation instructions at https://john-quensen.com/tutorials/figaro/.

**copy_miga_16s_files.sh** - cd to the MiGA results directory and then run this script to copy all 16S sequences MiGA found to the sub-directory 16S_sequences. Empty files are automatically deleted. Because more than one 16S sequences may occur in a genome or bin, each file is potentially a multi-fasta file.

**seq_id_2_file_name.py** - This script is useful when processing 16S sequences retrieved from MiGA results. For example, for all files in the sub-directory 16S_sequences created by copy_miga_16s_files.sh, it writes separate fasta files for each sequence named to match the genome or bin they came from. The names are appended with a digit to keep separate multiple copies from the same genome or bin.

**extract_gene_sequences_from_genbank.py** - This script extracts the nucleotide and protein sequences of a gene or list of genes from a GenBank file. The nucleotide and protein sequences are written to separate fasta files: nucleotides.fasta and proteins.fasta.
usage: extract_gene_sequences_from_genbank.py [-h] [-g gbk_file] [-f feature [gene_id protein_id locus_tag product]] [-l gene_list] [-g single_gene]
Must provide the name of a single gene or a list of genes in a text file, one gene per line.

**.bashrc** and **.bash_profile** are bash configuration files for use with a Mac cmomputer. They change the behaviour of the terminal prompt to make it more informative. Put them in your user home directory after you have configured the terminal to use bash instead of zsh.

**splitInterleavedFASTQ.py** splits interleaved FASTQ files into separate forward and reverse read files. Assumes the order of the sequences is stricly alternate beginning with read 1 (forward) and then read 2 (reverse) for each pair.

**scan_annot_files_for_genes.sh** - MicrobeAnnotator outputs annotation files with the extension ".annot." This script scans all annot files in the present directoy for the presence of genes and outputs a tab-delimited file named "gene_presence.tsv." The genes to look for must be provided in a file named "genes.txt," one gene per line. The first column in the output file is the annot file name and subsequent columns give the presence (1) or absence (0) of each gene included in gene.txt.

**rdp2rdp_train_files.py** - A python3 script for parsing the raw RDP Classifier training data downloaded from Sourceforge and creating the files rawSeqs.fasta and rawTaxonomy.txt required for training the RDP Classifier. This allows using a subset of the training data or adding to it.

**gtdb2rdp_train_files.py** - A python3 script for parsing 16S rRNA gene sequences downloaded from GTDB and creating the files rawSeqs.fasta and rawTaxonomy.txt required for training the RDP Classifier.

**lineage2taxTrain3.py** - Python3 version of lineage2taxTrain.py. Converts the rawTaxonomy file to ready4train.taxonmy.txt, a reformatted version of the taxonomy file required for training the RDP Classifier.

**addFullLineage3.py** - Python3 version of addFullLineage.py. Converts rawSeqs.fasta to ready4train_seqs.fasta, a reformatted version of the fasta file required for training the RDP Classifier.


