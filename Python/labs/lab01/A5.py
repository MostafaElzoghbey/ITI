# Write a program that prints the locations of "i" character in any string you added.


s = "01234i6i"
j = 0
print()

for i in range(len(s)):
    
    if s[i] == "i":
        
        j += 1
        print("location number {n} of i is".format(n = j), i)


print()
