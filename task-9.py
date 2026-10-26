
# Smart Public Transport Fare Reconciliation

routes = int(input("Enter number of routes: "))

if routes <= 0:
    print("Invalid number of routes!")

else:
    expected_revenue = 0
    collected_revenue = 0

    for i in range(1, routes + 1):
        print("\nRoute", i)

        route_name = input("Enter route name: ")
        base_fare = float(input("Enter base fare (Rs.): "))

        if base_fare < 0:
            print("Invalid fare! Skipping route.")
            continue

        categories = int(input("Enter number of passenger categories: "))

        for j in range(1, categories + 1):
            print("\nPassenger Category", j)

            category = input("Enter category (Adult/Child/Senior): ")
            passengers = int(input("Enter number of passengers: "))

            if category.lower() == "adult":
                rate = 1.0
            elif category.lower() == "child":
                rate = 0.5
            elif category.lower() == "senior":
                rate = 0.7
            else:
                print("Unknown category. Using adult fare.")
                rate = 1.0

            fare_per_passenger = base_fare * rate
            expected = fare_per_passenger * passengers

            collected = float(input(
                "Enter actual collected revenue (Rs.): "
            ))

            if passengers < 0 or collected < 0:
                print("Invalid input! Skipping this category.")
                continue

            expected_revenue += expected
            collected_revenue += collected

            discrepancy = collected - expected

            print("Expected revenue: Rs.", round(expected, 2))
            print("Collected revenue: Rs.", round(collected, 2))

            if discrepancy < 0:
                print("Revenue shortage: Rs.", round(-discrepancy, 2))
            elif discrepancy > 0:
                print("Extra collection: Rs.", round(discrepancy, 2))
            else:
                print("Revenue reconciled successfully.")

    print("\n----- FINAL RECONCILIATION REPORT -----")
    print("Expected revenue: Rs.", round(expected_revenue, 2))
    print("Collected revenue: Rs.", round(collected_revenue, 2))

    difference = collected_revenue - expected_revenue

    print("Net discrepancy: Rs.", round(difference, 2))

    if difference < 0:
        print("Status: Revenue shortage")
    elif difference > 0:
        print("Status: Excess collection")
    else:
        print("Status: Fully reconciled")
