from tabulate import tabulate
import random
import string

# Dummy data for events and users
events = {
    "1": {
        "name": "Music Festival",
        "date": "2025-04-15",
        "venue": "Istora Senayan",
        "seating_categories": {
            "VIP": {"capacity": 500, "price": 1500000},
            "Tribune": {"capacity": 3000, "price": 750000},
            "General": {"capacity": 3700, "price": 500000}
        },
        "status": "Upcoming"
    },
    "2": {
        "name": "K-Pop Concert",
        "date": "2025-05-10",
        "venue": "Istora Senayan",
        "seating_categories": {
            "VIP": {"capacity": 700, "price": 2000000},
            "Tribune": {"capacity": 2500, "price": 1200000},
            "General": {"capacity": 4000, "price": 800000}
        },
        "status": "Upcoming"
    },
    "3": {
        "name": "keshi REQUIME World Tour",
        "date": "2025-02-23",
        "venue": "Istora Senayan",
        "seating_categories": {
            "VIP": {"capacity": 600, "price": 2500000},
            "CAT 1": {"capacity": 1500, "price": 1300000},
            "CAT 2": {"capacity": 3500, "price": 1000000}
        },
        "status": "Upcoming"
    },
    "4": {
        "name": "DAY6 3RD WORLD TOUR <FOREVER YOUNG> in JAKARTA 2025",
        "date": "2025-05-03",
        "venue": "Jakarta International Stadium",
        "seating_categories": {
            "VIP": {"capacity": 800, "price": 3500000},
            "CAT 1": {"capacity": 2000, "price": 2300000},
            "CAT 2": {"capacity": 3700, "price": 1500000}
        },
        "status": "Upcoming"
    },
    "5": {
        "name": "NIKI Buzz World Tour Jakarta",
        "date": "2025-02-16",
        "venue": "Beach City International Stadium",
        "seating_categories": {
            "VIP": {"capacity": 650, "price": 4000000},
            "CAT 1": {"capacity": 1500, "price": 2500000},
            "CAT 2": {"capacity": 2000, "price": 1800000}
        },
        "status": "Upcoming"
    }
}

past_events = {}

recycle_bin = {}

users = {
    "admin": {"password": "admin123", 
              "role": "admin"},
    "user1": {"password": "password", 
              "role": "customer", 
              "tickets": []}
}

