from colorama import init 
init() 
from colorama import Fore,Back,Style
import random

def motus():
    motale=motaleatoire()                             #appel la fonction motaleatoire 
    print(motale)      #aide info mot aleatoire
    tentative = 0   
    mottrouver = False
    while ((mottrouver != True) and (tentative < 8)):
        tentative += 1
        motpropo=propositionmot(motale)             #appel la fonction propositionmot et récupère le mot proposé
        mottrouver=comparer(motale,motpropo)        #appel la fonction comparer et récupère un booléen si bon ou non 
        if (mottrouver == False):
            print("faux")
    if(mottrouver == True):
        win()                                       #appel la fonction win
    elif(tentative == 8):
       loose()                                      #appel la fonction win
    elif((mottrouver == True) and (tentative == 8)):
        win()                                       #appel la fonction loose
        
        
def motaleatoire():
    mot=["relier","manger","dormir","courir","tomber","avance","sourie","manier","charge","vaincu"]
    valmotale = random.randint(0,9)
    motale = mot[valmotale]
    return(motale)
 
def propositionmot(mot):
    motpropo=input("Entre un mot de 6 lettre :")
    while (len(motpropo) != 6):
        print("Le mot ecrit ne contient pas 6 lettre : Recommencer !")#vérifie que le mot choisie a 6 lettre 
        motpropo=input("Entre un mot de 6 lettre :")
    return(motpropo)

# def comparer(motale,motpropo):
    # for i in range(len(motpropo)) :
        # if (motpropo[i] == motale[i]):
            # print(Back.BLUE + motpropo[i]) 
        # else:
            # for j in range(len(motpropo)):        #Marche pas ! car meme si il trouve la bonne couleur la change juste apres T_T 
                # if (motpropo[i] == motale[i]):                            
                # print(Back.YELLOW + motpropo[i])
                # else:
                # print(Back.RED + motpropo[i])
    # mottrouver = False
    # if (motale == motpropo):
        # mottrouver = True
    # else:
        # mottrouver = False 
    # return(mottrouver)

def comparer(motale,motpropo):
    mot=""
    for i in range(0,6) :
        if (motpropo[i] == motale[i]):
            mot = motpropo[i]+"B"           #lettre bonne 
        if (motpropo[i] != motale[i]):
            mot = motpropo[i]+"F"           #lettre Fausse
        print(mot,end="")
    print("")
    mottrouver = False
    if (motale == motpropo):
        mottrouver = True
    else:
        mottrouver = False 
    return(mottrouver)





def win():
    print("Felicitation vous avez gagné !!")
    
def loose():
    print("Dommage,Game Over")
    print("Vous ferez mieux la prochaine fois !")

 
    
motus()