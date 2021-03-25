#!/usr/bin/python

import json
import os

header=['Genome', 'Completeness', 'Contamination', 'Quality']
print('\t'.join(header))

directory='/mnt/d/miga-web-3/miga_arthro_bins/data/07.annotation/01.function/01.essential'
for filename in os.listdir(directory):
	if filename.endswith('.json'):
		f=open(os.path.join(directory, filename))
		genome=filename.split('.')[0]
		data = json.load(f)
		com=(data.get('stats').get('completeness')[0])
		cont=(data.get('stats').get('contamination')[0])
		qual=(data.get('stats').get('quality'))
		qual=round(qual, 2)
		items=[genome, str(com), str(cont), str(qual)]
		out='\t'.join(items)
		print(out)
		# Closing file
		f.close()