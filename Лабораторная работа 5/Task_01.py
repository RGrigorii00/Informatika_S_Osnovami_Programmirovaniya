def Max_Num(num):
	max_num = 0;

	while (num > 0):
		tmp = num % 10;
		num = num // 10;
		if (tmp > max_num):
			max_num = tmp;
		else: continue;
	else: print("Максимальная цифра в числе: " + str(max_num));