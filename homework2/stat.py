# ECE 2524 Homework 2 Problem 3 Luke Spieler

with open('account', 'r') as f:
	print "ACCOUNT SUMMARY"
	totalamount = 0
	averageamount = 0
	maxamount = 0;
	minamount = float("inf")
	count = 0
	maxname = ""
	minname = ""
	for line in f:
		line1 = line.split()
		moneyowed = float(line1[2])
		totalamount = totalamount + moneyowed		
		if maxamount < moneyowed:
			maxamount = moneyowed
			maxname = line1[1]
		if minamount > moneyowed:
			minamount = moneyowed
			minname = line1[1]
		count = count + 1
	averageamount = totalamount / count
	print "Total amount owed = " + str(totalamount)
	print "Average amount owed = " + str(averageamount)
	print "Maximum amount owed = " + str(maxamount) + " by " + maxname
	print "Minimum amount owed = " + str(minamount) + " by " + minname

