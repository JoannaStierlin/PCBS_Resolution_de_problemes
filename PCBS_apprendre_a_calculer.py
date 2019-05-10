# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:20:09 2019

@author: Joanna
"""

from tkinter import *

#exercices=[["Combien font 2+2?","4"],
#           ["5*3 ?", "15"]]

with open('questions_reponses.txt', 'r') as mon_fichier:
    lignes=mon_fichier.readlines()
    
#print(lignes)
exercices=[]
for ligne in lignes:
   ligne = ligne.replace("\n", "")
   donnees = ligne.split('; ')
   exercices.append(donnees)

nbexercices=len(exercices)
numexo=0
typeitem=1
consigne=2
corexo=3

numero_exercice=0
def estjuste(reponse):
    global numero_exercice
    
    if entree.get()==exercices[numero_exercice][corexo]:
        correction.configure(text="Bravo, c'est la bonne réponse!")
        numero_exercice+=1
        #print(numero_exercice)
        
        if numero_exercice==nbexercices: 
            boite.grid_forget()
            quitter.grid(column=0, row=5)
        else: etape_suivante.grid(column=0,row=8)
    
    else: correction.configure(text="Essaie encore, tu ne dois pas être loin!")
    
def exercicesuivant():
    entree.delete(0,END)
    etape_suivante.grid_forget()
    
    supprimerboite()
    boite.grid(column=1, row=5)
    
    Num_Exo.configure(text=exercices[numero_exercice][numexo])
    consigne2.configure(text=exercices[numero_exercice][consigne])
    correction.configure(text=" ")

def afficherboite():    
    boite.grid_forget()
    aideboite.grid(column=1, row=5, columnspan=3)
    tout.grid(column=1,row=6, columnspan=3)
    partie1.grid(column=1,row=7,  columnspan=2)
    partie2.grid(column=2,row=7,  columnspan=2)
    
def supprimerboite():
    tout.delete(0,END)
    partie1.delete(0,END)
    partie2.delete(0,END)
    aideboite.grid_forget()
    tout.grid_forget()
    partie1.grid_forget()
    partie2.grid_forget()
    
 # création du widget principal
fenetre = Tk()
fenetre.title("Apprendre à calculer")


Num_Exo=Label(fenetre, text="Exercice 1")
Num_Exo.grid(column=0, row=0)

#premier cadre pour l'énoncé
cadre1 = Frame(fenetre, height=400,width=300,  borderwidth=1, relief="groove")
cadre1.grid(column=0,row=1)

consigne1 = Label(cadre1, text="Lis bien l'énoncé: ")
consigne2 =Label(cadre1, text=exercices[numexo][consigne])
consigne1.pack(fill=BOTH)
consigne2.pack(fill=BOTH)

#deuxième cadre pour récupérer la réponse
cadre2 = Frame(fenetre, height=400,width=300,  borderwidth=1)

Label(cadre2, 
      text="Tu peux écrire ta réponse ici:\n Appuie sur la touche entrée pour vérifier la réponse").grid(column=0,row=2)

entree = Entry(cadre2, width=30)
entree.bind("<Return>", estjuste)

correction=Label(cadre2)

cadre2.grid(column=0,row=2)
entree.grid(column=0,row=0)
correction.grid(column=0,row=1)

#troisième cadre
cadre3=Frame(fenetre, height=400,width=300,  borderwidth=1, relief="ridge")
aideboite=Label(cadre3, text="Aide-toi de la boîte pour faire tes calculs")
cadre3.grid(column=0,row=3)

tout=Entry(cadre3,width=20)
partie1=Entry(cadre3,width=10)
partie2=Entry(cadre3,width=10)

#bouton pour passer à l'étape suivante
etape_suivante=Button(fenetre, text="On continue!", command=exercicesuivant)

#bouton pour afficher la boîte si l'élève le veut

boite=Button(cadre3, text="Aide Boîte", command=afficherboite)
boite.grid(column=1, row=5)

#bouton permettant de quitter
quitter=Button(fenetre, text="Quitter", command=fenetre.destroy)

fenetre.mainloop()
fenetre.destroy()