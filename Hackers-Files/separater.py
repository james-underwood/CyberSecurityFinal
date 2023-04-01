import os
import csv

if not os.path.exists("separated"):
    os.mkdir("separated")

with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        method = row[2]
        filename = os.path.join("separated", method + '.txt')
        with open(filename, 'a') as f:
            f.write(row[3] + '\n')
