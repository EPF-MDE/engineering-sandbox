from datetime import datetime



## Functions ##

def Course():
    Course_d = {}
    nom_depense = input("Nom de la dépense : ")
    Course_d["Nom"] = nom_depense
    while True:
        try:
            date = input("Date de la dépense (JJ/MM/AAAA) : ")
            date = datetime.strptime(date, "%d/%m/%Y")
            Course_d["Date"] = date
            break
        except ValueError:
            print("Format invalide. Veuillez entrer la date au format JJ/MM/AAAA.")
    # Course["date"] = date
    while True:
        try:
            prix = int(input("Prix  : "))
            Course_d["Prix"] = prix
            break
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")
    print("\nrécap ->", Course_d)


def Charge():
    Charge_d = {}
    nom_depense = input("Nom de la depense : ")
    Charge_d["Nom"] = nom_depense
    while True:
        try:
            date = input("Date de la dépense (JJ/MM/AAAA) : ")
            date = datetime.strptime(date, "%d/%m/%Y")
            print(date)
            Charge_d["Date"] = date
            print(date)
            break
        except ValueError:
            print("Format invalide. Veuillez entrer la date au format JJ/MM/AAAA.")
    # Charge_d["date_depense"] = date
    while True:
        try:
            prix = int(input("Prix : "))
            Charge_d["Prix"] = prix
            break
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")
    print("\nrécap ->", Charge_d)


def Loisir():
    Loisir_d = {}
    nom_depense = input("nom de la depense : ")
    Loisir_d["Nom"] = nom_depense
    while True:
        try:
            date = input("Date de la dépense (JJ/MM/AAAA) : ")
            date = datetime.strptime(date, "%d/%m/%Y")
            Loisir_d["Date"] = date
            break
        except ValueError:
            print("Format invalide. Veuillez entrer la date au format JJ/MM/AAAA.")
    # Loisir_d["date_depense"] = date
    while True:
        try:
            prix = int(input("Prix : "))
            Loisir_d["Prix"] = prix
            break
        except ValueError:
            print("Erreur : Veuillez entrer un entier valide.")
    print("\nrécap -> ", Loisir_d)

creations_l = []
def Creation():
    nom_utilisateur = input("Veillez créer votre nom d'utilisateur : ")
    mdp = input("Veillez créer votre mot de passe : ")

    creation_l = {"nom" : nom_utilisateur, "password" : mdp}
    creations_l.append(creation_l)
    print("Compte bien créé !")



def Connexion():
    nom_utilisateur = input("Veillez indiquer votre nom d'utilisateur : ")
    mdp = input("Veuillez indiquer le mot de passe : ")
    for creation_l in creations_l:
        if creation_l["nom"] != nom_utilisateur and creation_l["password"] != mdp:
            print("Connexion échouée, nom d'utilisateur ou mot de passe incorect !")
        else:
            print("Connexion réussie !")



## Main ##
if __name__ == "__main__" :
    print("Bonjour à toi, bienvenue sur ta plateforme 'tracking expenses' !")
    choix = int(input("1. Création de compte \n2. Connexion au compte \n-> "))


    if choix == 1:
        Creation()
        Connexion()
    elif choix == 2:
        Connexion()
    else:
        print("Saisissez 1 ou 2 !")
        
    print ("\nTu peux à présent sélectionner ta catégorie parmi les trois chois suivants : 'Course','Charge', 'Loisir'")
    
    ta_catégorie = input("-> ")
    if ta_catégorie == "Course":
        Course()
    elif ta_catégorie == "Charge":
        Charge()
    elif ta_catégorie == "Loisir":
        Loisir()
    else:
        print(
            "Attention ! Tu dois revoir la syntaxe de ta réponse",
            "elle doit respecter la même syntaxe que dans les propositions. ",
        )
