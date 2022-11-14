# Descriptions / Interface
import print_functions;
import Task_01;
import Task_02;
import Task_03;
import Task_04;
import Task_05;
import Task_06;

def Start():
	print_functions.Menu();

# Var's
	task_number = int(input());
	#print("");

# Logic
	if (task_number == 1):
		print_functions.___();
		print("Вы выбрали задачу номер 1");
		Task_01.Task_01();
	elif (task_number == 2):
		print_functions.___();
		print("Вы выбрали задачу номер 2");
		Task_02.Task_02();
	elif (task_number == 3):
		print_functions.___();
		print("Вы выбрали задачу номер 3");
		Task_03.Task_03();
	elif (task_number == 4):
		print_functions.___();
		print("Вы выбрали задачу номер 4");
		Task_04.Task_04();
	elif (task_number == 5):
		print_functions.___();
		print("Вы выбрали задачу номер 5");
		Task_05.Task_05();
	elif (task_number == 6):
		print_functions.___();
		print("Вы выбрали задачу номер 6");
		Task_06.Task_06();

Start();