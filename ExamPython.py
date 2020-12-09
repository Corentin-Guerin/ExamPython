from colorama
import init init() 
from colorama import Fore, Back, Style



import random

def motus():

    mot=["mmmot0","mmmot1","mmmot2","mmmot3","mmmot4","mmmot5","mmmot6","mmmot7","mmmot8","mmmot9"]
    valmotale = random.randint(0,9)
    motale = mot[valmotale]
    print(motale)      #Temporaire info mot choisie
    
    
    propmot=propositionmot(motale)


def propositionmot(mot):

    propmot=input("Entre un mot de 6 lettre :")
    while (len(propmot) != 6):
        print("Le mot etre ne contien pas 6 lettre : Recommencer !")#vérifie que le mot choisie a 6 lettre 
        propmot=input("Entre un mot de 6 lettre :")
    print(propmot)
    return(propmot)




motus()  

    
   


#propmot=int(input("Entre un mot de 6 lettre :"))