from colorama import init 
init() 
from colorama import Fore,Back,Style
import random

def motus():

    motale=motaleatoire()                             #appel la fonction motaleatoire 
    print(motale)      #Temporaire info mot choisie
    
    tentative = 0   
    mottrouver = false
    while ((mottrouver == true) or (tentative >= 8)):
        tentative += 1
        motpropo=propositionmot(motale)             #appel la fonction propositionmot et récupère le mot proposé
        mottrouver=comparer(motale,motpropo)        #appel la fonction comparer et récupère un booléen si bon ou non 
        
        
    if(mottrouver == true):
        win()
    elif(tentative = 8):
       loose()
    elif((mottrouver == true) and (tentative = 8)):
        win()
        
def motaleatoire():
     
    mot=["mmmot0","mmmot1","mmmot2","mmmot3","mmmot4","mmmot5","mmmot6","mmmot7","mmmot8","mmmot9"]
    valmotale = random.randint(0,9)
    motale = mot[valmotale]
   
    return(motale)
 
def propositionmot(mot):

    motpropo=input("Entre un mot de 6 lettre :")
    while (len(motpropo) != 6):
        print("Le mot ecrit ne contient pas 6 lettre : Recommencer !")#vérifie que le mot choisie a 6 lettre 
        motpropo=input("Entre un mot de 6 lettre :")
    print(motpropo)
    return(motpropo)

def comparer(motale,motpropo):
    for i in range(len(motpropo)) :
        if (motpropo[i] == motale[i]):
            print(Back.BLUE + motpropo[i]) 
        else:
            for j in range(len(motpropo)):
                if (motpropo[i] == motale[i])
                print(Back.Yellow + motpropo[i])
                else:
                print(Back. + motpropo[i])
     
    if (motale == motpropo):
        return(True)
    else:
        return(False)

def win():
    print("Felicitation vous avez gagné !!")
    
def loose():
    print("Dommage,Game Over")
    print("Vous ferez mieux la prochaine fois !")



motus()  
