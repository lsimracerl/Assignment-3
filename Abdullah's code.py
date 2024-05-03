# I import necessary modules for my program.
import pickle  # For serializing and deserializing Python objects
from datetime import datetime  # For working with dates and times
import tkinter as tk  # For creating graphical user interfaces
from tkinter import ttk  # For additional Tkinter widgets
from tkinter import messagebox  # For displaying message boxes
import uuid  # For generating universally unique identifiers

# I define the Employee class with a constructor and a method to display employee details.
class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager_id):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id

    # I provide a method to display employee details in a formatted manner.
    def display(self):
        return {
            "Name": self.name,
            "Employee ID": self.employee_id,
            "Department": self.department,
            "Job Title": self.job_title,
            "Basic Salary": self.basic_salary,
            "Age": self.age,
            "Date of Birth": self.date_of_birth.strftime("%Y-%m-%d"),  # I format the date as a string
            "Passport Details": self.passport_details,
            "Manager ID": self.manager_id
        }

# I define the Client class with a constructor to initialize client details.
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

# I define the Guest class with a constructor and a method to display guest details.
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # I provide a method to display guest details in a formatted manner.
    def display(self):
        return {
            "Guest ID": self.guest_id,
            "Name": self.name,
            "Address": self.address,
            "Contact Details": self.contact_details
        }

# I define the GuestManager class with methods to manage guests.
class GuestManager:
    def __init__(self):
        self.address = None
        self.name = None
        self.client_id = None
        self.guests = {}  # I initialize a dictionary to store guests.
        self.load_guests()  # I load existing guests from a file during initialization.

    # I implement a method to add a guest.
    def add_guest(self, guest):
        if guest.guest_id in self.guests:
            raise KeyError("Guest ID already exists.")
        self.guests[guest.guest_id] = guest

    # I implement a method to delete a guest.
    def delete_guest(self, guest_id):
        if guest_id in self.guests:
            del self.guests[guest_id]
        else:
            raise KeyError("Guest not found.")

    # I implement a method to get details of a guest.
    def get_guest(self, guest_id):
        if guest_id in self.guests:
            return self.guests[guest_id].display()
        else:
            raise KeyError("Guest not found.")

    # I implement a method to save guests to a file.
    def save_guests(self):
        with open('guests.pkl', 'wb') as file:
            pickle.dump(self.guests, file)

    # I implement a method to load guests from a file.
    def load_guests(self):
        try:
            with open('guests.pkl', 'rb') as file:
                self.guests = pickle.load(file)
        except FileNotFoundError:
            self.guests = {}  # I create an empty dictionary if the file doesn't exist.

    # I provide a method to display client details.
    def display(self):
        return {
            "Client ID": self.client_id,
            "Name": self.name,
            "Address": self.address,
            "Contact Details": self.contact_details,
            "Budget": self.budget
        }
# I define the ClientManager class with methods to manage clients.
class ClientManager:
    def __init__(self):
        self.clients = {}  # I initialize an empty dictionary to store client data.
        self.load_clients()  # I load client data from a file.

    # I implement a method to add a client.
    def add_client(self, client):
        if client.client_id in self.clients:
            raise KeyError("Client ID already exists.")  # I check for duplicate client IDs before adding.
        self.clients[client.client_id] = client  # I add the new client to the dictionary.

    # I implement a method to delete a client.
    def delete_client(self, client_id):
        if client_id in self.clients:
            del self.clients[client_id]  # I delete the client from the dictionary if found.
        else:
            raise KeyError("Client not found.")  # I raise an error if the client ID is not found.

    # I implement a method to get details of a client.
    def get_client(self, client_id):
        if client_id in self.clients:
            return self.clients[client_id].display()  # I return the display info of the client.
        else:
            raise KeyError("Client not found.")  # I raise an error if the client ID is not found.

    # I implement a method to save clients to a file.
    def save_clients(self):
        with open('clients.pkl', 'wb') as file:
            pickle.dump(self.clients, file)  # I serialize and save the clients dictionary to a file.

    # I implement a method to load clients from a file.
    def load_clients(self):
        try:
            with open('clients.pkl', 'rb') as file:
                self.clients = pickle.load(file)  # I load and deserialize the clients dictionary from file.
        except FileNotFoundError:
            self.clients = {}  # I reset clients to an empty dictionary if the file is not found.

