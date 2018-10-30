#MACHINE PROB 6

file_name = str(input())
dictionary = open(file_name,"r")
dictionary1 = dictionary.read()
dictionary1 = [dictionary1 for dictionary1 in dictionary1.split()]
t = int(input())
for i in range(t):
	scm = str(input())
	srtscm = "".join(sorted(scm))
	tot = ""
	a1 = "eaionrtlsu"
	a2 = "dg"
	a3 = "bcmp"
	a4 = "fhvwy"
	a5 = "k"
	a8 = "jx"
	a10 = "qz"
	fin = []
	score = []
	for a in srtscm:
		if a not in tot:
			tot+=a
		else:
			continue
	for b in range(len(dictionary1)):
		for i in range(len(dictionary1[b])):
			word = dictionary1[b]
			if word[i] in tot:
				if scm.count(word[i]) < word.count(word[i]):
					break
				elif scm.count(word[i]) >= word.count(word[i]):
					if i == len(word)-1:
						if word not in fin:
							fin.append(word)
						else:
							continue
					else: 
						continue
			else:
				break
	res = "".join(fin)
	for c in res:
		if c in a1:
			score.append(1)
		elif c in a2:
			score.append(2)
		elif c in a3:
			score.append(3)
		elif c in a4:
			score.append(4)
		elif c in a5:
			score.append(5)
		elif c in a8:
			score.append(8)
		elif c in a10:
			score.append(10)
	print(sum(score))

