#number guessing game it is!!
import random

noofguesses=0
number=random.randint(1,20)

print("HELLO  !WELCOME,WHAT IS YOUR NAME PLAYER?")
name=input()


while noofguesses < 5:
  print(' WELL '+name+' I AM THINKING OF THE NUMBER')
  print(" TAKE A GUESS!!!!")
  guess=input()
  guess=int(guess)
  noofguesses=noofguesses+1

  if guess < number:
   print("SORRY! NUMBER GUESSED IS TOO LOW")

  if guess > number:
   print("SORRY! NUMBER GUESSED IS HIGH")

  if guess==number:
   break

if guess == number:
  noofguesses=str(noofguesses)
  print("CONGRATS!!,"+name+" YOU GUESSED THE SECRET NUMBER "+" IN "+noofguesses+" ATTEMPTS!");

if guess != number:
    number=str(number)
    print("SORRY!YOU LOOSE ,THE NUMBER I WAS THINKING WAS "+number)
 
