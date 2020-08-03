import random

jeu = ['pierre', 'feuille', 'ciseaux', 'puit']
print("Bienvenue dans le jeu Pierre Feuille Ciseaux !")

def play():

    bot = random.choice(jeu)

    choix = input('Choisissez entre "pierre", "feuille", "puit ou "ciseaux" !    ')
    if(choix == bot):
        print('Egalité ! Le robot a choisit', bot, 'comme vous !')
    else:
        if(choix == 'pierre' and bot == 'feuille'):
            print('Vous avez gagner ! La pierre écrase la', bot, '!')
        elif(choix == 'feuille' and bot == 'pierre'):
            print('Vous avez perdu ! La feuille se fait écraser par la', bot)
        elif(choix == 'ciseaux' and bot == 'pierre'):
            print('Vous avez perdu ! La pierre écrase le ciseaux !')
        elif(choix == 'pierre' and bot == 'ciseaux'):
            print('Vous avez gagner ! La pierre écrase le ciseaux !')
        elif(choix == 'ciseaux' and bot == 'feuille'):
            print('Vous avez gagner ! Le ciseaux coupe la feuille !')
        elif(choix == 'feuille' and bot == 'ciseaux'):
            print('Vous avez perdu ! Le ciseaux coupe la feuille !')
        elif(choix == 'pierre' and bot == 'puit'):
            print('Vous avez perdu ! La pierre tombe dans le puit !')
        elif(choix == 'puit' and bot == 'pierre'):
            print('Vous avez gagner ! La pierre tombe dans le puit !')
        elif(choix == 'feuille' and bot == 'puit'):
            print('Vous avez gagner ! La feuille bouche le puit !')
        elif(choix == 'puit' and bot == 'feuille'):
            print('Vous avez perdu ! Le puit se fait boucher par la feuille !')
        elif(choix == 'ciseaux' and bot == 'puit'):
            print('Vous avez perdu ! Le puit écrase le ciseaux !')
        elif(choix == 'puit' and bot == 'ciseaux'):
            print('Vous avez gagner ! Le puit écrase le ciseaux !')
        else:
            print('Une erreur est survenue !')

    rejouer()
        
def rejouer():
    choix2 = input('Voulez vous rejouer ? (Y/N)')
    if(choix2 == 'Y'):
        play()
    if(choix2 == 'y'):
        play()
    if(choix2 == 'yes'):
        play()
    else:
        exit

play()

