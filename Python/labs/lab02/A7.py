# Word guessing game (hangman)

import random


def hangman():

    words = ["apple", "banana", "orange", "grape", "game"]
    print("Hangman GAME")
    Name = input("Enter your name: ")
    print(f"Hello {Name}, Let's play!")
    print("You should guess this letters of a word")
    r = random.randint(0, len(words) - 1)
    TheWord = words[r]
    Turns = 7
    AllUserLetters = []
    UserWord = '_'*len(TheWord)
    win = 0

    while Turns > 0:

        print()
        print(f"TheWord: {UserWord}")
        print(f"Turns left: {Turns}")
        Letter = input("Guess a letter: ").lower()

        if not Letter.isalpha() or len(Letter) != 1:

            print("\n***This is not a letter***")
            continue

        if Letter not in AllUserLetters:

            AllUserLetters.append(Letter)
            Turns -= 1

        else:
            print("\n***You have entered this letter before***")
            continue

        UserWord = ''
        for Let in TheWord:

            if Let in AllUserLetters:

                UserWord += Let

            else:
                UserWord += '_'

        if UserWord == TheWord:

            print(
                f"\ncongratulation {Name}, you guessed the word correctly!\n")
            win = 1
            break

        if Turns != 0:

            if Letter in TheWord:

                print("\nCorrect guess!")
            else:
                print("\nWrong guess!")

    if win == 0:

        print("\nGame over! The word was: " + TheWord, "\n")


hangman()
