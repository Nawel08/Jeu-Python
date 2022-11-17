
import random#on importe random pour utiliser randit lors de la création d'objet
#Personnage 
def display_m(M,d):#Création fonction qui affiche plateau de jeux
    for i in M:
        for j in i:
            if j in d:
                print(d[j],end="")
        print()#retour à la ligne                
M = [[0, 0, 0, 1, 2, 0, 0],[0, 1, 0, 0, 0, 0, 0],[0, 1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 2, 0]]#matrice du plateau de jeux 
d={0:'_',1:'#',2:" "}#dictionnaire utiliser pour convertir les éléments de la matrice en caractère pour donner une forme au plateau: les 0 sont des "_" et les 1 des "#"
#Personnage 
depart=(0,0)#Initialisation de la position de départ du personnage
def create_perso(depart):#création du personnage en indiquant le caractère qui le représente + sa position 
    return {"repr" :'\U0001f478',"x":depart[0],"y":depart[1],"score":0} # on initialise le score 

def display_map_and_char(m,d,p):#création d'une fonction qui modifie le plateau en y insérant le personnage
    d={0:'_',1:'#',2:" "}#dictionnaire utiliser pour convertir les éléments de la matrice en caractère pour donner une forme au plateau: les 0 sont des "_" et les 1 des "#"
    for i in range (len(M)):
        for j in range(len(M[i])):
            if (i,j)==(p["x"],p["y"]):#parcours la matrice et affiche personnage à sa position de départ
                print(p["repr"],end="")
            elif M[i][j] in d and (i,j)!=(p["x"],p["y"]):#affiche le reste du plateau
                  print(d[M[i][j]],end="")
        print()#retour à la ligne
p=create_perso(depart)
#Deplacement
#création objets
nb_objects=6#attribue un nombre d'objet à crée (chosiit au hasard)
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
def display_map_char_and_objects(M,d,p,t):#création d'une fonction qui modifie le plateau en y insérant le personnage et les nouveaux objets
    d={0:'_',1:'#',2:" "}#dictionnaire utiliser pour convertir les éléments de la matrice en caractère pour donner une forme au plateau: les 0 sont des "_" et les 1 des "#"
    for i in range (len(M)):#parcours la matrice 
        for j in range(len(M[i])):
            if (i,j)==(p["x"],p["y"]):
                print(p["repr"],end="")#affiche personnage à sa position de départ
            if M[i][j] in d and (i,j)!=(p["x"],p["y"]):
                  print(d[M[i][j]],end="")#affiche reste plateau
            if (i,j) in t:
                  print('\U0001f56f',end="")#affiche objet à leur position
        print()#retour à la ligne
t=create_objects(nb_objects,M)#attribue à T le dictionnaire des objets crée pour utiliser dans les prochaines fonction
p=create_perso(depart)#attribu à p le dictionnaire du personnage de départ pour l'utiliser dans les prochaines fonctions
letter=""#création case letter
def update_p(letter,p,M):
    letter= input("Où souhaitez-vous aller ?")#demander au joueur où il veut se déplacer (avec le système de lettre)
    if letter!="z" and letter!="q" and letter!="s" and letter!="d":#si il met une lettre différente des commande renvoie que ce n'est pas possible
        print ("La lettre entrée n'est pas reconnue, veuillez recommencer.")
    if letter=="z":
        if p["x"]>0:#vérifier que la position ne dépasse pas le cadre du plateau
           p["x"]-=1#enlève 1 à la position de la ligne pour monter
           if M[p["x"]][p["y"]]==1:#si la case n'est pas vide (=1), on ajoute 1 pour annuler le deplacement
               p["x"]+=1
               return print("Cette action n'est pas possible.")#si la case n'est pas vide (=1), on ajoute 1 pour annuler le deplacement
        else:
            print("ce n'est pas possible")
    if letter=="q":
      if p["y"]>0:#vérifier que la position ne dépasse pas le cadre du plateau
         p["y"]-=1# enleve 1 à la position de la colonne pour aller à gauche
         if M[p["x"]][p["y"]]==1:#si la case n'est pas vide (=1), on ajoute 1 pour annuler le deplacement
             p["y"]+=1
             return print("Cette action n'est pas possible.")#si la case n'est pas vide (=1), on ajoute 1 pour annuler le deplacement
      else:
             print("ce n'est pas possible")
    if letter=="s":
      if p["x"]<len(M):#vérifier que la position ne dépasse pas le cadre du plateau
            p["x"]+=1#ajoute un à la position de la ligne pour descendre
            if M[p["x"]][p["y"]]==1:#si la case n'est pas vide (=1), on enleve 1 pour annuler le deplacement

                p["x"]-=1
                return print("Cette action n'est pas possible.")  #si la case n'est pas vide (=1), on ajoute 1 pour annuler le deplacement
      else:
          print("ce n'est pas possible")
    if letter=="d":
      if p["y"]<(len(M[0])-1):#vérifier que la position ne dépasse pas le cadre du plateau
         p["y"]+=1 #ajoute 1 à la position au niveau de la colonne pour aller à droite
         if M[p["x"]][p["y"]]==1:#si la case n'est pas vide (=1), on enleve 1 pour annuler le deplacement
             p["y"]-=1 
             return print("Cette action n'est pas possible.")#on retourne que l'action n'est pas possible si la case n'est pas vide (=qu'il y a une échelle)
      else:
          print("ce n'est pas possible")
answer="oui"#on initialise answer="oui" pour la première éxécution, après answer est donner par le joueur.
while answer=="oui":
    if len(t)==0: #Si le disctionnaire qui contient l'emplacement des bougies est vide, ça signifie qu'il n'y a plus de bougie a ramasser donc on stoppe le jeu
        print("La partie est terminée. SCORE: ",p["score"]) #on affiche la fin de la partie et le score
        break #on sort de la boucle
    else:
        update_p(letter,p,M)
        update_objects(p,t)
        display_map_char_and_objects(M,d,p,t)
        print("Votre score est de: ",p["score"]) #on place ici l'initialisation du score pour que ça s'affiche à la fin de l'exécution sous la map
        answer=input("Voulez-vous continuez à jouer?")#demander au joueur si il veut continuer ou non pour savoir si arrêter le jeux ou non:#tant que answer=="oui" donc que le joueur veut continuer à jouer,on continue le jeux
        
