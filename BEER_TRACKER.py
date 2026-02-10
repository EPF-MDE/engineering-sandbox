# Beer list
BEERS = {"Heineken": 5.0, "Leffe": 6.6, "Rince Cochon": 8.5, "8.6": 8.6}

# Values
PINT_L = 0.5
DENSITY = 0.789  # To convert ml for g
R_MALE = 0.68  # Diffusion coeficient of alcohol in body
R_FEMALE = 0.55


# Functions
def grams_alcohol(number_beers, abv):
    volume_l = number_beers * PINT_L
    volume_ml = volume_l * 1000  # Convert to ml
    return (
        volume_ml * (abv / 100) * DENSITY
    )  # abv = alcohol by volume , divide by 100 cause it's a percentage


def bac_estimate(total_grams, weight, r):  # BAC = Blood Alcohol Concentration
    return total_grams / (weight * r)  # r dependes if MALE or FEMALE


def bac_status(bac):
    if bac < 0.2:
        return "Low"
    elif bac < 0.5:
        return "Be careful"
    elif bac < 0.8:
        return "High (do not drive)"
    else:
        return "Danger"


# Start of input
print("=== BEER TRACKER ===")

weight = float(input("Your weight (kg): "))
sex = input("Your sex (M/F): ").upper()

r = R_MALE if sex == "M" else R_FEMALE

drinks = []

# --- Menu ---
while True:
    print("\nMenu")
    print("1) Add beers")
    print("2) Show report")
    print("3) Reset")
    print("4) Exit")

    choice = input("Choose: ")

    # ADD BEERS
    if choice == "1":
        print("\nAvailable beers:")
        names = list(BEERS.keys())

        for i, name in enumerate(names):
            print(f"{i + 1}) {name} ({BEERS[name]}%)")

        beer_choice = int(input("Select beer: ")) - 1
        beer_name = names[beer_choice]
        abv = BEERS[beer_name]

        number_beers = float(input("Number of beers: "))

        grams = grams_alcohol(number_beers, abv)

        drinks.append({"beer": beer_name, "beers": number_beers, "grams": grams})

        print("Beers added!")

    # REPORT
    elif choice == "2":
        if not drinks:
            print("No beers recorded.")
            continue

        total_beers = sum(d["beers"] for d in drinks)
        total_grams = sum(d["grams"] for d in drinks)

        bac = bac_estimate(total_grams, weight, r)

        print("\n--- REPORT ---")
        print(f"Total beers: {total_beers:.1f}")
        print(f"Total alcohol: {total_grams:.1f} g")
        print(f"Estimated BAC: {bac:.2f} g/L")
        print(f"Status: {bac_status(bac)}")

        print("\nHistory:")
        for d in drinks:
            print(f"- {d['beer']} : {d['beers']} beers")

        print("\n⚠ Estimate only.")

    # RESET
    elif choice == "3":
        drinks = []
        print("Session reset.")

    # EXIT
    elif choice == "4":
        break

    else:
        print("Invalid choice.")