# I define the EmployeeManager class with methods to manage employee data.
class EmployeeManager:
    def __init__(self):
        self.employees = {}  # I initialize an empty dictionary to store employee data.
        self.load_employees()  # I load employee data from a file.

    # I implement a method to add an employee.
    def add_employee(self, employee):
        if employee.employee_id in self.employees:
            raise KeyError("Employee ID already exists.")  # I check for duplicate employee IDs.
        self.employees[employee.employee_id] = employee  # I add the new employee to the dictionary.

    # I implement a method to delete an employee.
    def delete_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]  # I remove the employee by ID.
        else:
            raise KeyError("Employee not found.")  # I raise an error if the employee ID does not exist.

    # I implement a method to get details of an employee.
    def get_employee(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id].display()  # I return a formatted display of employee details.
        else:
            raise KeyError("Employee not found.")  # I raise an error if the employee ID does not exist.

    # I implement a method to save employees to a file.
    def save_employees(self):
        with open('employees.pkl', 'wb') as file:  # I open a file in write-binary mode.
            pickle.dump(self.employees, file)  # I serialize and save the employees dictionary to file.

    # I implement a method to load employees from a file.
    def load_employees(self):
        try:
            with open('employees.pkl', 'rb') as file:  # I open a file in read-binary mode.
                self.employees = pickle.load(file)  # I load and deserialize the employees dictionary from file.
        except FileNotFoundError:
            self.employees = {}  # I initialize employees as an empty dictionary if the file is not found.

# I define the Venue class with attributes and a display method.
class Venue:
    def __init__(self, venue_id, name, location, capacity):
        self.venue_id = venue_id
        self.name = name
        self.location = location
        self.capacity = capacity

    # I provide a method to display venue details.
    def display(self):
        return {
            "Venue ID": self.venue_id,
            "Name": self.name,
            "Location": self.location,
            "Capacity": self.capacity
        }
# I define the VenueManager class with methods to manage venues.
class VenueManager:
    def __init__(self):
        self.venues = {}  # I initialize an empty dictionary to store venue data.
        self.load_venues()  # I load venue data from a file.

    # I implement a method to add a venue.
    def add_venue(self, venue):
        if venue.venue_id in self.venues:
            raise KeyError("Venue ID already exists.")  # I check for duplicate venue IDs.
        self.venues[venue.venue_id] = venue  # I add the new venue to the dictionary.

    # I implement a method to delete a venue.
    def delete_venue(self, venue_id):
        if venue_id in self.venues:
            del self.venues[venue_id]  # I delete the venue from the dictionary if found.
        else:
            raise KeyError("Venue not found.")  # I raise an error if the venue ID is not found.

    # I implement a method to get details of a venue.
    def get_venue(self, venue_id):
        if venue_id in self.venues:
            return self.venues[venue_id].display()  # I return the display info of the venue.
        else:
            raise KeyError("Venue not found.")  # I raise an error if the venue ID is not found.

    # I implement a method to save venues to a file.
    def save_venues(self):
        with open('venues.pkl', 'wb') as file:
            pickle.dump(self.venues, file)  # I serialize and save the venues dictionary to file.

    # I implement a method to load venues from a file.
    def load_venues(self):
        try:
            with open('venues.pkl', 'rb') as file:
                self.venues = pickle.load(file)  # I load and deserialize the venues dictionary from file.
        except FileNotFoundError:
            self.venues = {}  # I initialize venues as an empty dictionary if the file is not found.

# I define the Supplier class with attributes and a display method.
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # I provide a method to display supplier details.
    def display(self):
        return {
            "Supplier ID": self.supplier_id,
            "Name": self.name,
            "Address": self.address,
            "Contact Details": self.contact_details
        }

