def Z3():
	count = 0;
	pr = 0;


	for i in range(1, 3000):
		pr = 343**5 + 7**3 - 1 - i;

		while (pr > 0):
			if (pr % 7 == 6):
				count += 1;
			pr //= 7;
		
		if count == 12:
			print(i);
			break;


