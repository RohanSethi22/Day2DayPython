import sys

# transform text file to text file
def main(input_file, output_file):
	infile = open(input_file, 'r')
	outfile = open(output_file, 'w')
	for line in infile:
		words = line.split(' ')
		# parse the line as required
		outfile.write('New ' + words[0] + '<eol>\n')
	outfile.close()
	infile.close()

import binascii
# transform binary file to text file
def bin_main(input_file, output_file):
	infile = open(input_file, 'rb')
	outfile = open(output_file, 'w')
	bytes_in = infile.read(4)
	count = 1
	while bytes_in:
		hexa = binascii.hexlify(bytes_in).decode('ascii')
		parsed_str = hexa[6:] + hexa[4:6] + hexa[2:4] + hexa[:2]
		outfile.write(parsed_str)
		bytes_in = infile.read(4)
		eol = '_'
		if count == 4:
			count = 0
			eol = '\n'
		outfile.write(eol)
		count += 1
	outfile.close()
	infile.close()

if __name__ == '__main__':
	option = sys.argv[1]
	infile = sys.argv[2]
	outfile = 'output.txt'
	print('Processing', infile)
	if option == 't' or option == 'text':
		main(infile, outfile)
	elif option == 'b' or option == 'bin' or option == 'binary':
		bin_main(infile, outfile)
	print('Output file', outfile, 'generated')
