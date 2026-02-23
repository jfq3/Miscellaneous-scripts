#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("addFullLineage.py taxonomyFile fastaFile")
    sys.exit(1)

taxonomy_file = sys.argv[1]
fasta_file = sys.argv[2]

# Read taxonomy file
lineage_map = {}

with open(taxonomy_file, "r", encoding="utf-8") as f1:
    lines = f1.readlines()

for line in lines[1:]:  # skip header
    line = line.strip()
    if not line:
        continue

    cols = line.split('\t')

    lineage = ['Root']
    for node in cols[1:]:
        node = node.strip()
        if node not in ('-', ''):
            lineage.append(node)

    ID = cols[0]
    lineage_str = ';'.join(lineage).strip()
    lineage_map[ID] = lineage_str

# Process fasta file
with open(fasta_file, "r", encoding="utf-8") as f2:
    for line in f2:
        line = line.strip()
        if not line:
            continue

        if line.startswith('>'):
            ID = line.split()[0].replace('>', '')

            if ID not in lineage_map:
                print(ID, "not in taxonomy file")
                sys.exit(1)

            lineage = lineage_map[ID]
            print(f">{ID}\t{lineage}")
        else:
            print(line)