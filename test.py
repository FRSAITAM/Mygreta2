#-------------------------------------------------------------------------------
# Name:        pandas
# Purpose:
#
# Author:      FRsaitam
#
# Created:     17/01/2022
# Copyright:   (c) FRsaitam 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#%matplotlib inline

import pandas as np
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns



#print(pandas.__version__)

df = np.read_csv("F:\Formation_Python\cours\Panda\coeur2.csv",sep=';', header = 0 ) #sep séparateur et header est l'entête

#print(type(df)) #affiche le frame comme metadata
#print(df.shape)
#print(df.head(100)) #on demande d'afficher que les 100 premiers ligne pour voir notre fichier
#print(df.columns)
#print(df.dtypes) #affiche les type de chaque colonne pour adapter à nos  traitements
#print(df.info()) #affiche si on a tous les colonnes remplisent sinon impossible d'utiliser le fichier

#print(df.describe(include='all')) #affiche les NAN sinon affiche les données existentess

'''print(df[['pression', 'sucre']]) #ça récupere les données du header
print(df['age'].head()) #affiche les 5 premiers
print(df['age'].tail()) #affiche les 5 derniers
print(df['age'].head(3)) #affiche les 3 premiers
print(df[['age']].describe()) #sigma de la variance
print(df[['age']].mean()) #la moyenne explicite

#print(df.age[0:3]) #le slicing
print(df['age'].sort_values())
print(df['type_douleur'].value_counts()) #comptage de combien existe de type A, B ...etc dans le tableau
print(df['age'][0]) # premier element dans la colonne age
print(df['sucre'][2:6])
print(df.age[0:3])
print(df['age'].sort_values()) #ordre croissant
print(df['age'].argsort()) #affcihe en ordre les indices des valeurs triées
print(df.sort_values(by='age').head()) #il affiche les 5 premiers lignes par ordre d'age

for col in df.columns:
    print(df[col].dtype)

def operation(x):
    return(x.mean())

resultat = df.select_dtypes(exclude=['object']).apply(operation, axis = 0) #exclude les variables non numérique, affiche que les
print(resultat)'''


#print(df.iloc[0,0]) #pour acceder à la valeur 0 ligne colonne 0 [0,0]
#print(df.iloc[-1,0]) #valeur en derniere ligne est premiere colonne
#print(df.iloc[df.shape[0]-1,0]) #valeur en derniere ligne est premiere colonne

#print(df.iloc[df.shape[0]-1,df.shape[1]-1]) #ça donne présence derniere ligne derniere colonne
#print(df.iloc[-1,-1]) # ça donne le même résultat de derniere ligne derniere colonne

#print(df.iloc[0:5,:]) #affiche les 5 premiers lignes de tous les colonnes

#print(df.iloc[0:5,0:2])
var = df.iloc[0:5,0:2]
#print(var[2:3]) # pour afficher que l'indice 2

#print(df.iloc[0:5,0:5:2]) #affichage de 5 lignes et de 5 colonnes mais avec un saut du 2 colonne a chaque fois

#print(df.iloc[0:5,[0,2,4]]) #affichage du 5 premiers colonne des colonne au niveau 0, 2 et 4

#print(df['type_douleur']=="A") #on indexe avec un vecteur de booleens si on va dans le détail
#print(df.loc[df['type_douleur']=="A", :]) #affiche les individus présentent une douleur de type A

#print(df.iloc[-5:,:]) #affichage des 5 deriere lignes de tous les colonne (ligne -5: et colonne (:))
#print(df.iloc[0:5,0:2]) #ligne de 0 a 4 et les colonne de 0 à 1

#print(df.iloc[0:5, [0,2,4]]) #colonne 0, 2 et 4

#print(df.iloc[0:5,0:5:2]) #exactelent la même chose colonne 0, 2 et 4


#restriction avec les conditions - les requetes
#print(df.loc[df['type_douleur']=="A",:]) #les (:) serve à faire le passage de tous les colonnes ou on le type de douleur de type A

#print(df['type_douleur']=="A") #pas besoin de méthode ou fonction pour retourner un booleen

#print((df['type_douleur']=="A").value_counts())

#print(df.loc[df['type_douleur'].isin(['A','B']),:]) #afficher le type de douleur où on a que A et B; isin veut dire is in en anglais

#print(df.loc[df['type_douleur'].isin(['A']) & (df['angine']=="oui"),:])

#print(df.loc[(df['age']<45) & (df['sexe']=="masculin")& (df['coeur']== "presence"), : ])

