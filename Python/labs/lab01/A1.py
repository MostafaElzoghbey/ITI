# Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.


def count_number_vowels(str):

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in range(len(str)):

        if str[i] in vowels:

            count += 1

    print("The number of vowels in this string is: ", count)


str = "Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.iiiooo"

count_number_vowels(str)
