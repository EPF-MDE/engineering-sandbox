from playwright.sync_api import sync_playwright
import time


def est_dans_le_frigo(ingredients_recette, mon_frigo):
    """Verify if the main ingredients from the fridge are in the recipe"""
    recette_str = " ".join(ingredients_recette).lower()
    # We count how many of the fridge ingredients are present in the recipe
    trouves = [ing for ing in mon_frigo if ing.lower() in recette_str]

    # We consider it valid if we have at least 75% of the fridge ingredients
    # Or we can change the rule to require 100% (len(trouves) == len(mon_frigo))
    return len(trouves) >= len(mon_frigo) * 0.75


def master_chef_marmiton(ingredients_frigo):
    query = " ".join(ingredients_frigo)
    url_recherche = f"https://www.marmiton.org/recettes/recherche.aspx?aqt={query}"

    valides = []

    with sync_playwright() as p:
        print("👨‍🍳 Starting the cooking robot...")
        browser = p.chromium.launch(
            headless=True
        )  # Set to True to hide the browser window
        context = browser.new_context()
        page = context.new_page()

        # --- STEP 1 : GLOBAL SEARCH ---
        print(f"🌍 Searching with ingredients: {ingredients_frigo}")
        page.goto(url_recherche, wait_until="domcontentloaded")

        # Cookie handling
        try:
            if page.locator("#didomi-notice-agree-button").is_visible():
                page.click("#didomi-notice-agree-button")
                time.sleep(1)
        except:
            pass

        # Retrieve recipe links (limited to 3 for simplicity)
        liens_bruts = page.locator("a[href*='/recettes/recette_']").all()
        urls_a_tester = []
        for lien in liens_bruts[:3]:
            url_final = lien.get_attribute("href")
            # if u != None and u not in urls_a_tester:
            if url_final and url_final not in urls_a_tester:
                if not url_final.startswith("http"):
                    url_final = "https://www.marmiton.org" + url_final
                urls_a_tester.append(url_final)

        # Remove duplicates
        urls_a_tester = list(set(urls_a_tester))
        print(
            f"🧐 {len(urls_a_tester)} potential recipes found. Analyzing ingredients..."
        )

        # --- STEP 2 : DETAILED INSPECTION ---
        for i, url in enumerate(urls_a_tester, 1):
            print(f"   [{i}/{len(urls_a_tester)}] Analyzing recipe...")
            try:
                page.goto(url, wait_until="domcontentloaded")

                # Retrieve the title
                titre = page.title().split("-")[0].strip()

                # --- INGREDIENT SELECTOR ---
                # Marmiton stores ingredients in specific div blocks
                # We extract all ingredients from the ingredient section
                # Common selectors in 2025/2026 :
                # .card-ingredient, .ingredient-name, .mrtn-recette_ingredients

                liste_ingr = []
                # Try to locate the ingredient blocks
                elements = page.locator(
                    ".card-ingredient-content, .item-ingredient-name, .recipe-ingredients__list__item"
                ).all_inner_texts()

                if not elements:
                    # Fallback: search for any text under the 'Ingredients' section
                    elements = page.locator(
                        ".mrtn-recette_ingredients-items"
                    ).all_inner_texts()

                # Clean extracted texts
                liste_ingr = [
                    e.replace("\n", " ").strip() for e in elements if len(e) > 2
                ]

                # --- VERIFICATION ---
                if est_dans_le_frigo(liste_ingr, ingredients_frigo):
                    print(f"      ✅ MATCH! This recipe contains your ingredients.")
                    valides.append(
                        {"nom": titre, "url": url, "ingredients": liste_ingr}
                    )
                else:
                    print(f"      ❌ Skipped (missing ingredients)")

            except Exception as e:
                print(f"      ⚠️ Error on this page: {e}")
                continue

        browser.close()
        return valides


print("------------------------------------------------")
print("🥦 WHAT DO YOU HAVE IN YOUR FRIDGE?")
print("Separate ingredients with a comma in FRENCH  (ex: chicken, cream, curry)")
print("------------------------------------------------")

user_input = input("Your list > ")

# Processing the input:
# 1. Split by comma (.split(','))
# 2. Remove spaces (.strip())
# 3. Ignore empty inputs
mon_frigo = [item.strip() for item in user_input.split(",") if item.strip()]

if not mon_frigo:
    print("❌ You didn't enter anything! I can't cook with nothing.")
else:
    print(f"\nSearching with: {mon_frigo} ...")
    resultats = master_chef_marmiton(mon_frigo)

    print("\n" + "=" * 40)
    print(f"🥗 RESULT: {len(resultats)} IDEAL RECIPES")
    print("=" * 40)

    for r in resultats:
        print(f"\n🥘 {r['nom']}")
        print(f"🔗 {r['url']}")
        print(f"📝 Key ingredients: {', '.join(r['ingredients'][:5])}...")
