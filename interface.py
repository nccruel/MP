def start():
	print("="*60)
	print("Hewwo! Welcome to The Uwurd Unscwambler!")
	print()
	print("Choose an option!")
	print("(a) Play c:")
	print("(b) Exit :(")
	inp = str(input())
	if inp == "a":
		print("Yay!")
		play()
	elif inp == "b":
		print("Sure u wanna go? :( (a) yes :c bye!  (b) no!!! i wanna play!")
		inp1 = str(input())
		if inp1 == "a":
			print("Okay byeee!")
			exit()
		elif inp1 == "b":
			play()

def play():
	print("="*60)
	print("Uwurd Unscwambler <3")
	print()
	print("Game mode?")
	print("(a) Anagwams!")
	print("(b) Combining words :O")
	print("(c) Go back!")
	print("(d) Exit :(")
	inp = str(input())
	if inp == "a":
		inanag()
	elif inp == "b":
		incmb()
	elif inp == "c":
		start()
	elif inp == "d":
		print("Okay byeee!")
		exit()

def inanag(): #ANAGRAMS MODE
	print("="*60)
	print("Uwurd Unscwambler <3")
	print("ANAGWAMS MODE!!!")
	print("Loading...")
	from engine import ang

def incmb(): #COMBINING WORDS MODE 
	life = 3
	score = 0
	correct = []
	incorrect = []
	def dcmb():
		print("="*60)
		print("Uwurd Unscwambler <3")
		print("COMBWINING WORDS MODE!!!")
	def dcmb1():
		print("heart:", life)
		print("score:", score, "/", engine.cmb.tot)
	dcmb()
	print("Loading...")
	import engine
	engine.cmb()
	while life >= 0 and score <= engine.cmb.tot:
		if score == engine.cmb.tot:
			dcmb()
			dcmb1()
			print()
			print("Words for: " + '"' + engine.cmb.scramble + '"' + ": ", end="")
			for x in range(len(correct)):
				if x == len(correct)-1:
					print(correct[x])
				else:
					print(correct[x] + ", ", end="")
			print()
			print("Whoa! You really found all the words! Congwats UwU!")
			break
		elif score >= 0 or life <= 3:
			dcmb()
			dcmb1()
			print()
			print("Find the words that can be made with the letters of:", engine.cmb.scramble)
			if score == 0 and life <= 3:
				print("Correct guesses:")
			elif score > 0:
				print("Correct guesses: ", end="")
			for y in range(len(correct)):
				if y == len(correct)-1:
					print(correct[y])
				else:
					print(correct[y] + ", ", end="")
			if score == 0:
				if life == 3:
					print("Incorrect guesses: ")
				else:
					print("Incorrect guesses: ", end="")
			elif score > 0:
				if life == 3:
					print("Incorrect guesses: ")
				else:
					print("Incorrect guesses: ", end="")
			for z in range(len(incorrect)):
				if z == len(incorrect)-1:
					print(incorrect[z])
				else:
					print(incorrect[z] + ", ", end="")
			print()
			
			guess = str(input("Your guess: "))                       #ENTER GUESS PART AND CHECK IF CORRECT
			if guess in engine.load.d:
				for i in range(len(guess)):
					if guess[i] in engine.cmb.chk:
						if engine.cmb.scramble.count(guess[i]) < guess.count(guess[i]):
							res = "False"
							break
						else:
							if i == len(guess)-1:
								res = "True"
							else:
								continue
					else:
						res = "False"
						break
			else:
				res = "False"
			if res == "True":
				correct.append(guess)
				engine.compute(guess)
				score+=engine.compute.total
			else:
				incorrect.append(guess)
				life-=1
	if life < 0:
		dcmb()
		print("heart:", "0")
		print("score:", score, "/", engine.cmb.tot)
		print("Correct guesses: ", end="")
		for x in range(len(correct)):
			if x == len(correct)-1:
				print(correct[x])
			else:
				print(correct[x] + ", ", end="")
		print("Incorrect guesses: ", end="")
		for y in range(len(incorrect)):
			if y == len(incorrect)-1:
				print(incorrect[y])
			else:
				print(incorrect[y] + ", ", end="")
		print()
		print("GAME OVER!")
		exit()


start()



