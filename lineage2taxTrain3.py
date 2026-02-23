#!/usr/bin/env python3
# Converted to python3 from program by Benli Chai, June 24, 2016
# Convert a taxonomy tab-delimited lineage file
# to RDP Classifier taxonomy training format

import sys

if len(sys.argv) != 2:
    print("lineage2taxTrain.py taxonomyFile")
    sys.exit(1)

taxonomy_file = sys.argv[1]

with open(taxonomy_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip().split('\t')[1:]  # list of ranks

name_to_id = {"Root": 0}   # taxon name → taxid
ranks = {}                 # column index → rank name
lineages = []              # unique lineage paths

# map column index to rank
for i, rank_name in enumerate(header):
    ranks[i] = rank_name

# print root record
root = ['0', 'Root', '-1', '0', 'rootrank']
print('*'.join(root))

ID = 0  # taxon id counter

for line in lines[1:]:
    cols = line.strip().split('\t')[1:]

    for i in range(len(cols)):

        name_parts = []
        for node in cols[:i + 1]:
            node = node.strip()
            if node not in ('-', ''):
                name_parts.append(node)

        if not name_parts:
            continue

        parent_name = ';'.join(name_parts[:-1])

        if name_parts not in lineages:
            lineages.append(name_parts)

        depth = len(name_parts)
        full_name = ';'.join(name_parts)

        if full_name in name_to_id:
            continue

        try:
            rank = ranks[i]
        except KeyError:
            print(cols)
            sys.exit(1)

        if i == 0:
            parent_name = 'Root'

        parent_id = name_to_id[parent_name]

        ID += 1
        name_to_id[full_name] = ID

        out = [
            str(ID),
            full_name.split(';')[-1],
            str(parent_id),
            str(depth),
            rank
        ]

        print('*'.join(out))