# I define the SupplierManager class with methods to manage suppliers.
class SupplierManager:
    def __init__(self):
        self.suppliers = {}  # I initialize an empty dictionary to store supplier data.
        self.load_suppliers()  # I load supplier data from a file.

    # I implement a method to add a supplier.
    def add_supplier(self, supplier):
        if supplier.supplier_id in self.suppliers:
            raise KeyError("Supplier ID already exists.")  # I check for duplicate supplier IDs.
        self.suppliers[supplier.supplier_id] = supplier  # I add the new supplier to the dictionary.

    # I implement a method to delete a supplier.
    def delete_supplier(self, supplier_id):
        if supplier_id in self.suppliers:
            del self.suppliers[supplier_id]  # I delete the supplier from the dictionary if found.
        else:
            raise KeyError("Supplier not found.")  # I raise an error if the supplier ID is not found.

    # I implement a method to get details of a supplier.
    def get_supplier(self, supplier_id):
        if supplier_id in self.suppliers:
            return self.suppliers[supplier_id].display()  # I return the display info of the supplier.
        else:
            raise KeyError("Supplier not found.")  # I raise an error if the supplier ID is not found.

    # I implement a method to save suppliers to a file.
    def save_suppliers(self):
        with open('suppliers.pkl', 'wb') as file:
            pickle.dump(self.suppliers, file)  # I serialize and save the suppliers dictionary to file.

    # I implement a method to load suppliers from a file.
    def load_suppliers(self):
        try:
            with open('suppliers.pkl', 'rb') as file:
                self.suppliers = pickle.load(file)  # I load and deserialize the suppliers dictionary from file.
        except FileNotFoundError:
            self.suppliers = {}  # I initialize suppliers as an empty dictionary if the file is not found.

# I define the Event class with attributes and a display method.
class Event:
    def __init__(self, event_id, name, date, venue_id, information):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.venue_id = venue_id
        self.information = information

    # I provide a method to display event details.
    def display(self):
        return {
            "Event ID": self.event_id,
            "Name": self.name,
            "Date": self.date.strftime("%Y-%m-%d"),  # I format the date as a string.
            "Venue ID": self.venue_id,
            "information": self.information
        }
# I define the EventManager class with methods to manage events.
class EventManager:
    def __init__(self):
        self.events = {}  # I initialize an empty dictionary to store event data.
        self.load_events()  # I load event data from a file.

    # I implement a method to add an event.
    def add_event(self, event):
        if event.event_id in self.events:
            raise KeyError("Event ID already exists.")  # I check for duplicate event IDs.
        self.events[event.event_id] = event  # I add the new event to the dictionary.

    # I implement a method to delete an event.
    def delete_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]  # I delete the event from the dictionary if found.
        else:
            raise KeyError("Event not found.")  # I raise an error if the event ID is not found.

    # I implement a method to get details of an event.
    def get_event(self, event_id):
        if event_id in self.events:
            return self.events[event_id].display()  # I return the display info of the event.
        else:
            raise KeyError("Event not found.")  # I raise an error if the event ID is not found.

    # I implement a method to save events to a file.
    def save_events(self):
        with open('events.pkl', 'wb') as file:
            pickle.dump(self.events, file)  # I serialize and save the events dictionary to file.

    # I implement a method to load events from a file.
    def load_events(self):
        try:
            with open('events.pkl', 'rb') as file:
                self.events = pickle.load(file)  # I load and deserialize the events dictionary from file.
        except FileNotFoundError:
            self.events = {}  # I initialize events as an empty dictionary if the file is not found.

