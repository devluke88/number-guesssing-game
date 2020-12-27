import random
from art import logo
print(logo)
print("Welome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
# print(f"Correct answer: {number}")

# Fuction to guess the number, where as an argument we provide our level of choice - 'easy' or 'hard'
def level(choice):
    level_dict = {
      "easy": 10,
      "hard": 5
    }
    print(f"Run {choice}")
    remaining_lives = level_dict[choice]
    while remaining_lives > 0:
        print(f"You have {remaining_lives} attempts remaining to guess the numer.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        else:
            remaining_lives -= 1
            if guess > number:
                print("Too high.")
            else:
                print("Too low.")
            if remaining_lives == 0:
                print("You've run out of guesses, you lose.")
                break
            else:
                print("Guess again.")

# Play game function
def play_game():
  want_play = True
  while want_play:
      # Get level choice from the user 
      choose_level = input("Choose a diffuculty. Type 'easy' or 'hard': ").lower()
      if choose_level == 'easy' or choose_level == 'hard':
          level(choose_level)   
      else:
          print("Your answer was not 'easy' or 'hard'. Please choose level of difficulty again!")
          continue
      want_play = False

play_game()