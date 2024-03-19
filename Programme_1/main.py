"""
Premier programme
"""

# Fonction pour demander le prénom
def demander_prenom():
    reponse_prenom = ""
    while reponse_prenom == "":
        reponse_prenom = input("Quel est ton prénom ?\n")
    return reponse_prenom


# Fonction pour demander l'âge
def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est ton âge ?\n")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR : Tu dois entrer un nombre !")
    return age_int


# On demande le prénom
prenom = demander_prenom()

# On demande l'âge
age = demander_age()
        
# On affiche les résultats
print("Tu t'appelle " + prenom + " et tu as " + str(age) + " ans.")
print("L'an prochain, tu auras " + str(age+1) + " ans.")



