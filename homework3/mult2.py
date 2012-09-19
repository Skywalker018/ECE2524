#!/usr/bin/env python2
import argparse
import sys
import 	fileinput

parser = argparse.ArgumentParser(description = 'Takes values from standard input, multiplies them, and outputs them to the standard output.')
parser.add_argument('file', metavar = 'F', type = str, nargs = '*', help = 'file')
parser.add_argument('--ignore-blank', dest = 'igbl', action = 'store_const', const = 'on', default = 'off', help = 'Ignores blank spaces in input')
parser.add_argument('--ignore-non-numeric', dest = 'ignn', action = 'store_const', const = 'on', default = 'off', help = 'Ignores non-numeric inputs')
args = parser.parse_args()

x = 1;

if (len(args.file) == 0):
	while 1:
		try:
			curline = sys.stdin.readline()
			if curline == '\n':
				raise EOFError
			if curline == '^D':
				raise KeyboardInterrupt
			if curline == '':
				raise KeyboardInterrupt
			newline = int(curline)
			x = x * newline
		except EOFError:
			print(x)
			x = 1
		except ValueError:
			sys.stderr.write('Error: The input is not an integer\n')
		except KeyboardInterrupt:
			print(x)
			sys.exit(0)
else:
	try:
		while(len(args.file) != 0):
			pop = args.file.pop()
			for line in fileinput.input(pop):
				if args.igbl == 'on':
					if line == '\n'
						line == '1'
				else:
					if line == '\n'
						print(x)
						x == 1
						line == '1'
				if args.ignn == 'on':
					if line != '\n'
						try:
							int(line)
						except ValueError:
							line = '1'
				x = x * line
	except ValueError:
		sys.stderr.write('Error: The input may have non-numeric values')
		sys.exit(1)
	print(x)
