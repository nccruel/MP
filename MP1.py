#MACHINE PROB 1

file_name = str(input())
dictionary = open(file_name,"r")
d = (dictionary.read())
dl = d.split()
for x in dl:
	print(x)
dictionary.close()