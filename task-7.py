
# Bus Passenger Occupancy Simulation

capacity = int(input("Enter maximum bus capacity: "))
passengers = int(input("Enter initial passengers: "))
stops = int(input("Enter number of stops: "))

if capacity <= 0 or passengers < 0 or stops <= 0:
    print("Invalid input! Check capacity, passengers, and stops.")

elif passengers > capacity:
    print("Invalid input! Initial passengers exceed bus capacity.")

else:
    violations = 0

    print("\n----- BUS OCCUPANCY REPORT -----")
    print("Initial passengers:", passengers)

    for i in range(1, stops + 1):
        print("\nStop", i)

        boarding = int(input("Passengers boarding: "))
        alighting = int(input("Passengers alighting: "))

        if boarding < 0 or alighting < 0:
            print("Invalid counts! Enter non-negative values.")
            continue

        if alighting > passengers:
            print("Error: More passengers alighting than onboard.")
            continue

        passengers = passengers - alighting + boarding

        print("Passengers after stop:", passengers)
        print("Available seats:", max(0, capacity - passengers))

        if passengers > capacity:
            print("CAPACITY VIOLATION!")
            violations += 1
        else:
            print("Status: Within capacity")

    print("\n----- FINAL SUMMARY -----")
    print("Final passengers:", passengers)
    print("Bus capacity:", capacity)
    print("Capacity violations:", violations)
