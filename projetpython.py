import random
import datetime #Vu dans le TD6, permet de chronometrer le temps d'execution
import son as son#nom du fichier où il y a la fenêtre d'acceuil et le son pour l'éxécuter en executant ce programme



def display_m(m,d):
    for i in m:
        for j in i:
            if j in d:
                print(d[j],end="")
        print()


def create_perso(depart):
    return {"repr" :'o',"x":depart[0],"y":depart[1],"score":0} 



def display_map_and_char(m,d,p):   
    for i in range (len(m)): 
        for j in range(len(m[i])):
            if (i,j)==(p["x"],p["y"]):
                print(p["repr"],end="")
            elif m[i][j] in d and (i,j)!=(p["x"],p["y"]):
                  print(d[m[i][j]],end="")
        print()

        
def create_objects(nb_objects,m):
    t=set()
    for i in range (nb_objects):
        n=random.randint(0, len(m)-1)
        o=random.randint(0, (len(m[0])-1))
        if m[n][o]==0:
            t.add((n,o))
    return t


def update_objects(p,t):
    if (p["x"],p["y"]) in t: 
        p["score"]+=1 
        t.remove((p["x"],p["y"])) 
    return t


def display_map_char_and_objects(m,d,p,t):
    for i, ch in enumerate(m): 
        for j, cha in enumerate(ch):
           if (i,j)==(p["x"],p["y"]):
                print(p["repr"],end="")
           elif (i,j) in t:

                  print('i',end="")
           elif m[i][j] in d :
                  print(d[m[i][j]],end="")
        print()

        
def update_p(letter,p,m):
    if letter=="z":
        if p["x"]>0:
           if m[p["x"]][p["y"]]==1:
               p["x"]-=1
           else:
              return print("Cela n'est pas possible.") 
        else:
            print("Cela n'est pas possible.") 
    if letter=="q":
      if p["y"]>0:
         p["y"]-=1 
         if m[p["x"]][p["y"]]==2:
             p["y"]+=1
             return print("Cela n'est pas possible.")
      else:
          print("Cela n'est pas possible.")
    if letter=="s":
      if p["x"]<(len(m)-1):
          p["x"]+=1
          if m[p["x"]][p["y"]]!=1:
              p["x"]-=1
              return print("Cela n'est pas possible.")
      else:
          print("Cela n'est pas possible.")

    if letter=="d":
      if p["y"]<(len(m[0])-1):
         p["y"]+=1 
         if m[p["x"]][p["y"]]==2:
             p["y"]-=1
             return print("Cela n'est pas possible.")
      else:
            print("Cela n'est pas possible.")


D={0:'_',1:'#',2:" "}
dep=(0,0)


'''
Cette partie du code correspond à la création des 3 niveaux.
Pour réussir un niveau et passer au suivant il faut que tous les objets aient été ramassés (len(T)==0).
A chaque niveau la difficulté augmente. Une nouvelle carte est crée avec moins d'échelles et plus de trous.
Par ailleurs, le nombre d'objets augmente aussi avec les niveaux.
A partir du niveau 2 le nombre de déplacement devient limités à 10.
'''

''' Ci-dessous, les premiers éléments qui constitueront notre niveaux 1.'''
M = [[0, 0, 0, 1, 0, 0, 2],[0, 1, 0, 0, 1, 0, 0],[0, 1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 1, 0, 2]]
nb=2
T=create_objects(nb,M)
P=create_perso(dep)


letter="z"
answer=True

while answer and (letter=="z" or letter=="q" or letter=="s" or letter=="d"):
        start_time_1 = datetime.datetime.now() #On lance le chronomètre une fois que la carte s'affiche sur l'écran de l'utilisateur.
        display_map_char_and_objects(M,D,P,T)
        if len(T)==0:
            end_time_1 = datetime.datetime.now() #On le stoppe une fois tous les objets ramassés.
            time_diff_1 = (end_time_1 - start_time_1) #On calcul la différence
            execution_time_1 = time_diff_1.total_seconds()*100 
            print("La partie est terminée. \n SCORE: ",P["score"], "\n Temps: ",execution_time_1,"s")
            print("Bienvenue au niveau 2")
            break
        else:
            letter= input("Où souhaitez-vous aller ?")
            if letter!="z" and letter!="q" and letter!="s" and letter!="d":
                break
            update_p(letter,P,M)
            update_objects(P,T)
            print("Votre score est de: ",P["score"])

''' Ci-dessous, les éléments qui constitueront notre niveaux 2.'''
M1 = [[0, 0, 0, 1, 0, 0, 2],[0, 1, 0, 2, 0, 1, 0],[1, 2, 0, 0, 1, 2, 0],[0, 0, 1, 0, 0, 0, 2]]
Z=create_objects(6, M1)
U=create_perso((0,0))

i=0 #initilisation du compteur pour le nombre de déplacement.
while answer and (letter=="z" or letter=="q" or letter=="s" or letter=="d") and i<10: #la boucle s'arrête lorsque le nombre de déplacements autorisés est atteint.
            start_time_2 = datetime.datetime.now()
            display_map_char_and_objects(M1,D,U,Z)
            if len(Z)==0:
                end_time_2 = datetime.datetime.now()
                time_diff_2 = (end_time_2 - start_time_2)
                execution_time_2 = time_diff_2.total_seconds()*100
                print("La partie est terminée. \n SCORE: ",U["score"], "\n Temps: ",execution_time_2,"s","\n Nombre de déplacements: ",i," sur 10")
                print("Bienvenue au niveau 3")  
                break
            else:
                letter= input("Où souhaitez-vous aller ?")
                if letter!="z" and letter!="q" and letter!="s" and letter!="d":
                    break
                update_p(letter,U,M1)
                update_objects(U,Z)
                i+=1
                print("Votre score est de: ",U["score"],"\nIl vous reste",10-i,"déplacements.")





M2 = [[0, 0, 2, 0, 0, 0, 2],[0, 1, 0, 2, 1, 2, 0],[0, 0, 2, 0, 1, 0, 2],[1, 0, 1, 2, 1, 0, 2]]
Q=create_objects(8, M2)
R=create_perso((0,0))
u=0 #intilisation du nouveau compteur pour le niveau 3.
while answer and (letter=="z" or letter=="q" or letter=="s" or letter=="d") and i!=10 and u<10:
    display_map_char_and_objects(M2,D,R,Q)
    start_time_3 = datetime.datetime.now()
    if len(Q)==0: 
        end_time_3 = datetime.datetime.now()
        time_diff_3 = (end_time_3 - start_time_3)
        execution_time_3 = time_diff_3.total_seconds()*100
        print("La partie est terminée. \n SCORE: ",R["score"], "\n Temps: ",execution_time_3,"s","\n Nombre de déplacements: ",u," sur 10")
        print("Vous avez terminé le jeu.\n FELICITATION !")
        break

    else:
        letter= input("Où souhaitez-vous aller ?")
        if letter!="z" and letter!="q" and letter!="s" and letter!="d":
            break
        update_p(letter,R,M2)
        update_objects(R,Q)
        u+=1
        print("Votre score est de: ",R["score"],"\nIl vous reste",10-u,"déplacements.")