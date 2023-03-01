import csv

with open("CodeCleaner/csv/unique_words.csv") as csvfile:
    reader = csv.reader(csvfile)
    first_column = [row[0] for row in reader]

x = first_column

# List to store data from CSV files
# import AllList
# x = AllList.data

a=[]
b=[]
for i in range(len(x)): #0-25
    for j in range(len(x[i])):
        a.append(str(ord(x[i][j].upper())))
    a = a + [0] * (25 - len(a))
    b.append(a)
    a=[]


with open('Mal.csv', 'w') as file:
    for row in b:
        file.write(','.join([str(x) for x in row]) + '\n')