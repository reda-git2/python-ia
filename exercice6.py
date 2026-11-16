# inversion d'une liste sans reverse

# initialisation
nombres = [3, 8, 1, 5]
nombres_inverses = []

# boucle qui parcourt la liste et inverse la liste
for i in range(len(nombres) - 1, -1, -1):
    nombres_inverses.append(nombres[i])

# affichage de la liste normal et son inversion
print("la liste est:", nombres)
print("la liste inversée est:", nombres_inverses)