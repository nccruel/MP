#MACHINE PROB 4

file_name = str(input())
dictionary = open(file_name,"r")
dictionary1 = dictionary.read()
dictionary1 = [dictionary1 for dictionary1 in dictionary1.split()]
t = int(input())
for i in range(t):
	words = str(input())
	list_words = [words for words in words.split()]
	final_checker = ""
	checker = ""
	final = ""
	last = ""
	for ctr in range(len(words)):
		if words[ctr] == " ":
			continue
		else:
			checker+=words[ctr]
	for letters in checker:
		if letters not in final_checker:
			final_checker+=letters
		else:
			continue
			
	for a in range(len(final_checker)):
		max_char = 0
		for word in list_words:
			temp = word.count(final_checker[a])
			if temp > max_char:
				max_char = temp	
		final+=(str(final_checker[a])*max_char)
	final = sorted(final)
	for char in final:
		last+= char
	print(last)
	