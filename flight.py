import sys
from collections import deque

#Define the all routes and durations
flight_routes = {
    "SL": {"UK": 11.45, "USA": None, "Japan": 8, "Singapore": 4, "Australia": 9.25},
    "UK": {"USA": 8, "SL": 11.45},
    "USA": {"UK": 8, "Japan": 16, "Australia": None},
    "Japan": {"USA": 16, "Australia": 10, "SL": 8, "Singapore": 4},
    "Singapore": {"Australia": 7.25, "Japan": 4, "SL": 4},
    "Australia": {"Japan": 10, "USA": None, "SL": 9.25, "Singapore": 7.25}
}

# Function to display all possible routes between two countries
print("\n\t\t\t\t\tWelcome to FlightRoutes Company!")
print("\t\t\t\t\t\t\tMain Menu")
print("1. Display all possible routes between two countries with durations.")
print("2. Find the least duration route between two countries.")
print("3. Exit")

while True:
    print("\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        start = input("Enter the starting country code (e.g., SL): ").upper()
        destination = input("Enter the destination country code (e.g., UK): ").upper()
        
        # Display all possible routes
        print("\n\t\t\t\t\tFlightRoutes Company!")
        print("\t\t All possible airline routes between two given countries with durations","\n\n\tStarting country:", start, "\t\t\tDestination country:", destination)
        print("\n")

        queue = deque([[start]])
        routes = []

        while queue:
            path = queue.popleft()
            current_country = path[-1]

            if current_country == destination:
                routes.append(path)
            else:
                for next_country in flight_routes[current_country]:
                    if flight_routes[current_country][next_country] is not None and next_country not in path:
                        queue.append(path + [next_country])

        if not routes:
            print("Sorry, there are no direct routes available.")
        else:
            for i, route in enumerate(routes, start=1):
                duration = sum(flight_routes[route[j]][route[j + 1]] for j in range(len(route) - 1))
                print(f"Route {i}: {' -> '.join(route)} Duration: {duration} Hours")

    elif choice == '2':
        start = input("\nEnter the starting country code (e.g., SL): ").upper()
        destination = input("Enter the destination country code (e.g., UK): ").upper()
        
        # Find the least duration route
        print("\n\t\t\t\t\tFlightRoutes Company!")
        print("\t\t\t\tThe least duration route between", start, "and", destination)
        print("\n")
        print("\t\tStarting Country :", start, "\t\t\t\tDestination Country :", destination)
        print("\n")

        queue = deque([[start]])
        routes = []

        while queue:
            path = queue.popleft()
            current_country = path[-1]

            if current_country == destination:
                routes.append(path)
            else:
                for next_country in flight_routes[current_country]:
                    if flight_routes[current_country][next_country] is not None and next_country not in path:
                        queue.append(path + [next_country])

        if not routes:
            print("Sorry, there are no direct routes available.")
        else:
            least_duration = float('inf')
            least_duration_route = None
            for route in routes:
                duration = sum(flight_routes[route[i]][route[i + 1]] for i in range(len(route) - 1))
                if duration < least_duration:
                    least_duration = duration
                    least_duration_route = route

            if least_duration_route:
                print(f"\t\tRoute: {' -> '.join(least_duration_route)} \t\t\t\tDuration: {least_duration} Hours")
                choice_exit = input("\nDo you want to Exit (Yes/No)? ").lower()
                if choice_exit == 'yes':
                    print("Exiting program. Thank you for using FlightRoutes Company!")
                    sys.exit()
            else:
                print("Sorry, there are no direct routes available.")

    elif choice == '3':
        print("Exiting program. Thank you for using FlightRoutes Company!")
        sys.exit()

    else:
        print("Invalid choice. Please enter a valid option.")
