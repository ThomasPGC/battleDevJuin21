
compteur_coupes = 0
nb_debris = int(lines[0])
orbite = lines[1]
type_debris = []

for deb in orbite:
    if deb not in type_debris:
        type_debris.append(deb)




### passage en revue de toutes les coupes (brute force)

for i in range(nb_debris//2):
    comparateur = False
    sonde1 = orbite[i:(nb_debris//2+i)]
    sonde2 = orbite[(nb_debris//2+i):]+orbite[:i]
    for deb in type_debris:
        if sonde1.count(deb) != sonde2.count(deb):
            comparateur = False
            break
        else:
            comparateur = True

    if comparateur == True:
        compteur_coupes +=1
        
print(compteur_coupes*2)
