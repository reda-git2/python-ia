# somme minimum et maximum d'une liste

# initialisation
nombres = [5, 4, 7, 15, 10, 21]
somme = 0
minimum = nombres[0]
maximum = nombres[0]

# boucle somme, minimum et maximum
for nombre in nombres:
    somme += nombre

    if minimum > nombre:
        minimum = nombre 

    if maximum < nombre:
        maximum = nombre 

# affichage
print("La somme de la liste est:", somme)
print("Le minimum est:", minimum)
print("Le maximum est:", maximum)
