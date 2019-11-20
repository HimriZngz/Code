for row in range(1,10):
	for column in range(1,row+1):
		print("%d*%d=%d" % (column,row,column*row),end=' ')
	print("")