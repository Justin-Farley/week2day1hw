# restaurant_menu = {
#     "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
#     "Main Course": {"Steak": 15.99, "Salmon": 13.99},
#     "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
# }
# thebev = {"Beverages": {"Lemonade": 1.99, "Tea": 2.22}}
# restaurant_menu.update(thebev)
# restaurant_menu["Main Course"]["Steak"] = 17.99

# if 'Bruschetta' in restaurant_menu["Starters"]:
#     removed = restaurant_menu["Starters"].pop('Bruschetta')
#     print("removed:", removed)
# else:
#     print("'Bruschetta' not found in Starters category.")

# print(restaurant_menu)

class Ticket:
    def __init__(self, ticket_id, customer_name, issue_description):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.status = "Open"

    def update_status(self, new_status):
        self.status = new_status

    def display_ticket(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Issue Description: {self.issue_description}")
        print(f"Status: {self.status}")
        print("-----------------------------")

class TicketManager:
    def __init__(self):
        self.tickets = {}
        self.ticket_count = 0

    def add_ticket(self, customer_name, issue_description):
        self.ticket_count += 1
        new_ticket = Ticket(self.ticket_count, customer_name, issue_description)
        self.tickets[self.ticket_count] = new_ticket
        return new_ticket

    def update_ticket_status(self, ticket_id, new_status):
        if ticket_id in self.tickets:
            self.tickets[ticket_id].update_status(new_status)
        else:
            print(f"Ticket with ID {ticket_id} not found.")

    def resolve_ticket(self, ticket_id):
        if ticket_id in self.tickets and self.tickets[ticket_id].status == "Open":
            # No need to provide feedback, simply update status to "Closed"
            self.tickets[ticket_id].update_status("Closed")
        else:
            print(f"Ticket with ID {ticket_id} either not found or already closed.")

    def display_all_tickets(self):
        if not self.tickets:
            print("No tickets to display.")
        else:
            for ticket_id, ticket in self.tickets.items():
                ticket.display_ticket()


ticket_manager = TicketManager()

ticket1 = ticket_manager.add_ticket("Alice", "Login problem")
ticket2 = ticket_manager.add_ticket("Bob", "Payment issue")

ticket_manager.display_all_tickets()


ticket_manager.update_ticket_status(ticket1.ticket_id, "Open")

ticket_manager.display_all_tickets()

ticket_manager.resolve_ticket(ticket1.ticket_id)
ticket_manager.resolve_ticket(ticket2.ticket_id)

ticket_manager.display_all_tickets()






