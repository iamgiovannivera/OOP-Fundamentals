# class Vehicle:
#     def __init__(self, reg_num, vehicle_type, owner):
#         self.registration_number = reg_num
#         self.type = vehicle_type
#         self.owner = owner
    
#     def update_owner(self, new_owner):
#         self.owner = new_owner

# # Create instances

# vehicle1 = Vehicle("ABC123", "Car", "John Doe")
# vehicle2 = Vehicle("XYZ789", "Truck", "Jane Smith")

# print(f"Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, {vehicle1.owner}")
# print(f"Vehicle 2: {vehicle2.registration_number}, {vehicle2.type}, {vehicle2.owner}")

# # Update owner
# vehicle1.update_owner("Alice Brown")
# print(f"Updated Vehicle 1: {vehicle1.registration_number}, {vehicle1.type}, {vehicle1.owner}")



# Task 2: 
    
    
    
# class Event:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date
#         self.participant_count = 0
    
#     def add_participant(self):
#         self.participant_count += 1
    
#     def get_participant_count(self):
#         return self.participant_count

# # Create an event 


# event = Event("Music Festival", "2023-08-15")
# print(f"Event: {event.name}, Date: {event.date}, Participants: {event.get_participant_count()}")

# # Add participants
# event.add_participant()
# event.add_participant()
# print(f"Updated Participants: {event.get_participant_count()}")
# Task 1: File Handling for Building Records
# Building class with file handling




# import json

# class Building:
#     def __init__(self, name, floors):
#         self.name = name
#         self.floors = floors
    
#     def save_to_file(self, filename):
#         with open(filename, 'w') as file:
#             json.dump({"name": self.name, "floors": self.floors}, file)
    
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             return cls(data["name"], data["floors"])

# # Create a building and save to file
# building = Building("Skyscraper", 50)
# building.save_to_file("building.json")

# # Load building from file
# loaded_building = Building.load_from_file("building.json")
# print(f"Loaded Building: {loaded_building.name}, Floors: {loaded_building.floors}")



# Task 1:
    
    
    
# class Bus:
#     city_name = "Metropolis"
#     base_fare = 2.5
    
#     def __init__(self, route_number, passenger_capacity):
#         self.route_number = route_number
#         self.passenger_capacity = passenger_capacity

# # Create instances 


# bus1 = Bus(101, 50)
# bus2 = Bus(102, 75)

# print(f"Bus 1: Route {bus1.route_number}, Capacity {bus1.passenger_capacity}, City {Bus.city_name}, Base Fare {Bus.base_fare}")
# print(f"Bus 2: Route {bus2.route_number}, Capacity {bus2.passenger_capacity}, City {Bus.city_name}, Base Fare {Bus.base_fare}")