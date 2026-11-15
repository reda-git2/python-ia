# demande et validation du choix
conversion = input("Quelle conversion voulez vous faire? (f pour Fahrenheit en Celsius ou c pour Celsius en Fahrenheit): ")
while conversion != "f" and conversion != "c":
    conversion = input("Veuillez choisir f pour Fahrenheit en Celsius ou c pour Celsius en Fahrenheit: ")

# demande de la température
temperature = float(input("combien de degrés?: "))

# calcul et affichage de la conversion
if conversion == "f":
    reponse = round((temperature - 32) * 5 / 9, 1)
    print("votre conversion est", reponse, "degrés celsius")
elif conversion == "c":
    reponse = round(temperature * 9 / 5 + 32, 1)
    print("votre conversion est", reponse, "degrés Fahrenheit")




