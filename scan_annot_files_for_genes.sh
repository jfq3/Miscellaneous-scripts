#!/bin/bash

awk -F'\t' '
BEGIN {
    # read gene list
    while ((getline line < "genes.txt") > 0) {
        sub(/\r$/, "", line)
        if (line == "") continue
        genes[line] = 0
        order[++n] = line
        regex = regex ? regex "|" line : line
    }
    close("genes.txt")

    # exact-word boundary regex
    regex = "(^|[^A-Za-z0-9_])(" regex ")([^A-Za-z0-9_]|$)"

    # print header
    printf "file"
    for (i = 1; i <= n; i++) printf "\t%s", order[i]
    printf "\n"
}

FNR == 1 {
    for (g in genes) genes[g] = 0
}

FNR > 1 {
    text = $5
    while (match(text, regex, m)) {
        genes[m[2]] = 1
        text = substr(text, RSTART + RLENGTH)
    }
}

ENDFILE {
    printf "%s", FILENAME
    for (i = 1; i <= n; i++) printf "\t%d", genes[order[i]]
    printf "\n"
}
' *.annot > gene_presence.tsv

