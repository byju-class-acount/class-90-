import random


number = random.randint(1, 9)


while True:
  guess = int(input("Guess a number between 1 and 9: "))

  
  if guess > number:
    print("Sorry your guess was too high.")
    break

  
  if guess < number:
    print("Sorry your guess was too low.")
    break

  
  print("You won good job!")
  break