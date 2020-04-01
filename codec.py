

class Node: 
    """ cette classe permet de définir un objet noeud """
    
    def __init__(self, voisin_gauche = None, voisin_droite = None, nom = None):
        """Constructeur de la classe Node
        
        Entrée:
            - voisin_gauche : str -> correspond au voisin gauche du noeud 
            - voisin_droite : str -> correspond au voisin droite du noeud 
            - nom : str -> correspond au nom du noeud
        """ 
        
        self.voisin_gauche = voisin_gauche
        self.voisin_droite = voisin_droite
        self.nom = nom
        
        
    
class TreeBuilder:
    """Cette classe permet la construction d'un arbre binaire en utilisant le codage d'Huffman"""
    
    def __init__(self, text):
        """Constructeur de la classe Treebuilder
        
        Entree:
            - text : str -> correspond au texte que l'on souhaite coder 
        """
        
        self.text = text
    
    def tree(self): ###
        """Construction de l'arbre binaire.
        On récupère chaque lettre du texte et on indique son occurence dans un dictionnaire (dico).
        On crée une liste de noeuds que l'on trie par ordre croissant suivant l'occurence qui correspondait 
        à la lettre avant sa transformation en noeud.
        On construit ensuite l'arbre en reliant les deux premiers noeuds de la liste_noeud ce qui conduit à
        un nouveau noeud que l'on intègre ensuite dans la liste des noeuds. On retrie à la nouvelle liste_noeud par 
        ordre croissant, en cas d'égalité entre deux elements lors du tri, les noeuds deja reliées sont moins prioritaires. 
        On réitère ce processus jusqu'à ce qu'il ne reste qu'un  seul noeud (appelé noeud-racine).
        
        Sortie :
            - noeud -> on revoie le noeud racine (noeud à partir duquel sont reliés tous les autres noeuds)
        """
        
        liste_lettres = list(set(self.text))
        dico = {lettre: self.text.count(lettre) for lettre in liste_lettres}
        def f(noeud):
            """ fonction qui renvoie les clés pour le tri"""
            return dico[noeud.nom]
        liste_noeuds = [Node(nom = c) for c in liste_lettres]
        liste_noeuds = sorted(liste_noeuds, key = f) 
        
        while len(liste_noeuds) > 1:
            n1 = liste_noeuds.pop(0)
            n2 = liste_noeuds.pop(0)
            nouveau_noeud = Node(n1, n2, n1.nom + n2.nom)
            dico[nouveau_noeud.nom] = dico[n1.nom] + dico[n2.nom] 
            liste_noeuds.append(nouveau_noeud)
            #Pas de soucis avec le placement du nouveau noeud apres tri
            #Il sera placé apres les noeuds prioritaires puisque ajouté a la fin de liste
            liste_noeuds = sorted(liste_noeuds, key = f) 
            #Le nouveau noeud etant placé a la fin, il sera placé derriere ceux ayants une occurence equivalente.
            
        return liste_noeuds[0] #on renvoie le seul noeud qui reste dans la liste_noeuds
    

class Codec:
    
    def __init__(self, noeud_racine):
        self.noeud_racine = noeud_racine

    def encode(self, txt):
        code = ''
        noeud = self.noeud_racine 
        for c in txt:
            while len(noeud.nom) > 1:
                if c in noeud.voisin_gauche.nom:
                    code += '0'
                    noeud = noeud.voisin_gauche
                else:
                    code += '1'
                    noeud = noeud.voisin_droite
            noeud = self.noeud_racine
        return code
    
    def decode(self, code):
        txt = ''
        noeud = self.noeud_racine
        for b in code:
            if b == '0':
                noeud = noeud.voisin_gauche
            else:
                noeud = noeud.voisin_droite
            if len(noeud.nom) == 1:
                txt += noeud.nom
                noeud = self.noeud_racine
        return txt

    
text = "a dead dad ceded a bad babe a beaded abaca bed"
builder = TreeBuilder(text)
binary_tree = builder.tree()


            
            
    
            
        
    

