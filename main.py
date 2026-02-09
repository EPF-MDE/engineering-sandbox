# main.py
"""To run this, you need to pip install openfoodfacts"""

import openfoodfacts

api = openfoodfacts.API(user_agent="MySchoolProject/1.0 (demerdjievm99@mail.com)")


def main():
    code = input("Enter the product code: ")
    product = getProduct(code)

    # type of product is dict
    print(product)


def getProduct(code):
    product = api.product.get(
        code,
        fields=[
            "code",
            "product_name",
            "nutrition_grades",
            "nova_group",
            "nova_groupnova-group",
            "nova-group_100g",
            "nove-group-serving",
        ],
    )
    return product


if __name__ == "__main__":
    main()
