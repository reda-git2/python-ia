# À améliorer : gérer les saisies invalides (texte, âge négatif) avec try/except
reponse = input("quel est votre âge? ")
age = int(reponse)
if age < 18:
    print("tu es mineur")
else:
    print("tu es majeur")