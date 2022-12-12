#!/bin/bash

# Test FIGARO installation
# Activate the FIGARO environment
source ~/miniconda3/etc/profile.d/conda.sh # If necessary for your conda installation.
conda activate figaro

cd 
mkdir test_figaro
cd test_figaro

# Download example files from the QIIME2 tutorial pages
wget "https://data.qiime2.org/2020.2/tutorials/atacama-soils/1p/forward.fastq.gz"
wget "https://data.qiime2.org/2020.2/tutorials/atacama-soils/1p/reverse.fastq.gz"
 
 # Decompress
 gzip -d *.fastq.gz
 
 # Rename the files in Zymo format
 mv forward.fastq sam1_16s_R1.fastq
 mv reverse.fastq sam1_16s_R2.fastq
 
 # Run FIGARO
 # cd to installation folder
 cd ~/figaro-master/figaro
 python figaro.py -i ~/test_figaro/ -o ~/test_figaro/ -f 10 -r 10 -a 253 -F zymo
 
 conda deactivate
