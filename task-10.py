
# Energy Conservation Before-and-After Analysis

n = int(input("Enter number of appliances: "))

if n <= 0:
    print("Invalid number of appliances!")

else:
    appliances = {}

    for i in range(n):
        print("\nAppliance", i + 1)

        name = input("Enter appliance name: ")
        before = float(input("Enter usage before intervention (kWh): "))
        after = float(input("Enter usage after intervention (kWh): "))

        if before < 0 or after < 0:
            print("Invalid usage! Values cannot be negative.")
            continue

        savings = before - after

        if before > 0:
            percentage = (savings / before) * 100
        else:
            percentage = 0

        appliances[name] = {
            "before": before,
            "after": after,
            "savings": savings,
            "percentage": percentage
        }

    print("\n----- ENERGY CONSERVATION REPORT -----")

    total_before = 0
    total_after = 0

    for name, data in appliances.items():
        print("\nAppliance:", name)
        print("Before:", round(data["before"], 2), "kWh")
        print("After:", round(data["after"], 2), "kWh")
        print("Energy savings:", round(data["savings"], 2), "kWh")
        print("Savings percentage:",
              round(data["percentage"], 2), "%")

        if data["savings"] > 0:
            print("Status: Energy saved")
        elif data["savings"] < 0:
            print("Status: Energy consumption increased")
        else:
            print("Status: No change")

        total_before += data["before"]
        total_after += data["after"]

    total_savings = total_before - total_after

    if total_before > 0:
        overall_percentage = total_savings / total_before * 100
    else:
        overall_percentage = 0

    print("\n----- OVERALL SUMMARY -----")
    print("Total before:", round(total_before, 2), "kWh")
    print("Total after:", round(total_after, 2), "kWh")
    print("Total savings:", round(total_savings, 2), "kWh")
    print("Overall savings:",
          round(overall_percentage, 2), "%")

    print("\n----- APPLIANCE RANKING -----")

    ranked = sorted(
        appliances.items(),
        key=lambda item: item[1]["savings"],
        reverse=True
    )

    for rank, (name, data) in enumerate(ranked, start=1):
        print(rank, name, "-",
              round(data["savings"], 2), "kWh saved")
