def Task_03():
	# Var's
	chislo = int(input());
	prom_chislo = 0;

	# Logic
	if (1 <= chislo <= 1000):
		for i in range(1, chislo):
			if (chislo % i == 0):
				prom_chislo += i;
	else: print("Число вышло за диапазон! Введите число в диапазоне [1, 1000]");

	if (prom_chislo == chislo):
		print(str(chislo) + " - " + "Это число совершенное");
	elif (prom_chislo != 0): 
		print("Число" + " " + str(chislo) + " " + "не совершенное");

	# Help
		"""
		Совершенных чисел не так много. 
		В диапазоне от 1 до 1000 их всего 3.
		Это 6, 28, 496
		"""

	import main;
	main.Start();