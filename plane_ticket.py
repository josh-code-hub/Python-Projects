def calculate_ticket_price(distance, ticket_class):
    if ticket_class.lower() == "economy":
        return distance * 50
    elif ticket_class.lower() == "business":
        return distance * 100
    else:
        return "Invalid ticket class"

distance = float(input("Enter distance in km: "))
ticket_class = input("Enter ticket class (Economy/Business): ")

price = calculate_ticket_price(distance, ticket_class)
print("Ticket Price:", price)
