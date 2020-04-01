from ruler import Ruler
import sys

dataset = sys.argv[1]

"""On ouvre le fichier contenant les chaines à comparer.
    On parcourt le fichier et on remplit une liste avec les lignes non vides du texte.
    On compare les lignes deux à deux en utilisant la classe Ruler. puis on 
    renvoie sous le format demandé les informations voulues
    """

with open(dataset, 'r') as fichier: #ouvre le fichier dataset
    liste = []
    
    for ligne in fichier.readlines():
        if ligne != '\n': #la ligne est non vide
            
            if ligne[-1] == '\n': 
                ligne = ligne[:-1]
            
            liste.append(ligne)
            i = 1
            if len(liste)>1:
                ruler = Ruler(liste[0], liste[1])
                ruler.compute()
                print(f'====== example # {i} - distance = {ruler.distance}')
                print(ruler.top)
                print(ruler.bottom)
                i = i+1
                liste = []