#to generate ticket code
def generate_ticket_code():
    """Generate a random alphanumeric ticket code."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

#to help sort events by date using Insertion Sort
def insertion_sort(events_list):
    """Sort events by date using Insertion Sort."""
    for i in range(1, len(events_list)):
        key = events_list[i]
        j = i - 1
        while j >= 0 and events_list[j][1]["date"] > key[1]["date"]:
            events_list[j + 1] = events_list[j]
            j -= 1
        events_list[j + 1] = key
    return events_list

#to format the seating categories
def format_seating(seating_categories, is_admin = False):
    """Format seating categories for better readability."""
    if is_admin:
        return "\n".join([f"{cat}: {data['capacity']} seats, {data['price']} IDR" for cat, data in seating_categories.items()])
    else:
        return "\n".join([f"{cat}: {data['price']} IDR" for cat, data in seating_categories.items()])

#Added Feature for login and new user registration
def login():
    """Authenticate user login with a retry limit."""
    attempts = 0
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username]['password'] == password:
            print("Login successful!")
            return users[username]['role'], username # Return role and username
        
        print("Your username or password doesn't match. Please try again.")
        attempts += 1
        if attempts == 3:
            print("Login failed 3 times. Please try again later.")
            return None, None # Prevent further login attempts

def newUser():
    """Register a new user."""
    print("Register a new user:")
    new_username = input("Enter a new username: ")
    
    if new_username in users:
        print("Username already exists! Try a different one.")
        return
    
    new_password = input("Enter a new password: ")

    # Ask for user role (admin/customer) with validation
    while True:
        role = input("Enter user role (admin/customer): ").strip().lower()
        if role in ["admin", "customer"]:
            break
        
        print("Invalid role. Please enter 'admin' or 'customer'.")

    users[new_username] = {"password": new_password, "role": role, "tickets": [] if role == "customer" else None}
    
    print(f"User {new_username} registered successfully as {role}! Please log in.")

    # Automatically redirect to login after successful registration
    role, username = login()
    if role == "customer":
        customer_menu(username)
    
    elif role == "admin":
        admin_menu(username)

def create_event():
    """Create a new event."""
    event_id = input("Enter Event ID: ")
    if event_id in events:
        print("Event ID already exists!")
        return
    name = input("Enter Event Name: ")
    date = input("Enter Event Date (YYYY-MM-DD): ")
    venue = input("Enter Venue: ")
    seating_categories = {}
    categories_input = input("Enter Seating Categories (Format: Category:Capacity:Price,...): ")
    
    try:
        for category in categories_input.split(','):
            cat_name, cap, price = category.split(':')
            seating_categories[cat_name] = {"capacity": int(cap), "price": int(price)}
    except ValueError:
        print("Invalid seating category format! Use: Category:Capacity:Price,Category:Capacity:Price,...")
        return
    
    events[event_id] = {"name": name, "date": date, "venue": venue, "seating_categories": seating_categories, "status": "Upcoming"}
    print(f"Event '{name}' added successfully!")

def update_event():
    """Update an existing event."""
    event_id = input("Enter Event ID to update: ")
    if event_id not in events:
        print("Event not found.")
        return
    name = input(f"Enter new name [{events[event_id]['name']}]: ") or events[event_id]['name']
    date = input(f"Enter new date [{events[event_id]['date']}]: ") or events[event_id]['date']
    venue = input(f"Enter new venue [{events[event_id]['venue']}]: ") or events[event_id]['venue']
    
    events[event_id].update({"name": name, "date": date, "venue": venue})
    print(f"Event '{event_id}' updated successfully!")

def delete_event():
    """Move an event to the recycle bin instead of deleting it permanently."""
    event_id = input("Enter Event ID to delete: ")
    
    if event_id in events:
        recycle_bin[event_id] = events.pop(event_id)
        print(f"Event '{recycle_bin[event_id]['name']}' moved to recycle bin.")
    
    else:
        print(f"Event {event_id} not found!")

def restore_event():
    """Restore an event from the recycle bin or reinstate a canceled event."""
    event_id = input("Enter Event ID to restore: ")

    if event_id in recycle_bin:
        events[event_id] = recycle_bin.pop(event_id)
        events[event_id]["status"] = "Upcoming"
        print(f"Event '{event_id}' restored successfully and marked as Upcoming!")

    elif event_id in past_events and past_events[event_id]["status"] == "Cancel":
        events[event_id] = past_events.pop(event_id)
        events[event_id]["status"] = "Upcoming"
        print(f"Canceled event '{event_id}' reinstated and marked as Upcoming!")

    else:
        print(f"Event {event_id} not found or not eligible for restoration!")

def change_event_status():
    """Update the status of an event and move it if necessary."""
    event_id = input("Enter Event ID to update status: ")
    
    if event_id in recycle_bin:
        print("Cannot change status of a deleted event. Restore it first.")
        return
    
    if event_id not in events and event_id not in past_events:
        print("Event not found.")
        return
    
    new_status = input("Enter new status (Upcoming/Done/Cancel): ").strip().capitalize()
    
    if new_status not in ["Upcoming", "Done", "Cancel"]:
        print("Invalid status. Please enter 'Upcoming', 'Done', or 'Cancel'.")
        return
    
    if event_id in past_events:
        if new_status == "Upcoming" and past_events[event_id]["status"] == "Cancel":
            events[event_id] = past_events.pop(event_id)
            events[event_id]["status"] = "Upcoming"
            print(f"Event '{event_id}' reinstated and marked as Upcoming.")
            return
        else:
            print("Only canceled events can be reinstated.")
            return
    
    if new_status in ["Done", "Cancel"]:
        past_events[event_id] = events.pop(event_id)
    
    events[event_id]["status"] = new_status
    print(f"Event '{event_id}' status updated to '{new_status}'.")

def list_events(user_role="customer"):  # Default to customer view
    """Display all events with improved table formatting, adjusting for admin/customer view."""
    if not events:
        print("No events available.")
        return
    headers = ["ID", "Name", "Date", "Venue", "Seating Categories", "Status"]
    is_admin = user_role == "admin"
    table_data = [[event_id, event['name'], event['date'], event['venue'], format_seating(event['seating_categories'], is_admin), event['status']] for event_id, event in events.items()]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def view_deleted_events():
    """View events in the recycle bin."""
    combined_events = list({**past_events, **recycle_bin}.items())
    sorted_events = insertion_sort(combined_events)
    
    if not sorted_events:
        print("No past or deleted events available.")
        return
    
    table_data = [[event_id, data["name"], data["date"], data["status"]] for event_id, data in sorted_events]
    print(tabulate(table_data, headers=["Event ID", "Name", "Date", "Status"], tablefmt="rounded_outline"))


def search_events():
    """Search events by artist name or date, displaying only upcoming events."""
    keyword = input("Enter artist name or date (YYYY-MM-DD) to search: ")
    found_events = [event for event in events.values() if (keyword.lower() in event['name'].lower() or keyword == event['date']) and event['status'] == "Upcoming"]
    
    if found_events:
        headers = ["Name", "Date", "Venue", "Seating Categories", "Status"]
        table_data = [[event['name'], event['date'], event['venue'], event['seating_categories'], event['status']] for event in found_events]
        print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))
    
    else:
        print("No matching upcoming events found.")

def book_ticket(username):
    """Allow customers to book tickets for an event."""
    event_id = input("Enter Event ID to book: ")
    if event_id not in events:
        print("Event not found.")
        return
    
    print("Available seating categories:")
    
    categories = list(events[event_id]['seating_categories'].keys())
    for i, category in enumerate(categories, 1):
        cap = events[event_id]['seating_categories'][category]['capacity']
        price = events[event_id]['seating_categories'][category]['price']
        
        print(f"{i}. {category} (Capacity: {cap}, Price: {price})")
    
    try:
        category_choice = int(input("Select category number: ")) - 1
        if category_choice < 0 or category_choice >= len(categories):
            raise ValueError
        selected_category = categories[category_choice]
        
        if events[event_id]['seating_categories'][selected_category]['capacity'] <= 0:
            print("Sorry, this category is sold out.")
            return
        
        events[event_id]['seating_categories'][selected_category]['capacity'] -= 1
        ticket_code = generate_ticket_code()
        users[username]['tickets'].append({"event": event_id, "category": selected_category, "ticket_code": ticket_code})
        
        print(f"Ticket booked successfully! Your ticket code is {ticket_code}")
    
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid category number.")

def view_tickets(username):
    """Allow customers to view their booked tickets."""
    tickets = users[username]['tickets']
    if not tickets:
        print("No tickets found.")
        return
    
    headers = ["Event", "Category", "Ticket Code"]
    table_data = [[events[ticket['event']]['name'], ticket['category'], ticket['ticket_code']] for ticket in tickets]
    
    print("Your Booked Tickets: \n")
    print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))

def admin_menu(username):
    """Display the admin menu and handle admin actions."""
    while True:
        print("""
              Admin Menu:
              
              1. Create Event
              2. Update Event
              3. Delete Event
              4. Restore Event
              5. Change Event Status
              6. View Events
              7. View Deleted Events
              8. Logout
              """)
        choice = input("Enter your choice: ")
        if choice == "1":
            create_event()
        elif choice == "2":
            update_event()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            restore_event()
        elif choice == "5":
            change_event_status()
        elif choice == "6":
            list_events()
        elif choice == "7":
            view_deleted_events()
        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu(username):
    """Display the customer menu and handle customer actions."""
    while True:
        print("""
              Customer Menu:

              1. View Events
              2. Search Events
              3. Book Ticket
              4. View Tickets
              5. Logout
              """)
        choice = input("Enter your choice: ")
        if choice == "1":
            list_events()
        elif choice == "2":
            search_events()
        elif choice == "3":
            book_ticket(username)
        elif choice == "4":
            view_tickets(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main Menu
def main():
    """Main function to handle user login and menu navigation."""
    while True:
        print("""
              Welcome to the Ticketing System!

              Are you a registered user?
              1. Yes (Login)
              2. No (Register)
              Press E to exit the program.
              """)
        status = input("Enter your choice: ")
        
        if status.lower() == "yes" or status == "1":
            role, username = login()
            if role == "admin":
                admin_menu(username)
            elif role == "customer":
                customer_menu(username)
        elif status.lower() == "no" or status == "2":
            newUser()
        elif status.lower() == "e":
            print("Exiting system...\nGoodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSystem interrupted. Exiting...")