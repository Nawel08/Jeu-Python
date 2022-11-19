# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:22:47 2022

@author: Siham
"""
import random#on importe random pour utiliser randit lors de la création d'objet 
def display_m(M,d):#Création fonction qui affiche plateau de jeux
    for i in M:
        for j in i:
            if j in d:
                print(d[j],end="")
        print()#retour à la ligne                
#Personnage 
def create_perso(depart):#création du personnage en indiquant le caractère qui le représente + sa position 
    return {"repr" :'o',"x":depart[0],"y":depart[1],"score":0} # on initialise le score \U0001f478

def display_map_and_char(m,d,p):#création d'une fonction qui modifie le plateau en y insérant le personnage
    d={0:'_',1:'#',2:" "}#dictionnaire utiliser pour convertir les éléments de la matrice en caractère pour donner une forme au plateau: les 0 sont des "_" et les 1 des "#"
    for i in range (len(M)):
        for j in range(len(M[i])):
            if (i,j)==(p["x"],p["y"]):#parcours la matrice et affiche personnage à sa position de départ
                print(p["repr"],end="")
            elif M[i][j] in d and (i,j)!=(p["x"],p["y"]):#affiche le reste du plateau
                  print(d[M[i][j]],end="")
        print()#retour à la ligne
#création objets
def create_objects(nb_objects,M):
    t=set()#crée ensemble vide pour y insérer position objet crée
    for i in range (nb_objects):
        n=random.randint(0, len(M)-1)#création d'un numéro de ligne de plateau aléatoire pour l'objet
        m=random.randint(0, (len(M[0])-1))#création d'un numéro de colonne de plateau aléatoire pour l'objet
        if M[n][m]==0:
            t.add((n,m))#ajoute le couple (numéro ligne,numéro collonne) dans l'ensemble des objets
    return t
#Création de la fonction qui prend en argument le personnage et l'ensemble qui contient la position des objects.
def update_objects(p,t):
    
    if (p["x"],p["y"]) in t: # si la position du joueur correspond à une position de bougie
        p["score"]+=1 #on incrémente de 1 le score de l'utilisateur quand il est sur  une bougie 
        t.remove((p["x"],p["y"])) #on enlève la position de la bougie (qui est égale à la position du joueur)
    return t 
def generate_ranom_map(size_map,proportion_empty, proportion_lader):
    M1=[] #novuelle matrice de la carte
    for i in range(size_map[0]):
        for j in range(size_map[1]):
            M1[i][j].append(0)
    #on a rempli notre nouvelle matrice de 0 en fonction de sa taille
    for k in range(proportion_empty): #pour ajouter les trous
        a=random.randint(0, len(M)-1)#création d'un numéro de ligne de plateau aléatoire pour l'objet
        b=random.randint(0,len(M)-1)#création d'un numéro de colonne de plateau aléatoire pour l'objet
        if M[a][b]==0:
            M[a][b].append(1)
    for k in range(proportion_lader): #pour ajouter les échelles
        c=random.randint(0, len(M)-1)#création d'un numéro de ligne de plateau aléatoire pour l'objet
        d=random.randint(0,len(M)-1)#création d'un numéro de colonne de plateau aléatoire pour l'objet
        if M[c][d]==0:
            M[c][d].append("#")  
    
    return M1
def display_map_char_and_objects(M,d,p,t):#création d'une fonction qui modifie le plateau en y insérant le personnage et les nouveaux objets
    d={0:'_',1:'#',2:" "}#dictionnaire utiliser pour convertir les éléments de la matrice en caractère pour donner une forme au plateau: les 0 sont des "_" et les 1 des "#"
    for i in range (len(M)):#parcours la matrice 
        for j in range(len(M[i])):
            if (i,j)==(p["x"],p["y"]):
                print(p["repr"],end="")#affiche personnage à sa position de départ
            if (i,j) in t:
                  print('i',end="")#affiche objet à leur position \U0001f56f
            elif M[i][j] in d and (i,j)!=(p["x"],p["y"]):
                  print(d[M[i][j]],end="")#affiche reste plateau

        print()#retour à la ligne
def update_p(letter,p,M):
    if letter=="z":
        if p["x"]>0:
           p["x"]-=1
           if M[p["x"]][p["y"]]!=1:
               p["x"]+=1
               return print("ce n'est pas possible") 
        else:
            print("ce n'est pas possible") 
    if letter=="q":
      if p["y"]>0:
         p["y"]-=1 
         if M[p["x"]][p["y"]]==2:
             p["y"]+=1
             return print("ce n'est pas possible")
      else:
          print("ce n'est pas possible")
    if letter=="s":
      if p["x"]<(len(M)-1): 
          p["x"]+=1
          if M[p["x"]][p["y"]]!=1:
              p["x"]-=1
              return print("ce n'est pas possible")
      else:
          print("ce n'est pas possible")
       
    if letter=="d":
      if p["y"]<(len(M[0])-1):
         p["y"]+=1 
         if M[p["x"]][p["y"]]==2:
             p["y"]-=1
             return print("ce n'est pas possible")
      else:
          print("ce n'est pas possible")
M = [[0, 0, 0, 1, 2, 0, 0],[0, 1, 0, 0, 0, 0, 0],[0, 1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 2, 0]]#matrice du plateau de jeux 
d={0:'_',1:'#',2:" "}#dictionnaire utiliser pour convertir les éléments de la matrice en caractère pour donner une forme au plateau: les 0 sont des "_" et les 1 des "# et les 2 des trous " " ."
depart=(0,0)#Initialisation de la position de départ du personnage
p=create_perso(depart)
nb_objects=6#attribue un nombre d'objet à crée (chosiit au hasard)
t=create_objects(nb_objects,M)#attribue à T le dictionnaire des objets crée pour utiliser dans les prochaines fonction
p=create_perso(depart)#attribu à p le dictionnaire du personnage de départ pour l'utiliser dans les prochaines fonctions
letter=""#création case letter
answer=True#on initialise answer="oui" pour la première éxécution, après answer est donner par le joueur.
while answer:#tant que answer=="oui" donc que le joueur veut continuer à jouer,on continue le jeux
    display_map_char_and_objects(M,d,p,t)
    if len(t)==0: #Si le disctionnaire qui contient l'emplacement des bougies est vide, ça signifie qu'il n'y a plus de bougie a ramasser donc on stoppe le jeu
        print("La partie est terminée. SCORE: ",p["score"]) #on affiche la fin de la partie et le score
        break #on sort de la boucle
    else:
        letter= input("Où souhaitez-vous aller ?")#demander au joueur où il veut se déplacer (avec le système de lettre)
        if letter!="z" and letter!="q" and letter!="s" and letter!="d":#si il met une lettre différente des commande renvoie que ce n'est pas possible
            break
        update_p(letter,p,M)
        update_objects(p,t)
        print("Votre score est de: ",p["score"]) #on place ici l'initialisation du score pour que ça s'affiche à la fin de l'exécution sous la map
        