
import random
from words import words
import string


def get_valid_word(words):
  valid_word = random.choice(words)
  while ' ' in valid_word or '_' in valid_word:
    valid_word = random.choice(words)
  return valid_word


def hangman():
  word = get_valid_word(words).upper()
  print(word)
  
  word_letters = set(word)
  
  alphabet = set(string.ascii_uppercase)
  
  used_letters = set()
  
  lives = 6
  
  while len(word_letters) > 0 and lives > 0:
    print(f"\nYou have got {lives} left.")
    print("You have used these letters : " + " ".join(used_letters))
    
    word_list = [letter if letter in used_letters else "_" for letter in word]
    print("Current word : ", ' '.join(word_list))
    
    user_input = input("Guess a letter : ").upper()
    
    if user_input in alphabet - used_letters:
      used_letters.add(user_input)
      if user_input in word_letters:
        word_letters.remove(user_input)
      else:
        lives -= 1
    else:
      print("You have used that letter already. Try another.")
  
  if lives == 0:
    print("You died. Correct word = " + word)
  else:
    print(f'You guess the word {word} correctly.')
    
    

hangman()