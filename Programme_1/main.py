"""
Premier programme
"""

# On demande le prénom et l'âge
prenom = input("Quel est ton prénom ?\n")
age = input("Quel est ton âge ?\n")
try:
    ageProchain = int(age) + 1
    # On affiche les résultats
except ValueError:
    print("ERREUR : Tu dois entrer un nombre !")
else:
    print("Tu t'appelle " + prenom + " et tu as " + age + " ans.")
    print("L'an prochain, tu auras " + str(ageProchain) + " ans.")


