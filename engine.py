#functions

def load():
#   file_name = str(input())
    dictionary = open("eng.txt", "r")
    dictionary1 = dictionary.read()
    load.d = dictionary1.split()
    load.d = sorted(load.d)

def ca():
    import random
    load()
    integers = []
    chkr = 2
    chb = 0
    while chb < chkr:
        num = random.randint(0, len(load.d))
        if num not in integers:
            chb+=1 
            integers.append(num)
    ca.w = []
    for j in range(len(integers)):
        ca.w.append(load.d[integers[j]])

def cb():
    import random
    load()
    t = random.randint(3, 4)
    integers = []
    chkr = t
    chb = 0
    while chb < chkr:
        num = random.randint(0, len(load.d))
        if num not in integers:
            chb+=1 
            integers.append(num)
    cb.w = []
    for j in range(len(integers)):
        cb.w.append(load.d[integers[j]])

def shuffle(grp):
    import random
    shuffle.word = ""
    for i in grp:
        shuffle.word+=i
    finalword = ""
    final = ""
    last = ""
    for letters in shuffle.word:
        if letters not in finalword:
                finalword+=letters
        else:
            continue
    for a in range(len(finalword)):
        max_char=0
        for w in grp:
            temp = w.count(finalword[a])
            if temp> max_char:
                max_char= temp  
        final+=(str(finalword[a])*max_char)
    final=sorted(final)
    for char in final:
        last+= char
    shuffled=[]
    include=""
    for letter in last:
        shuffled.append(letter)
    random.shuffle(shuffled)
    shuffle.randomized="".join(shuffled)

def ts(x):
    from engine import load
    srtscm = "".join(sorted(x))
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
    for b in range(len(load.d)):
        for i in range(len(load.d[b])):
            word = load.d[b]
            if word[i] in tot:
                if x.count(word[i]) < word.count(word[i]):
                    break
                elif x.count(word[i]) >= word.count(word[i]):
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
    ts.TS = sum(score)

def compute(res):
    a1 = "eaionrtlsu"
    a2 = "dg"
    a3 = "bcmp"
    a4 = "fhvwy"
    a5 = "k"
    a8 = "jx"
    a10 = "qz"
    compute.score = []
    for c in res:
        if c in a1:
            compute.score.append(1)
        elif c in a2:
            compute.score.append(2)
        elif c in a3:
            compute.score.append(3)
        elif c in a4:
            compute.score.append(4)
        elif c in a5:
            compute.score.append(5)
        elif c in a8:
            compute.score.append(8)
        elif c in a10:
            compute.score.append(10)
    compute.total = sum(compute.score)


def ang():
    import random
    load()
    ang.word = random.choice(load.d)
    ang.possible = []
    ang.anagram = []
    while len(ang.word) < 5:
        ang.word = random.choice(load.d)
    def anag():
        for a in range(len(load.d)):
            if len(load.d[a]) == len(ang.word):
                ang.possible.append(load.d[a])
        for b in range(len(ang.possible)):
            if sorted(ang.word) == sorted(ang.possible[b]):
                ang.anagram.append(ang.possible[b])
            else:
                continue
    while len(ang.anagram) < 3:
        ang.word = random.choice(load.d)
        while len(ang.word) < 5:
            ang.word = random.choice(load.d)
        ang.possible = []
        ang.anagram = []
        anag()
    for a in ang.anagram:
        if a == ang.word:
            ang.anagram.remove(a)
    ang.final = "".join(ang.anagram)
    compute(ang.final)
    ang.tot = len(ang.anagram)
    ang.score = 0
    ang.life = 3
    ang.correct = []
    ang.incorrect = []
    while ang.life != 0 and ang.score <= ang.tot:
        if ang.life == 0:
            print("=============================================================")
            print("Uwurd Unscwambler <3")
            print("ANAGWAMS MODE!!!")
            print("heart:", ang.life)
            print("score:", ang.score, "/", ang.tot)
            print("Find the anagrams for:", ang.word)
            print()
            print("GAME OVER!")
        elif ang.score == ang.tot:
            print("=============================================================")
            print("Uwurd Unscwambler <3")
            print("ANAGWAMS MODE!!!")
            print("heart:", ang.life)
            print("score:", ang.score, "/", ang.tot)
            print()
            print("Anagrams for " + '"' + ang.word + '"' + ": ", end="")
            for x in range(len(ang.correct)):
                if x == len(ang.correct)-1:
                    print(ang.correct[x])
                else:
                    print(ang.correct[x] + ", ", end="")
            print()
            print("Whoa! You really found all the anagwams! Congwats UwU!")
            break
        else:
            print("=============================================================")
            print("Uwurd Unscwambler <3")
            print("ANAGWAMS MODE!!!")
            print("heart:", ang.life)
            print("score:", ang.score, "/", ang.tot)
            print()
            #print(ang.anagram)
            print("Find the anagrams for:", ang.word)
            if len(ang.correct) != 0:
                print("Correct guesses: ", end="")
                for x in range(len(ang.correct)):
                    if x == len(ang.correct)-1:
                        print(ang.correct[x])
                    else:
                        print(ang.correct[x] + ", ", end="")
            else: 
                print("Correct guesses: ")
            if len(ang.incorrect) != 0:
                print("Incorrect guesses: ", end="")
                for x in range(len(ang.incorrect)):
                    if x == len(ang.incorrect)-1:
                        print(ang.incorrect[x])
                    else:
                        print(ang.incorrect[x] + ", ", end="")
            else:
                print("Incorrect guesses: ")
            print()
            print("Your guess: ", end="")
            inp = str(input())
            if inp in ang.anagram:
                ang.correct.append(inp)
                compute(inp)
                ang.score += 1
            else:
                ang.incorrect.append(inp)
                print("Oh no! That's wrong!")
                ang.life-=1

def cmb():
    load()
    ca()
    shuffle(ca.w)
    cmb.scramble = shuffle.randomized
    ts(shuffle.randomized)
    cmb.chk=""
    for n in cmb.scramble:
        if n not in cmb.chk:
            cmb.chk+=n
        else:
            continue
    cmb.tot = ts.TS

def guess(x):
    guess.gu = str(input("Your guess: "))
    if guess.gu in load.d:
        for i in range(len(guess.gu)):
            if guess.gu[i] in x:
                if cmb.scramble.count(guess.gu[i]) < guess.gu.count(guess.gu[i]):
                    guess.res = "False"
                    break
                else:
                    if i == len(guess.gu)-1:
                        guess.res = "True"
                    else:
                        continue
            else:
                guess.res = "False"
                break
    else:
        guess.res = "False"
