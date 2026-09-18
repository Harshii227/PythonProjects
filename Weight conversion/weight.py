weight = float(input("Enter the weight: "))
unit = input("kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205180
    unit = "kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not found")
