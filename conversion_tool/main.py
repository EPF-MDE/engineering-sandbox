# main file to run for the console

#length
def meters_to_kilometers(m: float) -> float:
    return m / 1000


def kilometers_to_meters(km: float):
    return km * 1000


def meters_to_centimeters(m: float):
    return m * 100


def centimeters_to_meters(cm: float):
    return cm / 100


def meters_to_millimeters(m: float):
    return m * 1000


def millimeters_to_meters(mm: float):
    return mm / 1000


def meters_to_feet(m: float):
    return m * 3.28084


def feet_to_meters(ft: float):
    return ft / 3.28084


def meters_to_inches(m: float):
    return m * 39.3701


def inches_to_meters(inch: float):
    return inch / 39.3701

#temperature 
def celsius_to_fahrenheit(c: float):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float):
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float):
    return c + 273.15


def kelvin_to_celsius(k: float):
    return k - 273.15


def fahrenheit_to_kelvin(f: float):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k: float) :
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


#clothing sizes
WOMEN_SIZES = [
    {"INTL": "S",     "USA": 2,  "UK": 6,  "IT": 38, "FR": 34, "DE": 32, "JP": 7,  "RU": 40},
    {"INTL": "S",     "USA": 4,  "UK": 8,  "IT": 40, "FR": 36, "DE": 34, "JP": 9,  "RU": 42},
    {"INTL": "M",     "USA": 6,  "UK": 10, "IT": 42, "FR": 38, "DE": 36, "JP": 11, "RU": 44},
    {"INTL": "M",     "USA": 8,  "UK": 12, "IT": 44, "FR": 40, "DE": 38, "JP": 13, "RU": 46},
    {"INTL": "L",     "USA": 10, "UK": 14, "IT": 46, "FR": 42, "DE": 40, "JP": 15, "RU": 48},
    {"INTL": "L",     "USA": 12, "UK": 16, "IT": 48, "FR": 44, "DE": 42, "JP": 17, "RU": 50},
    {"INTL": "XL",    "USA": 14, "UK": 18, "IT": 50, "FR": 46, "DE": 44, "JP": 19, "RU": 52},
    {"INTL": "1X",    "USA": 16, "UK": 20, "IT": 52, "FR": 48, "DE": 46, "JP": 21, "RU": 54},
    {"INTL": "2X",    "USA": 18, "UK": 22, "IT": 54, "FR": 50, "DE": 48, "JP": 23, "RU": 56},
    {"INTL": "3X",    "USA": 20, "UK": 24, "IT": 56, "FR": 52, "DE": 50, "JP": 25, "RU": 58},
    {"INTL": "3X",    "USA": 22, "UK": 26, "IT": 58, "FR": 54, "DE": 52, "JP": 27, "RU": 60},
    {"INTL": "4X",    "USA": 24, "UK": 28, "IT": 60, "FR": 56, "DE": 54, "JP": 29, "RU": 62},
]

MEN_SIZES = [
    {"INTL": "XS", "USA": 34, "UK": 34, "FR": 44, "DE": 44, "IT": 44, "AU": 34, "JP": 1},
    {"INTL": "S",  "USA": 36, "UK": 36, "FR": 46, "DE": 46, "IT": 46, "AU": 36, "JP": 2},
    {"INTL": "M",  "USA": 38, "UK": 38, "FR": 48, "DE": 48, "IT": 48, "AU": 38, "JP": 3},
    {"INTL": "L",  "USA": 40, "UK": 40, "FR": 50, "DE": 50, "IT": 50, "AU": 40, "JP": 4},
    {"INTL": "XL", "USA": 42, "UK": 42, "FR": 52, "DE": 52, "IT": 52, "AU": 42, "JP": 5},
    {"INTL": "2X", "USA": 44, "UK": 44, "FR": 54, "DE": 54, "IT": 54, "AU": 44, "JP": 6},
]

def convert_clothing_size(value, from_country, to_country, gender):
    gender = gender.lower()
    from_country = from_country.upper()
    to_country = to_country.upper()

    table = WOMEN_SIZES if gender == "women" else MEN_SIZES

    for row in table:
        if row[from_country] == value:
            return row[to_country]

    raise ValueError("Size not found for this gender")


#menus
def temperature_menu():
    print("\nTemperature conversions:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")

    choice = input("Choose an option: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"Result: {celsius_to_fahrenheit(value):.2f} °F")
    elif choice == "2":
        print(f"Result: {fahrenheit_to_celsius(value):.2f} °C")
    elif choice == "3":
        print(f"Result: {celsius_to_kelvin(value):.2f} K")
    elif choice == "4":
        print(f"Result: {kelvin_to_celsius(value):.2f} °C")
    else:
        print("Invalid option")


def length_menu():
    print("\nLength conversions:")
    print("1. Meters → Kilometers")
    print("2. Kilometers → Meters")
    print("3. Meters → Feet")
    print("4. Feet → Meters")

    choice = input("Choose an option: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(f"Result: {meters_to_kilometers(value):.4f} km")
    elif choice == "2":
        print(f"Result: {kilometers_to_meters(value):.2f} m")
    elif choice == "3":
        print(f"Result: {meters_to_feet(value):.2f} ft")
    elif choice == "4":
        print(f"Result: {feet_to_meters(value):.2f} m")
    else:
        print("Invalid option")

def clothing_menu():
    print("\nClothing size conversion")
    gender = input("Gender (men / women): ").strip().lower()

    value = input("Size (e.g. S, M, 38): ").strip()
    try:
        value = int(value)
    except ValueError:
        value = value.upper()

    from_c = input("From country (INTL, USA, UK, FR, DE, IT, AU, JP): ").upper()
    to_c = input("To country (USA, UK, FR, DE, IT, AU, JP): ").upper()

    try:
        result = convert_clothing_size(value, from_c, to_c, gender)
        print(f"Result: {value} ({from_c}) → {result} ({to_c}) [{gender}]")
    except ValueError as e:
        print("Error:", e)


def main():
    while True:
        print("\n=== Conversion Tool ===")
        print("1. Temperature")
        print("2. Length")
        print("3. Clothing sizes (men / women)")
        print("0. Exit")

        choice = input("Choose a category: ")

        if choice == "1":
            temperature_menu()
        elif choice == "2":
            length_menu()
        elif choice == "3":
            clothing_menu()
        elif choice == "0":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
