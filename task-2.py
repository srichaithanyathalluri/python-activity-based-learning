
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

total_fare = 0

for i in range(1, n + 1):
    print("\nPassenger", i)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter travel distance in km: "))

    print("Classes: 1. Sleeper  2. AC  3. First Class")
    choice = int(input("Choose travel class (1-3): "))

    if choice == 1:
        rate = 1.0
        reservation_fee = 20
    elif choice == 2:
        rate = 2.0
        reservation_fee = 40
    elif choice == 3:
        rate = 3.0
        reservation_fee = 60
    else:
        print("Invalid class. Using Sleeper class.")
        rate = 1.0
        reservation_fee = 20

    # Distance-based fare slabs
    if distance <= 100:
        base_fare = distance * rate
    elif distance <= 500:
        base_fare = 100 * rate + (distance - 100) * rate * 0.8
    else:
        base_fare = (100 * rate
                     + 400 * rate * 0.8
                     + (distance - 500) * rate * 0.6)

    # Example age-based concessions
    concession = 0

    if age < 5:
        concession = base_fare
    elif age >= 60:
        concession = base_fare * 0.20

    fare = base_fare - concession + reservation_fee

    print("Passenger:", name)
    print("Base fare: Rs.", round(base_fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation fee: Rs.", reservation_fee)
    print("Final fare: Rs.", round(fare, 2))

    total_fare += fare

print("\nTotal reservation amount: Rs.", round(total_fare, 2))

# Cancellation calculation
cancel = input("Do you want to calculate cancellation? (yes/no): ")

if cancel.lower() == "yes":
    penalty_rate = float(input("Enter cancellation penalty percentage: "))
    penalty = total_fare * penalty_rate / 100
    refund = total_fare - penalty

    print("Cancellation penalty: Rs.", round(penalty, 2))
    print("Refund amount: Rs.", round(refund, 2))
