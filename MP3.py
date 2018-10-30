#MACHINE PROB 3

file_name = str(input())
dictionary = open(file_name,"r")
dictionary1 = dictionary.read()
dictionary1 = [dictionary1 for dictionary1 in dictionary1.split()]
t = int(input())
for i in range(t):
	word = str(input())
	possible = []
	anagram = []
	for a in range(len(dictionary1)):
		if len(dictionary1[a])==len(word):
			possible.append(dictionary1[a])
	for b in range(len(possible)):
		if sorted(word)==sorted(possible[b]):
			anagram.append(possible[b])
		else:
			continue
	for c in range(len(anagram)):
		if c == len(anagram)-1:
			print(anagram[c])
		else:
			print(anagram[c], end=" ")
