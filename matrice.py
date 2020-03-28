 # -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    import numpy as np
    a = np.zeros(shape=(nbLignes,nbColonnes))
    return a

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice[0])

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice[ligne][colonne]=valeur


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    ligne=matrice[numLig]
    x=ligne[0]
    for i in range(len(ligne)-1):
      ligne[i]=ligne[i+1]
    ligne[-1]=nouvelleValeur
    return x


def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    ligne=matrice[numLig]
    x=ligne[-1]
    for i in range(len(ligne)-1):
      ligne[i]=ligne[i-1]
    ligne[0]=nouvelleValeur
    return x
  
def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    x=matrice[0][numCol]
    for ligne in range(len(matrice)-1):
      matrice[ligne][numCol]=matrice[ligne+1][numCol]
    matrice[-1][numCol]=nouvelleValeur
    return x


def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    x=matrice[-1][numCol]
    for ligne in range(len(matrice)-1):
      matrice[ligne][numCol]=matrice[ligne-1][numCol]
    matrice[0][numCol]=nouvelleValeur
    return x

if __name__=='__main__':  
  matrice=Matrice(3,4,valeurParDefaut=0)
  print(matrice)
  print(getNbLignes(matrice))
  print(getNbColonnes(matrice))
  print(getVal(matrice,1,0))
  print(setVal(matrice,1,1,2))
  print(matrice)
  print(decalageLigneAGauche(matrice, 0, nouvelleValeur=7))
  print(matrice)
  print(decalageLigneADroite(matrice, 2, nouvelleValeur=3))
  print(matrice)
  print(decalageColonneEnHaut(matrice, 3, nouvelleValeur=8))
  print(matrice)
  print(decalageColonneEnBas(matrice, 1, nouvelleValeur=9))
  print(matrice)