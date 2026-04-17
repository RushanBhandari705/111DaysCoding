#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:
    def __init__(self, name, total_seats, fare):
        self.name = name
        self.total_seats = total_seats
        self.fare = fare
        self.booked_seats = 0

    def book_ticket(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print(f"Ticket booked successfully! Remaining seats: {self.total_seats - self.booked_seats}")
        else:
            print("No seats available!")

    def get_status(self):
        print(f"Train: {self.name}, Total Seats: {self.total_seats}, Booked Seats: {self.booked_seats}, Available Seats: {self.total_seats - self.booked_seats}")

    def get_fare_info(self):
        print(f"Fare for train {self.name}: {self.fare} INR")