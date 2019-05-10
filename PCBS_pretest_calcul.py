# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:24:34 2019

@author: Joanna
"""
from tkinter import *

#exercices=[["Combien font 2+2?","4"],
#           ["5*3 ?", "15"]]

with open('exercices_evaluation_niveau.txt', 'r') as mon_fichier:
    lignes=mon_fichier.readlines()
    
#print(lignes)
exercices=[]
for ligne in lignes:
   ligne = ligne.replace("\n", "")
   donnees = ligne.split('; ')
   exercices.append(donnees)

nbexercices=len(exercices)
#noter à quoi correspondent les colonnes
numexo=0
typeitem=1
consigne=2
corexo=3

numero_exercice=0

donnees_eleve = open("donnees_eleve.txt", "w") 

def continuertest(reponse):
    global numero_exercice
    
    reponse_question=[exercices[numero_exercice][numexo]+"\t", 
                      exercices[numero_exercice][typeitem]+"\t",
                      exercices[numero_exercice][corexo]+"\t",
                      entree.get()+"\t",
                      CheckVar1.get()+"\n"]
    donnees_eleve.writelines(reponse_question)
    entree.delete(0,END)
    entree.grid_forget()
    cadre3.grid_forget()
    numero_exercice+=1
    
        
    if numero_exercice==nbexercices: 
        quitter.grid(column=0, row=5)
        donnees_eleve.close()

    else: 
        etape_suivante.grid(column=0,row=8)
        
    
def exercicesuivant():
    entree.grid(column=0,row=3)
    cadre3.grid(column=0,row=3)
    etape_suivante.grid_forget()
    
    Num_Exo.configure(text=exercices[numero_exercice][numexo])
    consigne2.configure(text=exercices[numero_exercice][consigne])
    

    
 # création du widget principal
fenetre = Tk()
fenetre.title("Apprendre à calculer")
fenetre.geometry("1000x600+300+0")

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
      text="Tu peux écrire ta réponse ici puis cocher:\n Appuie sur la touche entrée pour valider ta réponse").grid(column=0,row=2)

entree = Entry(cadre2, width=30)
entree.bind("<Return>", continuertest)


cadre2.grid(column=0,row=2)
entree.grid(column=0,row=0)

#troisieme cadre pour demander l'operation
cadre3 = Frame(fenetre, height=400,width=300,  borderwidth=1)
demanderoperation=Label(cadre3, text="Quelle operation as-tu fait dans ta tete pour trouver la reponse? \n J'ai fait :")

CheckVar1 = StringVar()

C1 = Radiobutton(cadre3, text = "Addition", variable = CheckVar1,
                 value="A")
C2 = Radiobutton(cadre3, text = "Soustraction", variable = CheckVar1,
                 value="S")
C3 = Radiobutton(cadre3, text = "J'ai fait autrement", variable = CheckVar1,
                 value="Autre")
C4 = Radiobutton(cadre3, text = "Je ne sais pas", variable = CheckVar1,
                 value="N")

cadre3.grid(column=0,row=3)
demanderoperation.grid(column=0,row=0)

C1.grid(column=0,row=1)
C2.grid(column=1,row=1)
C3.grid(column=2,row=1)
C4.grid(column=3,row=1)


#bouton pour passer à l'étape suivante
etape_suivante=Button(fenetre, text="On continue!", command=exercicesuivant)

#bouton permettant de quitter
quitter=Button(fenetre, text="Quitter", command=fenetre.destroy)

fenetre.mainloop()
fenetre.destroy()