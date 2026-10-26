
# Fuel Consumption and Route Comparison

distance = float(input("Enter journey distance in km: "))
fuel_price = float(input("Enter fuel price per litre (Rs.): "))
reserve_percent = float(input("Enter required fuel reserve percentage: "))

n = int(input("Enter number of vehicles: "))

vehicles = {}

for i in range(n):
    print("\nVehicle", i + 1)

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/litre): "))
    tank_capacity = float(input("Enter available fuel capacity in litres: "))

    if mileage <= 0 or tank_capacity < 0:
        print("Invalid mileage or fuel capacity.")
        continue

    trip_fuel = distance / mileage
    reserve_fuel = trip_fuel * reserve_percent / 100
    required_fuel = trip_fuel + reserve_fuel

    cost = required_fuel * fuel_price

    feasible = required_fuel <= tank_capacity

    vehicles[name] = {
        "trip_fuel": trip_fuel,
        "reserve_fuel": reserve_fuel,
        "required_fuel": required_fuel,
        "cost": cost,
        "feasible": feasible
    }

    print("Trip fuel required:", round(trip_fuel, 2), "litres")
    print("Reserve fuel:", round(reserve_fuel, 2), "litres")
    print("Total fuel required:", round(required_fuel, 2), "litres")
    print("Estimated cost: Rs.", round(cost, 2))
    print("Feasible:", "Yes" if feasible else "No")

# Identify the lowest-cost feasible vehicle
feasible_vehicles = {
    name: details
    for name, details in vehicles.items()
    if details["feasible"]
}

print("\n------ ROUTE COMPARISON SUMMARY ------")

if feasible_vehicles:
    best_vehicle = min(
        feasible_vehicles,
        key=lambda name: feasible_vehicles[name]["cost"]
    )

    print("Lowest-cost feasible vehicle:", best_vehicle)
    print("Total fuel required:",
          round(feasible_vehicles[best_vehicle]["required_fuel"], 2),
          "litres")
    print("Estimated journey cost: Rs.",
          round(feasible_vehicles[best_vehicle]["cost"], 2))
else:
    print("No vehicle has sufficient fuel capacity for this journey.")

