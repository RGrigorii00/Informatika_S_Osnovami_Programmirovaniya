def Task_03():
# Description / Interface
	print("Введите ваши 3 числа: ");

# Var's
	chislo_1 = int(input());
	chislo_2 = int(input());
	chislo_3 = int(input());

# Logic
	if (chislo_1 < chislo_2) & (chislo_1 < chislo_3):
		print("Наименьшее: ");
		print(chislo_1);
	elif (chislo_2 < chislo_1) & (chislo_2 < chislo_3):
		print("Наименьшее: ");
		print(chislo_2);
	elif (chislo_3 < chislo_2) & (chislo_3 < chislo_1):
		print("Наименьшее: ");
		print(chislo_3);
		
	import main;
	main.Start();