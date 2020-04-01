from colorama import Fore, Style
import numpy as np

class Ruler :
    """ classe qui récupère deux chaines de caratère et détermine leur 
    alignement en mettant en valeur les différences selon 
    l'algo de Needleman-Wunsch """
    
    def __init__(self, chaine1, chaine2):
        """Constructeur de la class Ruler
        
        Entree :
            - chaine1 : str -> premiere chaine à comparer
            - chaine2 : str -> deuxieme chaine à comparer
        """
        
        self.chaine1 = chaine1
        self.chaine2 = chaine2
        self.distance = None
        self.top = None
        self.bottom = None
        
    
    def compute(self):
        """
        On commence par construire une matrice qui calcule les 
        Dans la 1ere colonne se trouve chaque caractère de la chaine1, et 
        dans la 1ere ligne se trouve chaque caractère de la chaine2
        On remplit ensuite la matrice en choisissant à chaque fois le minimum des trois choix (voir algo).
        La distance entre les deux chaies est le coefficient se trouvant dans la dernière ligne et dernière colonne.
        On construit ensuite les deux chaines qui sont comparées (self.bottom et self.top). 
        Différents cas se présentent alors, on utilise des symboles '=' en rouge dans la chaine self.bottom
        si un caractère manque, on met en rouge les caractères des deux chaines si ceux-ci sont différents.
        """
    
        
        taille = (len(self.chaine1)+1,len(self.chaine2)+1)
        matrice = np.zeros(taille)
        
        for i in range(taille[0]):
            matrice[i,0] = i
        
        for j in range(taille[1]):
            matrice[0,j] = j
            
        for i in range(1, taille[0]):
            for j in range(1,taille[1]):
                choix1 = matrice[i,j-1] + 1 #hypothèse départ(d=1)
                choix2 = matrice[i-1,j] + 1
                choix3 = matrice[i-1,j-1] + int(self.chaine1[i-1]!=self.chaine2[j-1])
                matrice[i,j] = min(choix1, choix2, choix3)
                
        self.distance = matrice[-1,-1]
    
        self.bottom = ''
        self.top = ''
        i = len(self.chaine1)
        j = len(self.chaine2)
        
        while i>0 or j>0:
            if i>0 and j>0 and matrice[i,j] == matrice[i-1, j-1] + int(self.chaine1[i-1]!=self.chaine2[j-1]):
                if self.chaine1[i-1] == self.chaine2[j-1]:
                    self.top = self.chaine1[i-1] + self.top 
                    self.bottom = self.chaine2[j-1] + self.bottom
                else :
                    self.top = red_text(self.chaine1[i-1]) + self.top 
                    self.bottom = red_text(self.chaine2[j-1]) + self.bottom
                    
                i = i-1
                j = j-1
                
            elif i>0 and matrice[i,j] == (matrice[i-1,j] + 1):
                self.top = self.chaine1[i-1] + self.top 
                self.bottom = red_text('=') + self.bottom
                i = i-1
        
            else : 
                self.top = red_text('=') + self.top 
                self.bottom = self.chaine2[j-1] + self.bottom
                j = j-1
    
    def report(self):
        """cette fonction renvoie les deux chaines comparées"""
        
        return self.top, self.bottom
    

def red_text(text):
    """Transforme un texte en rouge
    
    Entree :
        - text : str -> chaine de caractère a changer
    Sortie :
        - str -> chaine de caractère transformée
    """
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

