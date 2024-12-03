def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
     return float(d.strip('$'))
# Turns the amount given into an actual float, so it can be dollars and cents
def percent_to_float(p):
     return float(p.strip('%')) / 100
# Makes the percentage numbe given into an actual percentage

main()