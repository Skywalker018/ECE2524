# ECE 2524 Homework 2 Problem 1 Luke Spieler

with open('/etc/passwd', 'r') as f:
	for line in f:
		line1 = line.split(':')
		print line1[0],
		print '\t',
		print line1[5]
