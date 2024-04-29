import random

words = ["apple", "tea", "omega", "football"]
random_word = random.choice(words)
display_word = ["_"] * len(random_word)

hangman = [
  """
    x-------x
          |
          |
          |
         ===""",
  """
    x-------x
    O       |
          |
          |
         ===""",
  """
    x-------x
    O       |
    |       |
          |
         ===""",
  """
    x-------x
    O       |
   /|       |
          |
         ===""",
  """
    x-------x
    O       |
   /|\      |
          |
         ===""",
  """
    x-------x
    O       |
   /|\      |
   /        |
         ===""",
  """
    x-------x
    O       |
   /|\      |
   / \      |
         ==="""
]

lives = len(hangman) - 1

while True:
    print("\n" + hangman[lives])
    print(' '.join(display_word))
    guess = input("Guess a letter: ")
    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                display_word[i] = guess
        if "_" not in display_word:
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        lives -= 1
        if lives == 0:
            print("You've run out of lives! Game Over.")
            print(f"The word was: {random_word}")
            break