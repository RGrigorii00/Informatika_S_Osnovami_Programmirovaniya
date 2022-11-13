def Task_05():
# Important Things
	import math;

# Description / Interface
	print("Введите радиус круга: ");

# Var's
	radius = int(input());
	s = 0; # Площадь круга
	l = 0; # Длина окружности

# Logic
	l = math.pi * 2 * radius;
	s = math.pi * radius ** 2;
	print("Длина окружности: " + str(l));
	print("Площадь круга: " + str(s));
	
	import main;
	main.Start();