def Task_04():
# Description / Interface
	print("Введите длины сторон: ");

# Var's
	storona_1 = int(input());
	storona_2 = int(input());
	storona_3 = int(input());

# Logic
	if ((storona_1 + storona_2) > storona_3) & ((storona_2 + storona_3) > storona_1) & ((storona_3 + storona_1) > storona_2):
		print("Со сторонами: " + str(storona_1) + ", " + str(storona_2) + ", " + str(storona_3) + ", можно построить треугольник");
	else: 
		print("Со сторонами: " + str(storona_1) + ", " + str(storona_2) + ", " + str(storona_3) + ", невозможно построить треугольник");
		
	import main;
	main.Start();