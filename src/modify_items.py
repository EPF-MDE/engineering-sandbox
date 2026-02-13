import json
from pathlib import Path
from datetime import datetime

# Define the path to the data file
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "data.json"

# Ensure the data directory exists
if DATA_FILE.exists():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        products = json.load(f)
else:
    products = []


def RegisterNewProduct():
    product_name = input("Enter product name : ")

    # Validate the expiry date format
    while True:
        input_expiry_date = input("Enter Expiry Date (DD/MM/YYYY) : ")
        try:
            product_expiry_date = datetime.strptime(
                input_expiry_date, "%d/%m/%Y"
            ).date()
            break
        except ValueError:
            print("Retry. Invalid format. Example : 12/07/2009")

    new_product = {
        "name": product_name,
        "date": product_expiry_date.strftime("%d/%m/%Y"),
    }

    products.append(new_product)

    # Save the updated products list back to the JSON file
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file)


# Function to delete an existing product
def DeleteExistingProduct():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        products = json.load(f)
    possibleProducts = []

    productName = input("What item do you want to delete?")
    for product in products:
        if product["name"] == productName:
            possibleProducts.append(product)
    if len(possibleProducts) == 0:
        print("\nThis product doesn't exist\n")
        return
    elif len(possibleProducts) <= 1:
        products.remove(possibleProducts[0])
    else:
        for i in range(len(possibleProducts)):
            print(f"{i + 1}. {possibleProducts[i]}")
        while True:
            try:
                productToRemove = int(
                    input("What product do you want to remove? (Write the number)")
                )
            except ValueError:
                print("\n Value error. Please write a correct number")
            try:
                if productToRemove <= 0:
                    indexErrorList = []
                    indexErrorList[1]
                products.remove(possibleProducts[productToRemove - 1])
                break
            except IndexError:
                print("\n Value error. Please write a correct number")
    # Save the updated products list back to the JSON file
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file)
