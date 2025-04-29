from arete import Arete
from sommet import Sommet
from graph import Graph

def get_graph_object_from_text(path):
    sommets = []
    aretes = []

    # Lire le fichier et construire la matrice d'adjacence
    with open(path, 'r') as fichier:
        matrice = [list(map(int, ligne.split())) for ligne in fichier.readlines()]

    # Créer les sommets
    for i in range(len(matrice)):
        if i == 0:
            sommets.append(Sommet(etiquette="s", rentrant=[], sortant=[]))
        elif i == len(matrice) - 1:
            sommets.append(Sommet(etiquette="t", rentrant=[], sortant=[]))
        else:
            sommets.append(Sommet(etiquette=i, rentrant=[], sortant=[]))

    # Créer les arêtes à partir de la matrice d'adjacence
    for i, ligne in enumerate(matrice):
        for j, valeur in enumerate(ligne):
            if valeur > 0:  # Si une connexion existe
                arete = Arete(origine=sommets[i], destination=sommets[j], capacite=valeur, cout=0)
                aretes.append(arete)
                sommets[i].sortant.append(arete)
                sommets[j].rentrant.append(arete)

    # Créer et retourner l'objet Graph
    return Graph(aretes=aretes, sommets=sommets)

# Exemple d'utilisation
graph = get_graph_object_from_text('assets/model/test.txt')
parcours = graph.parcoursEnLargeur()
for sommet in parcours:
    print(sommet.etiquette, end=" ")
print("\n")