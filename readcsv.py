import csv

with open('myfile.csv', 'r', newline='') as csvfile:
    # Create a reader object
    myreader = csv.reader(csvfile)

    # print(f"Header: {header}")

    for row in myreader:
        print(row)