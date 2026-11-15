# affichage d un nombre de 1 a 100 en remplaçant les multiple de 3 par Fizz et ceux de 5 par Buzz et et les deux par FizzBuzz

for i in range(1, 101):
    resultat = "vide"
    if i % 3 == 0:
        resultat = "Fizz"
    if i % 5 == 0:
        resultat = "Buzz"
    if i % 3 == 0 and i % 5 == 0:
        resultat = "FizzBuzz"
    if resultat == "vide":
        resultat = i
    print (resultat)