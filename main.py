import csv
import argparse

from utils.openspace import Openspace

# Setup argparse
parser = argparse.ArgumentParser(description='OpenSpace Organizer')
parser.add_argument('filepath', help='The filepath of the CSV file containing the list of colleagues.')
args = parser.parse_args()

def read_names_from_csv(filepath):
    names = []
    with open(filepath, newline='') as csvfile:
        for row in csv.reader(csvfile):
            names.append(row[0]) # make sure that names are in the first column
    return(names)

openspace = Openspace(6)

names = read_names_from_csv(args.filepath)

result = openspace.organize(names)

if result is not None:
    print(result)


openspace.display()
print()

# Count and display the total free seats left
total_free_seats = 0
for table in openspace.tables:
    for seat in table.seats:
        # Check if the seat is free by checking if the occupant is None
        if seat.occupant is None:
            total_free_seats += 1
print(f"Total free seats left: {total_free_seats}")

print()

openspace.store('seating_arrangement.xlsx')
