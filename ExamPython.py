from colorama
import init init() 
from colorama import Fore, Back, Style 
import random



def motus():

    mot=["mot0","mot1","mot2","mot3","mot4","mot5","mot6","mot7","mot8","mot9"]
    valmotale = random.randint(0,9)
    motale = mot[valmotale]
    
    print(motale)

motus():    

#propmot=int(input("Entre un mot de 6 lettre :"))