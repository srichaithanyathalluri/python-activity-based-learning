
# Water Distribution Fairness Analysis

areas = int(input("Enter number of areas: "))
days = int(input("Enter number of days: "))

if areas <= 0 or days <= 0:
    print("Invalid input! Areas and days must be positive.")

else:
    data = {}

    for i in range(areas):
        name = input(f"\nEnter area {i + 1} name: ")
        demand = float(input("Enter daily water demand (litres): "))

        if demand <= 0:
            print("Invalid demand! Using 1 litre.")
            demand = 1

        total_supply = 0
        total_shortage = 0

        for day in range(1, days + 1):
            supply = float(input(
                f"Day {day} water supply for {name} (litres): "
            ))

            if supply < 0:
                print("Invalid supply! Counting it as 0.")
                supply = 0

            shortage = max(0, demand - supply)
            total_supply += supply
            total_shortage += shortage

            print("Shortage:", round(shortage, 2), "litres")

        average_supply = total_supply / days
        average_shortage = total_shortage / days
        fulfillment = (total_supply / (demand * days)) * 100

        data[name] = {
            "demand": demand,
            "supply": total_supply,
            "shortage": total_shortage,
            "average_supply": average_supply,
            "average_shortage": average_shortage,
            "fulfillment": fulfillment
        }

    print("\n----- WATER DISTRIBUTION REPORT -----")

    for name, info in data.items():
        print("\nArea:", name)
        print("Total demand:", info["demand"] * days, "litres")
        print("Total supply:", round(info["supply"], 2), "litres")
        print("Total shortage:", round(info["shortage"], 2), "litres")
        print("Average daily supply:",
              round(info["average_supply"], 2), "litres")
        print("Demand fulfilled:",
              round(info["fulfillment"], 2), "%")

    # Identify the most underserved area
    if data:
        worst_area = min(
            data,
            key=lambda name: data[name]["fulfillment"]
        )

        print("\nMost underserved area:", worst_area)
        print("Demand fulfilled:",
              round(data[worst_area]["fulfillment"], 2), "%")
        print("Total shortage:",
              round(data[worst_area]["shortage"], 2), "litres")



