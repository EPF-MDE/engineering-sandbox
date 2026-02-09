# main.py
"""To run this, you need to pip install openfoodfacts"""

import openfoodfacts

api = openfoodfacts.API(user_agent="MySchoolProject/1.0 (demerdjievm99@mail.com)")


def main():
    code = input("Enter the product code: ")
    product = api.product.get(code, fields=["code", "product_name", "nutrition_grades"])
    print(type(product))


if __name__ == "__main__":
    main()
