        # -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random
#Filitika

"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte (nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
   """
    carte = {'nord':nord, 'est':est, 'sud':sud, 'ouest':ouest, 'tresor':tresor, 'pions':[]}
    return carte
    
def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    res=False
    cpt=0
    for val in c.values():
      if val==True:
        cpt=cpt+1
    if cpt<=2:
      res=True
    return res

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c['nord']

def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c['sud']

def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c['est']

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    
    return c['ouest']

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """

    return c['pions']

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """

    res= c['pions'].extend(listePions)
    return res

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(['pions'])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    res=False
    if pion in c['pions']:
      res=True
    return res

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c['tresor']

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c['tresor']
    del c['tresor']
    c['tresor']=0
    return res

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=c['tresor']
    c['tresor']=tresor
    return res

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion in c['pions']:
      c['pions'].remove(pion)

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c['pions']:
      c['pions'].append(pion)

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien   """
    aux=c['ouest']
    c['ouest']=c['sud']
    c['sud']=c['est']
    c['est']=c['nord']
    c['nord']=aux

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    """
    aux=c['nord']
    c['nord']=c['est']
    c['est']=c['sud']
    c['sud']=c['ouest']
    c['ouest']=aux

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    """
    import random
    x=random.randint(1,100)
    for val in range(0,x,1) :
      tournerHoraire(c)
    return x

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    res=0
    if c['nord']==True:
      bN=1
    else:
      bN=0
    if c['est']==True:
      bE=1
    else:
      bE=0
    if c['sud']==True:
      bS=1
    else:
      bS=0
    if c['ouest']==True:
      bO=1
    else:
      bO=0
    res=bN+10*bE+100*bS+1000*bO
    return res

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    if code%10==1:
      c['nord']=True
    else:
      c['nord']=False
    code=code//10
    if code%10==1:
      c['est']=True
    else:
      c['est']=False
    code=code//10
    if code%10==1:
      c['sud']=True
    else:
      c['sud']=False
    code=code//10
    if code%10==1:
      c['ouest']=True
    else:
      c['ouest']=False
    

def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    res=0
    if c['nord']==True:
      res=res+2^0
    if c['est']==True:
      res=res+2^1
    if c['sud']==True:
      res=res+2^2
    if c['ouest']==True:
      res=res+2^3
    return listeCartes[res]

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['nord']==False and carte2['sud']==False:
      res=True
    else: 
      res=False
    return res

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['sud']==False and carte2['nord']==False:
      res='True'
    else: 
      res=False
    return res

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1['ouest']==False and carte2['est']==False:
      res= True
    else: 
      res=False
    return res

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    if carte1['est']==False and carte2['ouest']==False:
      res= True
    else: 
      res=False
    return res


if __name__=='__main__':
  c=Carte (True, True, True, False, tresor=0, pions=[])
  print(c)     
  #print(estValide(c))
  #print(murNord(c))
  #print(murSud(c))
  #print(murEst(c))
  #print(murOuest(c))
  #print(getListePions(c))
  #print(setListePions(c,[2,4]))
  #print(c)
  #print(getNbPions(c))
  #print(possedePion(c,2))
  #print(getTresor(c))
  #print(prendreTresor(c))
  #print(c)
  #print(mettreTresor(c,2))
  #print(c)
  #print(prendrePion(c,6))
  #print(c)
  #print(poserPion(c,5))
  #print(c)
  #print(tournerHoraire(c))
  #print(c)
  #print(tournerAntiHoraire(c))
  #print(c)
  print(tourneAleatoire(c))
  print(c)
  print(coderMurs(c))
  print(decoderMurs(c,1110))
  print(c)
  print(toChar(c))
  carte1=Carte (False, True, True, False, tresor=0, pions=[])
  carte2=Carte (True, False, False, True, tresor=0, pions=[])
  print(passageNord(carte1,carte2))
  print(passageSud(carte1,carte2))
  print(passageOuest(carte1,carte2))
  print(passageEst(carte1,carte2))