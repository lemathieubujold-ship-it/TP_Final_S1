import json
import random
import os

def charger_cartes(niveau):
    try:
        with open('cards.json', 'r', encoding='utf-8') as fichier:
            donnees = json.load(fichier)
            return donnees.get(niveau, [])
    except FileNotFoundError:
        print("Fichier introuvable")
        return []

def melanger_cartes(cartes):
    cartes_jeu = cartes * 2

    # Mélange les cartes
    random.shuffle(cartes_jeu)
    return cartes_jeu

def afficher_menu_principal():

    print("="*50)
    print("1. Jouer une partie")
    print("2. Afficher les scores")
    print("3. Quitter")
    print("="*50)
    
    while True:
        choix = input("Votre choix (1-3): ").strip()
        if choix in ['1', '2', '3']:
            return choix
        else:
            print("1 à 3 j'ai dis")
def jouer_partie() : 
    print("Pas encore dispo")

def afficher_scores():
    print("pas dispo encore")

def quitter_jeu():

    print("="*50)
    print("  Merci d'avoir joué au Jeu")
    print("="*50)
    return False 

def main():
    print("Jeu de Mémoire")
    continuer = True
    while continuer:
        choix = afficher_menu_principal()
        
        if choix == '1':
            jouer_partie()
        elif choix == '2':
            afficher_scores()
        elif choix == '3':
            continuer = quitter_jeu()

if __name__ == "__main__":
    main()