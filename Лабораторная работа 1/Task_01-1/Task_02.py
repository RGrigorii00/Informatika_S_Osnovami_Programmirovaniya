def Task_02():
# Description / Interface
	print("Введите ваши числа: ");

# Var's
	chislo_1 = int(input());
	chislo_2 = int(input());
	result = "";

# Logic
	if (chislo_1 > chislo_2) & (chislo_1 % chislo_2 == 0):
		result = str(chislo_1) + " кратно " + str(chislo_2);
		print(result);
	elif (chislo_2 > chislo_1) & (chislo_2 % chislo_1 == 0):
		result = str(chislo_2) + " кратно " + str(chislo_1);
		print(result);
		
	import main;
	main.Start();