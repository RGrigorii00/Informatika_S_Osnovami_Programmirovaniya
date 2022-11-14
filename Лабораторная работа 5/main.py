import Task_01;
import Task_02;
import Task_03;
import print_functions;


def Start():
	print_functions.Menu();

# Var's
	task_number = int(input());
	#print("");

# Logic
	if (task_number == 1):
		print_functions.___();
		print("Вы выбрали задачу номер 1");
		Task_01.Max_Num(int(input('Напишите любое положительное число: ')));
	elif (task_number == 2):
		print_functions.___();
		print("Вы выбрали задачу номер 2");
		Task_02.Trans(input());
	elif (task_number == 3):
		print_functions.___();
		print("Вы выбрали задачу номер 3");
		Task_03.Z3();

Start();