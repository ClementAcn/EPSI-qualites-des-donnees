import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import itertools
import mplcursors
import chardet
import numpy as np
import json


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
    par mois glissant de 30 jours centré sur la valeur lue                              OK      
														
	à partir de données opendata, retrouver le type de climat													
	reprendre les données typiques d'une localisation proche  fournies en complément , comparer les écarts. Qu'en concluez vous ?
    corelation convolution regression interpolation										
    '''
    # On charge le fichier csv
    data = pd.read_csv('data/data_SI.csv', sep=';', encoding="utf-8")

    print('Choisissez quel visualisation voulez-vous ? (1 - Mensuelle / 2 - Annuelle / 3 - Comparatif)')
    try:
        value=int(input("Saisissez 1, 2 ou 3:\n"))
    except ValueError:
        print("This is not a whole number.")
        return

    if value < 1 or value > 3:
        return

    if value == 1:
        mensuel(data)
    elif value == 2:
        annuel(data)
    elif value == 3:
        compare()

def mensuel(data):
    # Partie sur les statistiques
    with open("results/res_mens.txt", "w") as text_file:
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

def annuel(data):
    # Températures annuelles
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
    
def compare():
    compare = pd.read_csv('data/compare.csv', sep=';', encoding="utf-8")
    # with open('data/moscow_2017.json', 'r') as file:
    #     data_json=file.read()
    # data_moscow = json.loads(data_json)
    # temps = []
    # for k in data_moscow["data"]:
    #     temps.append(k['temperature'])
    # print(temps)
    # print(len(temps))
    compare['station_finlande'] = compare['station_finlande'].str.replace(',','.')
    compare['station_finlande'] = compare['station_finlande'].astype(float)
    print("Moyennes : \n{}".format(compare.mean()))
    print("Minimums : \n{}".format(compare.min()))
    print("Maximums : \n{}".format(compare.max()))
    print("Ecarts-type : \n{}".format(compare.std()))
    print("Corrélation : \n{}".format(compare.corr()))
    # print("Convolution : \n{}".format(np.convolve(compare['ville_mystere'], compare['station_finlande'])))

main()

# API key : atNedUkf
# Get station id : https://api.meteostat.net/v1/stations/search?q=moscow&key=atNedUkf
# Get weather data : https://api.meteostat.net/v1/history/daily?station=UUWW0&start=2017-12-31&end=2018-12-31&key=atNedUkf