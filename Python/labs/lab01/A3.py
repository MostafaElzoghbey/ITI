# Write a program that prints the number of times the string 'iti' occurs in anystring.


def number_of_iti(str):

    count = str.count('iti')

    print("The number of times the string 'iti' occurs in this string:", count)


str = "iti iti iti 3 times iti iti and 2 equal 5 times"

number_of_iti(str)
