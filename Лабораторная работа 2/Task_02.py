def Task_02():
	# Var's
	chislo = int(input());
	prom_chislo = 0;

	# Logic
	if (1 <= chislo <= 1000):
		for i in range(1, chislo + 1):
			if (chislo % i == 0):
				prom_chislo += 1;

	else: print("Число вышло за диапазон! Введите число в диапазоне [1, 1000]");

	if (prom_chislo == 2):
		print(str(chislo) + " - " + "Это число простое");
	elif (prom_chislo != 0): 
		print("У числа" + " " + str(chislo) + " " + "более двух делителей!");


	import main;
	main.Start();

			

