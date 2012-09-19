#!/usr/bin/env python2
import argparse
import sys

parser = argparse.ArgumentParser(description = 'Takes values from standard input, multiplies them, and outputs them to the standard output.')
parser.parse_args()

x = 1;
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
