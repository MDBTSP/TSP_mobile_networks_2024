# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import random

# Chargez le fichier CSV dans un DataFrame
insee_data = pd.read_csv('input_folder/insee.csv', sep=';')

# Creez une colonne pour les technologies deployees
insee_data['Technologies'] = ""

# Charger les donnees du fichier "calendar-regulation.csv"
calendar_regulation_data = pd.read_csv('input_folder/calendar-regulation.csv', sep=';')

#pour chaque ligne du fichier regulation, je regarde si la spéc est vérifiée 
#sinon je déploie 



# Appliquez les règles de déploiement
for density_code in [1, 2, 3, 4, 5, 6]:
    insee_data.loc[insee_data['density_code'] == density_code, 'Technologies'] = '4G'

# Sélectionnez uniquement les villes avec density_code 7
insee_data_density_7 = insee_data[insee_data['density_code'] == 7]
# Triez le DataFrame en fonction de la surface (décroissant) pour density_code 7
insee_data_density_7 = insee_data_density_7.sort_values(by='surface', ascending=False)
# Sélectionnez 50% des villes avec la plus grande surface
n = int(len(insee_data_density_7) * 0.5)  # 50% des villes
selected_cities = insee_data_density_7.head(n)

# Mettez à jour les valeurs de la colonne "Technologies" pour les villes sélectionnées
for index, row in selected_cities.iterrows():
    insee_data.at[index, 'Technologies'] = '4G'
    
    
    

# Affichez la liste des villes avec les technologies déployées
for index, row in insee_data.iterrows():
    if  row['density_code']==7 and row['Technologies'] != '':
        print(f"Cities : {row['city_code']} - Density Code : {row['density_code']} - Surface : {row['surface']} - Technologies : {row['Technologies']}")

#Affichage des villes non couvertes    
cities_wo_techno = insee_data[insee_data['Technologies'] == '']
print("\n"+f"Number and list of cities without technologies deployed : {len(cities_wo_techno)}")
for index, row in cities_wo_techno.iterrows():
    print(f"Cities : {row['city_code']} - Density Code : {row['density_code']} - Technologies : {row['Technologies']}")








# Utilisez la fonction value_counts() pour compter le nombre de villes pour chaque density_code
density_code_counts = insee_data['density_code'].value_counts()

# Triez les donnees par l'index (les density_code)
density_code_counts = density_code_counts.sort_index()
print(f"Number of cities of density_code 7: {density_code_counts[7]}"+"\n")

# Creez un histogramme
plt.bar(density_code_counts.index, density_code_counts.values)
# Ajoutez des etiquettes et un titre
plt.xlabel('Density Code')
plt.ylabel('Number of cities')
plt.title('Number of cities per Density Code')
# Affichez l'histogramme
#plt.show()