import random
from words import word_list

def get_word():
  word = random.choice(word_list)
  return word.upper()

def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("¡Juguemos ahorcado!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")

  # Check conditions
  while not guessed and tries > 0:
    guess = input("Por favor una letra o palabra: ").upper()
    # Check if is only one character
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("Ya has adivinado la letra ;)", guess)
      elif guess not in word:
        print(guess, "no está en la palabra :(")
        tries-=1
        guessed_letters.append(guess)
      else:
        print("¡Fantástico! ", guess, "está en la palabra ;)")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]

        for index in indices:
          word_as_list[index] = guess

        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True

    # Check if is a word
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("Ya has adivinado la palabra ;)", guess)
      elif guess != word:
        print(guess, "no es la palabra :(")
        tries-=1
        guessed_words.append(guess)
      else:
        guessed = True
        word_completion = word

    # Check if Other characters
    else:
      print("No es una opción válida :(")

    print(display_hangman(tries))
    print(word_completion)
    print("\n")

  if guessed:
    print("¡Genial, has adivinado la palabra! ¡Has ganado ;)!")

  else:
    print("Lo siento, has agotado tus intentos :(. La palabra era " + word + ". Suerte en la siguiente")

def display_hangman(tries):
  stages = [  # final state: head, torso, both arms, and both legs
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
            # head, torso, both arms, and one leg
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
            """,
            # head, torso, and both arms
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
            """,
            # head, torso, and one arm
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
            """,
            # head and torso
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
            """,
            # head
            """
                --------
                |      |
                |      O
                |
                |
                |
                -
            """,
            # initial empty state
            """
                --------
                |      |
                |
                |
                |
                |
                -
            """
  ]
  return stages[tries]

def main():
  word = get_word()
  play(word)

  while input("¿Jugar otra vez? (S/N)").upper() == "S":
    word = get_word()
    play(word)

if __name__ == "__main__":
  main()
