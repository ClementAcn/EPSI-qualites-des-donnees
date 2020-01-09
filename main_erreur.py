import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools
import mplcursors
import chardet
import numpy as np

def main():
    # Partie CSV avec données incorrecte
    '''
    pour cet échantillon :					
    moyenne		    par mois		        OK
    min /max		par mois et par année   OK
	écart type		par mois		        OK  
	utiliser par exemple  Python Scipy pour les parties mathématiques				
	tracer les coubes de chaque mois avec une bibliothèque grapohique python				
	assembler les courbes sur un seul graphique (J1 -> J365) 				
	présenter la valeur lue en parcourant la courbe à l'aide du pointeur, présenter les valeurs précédentes par mois et par année, par mois glissant de 30 jours centré sur la valeur lue				

	identifier les valeurs atypiques ou manquantes	                            OK			
	définir une méthode pour identifier une valeur atypique				        OK
	définir une loi pour valider la pertinence ou non d'une valeur atypique	    OK			
	implémenter ces lois dans votre application précédente				        
    '''
    # On charge le fichier csv
    data_erreur = pd.read_csv('data/data_SI_erreur.csv', sep=';', encoding="utf-8")

    # Suppression des valeurs non float par NaN
    for column in data_erreur:
        cpt = 0
        for row in data_erreur[column]:
            try:
                float(row)
            except ValueError:
                data_erreur.loc[cpt, column]=np.NaN
            cpt+=1
    data_erreur = data_erreur.astype(float)

    # Suppression des valeurs qui sortent du lot (cas extrème)
    for column in data_erreur:
        moyenne = data_erreur[column].mean()
        ecart_type = np.round(data_erreur[column].std(), 2)
        data_erreur[column] = np.where(data_erreur[column] < (moyenne + 3 * ecart_type), data_erreur[column], np.nan)
        data_erreur[column] = np.where(data_erreur[column] > (moyenne - 3 * ecart_type), data_erreur[column], np.nan)

    # On remplace les NaN
    data_erreur.interpolate(axis=0, inplace=True)

    # Suppression des valeurs de chaque mois inexistante
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month_cpt, column  in enumerate(data_erreur):
        for day_cpt, row in enumerate(data_erreur[column]):
            if day_cpt+1 > months_length[month_cpt]:
                data_erreur.loc[day_cpt, column]=np.nan

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
    
    # --- Graphiques --- #

    # Températures mensuelles
    data_erreur.plot(kind='line')
    mplcursors.cursor(hover=True)
    plt.title('Températures mensuelles')
    plt.ylabel('°C')
    plt.savefig('results/erreur_mensuelles.png')
    plt.show()
    plt.close()

    # Températures annuelles
    data_erreur_all = pd.DataFrame(data_erreur.values.T.ravel().tolist())
    data_erreur_all = data_erreur_all.dropna()
    data_erreur_all.plot(kind='line')
    mplcursors.cursor(hover=True)
    plt.title('Températures annuelles')
    plt.ylabel('°C')
    plt.savefig('results/erreur_annuelles.png')
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