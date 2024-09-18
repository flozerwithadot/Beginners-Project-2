import random

def forestgame():
    print("a wild monkey appears! guess all 5 fruits correctly to pass")
    fruits = ["apple", "banana", "orange", "kiwifruit", "blueberry"]
    correct = []
    while True:
        guess = input("guess a fruit: ")
        if len(correct) == 4:
            print("you guessed all 5 fruits correctly!")
            break
        elif guess in fruits:
            fruits.remove(guess)
            correct.append(guess)
            print(f"{guess} is one of the fruits! correct guesses: {correct}")
        else:
            print(f"incorrect :( correct guesses: {correct}")
    height = int(input("you come across a hungry tiger! the only way through is to cross a river. enter your height: "))
    if height < 160:
        print("you drown :(")
        exit()
    elif height > 180:
        print("the tiger spots you rip :(")
    else:
        print("you live :)")
    
    password = randint(1000, 9999)
    print(password)
    tries = 0
    passguess = int(input("there is a door that requires a 4-digit password"))
    if code == password:
        print("you guessed correctly! yippee")
        nextgame == input("would you like to play the other game? (yes/no): ")
        if nextgame == yes:
            quiz()
    else:
        print("thanks for playing! :3")
            
def quiz():
	quizcorrect = 0
	quizincorrect = 0
	comments = ["0/6, how does one even manage to get this bad...", "1/6... at least you're smarter than ben", "2/6, womp womp", "3/6... side eye.", "4/6, not bad", "5/6, so close!!", "all correct yippee!! :3"]
    
    print("what is the capital of france?")
    q1ans = input("a) Lisbon  b) Rome  c) Paris  d) Berlin")
	if q1ans == c:
		quizcorrect = quizcorrect + 1
	else:
		quizincorrect = quizincorrect + 1
	
	print("which element has the chemical symbol O?")
	q2ans = input("a) oxygen  b) nitrogen  c) gold  d) hydrogen")
	if q1ans == a:
		quizcorrect = quizcorrect + 1
	else:
		quizincorrect = quizincorrect + 1
	
	print("what is the solution to the equation 2x + 3 = 11?")
	q3ans = input("a) 5  b) 4  c) 6  d) 3")
	if q1ans == b:
		quizcorrect = quizcorrect + 1
	else:
		quizincorrect = quizincorrect + 1
	percentage = quizcorrect/6*100
	comment = comments.index(quizcorrect)
	print(f"you answered {quizcorrect} questions correct and {quizincorrect} questions wrong. your accuracy is {percentage}% ({comment})")
	
            
choice = random.choice([forestgame, quiz])
if choice == forestgame:
    forestgame()
else:
    quiz() 
