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
    # dtype={'Mars': np.int64, 'Juin': np.int64, 'Juillet': np.int64, 'Octobre': np.int64}
    data_erreur = pd.read_csv('data/data_SI_erreur.csv', sep=';', encoding="utf-8")
    print(data_erreur)
    # data_erreur = data_erreur.apply(pd.to_numeric, errors='coerce')
    print('------------------------------')
    for column in data_erreur:
        val_column = data_erreur[column]
        print(val_column)
        for value in val_column:
            print(value)
            if not value.isnumeric:
                value = val_column.mean()
        print(val_column)
        '''
        if not val_column.value.isnumeric:
            print(val_column)
            val_column = val_column.mean()
        '''
    print(data_erreur)
    # data_erreur = data_erreur.apply(lambda x: x.fillna(x.mean()))
    # print(data_erreur)
    
    '''
    for data in data_erreur:
        for value in data_erreur[data]:
            if not isinstance(value, int) or not isinstance(value, float):
                print(value)
                print(type(value))
                value = value.replace(value, 999)

    if isinstance(data_erreur, np.float64):
        data_erreur = data_erreur.astype('int64').dtypes
    if not isinstance(data_erreur, np.int64):
        data_erreur = data_erreur.replace(data_erreur, 999)
    '''
    '''
    for dataset in data_erreur_numeric:
        mars_avg = dataset['mars'].mean()
        mars_std = dataset['mars'].std()
        mars_null_count = dataset['mars'].isnull().sum()
        mars_null_random_list = np.random.randint(mars_avg - mars_std, mars_avg + mars_std, size=mars_null_count)    
        dataset.loc[np.isnan(dataset['mars']),'mars'] = mars_null_random_list
    '''
    
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