from table import Table
from random import shuffle

class Openspace:
    def __init__(self, number_of_tables: int):
        self.number_of_tables = number_of_tables
        self.tables = [Table(4) for _ in range(number_of_tables)]

    def __str__(self):
        return(f"Openspace with {self.number_of_tables} tables, 4 seats each.")

    def organize(self, names):
        shuffle(names) # Randomizes the order of names
        for name in names:
            













            

    def display(self):
        pass

    def store(filename):
        pass




def organize(self, names):
    shuffle(names)  # Randomizes the order of names
    for name in names:
        assigned = False
        for table in self.tables:
            if table.has_free_spot():
                table.assign_seat(name)
                assigned = True
                break  # Break out of the loop once the name is assigned
        if not assigned:
            print(f"Not enough seats for {name}.")
            break  # Optional: Stop assigning if you run out of seats
