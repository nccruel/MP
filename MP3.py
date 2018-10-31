#MACHINE PROB 3

file_name = str(input())
dictionary = open(file_name,"r")
d = dictionary.read()
dl = d.split()
t = int(input())
for i in range(t):
	word = str(input())
	possible = []
	anagram = []
	for a in range(len(dl)):
		if len(dl[a])==len(word):
			possible.append(dl[a])
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
dictionary.close()
