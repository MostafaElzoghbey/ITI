# Write a function which has an input of a string from user then it
# will return the same string reversed.


def rev_string():

    string = input("Enter your string: ")
    output = ""

    for i in range(len(string) - 1, -1, -1):

        output = output + string[i]

    return output


result = rev_string()
print("\n", result, "\n")
