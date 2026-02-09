# main.py
"""To run this, you need to pip install openfoodfacts"""

import openfoodfacts

api = openfoodfacts.API(user_agent="MySchoolProject/1.0 (demerdjievm99@mail.com)")


def main():
    while True:
        code = input("Enter the product code: ")

        product = getProduct(code)

        nutriscoreAnalyze(product)

        # type of product is dict
        print(product)


def nutriscoreAnalyze(product):
    nutriscore = product["nutrition_grades"]
    if nutriscore in ["a", "b"]:
        print("\n Safe to consume :)\n")
    elif nutriscore in ["c"]:
        print("\n To be consumed with moderation\n")
    elif nutriscore in ["d", "e"]:
        print("\n NOT SAFE\n")
    else:
        print(" Nutriscore not applicable ")


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
