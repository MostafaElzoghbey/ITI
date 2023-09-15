# Write a program that build a Mario pyramid


def build_pyramid(height):

    for i in range(1, height + 1):

        for j in range(height - i):

            print(" ", end='')

        for k in range(i):

            print("*", end='')

        print()


height = 15
build_pyramid(height)
