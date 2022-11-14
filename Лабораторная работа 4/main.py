#  s = '1 \t2 \t3 \n1 \t4 \t9 \n'; # \n1 --- это \n 1
#    1 \t2 \t3 
#  \n1 \t4 \t9 
#  \n1 \t8 \t27
s = '';
mnozh = 1;
x = input(); # Horizontal
y = input(); # Vertical

for xx in range(1, int(x) + 1):
	s += str(xx);


s_list = list(s);
s_list_ref = s_list.copy();
print(s_list_ref);

for z in range(len(s_list_ref)):
	for i in range(len(s_list_ref)):
		s_list_ref[i] = int(s_list[i])*mnozh;
		if mnozh == 10 or mnozh == int(y):
			break;
	mnozh += 1;
	print(s_list_ref);