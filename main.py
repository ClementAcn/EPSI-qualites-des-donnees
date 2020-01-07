import pandas as pd
import matplotlib.pyplot as plt
import itertools
import mplcursors

'''
pour cet échantillon :														
	moyenne		    par mois							OK	
	min /max		par mois et par année				OK							
	écart type		par mois											
	utiliser par exemple  Python Scipy pour les parties mathématiques					OK								
	tracer les coubes de chaque mois avec une bibliothèque grapohique python			OK										
	assembler les courbes sur un seul graphique (J1 -> J365) 							OK						
	présenter la valeur lue en parcourant la courbe à l'aide du pointeur, présenter les valeurs précédentes par mois et par année, par mois glissant de 30 jours centré sur la valeur lue													
														
	à partir de données opendata, retrouver le type de climat													
	reprendre les données typiques d'une localisation proche  fournies en complément , comparer les écarts. Qu'en concluez vous ?													
'''

def main():
    # On charge le fichier csv
    data = pd.read_csv('data/data_SI.csv', encoding='latin-1', sep=';')
    
    # Déclaration d'une liste pour stocker toutes les valeurs de l'année
    array_annee = list()

    # On vide le fichier texte de ses résultats
    with open("results/Resultats.txt", "w") as text_file:
        print('', file=text_file)
    
    for column in data:
        val = data[column]
        with open("results/Resultats.txt", "a") as text_file:
            print(f"Résultats de {column} : ", file=text_file)
            print(f"Moyenne: {str(round(val.mean(), 2))} °C", file=text_file)
            print(f"Minimum: {str(round(val.min(), 2))} °C", file=text_file)
            print(f"Maximum: {str(round(val.max(), 2))} °C", file=text_file)
            print(f"Ecart-type: {str(round(val.std(), 2))} °C", file=text_file)
            print('\n', file=text_file)

        # Création des graphiques mensuels sous forme d'image
        plt.plot(val)
        plt.title('Températures en ' + column)
        plt.ylabel('°C')
        plt.savefig('results/' + column + '.png')
        plt.close()
        array_annee.append(val.dropna().values.tolist())

    # Ecriture du minimum et du maximum annuel dans le fichier
    with open("results/Resultats.txt", "a") as text_file:
        print('Statistiques sur l\'année entière: ', file=text_file)
        print(f"Minimum: {str(round(data.dropna().values.min(), 2))} °C", file=text_file)
        print(f"Maximum: {str(round(data.dropna().values.max(), 2))} °C", file=text_file)

    # Partie sur la création du graphique sur les températures annuelles
    all = list(itertools.chain.from_iterable(array_annee))
    plt.plot(all)
    mplcursors.cursor(hover=True)
    plt.title('Températures en °C pour l\'année')
    plt.ylabel('°C')
    plt.savefig('results/Annuel.png')
    plt.show()
    plt.close()

main()