import os
import re
import sys

from argparse import ArgumentParser
from datetime import date

def FileExists(filename):
	FilePath = os.path.abspath(filename)
	return os.path.exists(FilePath)

def main():
	args = sys.argv[1:]
	parser = ArgumentParser(description='Script modifies copyright year',
						usage='''python sanitize.py -i <input_file> [-v]''')
	parser.add_argument('-i', '--input', help='Provide input filename', required=True)
	parser.add_argument('-v', '--verbose', help='Display all changes', action='store_true', required=False)

	args = parser.parse_args()

	ret = FileExists(args.input)
	if ret is False:
		print('ERROR: File does not exist: %s' % (args.input))
		sys.exit(1)

	verbose = False
	if args.verbose:
		verbose = True

	infile = open(args.input, mode='r')
	outfile = open('sanitized_'+args.input, mode='w')
	line = infile.readline()
	line_no = 1
	change_count = 0
	while line:
		if line.startswith('Copyright (c) '):
			current_year = date.today().year
			copyright_years = re.findall('(\d{4})', line)
			last_copyright_year = int(copyright_years[-1])
			last_copyright_year_index = line.index(copyright_years[-1])
			if last_copyright_year != current_year:
				change_count += 1
				if verbose:
					print('#'+str(change_count),'['+str(line_no)+'] Changed "'+line[:-1]+'" ->')
				if last_copyright_year == current_year - 1:
					if line[last_copyright_year_index-1] == '-':
						line = line[:last_copyright_year_index]+str(current_year)+line[last_copyright_year_index+4:]
					else:
						line = line[:last_copyright_year_index+4]+'-'+str(current_year)+line[last_copyright_year_index+4:]
				else:
					line = line[:last_copyright_year_index+4]+','+str(current_year)+line[last_copyright_year_index+4:]
				if verbose:
					print('\t\t to "'+line[:-1]+'"')
		elif '_blacklisted_keyword_' in line:
			change_count += 1
			if verbose:
				print('#'+str(change_count),'['+str(line_no)+'] Changed "'+line[:-1]+'" ->')
			line = line.replace('_blacklisted_keyword_','')
			if verbose:
				print(' '*len(str(change_count)),' '*len(str(line_no)),'  to       "'+line[:-1]+'"')
		outfile.write(line)
		line = infile.readline()
		line_no += 1
	print(change_count, 'lines changed. Output file sanitized_%s created' % args.input)
	outfile.close()

if __name__ == "__main__":
	if sys.hexversion < 0x3040000:
		sys.stderr.write("Please use Python 3.4 or greater!\n")
		sys.exit(-1)
	ret = main()
	sys.exit(ret)
