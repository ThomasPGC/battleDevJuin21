#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
def Comparateur(dico_coupe, dico_orbite):
    for cle, val in dico_coupe.items():
        if val*2 != dico_orbite[cle]:
            return False
    return True
        
	
	

### listage et comptage des différents débris

dico_debris = {}
#debris_classes = []
liste_coupe = {}
compteur_coupes = 0
nb_debris = int(lines[0])
orbite = lines[1]


for debris in orbite:
    if debris in dico_debris.keys():
        dico_debris[debris] += 1
    else:
        dico_debris[debris] = 1
        


coupe = orbite[:nb_debris//2]
for deb in dico_debris.keys():
    liste_coupe[deb] = coupe.count(deb)
if Comparateur(liste_coupe, dico_debris):
    compteur_coupes +=1

for i in range(nb_debris//2-1):
    liste_coupe[orbite[i]] -=1
    liste_coupe[orbite[i+(nb_debris//2)]] +=1
    if Comparateur(liste_coupe, dico_debris):
        compteur_coupes +=1
        
print(compteur_coupes*2)
