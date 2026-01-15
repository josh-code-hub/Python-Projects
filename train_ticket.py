import random
from datetime import datetime, timedelta

# Destination → Travel time (minutes)
travel_times = {
    "ibadan": 15,
    "ilorin": 25,
    "abuja": 45,
    "port harcourt": 40,
    "abeokuta": 9
}

# Destination → Base price (Naira)
base_prices = {
    "ibadan": 11000,
    "ilorin": 12900,
    "abuja": 15000,
    "port harcourt": 13500,
    "abeokuta": 5000
}

# Total rows
TOTAL_ROWS = 100

# Generate all seats (row 1–100, seat 1–6)
available_seats = [(row, seat) for row in range(1, TOTAL_ROWS + 1) for seat in range(1, 7)]

print("=== TRAIN TICKET ISSUER ===")

# Passenger details
name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))

# Age restriction check
if age < 15:
    print("Passenger is under 15 years old.")
    guardian_age = int(input("Enter accompanying adult's age (must be 18+): "))
    if guardian_age < 18:
        print("\n*** Cannot issue ticket: Guardian must be 18 or older ***")
        exit()
    else:
        print("Guardian confirmed. Proceeding with ticket issuance.")

# Destination
destination = input("Enter destination: ").lower()

# Validate destination
if destination not in travel_times:
    print("\n*** LOCATION NOT LISTED ***")
    exit()

# Ask user to pick class
print("\nAvailable Classes:")
print("1. First Class (+₦10,000)")
print("2. Business Class (+₦5,000)")
print("3. Economy Class (base price)")

class_choice = input("Enter your class choice (first/business/economy): ").lower()

if class_choice == "first":
    travel_class = "First Class"
    class_surcharge = 10000
    # Assign row in 1-20
    row = random.randint(1, 20)
elif class_choice == "business":
    travel_class = "Business Class"
    class_surcharge = 5000
    # Assign row in 21-40
    row = random.randint(21, 40)
elif class_choice == "economy":
    travel_class = "Economy Class"
    class_surcharge = 0
    # Assign row in 41-100
    row = random.randint(41, 100)
else:
    print("\n*** Invalid class choice ***")
    exit()

# Assign seat (1-6)
seat = random.randint(1, 6)
if (row, seat) in available_seats:
    available_seats.remove((row, seat))
else:
    # fallback if seat already taken
    seat = random.choice([s for r, s in available_seats if r == row])
    available_seats.remove((row, seat))

# Show price
base_price = base_prices[destination]
final_price = base_price + class_surcharge
print(f"\nThe price for {travel_class} to {destination.title()} is: ₦{final_price}")

# Confirm booking
confirm = input("Do you want to book this ticket? (yes/no): ").lower()
if confirm != "yes":
    print("Booking cancelled.")
    exit()

# Get departure time
departure_input = input("Enter departure time (HH:MM, 24-hour format): ")
departure_time = datetime.strptime(departure_input, "%H:%M")

# Calculate arrival time
duration_minutes = travel_times[destination]
arrival_time = departure_time + timedelta(minutes=duration_minutes)

# Print Ticket
print("\n====================================")
print("             TRAIN TICKET")
print("====================================")
print(f"Passenger Name : {name}")
print(f"Age            : {age}")
print(f"Destination    : {destination.title()}")
print(f"Class          : {travel_class}")
print(f"Row & Seat     : Row {row}, Seat {seat}")
print(f"Ticket Price   : ₦{final_price}")
print("------------------------------------")
print(f"Departure Time : {departure_time.strftime('%H:%M')}")
print(f"Arrival Time   : {arrival_time.strftime('%H:%M')}")
print(f"Duration       : {duration_minutes} minutes")
print("====================================")
print("     WISHING YOU A SAFE JOURNEY!")
print("====================================")
