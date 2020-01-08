import pandas as pd
import matplotlib.pyplot as plt
import itertools
import mplcursors
import chardet
import numpy as np



def main():
    # Partie CSV avec données correcte
    '''
    pour cet échantillon :														
	moyenne		    par mois							OK	
	min /max		par mois et par année				OK							
	écart type		par mois							OK			
	utiliser par exemple  Python Scipy pour les parties mathématiques					OK								
	tracer les courbes de chaque mois avec une bibliothèque graphique python			OK										
	assembler les courbes sur un seul graphique (J1 -> J365) 							OK						
	présenter la valeur lue en parcourant la courbe à l'aide du pointeur                OK
    présenter les valeurs précédentes par mois et par année, par mois glissant de 30 jours centré sur la valeur lue        
														
	à partir de données opendata, retrouver le type de climat													
	reprendre les données typiques d'une localisation proche  fournies en complément , comparer les écarts. Qu'en concluez vous ?													
    '''
    # On charge le fichier csv
    data = pd.read_csv('data/data_SI.csv', sep=';', encoding="utf-8")

    # Partie sur les statistiques
    with open("results/Resultats.txt", "w") as text_file:
        print("Moyennes : ", file=text_file)
        print(f"{np.round(data.mean(), 2)} : ", file=text_file)

        print('\nMinimums :', file=text_file)
        print(f"{data.min()} : ", file=text_file)

        print('\nMaximums :', file=text_file)
        print(f"{data.max()} : ", file=text_file)

        print('\nEcarts-type :', file=text_file)
        print(f"{np.round(data.std(), 2)} : ", file=text_file)

    # --- Graphiques --- #

    # Températures mensuelles
    data.plot(kind='line')
    mplcursors.cursor(hover=True)
    plt.title('Températures mensuelles')
    plt.ylabel('°C')
    plt.savefig('results/mensuelles.png')
    plt.show()
    plt.close()

    # Températures annuelles
    data_all = pd.DataFrame(data.values.T.ravel().tolist())
    data_all.plot(kind='line')
    mplcursors.cursor(hover=True)
    plt.title('Températures annuelles')
    plt.ylabel('°C')
    plt.savefig('results/annuelles.png')
    plt.show()
    plt.close()

main()