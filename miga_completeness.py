#!/usr/bin/python

# Import the argparse library
import argparse
import os
import sys
import json

# Create the parser
my_parser = argparse.ArgumentParser(description='Extract MiGA completeness report')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to the MiGA project')
my_parser.add_argument('out_file',
                       metavar='out_file',
                       type=str,
                       help='the name of the output file')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path
out_file=args.out_file
with open(args.out_file, 'w') as output_file:
	if not os.path.isdir(input_path):
		print('The path specified does not exist')
		sys.exit()

	# print('\n'.join(os.listdir(input_path)))

	header=['Completeness', 'Contamination', 'Quality', 'Genome']
	print('\t'.join(header))
	open(out_file, 'w')
	output_file.write("%s\n" % '\t'.join(header))
	directory=input_path + '/data/07.annotation/01.function/01.essential'
	for filename in os.listdir(directory):
		if filename.endswith('.json'):
			f=open(os.path.join(directory, filename))
			genome=filename.split('.')[0]
			data = json.load(f)
			try:
				com=(data.get('stats').get('completeness')[0])
				cont=(data.get('stats').get('contamination')[0])
				qual=(data.get('stats').get('quality'))
				qual=round(qual, 2)
				items=[str(com), str(cont), str(qual), genome]
				out='\t'.join(items)
				print(out)
				output_file.write("%s\n" % '\t'.join(items))
			except TypeError:
				items=["No data", genome]
				out='\t'.join(items)
				print(out)
				output_file.write("%s\n" % '\t'.join(items))
			# Closing file
			f.close()
	output_file.close()
