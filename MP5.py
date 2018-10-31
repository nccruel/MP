#MACHINE PROB 5

file_name = str(input())
dictionary = open(file_name,"r")
d = dictionary.read()
dl = d.split()
t = int(input())
for i in range(t):
	strings = str(input())
	strings = [strings for strings in strings.split()]
	randomized = strings[0]
	word = strings[1]
	chk = ""
	for n in randomized:
		if n not in chk:
			chk+=n
		else:
			continue
	if word in dl:
		for i in range(len(word)):
				if word[i] in chk:
					if randomized.count(word[i]) < word.count(word[i]):
						res = "False"
						break
					else:
						if i == len(word)-1:
							res = "True"
						else:
							continue
				else:
					res = "False"
					break
	else:
		res = "False"
	print(res)
dictionary.close()
	
	


		



