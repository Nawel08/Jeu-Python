# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:22:47 2022

@author: Siham
"""
import random
def display_m(m,d):
    for i in m:
        for j in i:
            if j in d:
                print(d[j],end="")
        print()

def create_perso(depart):
    return {"repr" :'\U0001f478',"x":depart[0],"y":depart[1],"score":0} 

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
                  print('\U0001f56f',end="")
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
M = [[0, 0, 0, 1, 0, 0, 2],[0, 1, 0, 0, 0, 0, 0],[0, 1, 0, 0, 1, 0, 0],[0, 0, 1, 0, 0, 0, 2]]
# Ne donne pas le même nom à tes variables que tu initialises et aux arguments de la fonction
D={0:'_',1:'#',2:" "}
dep=(0,0)
nb=4
T=create_objects(nb,M)
P=create_perso(dep)
letter=""
answer=True
while answer:
    display_map_char_and_objects(M,D,P,T)
    if len(T)==0: 
        print("La partie est terminée. SCORE: ",P["score"]) 
        break 
    else:
        letter= input("Où souhaitez-vous aller ?")
        if letter!="z" and letter!="q" and letter!="s" and letter!="d":
            break
        update_p(letter,P,M)
        update_objects(P,T)
        print("Votre score est de: ",P["score"]) 
Z=create_objects(6, M)
U=create_perso((0,0))
print("Bienvenue dans le niveau 2")
i=0
while answer:
    display_map_char_and_objects(M,D,U,Z)
    if len(Z)==0: 
        print("La partie est terminée. SCORE: ",U["score"]) 
        break 
    else:
        letter= input("Où souhaitez-vous aller ?")
        if letter!="z" and letter!="q" and letter!="s" and letter!="d":
            break
        update_p(letter,U,M)
        update_objects(U,Z)
        print("Votre score est de: ",U["score"]) 
        i+=1
Q=create_objects(8, M)
R=create_perso((0,0))
print("Bienvenue dans le niveau 2")
i=0
while answer:
    display_map_char_and_objects(M,D,R,Q)
    if len(Q)==0: 
        print("La partie est terminée. SCORE: ",R["score"]) 
        break 
    else:
        letter= input("Où souhaitez-vous aller ?")
        if letter!="z" and letter!="q" and letter!="s" and letter!="d":
            break
        update_p(letter,R,M)
        update_objects(R,Q)
        print("Votre score est de: ",R["score"]) 
        i+=1