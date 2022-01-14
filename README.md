# Day-to-Day Python Scripts

## Overview
### Contains a bunch of python scripts used in day-to-day activities.

1. extract_sum.py	- uses regular expression to compute sum of all integers present in input file.
2. count_word_freq.py	- displays frequency of occurence of words that meet our criteria in input file.
3. json_parser.py	- loads data from a remote json file & processes it as required.
4. xml_parser.py	- loads data from a remote xml file & processes it as required.
5. crawler1.py		- opens an HTML page & processes all <span> tags.
6. crawler2.py		- starts with fiven URL & crawls to other linked pages until limit is met.
7. db_manipulation1.py	- parses given input file & stores processed data into a local database.
8. send_mail.py	- uses SMPT to send computer generated e-mails automatically.
9. check_directory.py	- checks the files/sub-directories contained in given directory & compares if structure has changed since last run.
10. parse_script.py	- general purpose script that accepts type(text/bin) & name of input file as arguments & processes them as required.
11. sanitize.py	- complete script that uses argparser to accept input file & transforms it into required output file with correct copyright years.

## Usage
<pre>
Run command: python sanitize.py -i <input_filename> [-v]
Required arguments:
  -i, --input		: Proved input filename
Optional arguments:
  -h, --help		: Show this help message & exit
  -v, --verbose		: Display all changes
Example:
  python sanitize.py -v -i input.h
</pre>
