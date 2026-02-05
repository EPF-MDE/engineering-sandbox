from playwright.sync_api import sync_playwright
import time


def est_dans_le_frigo(ingredients_recette, mon_frigo):
    """Vérifie si les ingrédients principaux du frigo sont dans la recette"""
    recette_str = " ".join(ingredients_recette).lower()
    # On compte combien d'ingrédients du frigo sont trouvés
    trouves = [ing for ing in mon_frigo if ing.lower() in recette_str]

    # On considère que ça matche si au moins 75% des ingrédients du frigo sont dedans
    # Ou vous pouvez changer pour exiger 100% (len(trouves) == len(mon_frigo))
    return len(trouves) >= len(mon_frigo) * 0.75


def master_chef_marmiton(ingredients_frigo):
    query = " ".join(ingredients_frigo)
    url_recherche = f"https://www.marmiton.org/recettes/recherche.aspx?aqt={query}"

    valides = []

    with sync_playwright() as p:
        print("👨‍🍳 Démarrage du robot cuisinier...")
        browser = p.chromium.launch(headless=True)  # Mettre True pour cacher la fenêtre
        context = browser.new_context()
        page = context.new_page()

        # --- ÉTAPE 1 : RECHERCHE GLOBALE ---
        print(f"🌍 Recherche des recettes pour : {ingredients_frigo}")
        page.goto(url_recherche, wait_until="domcontentloaded")

        # Gestion cookies
        try:
            if page.locator("#didomi-notice-agree-button").is_visible():
                page.click("#didomi-notice-agree-button")
                time.sleep(1)
        except:
            pass

        # Récupération des liens (limité aux 3 premiers pour pas y passer la nuit)
        liens_bruts = page.locator("a[href*='/recettes/recette_']").all()
        urls_a_tester = []
        for l in liens_bruts[:3]:
            u = l.get_attribute("href")
            # if u != None and u not in urls_a_tester:
            if u and u not in urls_a_tester:
                if not u.startswith("http"):
                    u = "https://www.marmiton.org" + u
                urls_a_tester.append(u)

        # Dédoublonnage
        urls_a_tester = list(set(urls_a_tester))
        print(
            f"🧐 {len(urls_a_tester)} recettes potentielles trouvées. Analyse des ingrédients en cours..."
        )

        # --- ÉTAPE 2 : INSPECTION DÉTAILLÉE ---
        for i, url in enumerate(urls_a_tester, 1):
            print(f"   [{i}/{len(urls_a_tester)}] Analyse de la recette...")
            try:
                page.goto(url, wait_until="domcontentloaded")

                # Récupération du titre
                titre = page.title().split("-")[0].strip()

                # --- SÉLECTEUR D'INGRÉDIENTS ---
                # Marmiton met les ingrédients dans des div spécifiques.
                # On récupère tout le texte de la zone ingrédients.
                # Sélecteurs courants 2025/2026 : .card-ingredient, .ingredient-name, .mrtn-recette_ingredients

                liste_ingr = []
                # On essaie de trouver les blocs d'ingrédients
                elements = page.locator(
                    ".card-ingredient-content, .item-ingredient-name, .recipe-ingredients__list__item"
                ).all_inner_texts()

                if not elements:
                    # Fallback : on cherche n'importe quel texte sous la section "Ingrédients"
                    elements = page.locator(
                        ".mrtn-recette_ingredients-items"
                    ).all_inner_texts()

                # Nettoyage des textes
                liste_ingr = [
                    e.replace("\n", " ").strip() for e in elements if len(e) > 2
                ]

                # --- VÉRIFICATION ---
                if est_dans_le_frigo(liste_ingr, ingredients_frigo):
                    print(f"      ✅ MATCH ! Cette recette contient vos ingrédients.")
                    valides.append(
                        {"nom": titre, "url": url, "ingredients": liste_ingr}
                    )
                else:
                    print(f"      ❌ Ignoré (Ingrédients manquants)")

            except Exception as e:
                print(f"      ⚠️ Erreur sur cette page : {e}")
                continue

        browser.close()
        return valides


print("------------------------------------------------")
print("🥦 QU'AVEZ-VOUS DANS VOTRE FRIGO ?")
print("Séparez les ingrédients par une virgule (ex: poulet, crème, curry)")
print("------------------------------------------------")

user_input = input("Votre liste > ")

# Traitement de l'entrée :
# 1. On coupe à chaque virgule (.split(','))
# 2. On enlève les espaces autour (.strip())
# 3. On ignore les entrées vides
mon_frigo = [item.strip() for item in user_input.split(",") if item.strip()]

if not mon_frigo:
    print("❌ Vous n'avez rien écrit ! Je ne peux pas cuisiner du vide.")
else:
    print(f"\nRecherche en cours avec : {mon_frigo} ...")
    resultats = master_chef_marmiton(mon_frigo)

    print("\n" + "=" * 40)
    print(f"🥗 RÉSULTAT : {len(resultats)} RECETTES IDEALES")
    print("=" * 40)

    for r in resultats:
        print(f"\n🥘 {r['nom']}")
        print(f"🔗 {r['url']}")
        print(f"📝 Ingrédients clés : {', '.join(r['ingredients'][:5])}...")