# I define the MainApplication class which serves as the main interface for the event management system.
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Management System")
        self.geometry("1920x1080")

        # I initialize managers for various entities.
        self.employee_manager = EmployeeManager()
        self.client_manager = ClientManager()
        self.event_manager = EventManager()
        self.venue_manager = VenueManager()
        self.supplier_manager = SupplierManager()
        self.guest_manager = GuestManager()

        # I create tabs for different functionalities.
        tab_control = ttk.Notebook(self)
        self.employee_tab = ttk.Frame(tab_control)
        self.client_tab = ttk.Frame(tab_control)
        self.event_tab = ttk.Frame(tab_control)
        self.venue_tab = ttk.Frame(tab_control)
        self.supplier_tab = ttk.Frame(tab_control)
        self.guest_tab = ttk.Frame(tab_control)
        tab_control.add(self.employee_tab, text='Employees')
        tab_control.add(self.client_tab, text='Clients')
        tab_control.add(self.event_tab, text='Events')
        tab_control.add(self.venue_tab, text='Venues')
        tab_control.add(self.supplier_tab, text='Suppliers')
        tab_control.add(self.guest_tab, text='Guests')
        self.build_employee_tab()  # I populate and configure the employee tab.
        self.build_client_tab()  # I populate and configure the client tab.
        self.build_event_tab()  # I populate and configure the event tab.
        self.build_venue_tab()  # I populate and configure the venue tab.
        self.build_supplier_tab()  # I populate and configure the supplier tab.
        self.build_guest_tab()  # I populate and configure the guest tab.
        tab_control.pack(expand=1, fill="both")

        # I add a button to display inputted data.
        self.display_button = ttk.Button(self, text="Display Input", command=self.display_input)
        self.display_button.pack()

    # Method to populate and configure the employee tab.
    def build_employee_tab(self):
        frame = ttk.LabelFrame(self.employee_tab, text="Manage Employees")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Name:").grid(row=0, column=0)
        self.emp_name_entry = ttk.Entry(frame)
        self.emp_name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Employee ID:").grid(row=1, column=0)
        self.emp_id_entry = ttk.Entry(frame)
        self.emp_id_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Age:").grid(row=2, column=0)
        self.emp_age_entry = ttk.Entry(frame)
        self.emp_age_entry.grid(row=2, column=1)

        ttk.Button(frame, text="Add Employee", command=self.add_employee).grid(row=3, column=0, columnspan=2)

        ttk.Button(frame, text="Delete Selected", command=self.delete_selected_employee).grid(row=4, column=0, columnspan=2)

        self.employee_list = ttk.Treeview(frame, columns=("ID", "Name", "Department"), show="headings")
        self.employee_list.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.employee_list.heading("ID", text="ID")
        self.employee_list.heading("Name", text="Name")
        self.employee_list.heading("Department", text="Department")

        ttk.Button(frame, text="Refresh ", command=self.refresh_employees).grid(row=6, column=0, columnspan=2)

    # Method to delete the selected employee from the list.
    def delete_selected_employee(self):
        selected_items = self.employee_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            employee_id = self.employee_list.item(selected_item)['values'][0]
            try:
                self.employee_manager.delete_employee(employee_id)  # I attempt to delete the employee.
                self.employee_manager.save_employees()  # I save the changes to the file.
                self.employee_list.delete(selected_item)  # I remove the employee from the list.
            except KeyError:
                messagebox.showerror("Error", "Employee not found.")  # I show an error message if employee not found.
        else:
            messagebox.showerror("Error", "No employee selected.")  # I show an error if no employee is selected.

    # Method to add a new employee.
    def add_employee(self):
        name = self.emp_name_entry.get().strip()
        employee_id_str = self.emp_id_entry.get().strip()
        age_str = self.emp_age_entry.get().strip()

        if not name or not employee_id_str or not age_str:
            messagebox.showerror("Error", "All fields must be provided.")  # I validate all fields are provided.
            return

        try:
            employee_id = int(employee_id_str)
            age = int(age_str)
            if age < 18:
                raise ValueError(
                    "Employee must be at least 18 years old.")  # I check if employee is at least 18 years old.

            department = "Sales"  # This could be made dynamic if required
            new_employee = Employee(name, employee_id, department, "Manager", 5000, age, datetime.now(), "Passport-dubai",
                                    None)
            self.employee_manager.add_employee(new_employee)  # I add the new employee.
            self.employee_manager.save_employees()  # I save the changes to the file.
            self.refresh_employees()  # I refresh the employee list.
            messagebox.showinfo("Success", "Employee added successfully")  # I show a success message.
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))  # I show an error if age is invalid.
        except KeyError as ke:
            messagebox.showerror("Error", str(ke))  # I show an error if employee ID already exists.

    # Method to refresh the employee list.
    def refresh_employees(self):
        self.employee_list.delete(*self.employee_list.get_children())
        for emp in self.employee_manager.employees.values():
            self.employee_list.insert("", "end", values=(emp.employee_id, emp.name, emp.department))

    # Method to delete the selected client from the list.
    def delete_selected_client(self):
        selected_items = self.client_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            client_id = self.client_list.item(selected_item)['values'][0]
            try:
                self.client_manager.delete_client(client_id)  # I attempt to delete the client.
                self.client_manager.save_clients()  # I save the changes to the file.
                self.client_list.delete(selected_item)  # I remove the client from the list.
            except KeyError:
                messagebox.showerror("Error", "Client not found.")  # I show an error message if client not found.
        else:
            messagebox.showerror("Error", "No client selected.")  # I show an error if no client is selected.

    def build_client_tab(self):
        frame = ttk.LabelFrame(self.client_tab, text="Manage Clients")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Client Name:").grid(row=0, column=0)
        self.client_name_entry = ttk.Entry(frame)
        self.client_name_entry.grid(row=0, column=1)

        ttk.Button(frame, text="Add Client", command=self.add_client).grid(row=1, column=0, columnspan=2)

        self.client_list = ttk.Treeview(frame, columns=("ID", "Name", "Contact"), show="headings")
        self.client_list.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.client_list.heading("ID", text="ID")
        self.client_list.heading("Name", text="Name")
        self.client_list.heading("Contact", text="Contact")

        ttk.Button(frame, text="Refresh List", command=self.refresh_clients).grid(row=3, column=0, columnspan=2)

        ttk.Button(frame, text="Delete Selected", command=self.delete_selected_client).grid(row=4, column=0, columnspan=2)

    def add_client(self):
        name = self.client_name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Enter Client name.")
            return

        client_id = str(uuid.uuid4())
        try:
            new_client = Client(client_id, name, "1234 Address", "056-2321-123", 10000)
            self.client_manager.add_client(new_client)
            self.client_manager.save_clients()
            self.refresh_clients()
            messagebox.showinfo("Success", "Client added successfully")
        except KeyError as ke:
            messagebox.showerror("Error", str(ke))

    def refresh_clients(self):
        self.client_list.delete(*self.client_list.get_children())
        for client in self.client_manager.clients.values():
            self.client_list.insert("", "end", values=(client.client_id, client.name, client.contact_details))

    def delete_selected_client(self):
        selected_items = self.client_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            client_id = self.client_list.item(selected_item)['values'][0]
            try:
                self.client_manager.delete_client(client_id)
                self.client_manager.save_clients()
                self.client_list.delete(selected_item)
            except KeyError:
                messagebox.showerror("Error", "Client not found.")
        else:
            messagebox.showerror("Error", "No client selected.")

    def build_event_tab(self):  # Add this
        frame = ttk.LabelFrame(self.event_tab, text="Manage Events")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Event Name:").grid(row=0, column=0)
        self.event_name_entry = ttk.Entry(frame)
        self.event_name_entry.grid(row=0, column=1)

        ttk.Button(frame, text="Add Event", command=self.add_event).grid(row=1, column=0, columnspan=2)

        self.event_list = ttk.Treeview(frame, columns=("ID", "Name", "Date", "Venue ID", "information"), show="headings")
        self.event_list.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.event_list.heading("ID", text="ID")
        self.event_list.heading("Name", text="Name")
        self.event_list.heading("Date", text="Date")
        self.event_list.heading("Venue ID", text="Venue ID")
        self.event_list.heading("information", text="information")

        ttk.Button(frame, text="Refresh", command=self.refresh_events).grid(row=3, column=0, columnspan=2)

        ttk.Button(frame, text="Delete Selected", command=self.delete_selected_event).grid(row=4, column=0, columnspan=2)

    def add_event(self):
        name = self.event_name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter event name.")
            return

        event_id = str(uuid.uuid4())
        try:
            new_event = Event(event_id, name, datetime.now(), "123", "information")
            self.event_manager.add_event(new_event)
            self.event_manager.save_events()
            self.refresh_events()
            messagebox.showinfo("Success", "Event added ") #succses message
        except KeyError as ke:
            messagebox.showerror("Error", str(ke))

    def refresh_events(self):
        self.event_list.delete(*self.event_list.get_children())
        for event in self.event_manager.events.values():
            self.event_list.insert("", "end", values=(event.event_id, event.name, event.date.strftime("%Y-%m-%d"), event.venue_id, event.information))

    def delete_selected_event(self):
        selected_items = self.event_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            event_id = self.event_list.item(selected_item)['values'][0]
            try:
                self.event_manager.delete_event(event_id)
                self.event_manager.save_events()
                self.event_list.delete(selected_item)
            except KeyError:
                messagebox.showerror("Error", "The Event that you chose doesnt exsit.")
        else:
            messagebox.showerror("Error", "Please select an event.")

    # I start by creating a venue tab where I can manage venues.
    def build_venue_tab(self):
        frame = ttk.LabelFrame(self.venue_tab, text="Manage Venues")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # I add labels and entry fields for venue name, location, and capacity.
        ttk.Label(frame, text="Venue Name:").grid(row=0, column=0)
        self.venue_name_entry = ttk.Entry(frame)
        self.venue_name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Location:").grid(row=1, column=0)
        self.location_entry = ttk.Entry(frame)
        self.location_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Capacity:").grid(row=2, column=0)
        self.capacity_entry = ttk.Entry(frame)
        self.capacity_entry.grid(row=2, column=1)

        # I add a button to add a new venue.
        ttk.Button(frame, text="Add Venue", command=self.add_venue).grid(row=3, column=0, columnspan=2)

        # I create a treeview to display the list of venues.
        self.venue_list = ttk.Treeview(frame, columns=("ID", "Name", "Location", "Capacity"), show="headings")
        self.venue_list.grid(row=4, column=0, columnspan=2, sticky='nsew')
        self.venue_list.heading("ID", text="ID")
        self.venue_list.heading("Name", text="Name")
        self.venue_list.heading("Location", text="Location")
        self.venue_list.heading("Capacity", text="Capacity")

        # I add buttons to refresh the list of venues and delete a selected venue.
        ttk.Button(frame, text="Refresh", command=self.refresh_venues).grid(row=5, column=0, columnspan=2)
        ttk.Button(frame, text="Delete Selected", command=self.delete_selected_venue).grid(row=6, column=0,
                                                                                           columnspan=2)

    # I define a method to add a new venue.
    def add_venue(self):
        name = self.venue_name_entry.get().strip()
        location = self.location_entry.get().strip()
        capacity_str = self.capacity_entry.get().strip()

        # I ensure that all fields are provided.
        if not name or not location or not capacity_str:
            messagebox.showerror("Error", "Please fill all of the fields.")
            return

        try:
            capacity = int(capacity_str)
            venue_id = str(uuid.uuid4())
            new_venue = Venue(venue_id, name, location, capacity)
            self.venue_manager.add_venue(new_venue)  # I add the new venue
            self.venue_manager.save_venues()  # I save the changes to the file
            self.refresh_venues()  # I refresh the venue list
            messagebox.showinfo("Success", "Venue added")  # I show a success message
        except ValueError:
            messagebox.showerror("Error", "Please check what you enterd is correct.")

    # I define a method to refresh the list of venues.
    def refresh_venues(self):
        self.venue_list.delete(*self.venue_list.get_children())
        for venue in self.venue_manager.venues.values():
            self.venue_list.insert("", "end", values=(venue.venue_id, venue.name, venue.location, venue.capacity))

    # I define a method to delete the selected venue from the list.
    def delete_selected_venue(self):
        selected_items = self.venue_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            venue_id = self.venue_list.item(selected_item)['values'][0]
            try:
                self.venue_manager.delete_venue(venue_id)  # I delete the venue
                self.venue_manager.save_venues()  # I save the changes to the file
                self.venue_list.delete(selected_item)  # I remove the venue from the list
            except KeyError:
                messagebox.showerror("Error", "The venue you selected was not found.")  # I show an error message if the venue is not found
        else:
            messagebox.showerror("Error", "Please select venue.")  # I show an error if no venue is selected

    def build_supplier_tab(self):  # Add this
        frame = ttk.LabelFrame(self.supplier_tab, text="Manage Suppliers")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Supplier Name:").grid(row=0, column=0)
        self.supplier_name_entry = ttk.Entry(frame)
        self.supplier_name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Address:").grid(row=1, column=0)
        self.supplier_address_entry = ttk.Entry(frame)
        self.supplier_address_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Contact Details:").grid(row=2, column=0)
        self.supplier_contact_entry = ttk.Entry(frame)
        self.supplier_contact_entry.grid(row=2, column=1)

        ttk.Button(frame, text="Add Supplier", command=self.add_supplier).grid(row=3, column=0, columnspan=2)

        self.supplier_list = ttk.Treeview(frame, columns=("ID", "Name", "Address", "Contact Details"), show="headings")
        self.supplier_list.grid(row=4, column=0, columnspan=2, sticky='nsew')
        self.supplier_list.heading("ID", text="ID")
        self.supplier_list.heading("Name", text="Name")
        self.supplier_list.heading("Address", text="Address")
        self.supplier_list.heading("Contact Details", text="Contact Details")

        ttk.Button(frame, text="Refresh", command=self.refresh_suppliers).grid(row=5, column=0, columnspan=2)

        ttk.Button(frame, text="Delete Selected", command=self.delete_selected_supplier).grid(row=6, column=0,
                                                                                              columnspan=2)

    def add_supplier(self):
        name = self.supplier_name_entry.get().strip()
        address = self.supplier_address_entry.get().strip()
        contact_details = self.supplier_contact_entry.get().strip()

        if not name or not address or not contact_details:
            messagebox.showerror("Error", "All fields must be provided.")
            return

        supplier_id = str(uuid.uuid4())
        try:
            new_supplier = Supplier(supplier_id, name, address, contact_details)
            self.supplier_manager.add_supplier(new_supplier)
            self.supplier_manager.save_suppliers()
            self.refresh_suppliers()
            messagebox.showinfo("Success", "Supplier added")
        except KeyError as ke:
            messagebox.showerror("Error", str(ke))

    def refresh_suppliers(self):
        self.supplier_list.delete(*self.supplier_list.get_children())
        for supplier in self.supplier_manager.suppliers.values():
            self.supplier_list.insert("", "end", values=(
            supplier.supplier_id, supplier.name, supplier.address, supplier.contact_details))

    def delete_selected_supplier(self):
        selected_items = self.supplier_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            supplier_id = self.supplier_list.item(selected_item)['values'][0]
            try:
                self.supplier_manager.delete_supplier(supplier_id)
                self.supplier_manager.save_suppliers()
                self.supplier_list.delete(selected_item)
            except KeyError:
                messagebox.showerror("Error", "The Supplier that you selected was not found.")
        else:
            messagebox.showerror("Error", "Please select a supplier.")

    def build_guest_tab(self):  # Add this
        frame = ttk.LabelFrame(self.guest_tab, text="Manage Guests")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(frame, text="Guest Name:").grid(row=0, column=0)
        self.guest_name_entry = ttk.Entry(frame)
        self.guest_name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Address:").grid(row=1, column=0)
        self.guest_address_entry = ttk.Entry(frame)
        self.guest_address_entry.grid(row=1, column=1)

        ttk.Label(frame, text="Contact Details:").grid(row=2, column=0)
        self.guest_contact_entry = ttk.Entry(frame)
        self.guest_contact_entry.grid(row=2, column=1)

        ttk.Button(frame, text="Add Guest", command=self.add_guest).grid(row=3, column=0, columnspan=2)

        self.guest_list = ttk.Treeview(frame, columns=("ID", "Name", "Address", "Contact Details"), show="headings")
        self.guest_list.grid(row=4, column=0, columnspan=2, sticky='nsew')
        self.guest_list.heading("ID", text="ID")
        self.guest_list.heading("Name", text="Name")
        self.guest_list.heading("Address", text="Address")
        self.guest_list.heading("Contact Details", text="Contact Details")

        ttk.Button(frame, text="Refresh", command=self.refresh_guests).grid(row=5, column=0, columnspan=2)

        ttk.Button(frame, text="Delete", command=self.delete_selected_guest).grid(row=6, column=0,
                                                                                           columnspan=2)

    def add_guest(self):
        name = self.guest_name_entry.get().strip()
        address = self.guest_address_entry.get().strip()
        contact_details = self.guest_contact_entry.get().strip()

        if not name or not address or not contact_details:
            messagebox.showerror("Error", "All fields must be provided.")
            return

        guest_id = str(uuid.uuid4())
        try:
            new_guest = Guest(guest_id, name, address, contact_details)
            self.guest_manager.add_guest(new_guest)
            self.guest_manager.save_guests()
            self.refresh_guests()
            messagebox.showinfo("Success", "Guest added successfully")
        except KeyError as ke:
            messagebox.showerror("Error", str(ke))

    def refresh_guests(self):
        self.guest_list.delete(*self.guest_list.get_children())
        for guest in self.guest_manager.guests.values():
            self.guest_list.insert("", "end", values=(guest.guest_id, guest.name, guest.address, guest.contact_details))

    def delete_selected_guest(self):
        selected_items = self.guest_list.selection()
        if selected_items:
            selected_item = selected_items[0]
            guest_id = self.guest_list.item(selected_item)['values'][0]
            try:
                self.guest_manager.delete_guest(guest_id)
                self.guest_manager.save_guests()
                self.guest_list.delete(selected_item)
            except KeyError:
                messagebox.showerror("Error", "Guest not found.")
        else:
            messagebox.showerror("Error", "No guest selected.")

    def display_input(self):
        # Retrieve all the inputted data from the GUI elements
        employee_data = self.get_employee_data()
        client_data = self.get_client_data()
        event_data = self.get_event_data()
        venue_data = self.get_venue_data()
        supplier_data = self.get_supplier_data()
        guest_data = self.get_guest_data()

        # Display the data in the desired output format
        print("Employee Data:", employee_data)
        print("Client Data:", client_data)
        print("Event Data:", event_data)
        print("Venue Data:", venue_data)
        print("Supplier Data:", supplier_data)
        print("Guest Data:", guest_data)

    # Define functions to retrieve data from GUI elements (similar to refresh functions)
    def get_employee_data(self):
        employee_data = []
        for emp in self.employee_manager.employees.values():
            employee_data.append(emp.display())
        return employee_data

    def get_client_data(self):
        client_data = []
        for client in self.client_manager.clients.values():
            client_data.append(client.display())
        return client_data

    def get_guest_data(self):
        guest_data = []
        for guest in self.guest_manager.guests.values():
            guest_data.append(guest.display())

    def get_venue_data(self):
        venue_data = []
        for venue in self.venue_manager.venues.values():
            venue_data.append(venue.display())
        return venue_data

    def get_supplier_data(self):
        supplier_data = []
        for supplier in self.supplier_manager.suppliers.values():
            supplier_data.append(supplier.display())
        return supplier_data

        def get_event_data(self):
            event_data = []
            for event in self.event_manager.events.values():
                event_data.append(event.display())
            return event_data

        return guest_data
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
