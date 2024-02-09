import csv

from utils.openspace import Openspace

def read_names_from_csv(path):
    names = []
    with open(path, newline='') as csvfile:
        for row in csvfile:
            names.append(row[0]) # make sure that names are in the first column
    return(names)

openspace = Openspace(6)

names = read_names_from_csv('utils/new_colleagues.csv')

result = openspace.organize(names)

if result is not None:
    print(result)

openspace.display()

openspace.store('seating_arrangement.xlsx')
