def Trans(num):
	chislo = 0;
	
	for i in range( len(num) ):
		chislo += int(num[i]) * ( 2**(len(num) - i - 1));
	print(chislo);
