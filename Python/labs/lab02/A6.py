# Write a program which repeatedly reads numbers until the user
# enters “done”.
# Once “done” is entered, print out the total, count, and
# average of the numbers.
# If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.


def numbers():

    count = 0
    total = 0

    while True:

        user_input = input("Enter a number or 'done' to exit: ")

        if user_input.lower().strip() == "done":

            break

        try:
            number = float(user_input)
            total += number
            count += 1

        except:
            print("Invalid input. Please enter a number or 'done'.")

    if count == 0:

        print("No numbers were entered.")

    else:
        average = total / count
        print("Total:", total)
        print("Count:", count)
        print("Average:", average)


numbers()
