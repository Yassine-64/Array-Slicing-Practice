def Sous_tab(tab, e, f):
    sous_tableau = []
    for i in range(e, f):
        sous_tableau.append(tab[i])
    return sous_tableau

while True:
    T = []
    for i in range(10):
        valeur = int(input(f"veuillez entrez la valeur {i + 1}"))
        T.append(valeur)

    indice_debut = int(input("Veuillez entrer un entier: "))
    indice_fin = int(input("Veuillez entrer un entier: "))

    resultat = Sous_tab(T, indice_debut, indice_fin)
    print("Sous-tableau extrait:", resultat)

    reponse = input("Voulez-vous une nouvelle liste? (oui/non): ")
    if reponse != "oui":
        break
