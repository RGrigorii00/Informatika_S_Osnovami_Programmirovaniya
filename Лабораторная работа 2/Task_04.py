def Task_04():
	# Var's
	chislo = int(input());

	# Logic
	if (1 <= chislo <= 9):
		for i in range(1, chislo + 1):
			print(str(i) * i);

	import main;
	main.Start();