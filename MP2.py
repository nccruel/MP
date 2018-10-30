#MACHINE PROB 2

file_name = str(input())
dictionary = open(file_name,"r")
dictionary1 = dictionary.read()
dictionary1 = dictionary1.split()
t = int(input())
for i in range(t):
	integers = input()
	integers = integers.split()
	for a in range(len(integers)):
		if a == len(integers)-1:
			b = integers[a]
			print(dictionary1[int(b)], end="")
		else:
			b = integers[a]
			print(dictionary1[int(b)], end=" ")
	print()
dictionary.close()