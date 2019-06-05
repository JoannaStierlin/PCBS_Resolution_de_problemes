# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:24:34 2019

@author: Joanna
"""
from tkinter import *
import csv
#recuperer le fichier des exercices
exercices = csv.reader(open('exercices_evaluation_niveau.txt'), delimiter=";")
exercices= list(exercices)
nbexercices=len(exercices)


#noter à quoi correspondent les colonnes des reponses enregistrees
numexo=0
typeitem=1
consigne=2
corexo=3

numero_exercice=0
#ouvrir le fichier pour recolter les reponses
donnees_eleve = open("donnees_eleve.txt", "w") 

def continuertest(reponse):
    global numero_exercice
    
    reponse_question=[exercices[numero_exercice][numexo]+"\t", 
                      exercices[numero_exercice][typeitem]+"\t",
                      exercices[numero_exercice][corexo]+"\t",
                      entree.get()+"\t",
                      strategie.get()+"\n"]
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
      text="Tu peux écrire ta réponse ici puis cocher:\n Appuie sur la touche entrée pour valider ta réponse").grid(column=0,row=0)

entree = Entry(cadre2, width=30)
entree.bind("<Return>", continuertest)


cadre2.grid(column=0,row=2)
entree.grid(column=0,row=1)

#troisieme cadre pour demander l'operation
cadre3 = Frame(fenetre, height=400,width=300,  borderwidth=1)
demanderoperation=Label(cadre3, 
                        text="Quelle opération as-tu fait dans ta tête pour trouver la réponse? \n J'ai fait :")

strategie = StringVar()

addition = Radiobutton(cadre3, text = "Addition", variable = strategie,
                 value="A")
soustraction = Radiobutton(cadre3, text = "Soustraction", variable = strategie,
                 value="S")
autre = Radiobutton(cadre3, text = "J'ai fait autrement", variable = strategie,
                 value="Autre")
saispas = Radiobutton(cadre3, text = "Je ne sais pas", variable = strategie,
                 value="N")

cadre3.grid(column=0,row=3)
demanderoperation.grid(column=0,row=0, columnspan=4)

addition.grid(column=0,row=1)
soustraction.grid(column=1,row=1)
autre.grid(column=2,row=1)
saispas.grid(column=3,row=1)


#bouton pour passer à l'étape suivante
etape_suivante=Button(fenetre, text="On continue!", command=exercicesuivant)

#bouton permettant de quitter
quitter=Button(fenetre, text="Quitter", command=fenetre.destroy)

fenetre.mainloop()
fenetre.destroy()