#---------

colonnes = ['age', 'sexe', 'coeur', 'taux_max']
#print(df.loc[(df['age']<45) & (df['sexe']=="masculin") & (df['coeur']== "presence"),colonnes])

#print(df.loc[(df['age']<45) & (df['sexe']=="masculin") & (df['coeur']== "presence"),:])

#calculs récapitulatifs - croisement des variables
#print(pandas.crosstab(df['sexe'],df['coeur']))


# pour afficher le pourcentage des feminin en cross avec coeur et pareil pour mascullin
#print(pandas.crosstab(df['sexe'], df['coeur'], normalize='index'))  #normalize, index est la colonne d'excel de 1 a 271

#print(pandas.crosstab(df['sexe'], df['coeur'], values=df['age'], aggfunc=pandas.Series.mean))

#print(df.pivot_table(index=['sexe'], columns=['coeur'], values=['age'], aggfunc=pandas.Series.mean)) #même resulat que ci-dessus

#print(pandas.crosstab([df['sexe'], df['sucre']], df['coeur']))

#print(pandas.crosstab([df['sexe'], df['sucre']], df['coeur'], normalize = 'index'))


g = df.groupby('sexe') #scission des données selon le sexe de A à Z
#print(g) # à affiche la génération d'un objet
#print(g.get_group('masculin').shape) #calculer la dimension du sous-dataFrame associé aux hommes via la commande "shape"


#afficher la moyenne et std de l'age pour les deux sexes feminin et masculin
#print(g[['age']].agg([pandas.Series.mean, pandas.Series.std])) #std est l'écart type

'''for groupe in g:
    print(groupe[0]) #affiche juste les variable existant dans la colonne "sexe"
    #print(groupe[0]) #affiche tous les données dans le tableau DF mais groupe par feminin et masculin
    print(pandas.Series.mean(groupe[1]['age']))'''

'''print(df['sexe'].head()) #affiche les 5 premiers
a=df['sexe']
print(a[2])'''

#création d'une variable tauxnet (qui n'a aucune signification médicale)
#utilisation de la librairie numpy (log = logarthme népérien)
tauxnet = df['taux_max']*numpy.log(df['age'])
#print(tauxnet)
#print(df['taux_max']) #affiche que la colonne taux_max qui existe dans le tableau df


#laquelle variable peut être concaténée au DataFrame

newdf = pandas.concat([df, tauxnet], axis=1) #ajout d'une colonne au DF grace à axis 1, sinon axis =0 pour ajouter une ligne
#print(newdf.shape) #la nouvelle DF est de taille 270 lignes et 14 colonnes

#pour comparer les deux tableaux
#print(newdf)
#print(df)

code = pandas.Series(numpy.zeros(df.shape[0]))
#print(code)
#print(df.shape[1]) #nbr de colonne quand [1] et nbr de ligne quand [0]

code[(df['type_douleur']== 'A') | (df['type_douleur']== 'B')] = 1
#print(code.value_counts()) #it counts how many row for "Masculin" and how mant row for "feminin"

codebis = df['sexe'].eq('masculin').astype('int')
#print(codebis.value_counts())
#print(newdf.shape)

#%matplotlib inline #voir en top du code
#import matplotlib.pyplot as plt

#Graphe 1
#x1 = df.hist(column='age', by='sexe')

#graphe 2
#y1 =df.hist(column ='age')

#graphe 3
#y2 = df.plot.scatter(x='age',y='taux_max')

#y2 = df.plot.scatter(x='age')
#print(df.loc[df['type_douleur']=="A", :])

#subplot ne fonctionne pas pour moi !!
'''fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.plot(y1, y2)
ax2.plot(y1, -y2)'''

#df['age'].plot.kde() #ne fonctionne pas pour moi


#affichage du seeborn
data = sns.displot(df, x="age", col="type_douleur", row="sexe")
plt.show() #va afficher les deux graphes

#affichage nuage de point
'''sns.relplot(data = df, x="age", y="taux_max", hue='depression', style='sexe', size='type_douleur') #forme de l'affichage selon le sexe
plt.show() #va afficher les deux graphes'''

#affichage du camombert pour la colonne sex avec commande pie
x1 = df['sexe'].value_counts().plot.pie()
#plt.show()



#affichage du camombert pour la colonne sex avec commande seaborn
'''labels = ['fem', 'mas']
couleur = sns.color_palette('pastel')[0:2]
df['sexe'].value_counts().plot.pie(labels = labels, colors = couleur)
plt.show()'''


















