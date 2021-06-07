### listage et comptage des différents débris

dico_debris = {}
debris_classes = []
liste_coupe = {}
compteur_coupes = 0
nb_debris = int(lines[0])
orbite = lines[1]


for debris in orbite:
    if debris in dico_debris.keys():
        dico_debris[debris] += 1
    else:
        dico_debris[debris] = 1
        
sys.stderr.write(str(dico_debris))
sys.stderr.write('\n')

### classement des débris par nombre d'occurences

for (cle, val) in dico_debris.items():
    sys.stderr.write(str((cle,val)))
    sys.stderr.write('\n')
    if debris_classes == []:
        debris_classes.append((cle,val))
    else:
        for i in range(len(debris_classes)):
            if val <= debris_classes[i][1]:
                debris_classes.insert(i,(cle,val))
                break
            else:
                debris_classes.append((cle,val))
                break
                
debris_classes = debris_classes[:-1]
sys.stderr.write(str(debris_classes))
sys.stderr.write('\n')



## vérification de la parité des débris

for n_debris in dico_debris.values():
    if n_debris % 2 != 0:
        print('0')

### passage en revue de toutes les coupes (brute force)

for i in range(nb_debris//2):
    comparateur = False
    for deb in debris_classes:
        liste_coupe[deb[0]] = orbite[i:(nb_debris//2+i)].count(deb[0])
        if dico_debris[deb[0]] != liste_coupe[deb[0]]*2:
            comparateur = False
            break
        else:
            comparateur = True
            
    if comparateur == True:
        compteur_coupes +=1
        
print(compteur_coupes*2)
    
    
