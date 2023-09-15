# Write a program that remove all vowels from the input word and generate a brief version of it.


def remove_vowels():

    inp = input("Enter your word: ").strip()
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in vowels:

        inp = inp.replace(i, "")

    print("\nThe string after remove all vowels:", inp, "\n")


remove_vowels()
