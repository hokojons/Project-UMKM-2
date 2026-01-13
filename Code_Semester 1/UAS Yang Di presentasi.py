class Train:
    def __init__(self, train_number, destination, seats, ticket_price):
        self.train_number = train_number
        self.destination = destination
        self.seats = seats
        self.booked_seats = 0
        self.passenger_info = {}
        self.ticket_price = ticket_price

    def book_ticket(self, total_ticket, passenger_name, seat_number):
        if self.booked_seats + total_ticket <= self.seats:
            for seat in seat_number:
                if seat in self.passenger_info:
                    print(f"Seat {seat} is already booked!")
                    return
            self.booked_seats += total_ticket
            for seat in seat_number:
                self.passenger_info[seat] = passenger_name
            total_price = total_ticket * self.ticket_price
            print(f"{total_ticket}Ticket berhasil dipesan untuk {self.train_number}  to {self.destination} for {passenger_name}. Total price: ${total_price}.")
        else:
            print("Not enough seats available.")

    def available_seats(self):
        return self.seats - self.booked_seats

    def get_available_seat_numbers(self):
        return [str(i) for i in range(1, self.seats + 1) if str(i) not in self.passenger_info]

class TicketBookingSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def display_trains(self):
        print("Available Trains:")
        for train in self.trains:
            print(f"Train Number: {train.train_number}, Destination: {train.destination}, Available Seats: {train.available_seats()}, Ticket Price: ${train.ticket_price}")

    def book_ticket(self, train_number, number_of_tickets, passenger_name, seat_numbers):
        for train in self.trains:
            if train.train_number == train_number:
                train.book_ticket(number_of_tickets, passenger_name, seat_numbers)
                return
        print("Train not found!")

def main():
    system = TicketBookingSystem()

    system.add_train(Train("101", "Jakarta", 100, 50)) 
    system.add_train(Train("102", "Bandung", 100, 30))
    system.add_train(Train("103", "Surabaya", 100, 40))
    system.add_train(Train("104", "Jokjakarta",100,90))

    while True:
        print("\n--- Ticket Booking System ---")
        system.display_trains()
        train_number = input("Enter train number to book tickets (or 'exit' to quit): ")
        if train_number.lower() == 'exit':
            break
        number_of_tickets = int(input("Enter number of tickets to book: "))
        passenger_name = input("Enter your name: ")

        # available seats in train
        for train in system.trains:
            if train.train_number == train_number:
                available_seats = train.get_available_seat_numbers()
                print(f"Available seats for train {train_number}: {', '.join(available_seats)}")
                break

        while True:
            seat_numbers = input("Enter seat numbers you want to book (comma separated): ").split(',')
            seat_numbers = [seat.strip() for seat in seat_numbers]  
            
            # Check Kursi
            available_seats = train.get_available_seat_numbers()
            if len(seat_numbers) != number_of_tickets:
                print(f"You must select exactly {number_of_tickets} seats. Please try again.")
            elif not all(seat in available_seats for seat in seat_numbers):
                print(f"Some of the selected seats are not available. Available seats are: {', '.join(available_seats)}. Please try again.")
            else:
                system.book_ticket(train_number, number_of_tickets, passenger_name, seat_numbers)
                break  # Exit


if __name__ == "__main__":
    main()