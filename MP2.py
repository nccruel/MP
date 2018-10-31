#MACHINE PROB 2

file_name = str(input())
dictionary = open(file_name,"r")
d = dictionary.read()
d = d.split()
t = int(input())
for i in range(t):
	integers = input()
	integers = integers.split()
	for a in range(len(integers)):
		if a == len(integers)-1:
			b = integers[a]
			print(d[int(b)])
		else:
			b = integers[a]
			print(d[int(b)], end=" ")
dictionary.close()