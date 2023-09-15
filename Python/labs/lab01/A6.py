# Write a program that generate a multiplication table from 1 to th number passed.


def multiplication_table(n):

    table = []

    for i in range(1, n+1):

        row = []

        for j in range(1, i+1):

            row.append(i*j)

        table.append(row)

    return table


n = 5
table = multiplication_table(n)
print()
print(table)
print()