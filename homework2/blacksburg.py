# ECE 2524 Homework 2 Problem 2 Luke Spieler

with open('account', 'r') as f:
	print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
	for line in f:
		line1 = line.split()
		if line1[3] == 'Blacksburg':
			print line1[4] + ', ' + line1[1] + ', ' + line1[0] + ', ' + line1[2]
