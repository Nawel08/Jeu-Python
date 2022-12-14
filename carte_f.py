import random
import datetime
import Fenetre as Fenetre

"""
start_time = datetime.datetime.now()
# ici le code à évaluer
end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)
"""
def display_m(m,d):
    for i in m:
        for j in i:
            if j in d:
                print(d[j],end="")
        print()

def create_perso(depart):
    
    return {"repr" :'o',"x":depart[0],"y":depart[1],"score":0} 

def display_map_and_char(m,d,p):   
    for i in range (len(m)): #Tu appelles ici "M" alors qu'il ne fait pas partie des arguments
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
    for i, ch in enumerate(m): #Tu appelles ici "M" alors qu'il ne fait pas partie des arguments
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
              return print("ce n'est pas possible") 
        else:
            print("ce n'est pas possible") 
    if letter=="q":
      if p["y"]>0:
         p["y"]-=1 
         if m[p["x"]][p["y"]]==2:
             p["y"]+=1
             return print("ce n'est pas possible")
      else:
          print("ce n'est pas possible")
    if letter=="s":
      if p["x"]<(len(m)-1):
          p["x"]+=1
          if m[p["x"]][p["y"]]!=1:
              p["x"]-=1
              return print("ce n'est pas possible")
      else:
          print("ce n'est pas possible")
       
    if letter=="d":
      if p["y"]<(len(m[0])-1):
         p["y"]+=1 
         if m[p["x"]][p["y"]]==2:
             p["y"]-=1
             return print("ce n'est pas possible")
      else:
            print("ce n'est pas possible")


D={0:'_',1:'#',2:" "}
dep=(0,0)

nb=2
M = [[0, 0, 0, 1, 0, 0, 2],[0, 1, 0, 0, 1, 0, 0],[0, 1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 1, 0, 2]]
T=create_objects(nb,M)
P=create_perso(dep)
letter="z"
answer=True


while answer and (letter=="z" or letter=="q" or letter=="s" or letter=="d"):
        start_time_1 = datetime.datetime.now()
        display_map_char_and_objects(M,D,P,T)
        if len(T)==0:
            end_time_1 = datetime.datetime.now()
            time_diff_1 = (end_time_1 - start_time_1)
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
            
        
M1 = [[0, 0, 0, 1, 0, 0, 2],[0, 1, 0, 2, 0, 1, 0],[1, 2, 0, 0, 1, 2, 0],[0, 0, 1, 0, 0, 0, 2]]
Z=create_objects(6, M1)
U=create_perso((0,0))


while answer and (letter=="z" or letter=="q" or letter=="s" or letter=="d"):
            display_map_char_and_objects(M1,D,U,Z)
            start_time_2 = datetime.datetime.now()
            if len(Z)==0:
                end_time_2 = datetime.datetime.now()
                time_diff_2 = (end_time_2 - start_time_2)
                execution_time_2 = time_diff_2.total_seconds()*100
                print("La partie est terminée. \n SCORE: ",U["score"], "\n Temps: ",execution_time_2,"s")
                print("Bienvenue au niveau 3")  
                break
            else:
                letter= input("Où souhaitez-vous aller ?")
                if letter!="z" and letter!="q" and letter!="s" and letter!="d":
                    break
                update_p(letter,U,M1)
                update_objects(U,Z)
                print("Votre score est de: ",U["score"]) 
            


               
M2 = [[0, 0, 2, 0, 0, 0, 2],[0, 1, 0, 2, 1, 2, 0],[0, 0, 2, 0, 1, 0, 2],[1, 0, 1, 2, 1, 0, 2]]
Q=create_objects(8, M2)
R=create_perso((0,0))

while answer and (letter=="z" or letter=="q" or letter=="s" or letter=="d"):
    display_map_char_and_objects(M2,D,R,Q)
    start_time_3 = datetime.datetime.now()
    if len(Q)==0: 
        end_time_3 = datetime.datetime.now()
        time_diff_3 = (end_time_3 - start_time_3)
        execution_time_3 = time_diff_3.total_seconds()*100
        print("La partie est terminée. \n SCORE: ",R["score"], "\n Temps: ",execution_time_3,"s")
        print("Vous avez terminé le jeu.\n FELICITATION !")
        break
                            
    else:
        letter= input("Où souhaitez-vous aller ?")
        if letter!="z" and letter!="q" and letter!="s" and letter!="d":
            break
        update_p(letter,R,M2)
        update_objects(R,Q)
        print("Votre score est de: ",R["score"]) 
                        
