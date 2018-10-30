#MACHINE PROB 5

file_name = str(input())
dictionary = open(file_name,"r")
dictionary1 = dictionary.read()
dictionary1 = dictionary1.split()
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
	for a in range(len(word)):
		if word[a]in chk:
			if randomized.count(letter) < word.count(letter):
				res = "False"
				break
			else:
				if randomized.count(letter) >= word.count(letter):
					if a == len(word)-1:
						res= "True"
					else:
						continue
		else:
			res = "False"
			break
	if res == "True":
		if word in dictionary1:
			final = "True"
		else:
			final = "False"
	print(final)
	
	


		



