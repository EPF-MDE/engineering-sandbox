# main.py
"""To run this, you need to pip install openfoodfacts"""

import google.generativeai as genai
import openfoodfacts
import os

api = openfoodfacts.API(user_agent=os.environ.get("API_OPENFOODFACTS_USER_AGENT"))

genai.configure(api_key=os.environ.get("API_GEMINI_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")


def main():
    while True:
        code = input("Enter the product code: ")

        product = getProduct(code)

        nutriscoreAnalyze(product)

        # type of product is dict


def nutriscoreAnalyze(product):
    nutriscore = product["nutrition_grades"]
    if nutriscore in ["a", "b"]:
        print("\n Safe to consume :)\n")
    elif nutriscore in ["c"]:
        print("\n To be consumed with moderation\n")
    elif nutriscore in ["d", "e"]:
        print("\n NOT SAFE\n")
        AIResponse(product)

    else:
        print(" Nutriscore not applicable ")


def AIResponse(product):
    product_name = product["product_name"]
    response = model.generate_content(
        f"The following product has a Nutri-score of d or e: {product_name}. Give me an alternative to this product which would be safer to consume. I need a very brief response."
    )
    print(response.text)


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
