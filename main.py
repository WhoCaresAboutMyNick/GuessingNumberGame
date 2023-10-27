import random as r

guesses = 0
number = r.randint(1,10)

while guesses<3:
	q1=int(input("Guess the number(1,10): "))

	if q1==number:
		print(f"right, the number was {number}!")
		number = r.randint(1,10)
		guesses=0

		rep=str(input("Do you want to play again?(y/n): ")).lower()

		if rep=="y":
			pass
		else:
			break

	else:
		print("wrong")
		guesses+=1

	if guesses==3:
		guesses=0
		print(f"You lost, the number was {number}!")

		rep=str(input("Do you want to play again?(y/n): ")).lower()
		number = r.randint(1,10)
		
		if rep=="y":
			pass
		else:
			break
