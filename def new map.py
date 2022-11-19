import random
#size_map=[7,7]
#proportion_empty=0.3 #car c'est une proba on met entre 0 et 1
#proportion_lader=0.4 #entre 0 et 1 pour les echelles

def generate_random_map(size_map,proportion_empty, proportion_lader):
    M1=[] #novuelle matrice de la carte
    for i in range(size_map[0]):
        M1.append([])
        for j in range(size_map[1]):
            M1[i].append(0)
    count_empty=0
    count_lader=0
    count_empty_final=0.0
    count_lader_final=0.0
    proportion_empty_prct=proportion_empty*100
    while proportion_empty_prct<=count_empty_final:
        a=random.randint(0,len(M1)-1)#création d'un numéro de ligne de plateau aléatoire pour l'objet
        b=random.randint(0,len(M1)-1)#création d'un numéro de colonne de plateau aléatoire pour l'objet
        if M1[a][b]==0:
            M1[a][b]=(1)
            count_empty+=1
    #count_empty_final=count_empty/100
    proportion_lader_prct=proportion_lader*100
    while proportion_lader_prct<=count_lader_final:
        c=random.randint(0, len(M1)-1)#création d'un numéro de ligne de plateau aléatoire pour l'objet
        d=random.randint(0,len(M1)-1)#création d'un numéro de colonne de plateau aléatoire pour l'objet
        if M1[c][d]==0:
            M1[c][d]="#"
            count_lader+=1
    #count_lader_final=count_lader/100
    return M1
print(generate_random_map([7,7],0.3,0.4))
#print(size_map[0])
"""M=[]
M+=[]
print(M)
M1=[]
M1.append([])
print(M1)"""
"""
M1=[]
for i in range(7):
    M1.append([])
    for j in range(7):
        M1[i].append(0)
print(M1)"""
