import random
guessesTaken = 0

name = input("Hello, what is your name?")

number = random.randint(1, 20)
print("well, " + name + ", i am thinking of a number between 1 and 20.")

while guessesTaken < 20:
    print ("take a guess") 
    guess = input ()
    guess = int (guess)

    guessesTaken = guessesTaken + 1
    if guess < number:
        print ("Your number is too low.") 
    if guess > number:
               print ("your number is too high.")
    if guess == number:
           guessesTaken = str(guessesTaken)
           print("Well Done, " + name + "! you guessed my number in " + guessesTaken + " guesses")
if guess != number:
           number = str (number)
           print ("No. The number I was thinking of was" + number) 
