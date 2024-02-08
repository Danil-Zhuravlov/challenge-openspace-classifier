from random import shuffle

from table import Table

class Openspace:
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


    def display(self):
        pass

    def store(filename):
        pass
