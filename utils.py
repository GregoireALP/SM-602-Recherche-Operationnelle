# utils.py

import numpy as np

import numpy as np

def lire_fichier_sans_capacite(nom_fichier):
    """
    Lit un fichier contenant uniquement une matrice de capacités (sans ligne indiquant n).
    Renvoie la matrice sous forme de tableau numpy.
    """
    with open(nom_fichier, 'r') as f:
        lignes = [ligne.strip() for ligne in f if ligne.strip()]
    
    matrice = [list(map(int, ligne.split())) for ligne in lignes]
    return np.array(matrice)
    
def afficher_capacites(mat):
    n = mat.shape[0]
    print(f"{n}")
    for ligne in mat:
        print(" ".join(f"{val:3d}" for val in ligne))

def afficher_couts(mat):
    n = mat.shape[0]
    for ligne in mat:
        print(" ".join(f"{val:3d}" for val in ligne))
