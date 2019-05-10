# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:11:24 2019

@author: Joanna
"""

with open('donnees_eleve.txt', 'r') as mon_fichier:
    lignes=mon_fichier.readlines()
#print(lignes)

don_eleve=[]

for ligne in lignes:
   ligne = ligne.replace("\n", "")
   donnees = ligne.split('\t')
   don_eleve.append(donnees)

#print(don_eleve)


import matplotlib.pyplot as plt
import numpy as np

numexo=0
typeitem=1
corexo=2
repeleve=3

nb_exos=len(don_eleve)

#transformer les deux dernieres donnees en nombres
#
for i in range(nb_exos):
    don_eleve[i][corexo]=int(don_eleve[i][corexo])
    don_eleve[i][repeleve]=int(don_eleve[i][repeleve])
    
print(don_eleve)

## Début statistiques
#calcul du nombre d'items dans chaque catégorie
nb_exo_par_cat=[0]*4
nb_exo_par_cat[0]=nb_exos

for exo in range(len(don_eleve)):
    if don_eleve[exo][typeitem]=='Langage ':  #comment faire pour enlever l'espace après?
        nb_exo_par_cat[1]+=1
    elif don_eleve[exo][typeitem]=='Classique ':
        nb_exo_par_cat[2]+=1
    elif don_eleve[exo][typeitem]=='Incongruent ':
        nb_exo_par_cat[3]+=1
#print(nb_exo_par_cat)

#calcul des scores
score_global=0
score_langage=0
score_classique=0
score_incongruent=0

for exo in range(len(don_eleve)):
    if don_eleve[exo][repeleve]==don_eleve[exo][corexo]:
        score_global+=1
        
        if don_eleve[exo][typeitem]=='Langage ':  #comment faire pour enlever l'espace après??
            score_langage+=1
        elif don_eleve[exo][typeitem]=='Classique ':
            score_classique+=1
        elif don_eleve[exo][typeitem]=='Incongruent ':
            score_incongruent+=1
#Affichage graphique
fig = plt.figure()
items=['Global','Langage','Classique','Incongruent']
scores=[score_global,score_langage, score_classique, score_incongruent]
width=1
b1=plt.bar(items, nb_exo_par_cat, width, color='grey' )
b2=plt.bar(items, scores, width, color='g' )
plt.legend([b1,b2],['nb de réponses total','nb de réponses correctes'])
plt.title("Résultats en fonction de la catégorie de l'item")
#plt.savefig('Resultat_eleve.png')
plt.show()

#pourcentages de réussite
pourcentage_reussite=[]
for categorie in range(len(scores)):
    pourcentage_reussite.append(scores[categorie]/nb_exo_par_cat[categorie]*100)

#Affichage graphique  
fig = plt.figure()
items=['Global','Langage','Classique','Incongruent']

b3=plt.bar(items, pourcentage_reussite, width, color='b' )

plt.title("Pourcentages de réussite par catégories")
#plt.savefig('Resultat_eleve.png')
plt.show()
    
    
    
