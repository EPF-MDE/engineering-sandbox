# main.py
"""To run this, you need to pip install openfoodfacts"""

import openfoodfacts

api = openfoodfacts.API(user_agent="MySchoolProject/1.0 (demerdjievm99@mail.com)")

code = "3350033976269"
print(api.product.get(code, fields=["code", "product_name", "nutrition_grades"]))

print("hello j'ai reussi à push sur GitHub")
