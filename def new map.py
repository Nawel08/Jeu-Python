import random


def generate_random_map(size_map,proportion_empty, proportion_lader):
    p=size_map[0]*size_map[1]
    p_echelles=p*proportion_lader
    p_vides=p*proportion_empty
    #Creation de la nouvelle mtrice de la map vide.
    M1=[] 
    for i in range(size_map[0]):
        M1.append([])
        for j in range(size_map[1]):
             M1[i].append(0)

    #creation des cases vides.
    count_empty=0
    count_lader=0
    proportion_empty_prct=0.0
    while proportion_empty_prct<=p_vides:
        a=random.randint(0,len(M1)-1)
        b=random.randint(0,len(M1)-1)
        if M1[a][b]==0:
            M1[a][b]=1
            count_empty+=0.1
        proportion_empty_prct+=(count_empty*p)

    #création des echelles
    proportion_lader_prct=0.0
    while proportion_lader_prct<=p_echelles:
        c=random.randint(0, len(M1)-1)
        d=random.randint(0,len(M1)-1)
        if M1[c][d]==0:
            M1[c][d]="#"
            count_lader+=0.1
        proportion_lader_prct+=(count_lader*p)
        
    return M1
print(generate_random_map([7,7],0.4,0.2))


