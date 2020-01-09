import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
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
    présenter les valeurs précédentes par mois et par année
    par mois glissant de 30 jours centré sur la valeur lue       
														
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
    # data_all = pd.DataFrame(data.dropna().values.T.ravel().tolist())
    data_all = pd.DataFrame(data.values.T.ravel().tolist())
    data_all = data_all.dropna()
    data_all.plot(kind='line')
    mplcursors.cursor(hover=True)
    plt.title('Températures annuelles')
    plt.ylabel('°C')
    plt.savefig('results/annuelles.png')
    axamp = plt.axes([0.2, 0.025, 0.65, 0.03], polar=False)
    samp = Slider(axamp, 'Jours', 1, 365, valinit=20)
    al = plt.gcf().get_axes()
    plt.sca(al[0]) # Pour remettre l'axe du graphique par défaut et non celui du curseur
    def update(val):
        xvalue = samp.val
        if xvalue < 15:
            xvalue = 15
        elif xvalue > 350:
            xvalue = 350
        plt.xlim(xvalue-15, xvalue+15)

    samp.on_changed(update)
    plt.show()
    plt.close()



main()