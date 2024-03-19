"""
Premier programme
"""

# On demande le prénom
prenom = ""
while prenom == "":
    prenom = input("Quel est ton prénom ?\n")

# On demande l'âge
age = 0
while age == 0:
    age_str = input("Quel est ton âge ?\n")
    try:
        age = int(age_str)
    except:
        print("ERREUR : Tu dois entrer un nombre !")
        
# On affiche les résultats
print("Tu t'appelle " + prenom + " et tu as " + str(age) + " ans.")
print("L'an prochain, tu auras " + str(age+1) + " ans.")



