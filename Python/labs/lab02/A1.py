# Write a function that accepts two arguments (length, start) to 
# generate an array of a specific length filled with integer numbers
# increased by one from start.


def generate_array(length, start):
    
    arr = []

    for i in range(length):
        
        arr.append(start + i)
        
    print("\n", arr, "\n")


start = 11
length = 20

generate_array(length, start)
