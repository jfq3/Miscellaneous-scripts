#!/bin/bash

# Copy miga 16S files.

# cd to the miga project directory
mkdir 16S_sequences
cp ./data/07.annotation/01.function/02.ssu/*.ssu.all.fa.gz ./16S_sequences
cd ./16S_sequences
gzip -d *.gz
find . -size  0 -print -delete # This line deletes empty files.
