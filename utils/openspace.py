import pandas as pd
from random import shuffle

from table import Table

class Openspace:
    """
    Class to define an open space object

    Parameters: number_of_tables -> must be an integer

    Methods:

    - organize(self, names): Randomize the order of names and assign each name
    to a table if there a free spot, otherwise appends the name to not_assigned
    list and print all names who wasn't assigned in a user friendly form.

    - display(self): Print each table with an index of a table (starts from 1)
    and occupants on each table. If table is empty returns:'Nobody seats here'.

    - store(self.filename): Initialize a list to store data, after that adds
    dictionaries inside of a the list, which will be converted into Pandas
    DataFrame, after exports the DataFrame to an Excel file and prints the
    message with the file name, where it was exported.
    """

    def __init__(self, number_of_tables: int):
        self.number_of_tables = number_of_tables
        self.tables = [Table(4) for _ in range(number_of_tables)]


    def __str__(self):
        return(f"Openspace with {self.number_of_tables} tables, 4 seats each.")
    

    def organize(self, names):
        shuffle(names) # Randomizes the order of names
        not_assigned = []

        for name in names:

            succesfully_assigned = False
            for table in self.tables:
                # iterate through all tables to find a free seat
                if table.has_free_spot():
                    table.assign_seat(name)
                    succesfully_assigned = True
                    break # avoids multiple assigning for each person.
            # adds the name of person to the list with people without a seat
            if not succesfully_assigned:
                not_assigned.append(name)
        # checks if there are people in not_assigned list and return message
        # that includes all names of people who don't have a seat.          
        if len(not_assigned) > 0:
            message = "There is no place for " + ", ".join(not_assigned)
            return(message)
        else:
            return(None)


    def display(self):
        for i, table in enumerate(self.tables, start=1):
            occupants = [seat.occupant for seat in table.seats if seat.occupant is not None]
            if occupants:
                occupants_string = ', '.join(occupants)
                print(f"Table {i}: {occupants_string}")
            else:
                print(f"Table {i}: Nobody seats here.")
    
    def store(self, filename):
        # Initialize a list to store data
        data = []

        # Iterate through tables and seats to gather data
        for i, table in enumerate(self.tables, start=1):
            for seat in table.seats:
                # Assuming each seat has an 'occupant' attribute
                # Append a dictionary for each occupant to the data list
                data.append({'Table Number': i, 'Occupant Name': seat.occupant or 'Empty'})

        # Create a DataFrame from the data list
        df = pd.DataFrame(data)

        # Export the DataFrame to an Excel file
        df.to_excel(filename, index=False)

        print(f"Seating arrangement saved to {filename}.")
