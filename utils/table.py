class Seat:
    """
    Class to define a seat object.
    
    Parameters:

    - free: contains the information if there is or not anybody
    - occupant: contains the name of the person who seat there

    Methods:

    - set_occupant(self, name): check the status of free parameter
    and if it's True (means the seat is free) set the occupant name
    to the provided name and than set the status of free parameter
    to False.

    - remove_occupant(self, name): if seat is occupied store the
    the name of the last occupant in a variable last_occupant and
    set the occupant parameter to None, than return the last
    occupants name
    """

    def __init__(self, free: bool, occupant: str):
        self.free = free
        self.occupant = occupant

    def __str__(self):
        if self.free:
            return("Free seat")
        else:
            return(f"Seat of {self.occupant}")

    def set_occupant(self, name):
        if self.free == True:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        if self.free == False:
            last_occupant = self.occupant
            self.occupant = None
            self.free = True
            return(last_occupant)
        



class Table:
    """
    Class to define a table object.

    Parameters: capacity (number of seats in total) must be an integer.

    Methods: 

    - has_free_spot(self): returns True if there is at least 1 free seat,
    otherwise returns False.

    - assign_seat(self, name): assign a person to a free seat if there is
    a free seat available.

    - left_capacity(self): returns an integer of free seats left.  
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Creates (capacity) times Seat(free = True, occupant = None) objects
        #and asign it to the seats variable
        self.seats = [Seat(True, None) for _ in range(capacity)]

    def __str__(self):
        return(f"A table with {self.capacity} seats") 

    def has_free_spot(self) -> bool:
        for seat in self.seats:
            if seat.free:
                return(True)
        else:
            return(False)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                # using the method from set_occupant from the Seat class
                seat.set_occupant(name)
                # avoids assigning of a person to every free seat.
                break

    def left_capacity(self) -> int:
        seats_left = 0
        for seat in self.seats:
            if seat.free:
                seats_left += 1
        return(seats_left)
