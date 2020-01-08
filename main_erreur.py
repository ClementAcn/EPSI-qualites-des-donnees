import pandas as pd
import matplotlib.pyplot as plt
import itertools
import mplcursors
import chardet
import numpy as np

def main():
    # Partie CSV avec données incorrecte
    '''
    pour cet échantillon :					
    moyenne		    par mois		
    min /max		par mois et par année		
	écart type		par mois		
	utiliser par exemple  Python Scipy pour les parties mathématiques				
	tracer les coubes de chaque mois avec une bibliothèque grapohique python				
	assembler les courbes sur un seul graphique (J1 -> J365) 				
	présenter la valeur lue en parcourant la courbe à l'aide du pointeur, présenter les valeurs précédentes par mois et par année, par mois glissant de 30 jours centré sur la valeur lue				

	identifier les valeurs atypiques ou manquantes				
	définir une méthode pour identifier une valeur atypique				
	définir une loi pour valider la pertinence ou non d'une valeur atypique				
	implémenter ces lois dans votre application précédente				
    '''
    # On charge le fichier csv
    data_erreur = pd.read_csv('data/data_SI_erreur.csv', sep=';', encoding="utf-8")

    # Partie sur les statistiques
    with open("results/Resultats_erreur.txt", "w") as text_file:
        print("Moyennes : ", file=text_file)
        print(f"{np.round(data_erreur.mean(), 2)} : ", file=text_file)

        print('\nMinimums :', file=text_file)
        print(f"{data_erreur.min()} : ", file=text_file)

        print('\nMaximums :', file=text_file)
        print(f"{data_erreur.max()} : ", file=text_file)

        print('\nEcarts-type :', file=text_file)
        print(f"{np.round(data_erreur.std(), 2)} : ", file=text_file)
    
main()