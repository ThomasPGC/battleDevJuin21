### listage et comptage des différents débris

liste_debris = {}
liste_coupe = {}
compteur_coupes = 0
nb_debris = int(lines[0])
orbite = lines[1]


for debris in orbite:
    if debris in liste_debris.keys():
        liste_debris[debris] += 1
    else:
        liste_debris[debris] = 1



## vérification de la parité des débris

for n_debris in liste_debris.values():
    if n_debris % 2 != 0:
        print('0')

### passage en revue de toutes les coupes (brute force)

for i in range(nb_debris//2):
    comparateur = False
    for cle in liste_debris.keys():
        liste_coupe[cle] = orbite[i:(nb_debris//2+i)].count(cle)
    for cle in liste_debris.keys():
        if liste_debris[cle] != liste_coupe[cle]*2:
            comparateur = False
            break
        else:
            comparateur = True
            
    if comparateur == True:
        compteur_coupes +=1
        
print(compteur_coupes*2)
    
