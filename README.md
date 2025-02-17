# Ticketing CRUD System Using Python 

## Overview
This is a Python-based event ticketing system that allows admins to manage events and customers to book tickets. It operates and supports CRUD operations for event management.

## Features
This CRUD system offers two main features which are explained below.

### Admin Feature:
The following are the details of the admin function. This feature's main job is to allow users to create, read, update, and delete events.

- **Create Event**: Add new events with seating categories and prices.
- **Update Event**: Modify event details.
- **Delete Event**: Move an event to the recycle bin.
- **Restore Event**: Recover a deleted event.
- **Change Event Status**: Mark events as `Upcoming`, `Done`, or `Canceled`.
- **View Events**: Display all available events.
- **View Deleted Events**: Show past and deleted events.

### Customer Functions:
The following are the details of the customer function. This feature's main job is to allow customers to log in, search for events, book tickets, and view them.

- **View Events**: List available events.
- **Search Events**: Find events by artist name or date.
- **Book Ticket**: Reserve a seat in an event.
- **View Tickets**: See booked tickets.

## Installation & Requirements
- Python 3.12.2
- Packages used:
    - `tabulate`
    - `random`
    - `string`

## User Flow:
1. **Login/Register**
   - Admin: Can manage events.
   - Customer: Can book and view tickets.
2. **Choose Actions from the Menu**
3. **Exit the system when done**

### Flowcharts for a better understanding of the user flow:
![CAPSTONE Module 1 Flowchart-Login](https://github.com/user-attachments/assets/297aa8e3-5ea7-4a66-8c0f-c4e9bf946081)

#### Admin Menu
![CAPSTONE Module 1 Flowchart-Admin Menu CRUD](https://github.com/user-attachments/assets/62690b82-789e-4e7b-aafb-585ae9f5d790)

![CAPSTONE Module 1 Flowchart-Create Event ADMIN](https://github.com/user-attachments/assets/a63b0c8e-f413-4f56-b5bf-b4a38352c827)

![CAPSTONE Module 1 Flowchart-Update Events ADMIN](https://github.com/user-attachments/assets/e96f04a2-0444-4393-944f-4989bf3920f8)

![CAPSTONE Module 1 Flowchart-Read Events (Upcoming) ALL](https://github.com/user-attachments/assets/50c44eb3-ff91-4622-9cd9-5239ae27a709)

![CAPSTONE Module 1 Flowchart-View Deleted and Canceled Events ADMIN](https://github.com/user-attachments/assets/8cea8a88-cd34-4cd3-ab59-0958929d3ba7)

![CAPSTONE Module 1 Flowchart-Change Event Status ADMIN](https://github.com/user-attachments/assets/8d9fb19f-59b4-4363-a9ee-8c7d9a5e50b1)

![CAPSTONE Module 1 Flowchart-Restore Deleted Events ADMIN](https://github.com/user-attachments/assets/d7323a0d-668d-4dc8-8060-2aef0376a621)

![CAPSTONE Module 1 Flowchart-Delete Events ADMIN](https://github.com/user-attachments/assets/759addbd-ffbb-4910-9076-03c2ecfb18e4)


#### Customer Menu
![CAPSTONE Module 1 Flowchart-Customer Menu](https://github.com/user-attachments/assets/1df07940-c4e4-4ebf-b567-459c2d5b5f4b)

![CAPSTONE Module 1 Flowchart-Book Ticket CUSTOMER](https://github.com/user-attachments/assets/ddd64bbd-67dc-49f2-a716-3307244ee8cb)

![CAPSTONE Module 1 Flowchart-View Tickets CUSTOMER](https://github.com/user-attachments/assets/166acd36-6595-4e6c-87b1-15b0ca7cac5a)

![CAPSTONE Module 1 Flowchart-Search Events CUSTOMER](https://github.com/user-attachments/assets/5fa93287-92a7-4192-85ab-584ba8f98907)


## Data Storage and Description

- Events are stored in a dictionary (`events`).
- Deleted events move to `recycle_bin`.
- Completed and canceled events move to `past_events`.
- Users are stored in the `users` dictionary.

## Error Handling
- Limits login attempts to **3 tries**.
- Prevents overbooking of tickets.

## Future Enhancements
This CRUD system is filled with bird holes thus future enhancements that can be done to make this CRUD system better and more robust are as follows:

- Implement a better error handling
- Optimize the code for better efficiency and readability
- Remove more redundancies

## License
This capstone project was created by Alexandra Andira to complete Purwadhika's Module 1 Data Science and Machine Learning Bootcamp.

Feel free to use and modify.
