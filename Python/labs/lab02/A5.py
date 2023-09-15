# Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in
# alphabetical order is: abdu


def longest_alphabetical_ordered_substring(string):

    longest = string[0]

    for i in range(1, len(string)):

        if longest[-1] <= string[i]:

            longest += string[i]

    print("\nThe original string is:", string)
    print("The longest ordered substring is:", longest, "\n")


string = 'abdulrahman'

longest_alphabetical_ordered_substring(string)
