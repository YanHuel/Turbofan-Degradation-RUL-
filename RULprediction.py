# --------------- Bibliotheken --------------- #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 


import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score




# --------------- Daten einlesen und verstehen --------------- #

dirPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(dirPath)
df = pd.read_csv("inputs\\train_FD001.txt", sep=" ", header=None)

index_names = ["unit_number", "time_in_cycles"]
settings = ["setting 1", "setting 2", "setting 3"]
sensors = ["T2", "T24", "T30", "T50", "P2", "P15", "P30", "Nf", "Nc", "epr", "Ps30", "phi", "NRf", "NRc", "BPR", "farB", "htBleed", "Nf_dmd", "PCNfR_dmd", "W31", "W32"]
col_names = index_names + settings + sensors

dfTrain = pd.read_csv("inputs\\train_FD001.txt", sep="\s+", header=None, index_col=False, names=col_names)
dfValid = pd.read_csv("inputs\\test_FD001.txt", sep="\s+", header=None, index_col=False, names=col_names)
realRUL = pd.read_csv("inputs\\RUL_FD001.txt", sep="\s+", header=None, index_col=False, names=['RUL'])

#print("Form des Train-Datensatzes: ", dfTrain.shape)
#print("Form des Test-Datensatzes: ", dfValid.shape)
#print("Form des Valid-Datensatzes: ", dfvalid.shape)

# Sind NaN-Werte in den Daten vorhanden?
#print('Anzahl der NaN-Werte:\n', dfTrain.isna().sum())      # -> Nein

# Statistische Information über die ersten beiden Spalten der Daten
#print(dfTrain.loc[:, ['unit_number', 'time_in_cycles']].describe())

# Statistische Informationen über die Sensoren
#print(dfTrain.loc[:, "T2":].describe().transpose())


# --------------- Datenvisualisierung --------------- #

# Ein Balkendiagramm für die Zeitzyklen aller Sensoren
max_time_cycles = dfTrain[index_names].groupby('unit_number').max()
plt.figure(figsize = (10,10))
ax = max_time_cycles['time_in_cycles'].plot(kind = 'barh', width = 0.8, stacked = True, align = 'center')
plt.title('Strahltriebwerk Lebenszyklus', fontweight = 'bold', size = 15)
plt.xlabel('Zeitzyklus', fontweight = 'bold', size = 10)
plt.xticks(size = 10)
plt.ylabel('Unit', fontweight = 'bold', size = 10)
plt.yticks(size = 10)
plt.grid(True)
plt.tight_layout()
#plt.show()


# Anzahl vs Zeitzyklen
max_time_cycles = dfTrain[index_names].groupby('unit_number').max()
sns.displot(max_time_cycles['time_in_cycles'], kde=True, bins=20, height=6, aspect=2)
plt.xlabel("Maximaler Zeitzyklus", fontweight = 'bold', size = 10)
plt.ylabel("Anzahl", fontweight = 'bold', size = 10)
plt.title("Verteilung aller Lebenszyklen", fontweight = 'bold', size = 15)
#plt.show()


# Hinzufügen der RUL basierend auf dem maximalen Zeitzyklus
trainRUL = dfTrain.copy()

train_units = trainRUL.groupby('unit_number')
max_cycles = train_units['time_in_cycles'].max()
merged = trainRUL.merge(max_cycles.to_frame(name='max_cycles'), left_on='unit_number', right_index=True)
merged['RUL'] = merged['max_cycles'] - merged['time_in_cycles']
merged = merged.drop("max_cycles", axis=1)

trainRUL = merged
#print(trainRUL[['unit_number', 'RUL']])

maxRUL = trainRUL.groupby('unit_number').max().reset_index()
#print(maxRUL.head())


# Korrelationen berechnen
corr = trainRUL.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(10, 10))
cmap = sns.diverging_palette(230, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=0.3, center=0, square=True, linewidths=0.5, cbar_kws={"shrink": 0.5})
#plt.show()
plt.close()

# Verteilung der Sensorwerte über den Abfall der RUL
def plot_sensor(df, signal):
    plt.figure(figsize=(13,5))
    for i in df['unit_number'].unique():
        if(i % 10 == 0):
            plt.plot('RUL', signal, data=df[df['unit_number'] == i].rolling(10).mean())
    plt.xlim(250,0)
    plt.xticks(np.arange(0, 300, 25))
    plt.ylabel(signal)
    plt.xlabel('Remaining Useful Lifetime')
    #plt.show()
    plt.close()

for i in range(1,22):
    try:
        plot_sensor(trainRUL, sensors[i])
    except:
        pass

# Darstellung der Werte im Boxplot zur Untersuchung der Outlier
for j in sensors:
    plt.figure(figsize=(13,7))
    plt.boxplot(trainRUL[j])
    plt.title(j)
    #plt.show()
    plt.close()

# Rauswurf aller Sensoren, deren Werte konstant und eine sehr geringe Korrelation mit den RUL-Werte haben
for col in range(1,22):
    if col in [1, 5, 6, 10, 16, 18, 19]:
        trainRUL.drop(columns=sensors[col-1], inplace=True)
#print(trainRUL.head())

# --------------- Modellentwicklung --------------- #

# Aufteilung der Daten in Training und Test
train = trainRUL.copy()
train = train.drop(columns=index_names+settings)
Xtrain, Xtest, yTrain, yTest = train_test_split(train, train['RUL'], test_size=0.3, random_state=42)

# Skalierung der Werte
scaler = MinMaxScaler()
Xtrain.drop(columns=['RUL'], inplace=True)
Xtest.drop(columns=['RUL'], inplace=True)
Xtrain = scaler.fit_transform(Xtrain)
Xtest = scaler.fit_transform(Xtest)
Xvalid = dfValid.groupby('unit_number').last().reset_index().drop(columns=index_names + settings)
Xvalid = scaler.fit_transform(Xvalid)

