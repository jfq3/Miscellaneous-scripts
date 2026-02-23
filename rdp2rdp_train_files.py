#!/usr/bin/env python3

import sys

if len(sys.argv) != 4:
    print("Usage: python rdp2rdp_train_files.py input.fasta output.fasta taxonomy.tsv")
    sys.exit(1)

input_file = sys.argv[1]
fasta_out = sys.argv[2]
tax_out = sys.argv[3]

with open(input_file) as infile, \
     open(fasta_out, "w") as fasta_file, \
     open(tax_out, "w") as tax_file:

    tax_file.write("ID\tDomain\tPhylum\tClass\tOrder\tFamily\tGenus\n")

    seq_id = None
    sequence_lines = []

    for line in infile:
        line = line.rstrip()

        if line.startswith(">"):
            # Write previous sequence
            if seq_id:
                fasta_file.write(f">{seq_id}\n")
                fasta_file.write("".join(sequence_lines) + "\n")

            sequence_lines = []

            header = line[1:]
            parts = header.split(None, 1)

            seq_id = parts[0]

            taxonomy_string = parts[1] if len(parts) > 1 else ""
            taxa = taxonomy_string.split(";")

            # Ignore "Root" if present
            if taxa and taxa[0].lower() == "root":
                taxa = taxa[1:]

            # Ensure exactly 6 ranks (Domain → Genus)
            while len(taxa) < 6:
                taxa.append("")

            domain, phylum, class_, order, family, genus = taxa[:6]

            tax_file.write(
                f"{seq_id}\t{domain}\t{phylum}\t{class_}\t{order}\t{family}\t{genus}\n"
            )

        else:
            sequence_lines.append(line)

    # Write final sequence
    if seq_id:
        fasta_file.write(f">{seq_id}\n")
        fasta_file.write("".join(sequence_lines) + "\n")

