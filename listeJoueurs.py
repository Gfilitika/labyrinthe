# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    l=[]
    for x in nomsJoueurs:
      l.append(Joueur(x))
    return {'liste':l,'indice':0} 

def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs une liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs['liste'].append(joueur)

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs une liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    nbJoueurs=len(joueurs['liste'])
    joueurs['indice']=random.randint(0,nbJoueurs)

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """ 
    x=int(nbTresors/len(joueurs['liste']))
    for val in range(x-1):
      tresor=random.randint(0,nbTresorMax)
      for joueur in joueurs['liste']: 
        if joueur['tresor']!=nbTresors:
          joueur['tresor'].append(ajouterTresor(joueur,tresor))
      
      
      
    
def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """   
    joueurs['indice']=joueurs['indice']+1

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    cpt=0
    for joueur in joueurs['liste']:
      cpt=cpt+1
    return cpt

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs['liste'][joueurs['indice']]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorTrouve(joueurs['liste']['indice'])
    

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    nbtresor=getNbTresorsRestants(joueurs['liste'][numJoueur])
    return nbtresor

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs['indice']

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    nom=getNom(joueurs['liste'][joueurs['indice']])
    return nom
    

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    nom=getNom(joueurs['liste'][numJoueur])
    return nom


def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    tresor=prochainTresor(joueurs[numJoueur])
    return tresor

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(joueurs['liste'][joueurs['indice']])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    res=False
    if joueurs['liste'][joueurs['indice']]['tresors']==[]:
      res=True
    return res

if __name__=='__main__':
  joueurs=(ListeJoueurs(['Joseph','Mathieu','Pierre']))
  print(joueurs)
  #print(ajouterJoueur(joueurs, 'Leon'))
  #print(joueurs)
  #print(initAleatoireJoueurCourant(joueurs))
  #print(joueurs)
  ##print(distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0))
  #print(joueurs)
  #print(changerJoueurCourant(joueurs))
  #print(joueurs)
  #print(getNbJoueurs(joueurs))
  #print(getJoueurCourant(joueurs))
  #print(joueurCourantTrouveTresor(joueurs))
  #print(joueurs)
  #print(nbTresorsRestantsJoueur(joueurs,0))
  #print(numJoueurCourant(joueurs))
  #print(nomJoueurCourant(joueurs))
  #print(nomJoueur(joueurs,2))
  #print(ajouterTresor(joueurs))
  #print(joueurs)
  #print(prochainTresorJoueur(joueurs,0))
  #print(tresorCourant(joueurs))
  #print(joueurCourantAFini(joueurs))