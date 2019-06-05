# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:20:09 2019

@author: Joanna
"""

from tkinter import *
import csv
import random

#recuperer le fichier des exercices
exercices = csv.reader(open('questions_reponses.txt'), delimiter=";")
exercices= list(exercices)
nbexercices = len(exercices)

numexo=0
typeitem=1
consigne=2
corexo=3

#recuperation du nombre d'exercices de chaque categorie
nb_exo_par_cat=[0]*4
nb_exo_par_cat[3]=nbexercices  #total dans la derniere colonne

for exo in range(len(exercices)):
    if exercices[exo][typeitem]=='Langage':  
        nb_exo_par_cat[0]+=1
    elif exercices[exo][typeitem]=='Classique':
        nb_exo_par_cat[1]+=1
    elif exercices[exo][typeitem]=='Incongruent':
        nb_exo_par_cat[2]+=1
        
numero_exercice=0
categorie=0 

#recalculer les poids a partir de la liste
def normaliser(liste_poids):
    total=sum(liste_poids)
    liste_poids[0]=liste_poids[0]/total
    liste_poids[1]=liste_poids[1]/total
    liste_poids[2]=liste_poids[2]/total
    
#recuperer les poids
with open('poids_initiaux.txt', 'r') as mon_fichier:
    poids_str=mon_fichier.read()

poids_str = poids_str.split('\t')

poids=[]
for nombres in range(len(poids_str)-1):
    poids.append(float(poids_str[nombres]))

normaliser(poids)
print(poids)

def estjuste(reponse):
    global numero_exercice
    global categorie
    
    if entree.get()==exercices[numero_exercice][corexo]:
        correction.configure(text="Bravo, c'est la bonne réponse!")
                
        entree.grid_forget()
        bouton_boite.grid_forget()
        etape_suivante.grid(column=0,row=3)
    
    else: 
        correction.configure(text="Essaie encore, tu ne dois pas être loin!")
        correction.grid(column=0,row=2)
          
        poids[categorie]+=0.1  #changer les poids a la categorie car la personne s'est trompee
        normaliser(poids)
        
   
def exercicesuivant():
    global numero_exercice
    
    entree.delete(0,END)
    entree.grid(column=0,row=1)
    etape_suivante.grid_forget()
    correction.grid_forget()
    
    supprimerboite()
    bouton_boite.grid(column=1, row=5)
    
    numero_exercice=choisir_exercice(poids)
    Num_Exo.configure(text=exercices[numero_exercice][numexo])
    consigne2.configure(text=exercices[numero_exercice][consigne])
    
    
def choisir_exercice(liste_poids):
    global categorie
    numero_choisi=0
    nb_alea=random.random()
    
    numero_debut_classique=nb_exo_par_cat[0]
    numero_debut_incongruent=nb_exo_par_cat[0]+nb_exo_par_cat[1]
    if nb_alea <liste_poids[0]:
        numero_choisi=random.randint(0,numero_debut_classique-1)
        categorie=0
    elif liste_poids[0]<=nb_alea<liste_poids[0]+liste_poids[1]:
        numero_choisi=random.randint(numero_debut_classique, numero_debut_incongruent-1)
        categorie=1
    else:
        numero_choisi=random.randint(numero_debut_incongruent,numero_debut_incongruent+nb_exo_par_cat[2]-1)
        categorie=2
    return numero_choisi

def afficherboite():    
    bouton_boite.grid_forget()
    
    aideboite.grid(column=0, row=0, columnspan=2)
    tout.grid(column=0,row=1, columnspan=2)
    partie1.grid(column=0,row=2,sticky='e')
    partie2.grid(column=1,row=2,sticky='w')
    
def supprimerboite():
    aideboite.grid_forget()
    
    tout.delete(0,END)
    partie1.delete(0,END)
    partie2.delete(0,END)
    
    tout.grid_forget()
    partie1.grid_forget()
    partie2.grid_forget()
    
 # création du widget principal
fenetre = Tk()
fenetre.title("Apprendre à calculer")
fenetre.geometry("1000x600+300+0")

Num_Exo=Label(fenetre, text=exercices[numero_exercice][numexo])
Num_Exo.grid(column=0, row=0)

#premier cadre pour l'énoncé
cadre1 = Frame(fenetre, height=400,width=300,  borderwidth=1, relief="groove")
cadre1.grid(column=0,row=1)

consigne1 =Label(cadre1, text="Lis bien l'énoncé:")
consigne2 =Label(cadre1, text=exercices[numero_exercice][consigne])
consigne1.pack(fill=BOTH)
consigne2.pack(fill=BOTH)

#deuxième cadre pour récupérer la réponse
cadre2 = Frame(fenetre, height=400,width=300,  borderwidth=1)

Label(cadre2, 
      text="Tu peux écrire ta réponse ici:\n Appuie sur la touche entrée pour vérifier la réponse").grid(column=0,row=0)

entree = Entry(cadre2, width=30)
entree.bind("<Return>", estjuste)

correction=Label(cadre2)

cadre2.grid(column=0,row=2)
entree.grid(column=0,row=1)
correction.grid(column=0,row=2)

#troisième cadre pour s'aider de la boite
cadre3=Frame(fenetre, height=400,width=300,  borderwidth=1, relief="ridge")
aideboite=Label(cadre3, text="Aide-toi de la boîte pour faire tes calculs")
cadre3.grid(column=0,row=3)

tout=Entry(cadre3,width=14)
partie1=Entry(cadre3,width=7)
partie2=Entry(cadre3,width=7)

#bouton pour passer à l'étape suivante
etape_suivante=Button(cadre2, text="On continue!", command=exercicesuivant)

#bouton pour afficher la boîte si l'élève le veut
bouton_boite=Button(cadre3, text="Aide Boîte", command=afficherboite)
bouton_boite.grid(column=0, row=5)

#bouton permettant de quitter
quitter=Button(fenetre, text="Quitter", command=fenetre.destroy)

fenetre.mainloop()
fenetre.destroy()