# Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.


def input_elements_TOarray(numberOfElements):

    arr = []

    for i in range(numberOfElements):

        arr.append(input("Enter your element {n}: ".format(n=i + 1)))
        
	
    print("\nUser array:                    ", arr)
    arr.sort()
    print("User array in ascending order: ", arr)
    arr.sort(reverse=True)
    print("User array in descending order:", arr, "\n")


input_elements_TOarray(5)



