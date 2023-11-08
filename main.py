import random as r

guesses = 0
number = r.randint(1,10)

while True:
    q1=int(input("Guess the number(1,10): "))
    
    if q1==number:
        print(f"\nright, the number was {number}!")
        number = r.randint(1,10)
        guesses=0

        rep=str(input("\nDo you want to play again?(y/..): ")).lower()

        if rep=="y":
            print(" ")
        else:
            break
            
    elif q1>10:
        print("\nYou can choose only numbers ranging from 1 to 10.\n")        

    else:
        guesses+=1
        if q1<number and guesses==3:
            pass
        elif q1>number and guesses==3:
            pass
        elif q1<number:
            print("\nGuess higher.\n")
        elif q1>number:
            print("\nGuess lower.\n")
          
            

    if guesses==3:
        guesses=0
        print(f"\nYou lost, the number was {number}!")
        
        rep=str(input("\nDo you want to play again?(y/..): ")).lower()
        number = r.randint(1,10)
        
        if rep=="y":
            print(" ")
        else:
            break
               