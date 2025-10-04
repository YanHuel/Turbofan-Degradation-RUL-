##### Bibliotheken #####

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 


##### Daten einlesen und verstehen #####

dirPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(dirPath)
df = pd.read_csv("inputs\\train_FD001.txt", sep=" ", header=None)

index_names = ["unit_number", "time_in_cycles"]
settings = ["setting 1", "setting 2", "setting 3"]
sensors = ["T2", "T24", "T30", "T50", "P2", "P15", "P30", "Nf", "Nc", "epr", "Ps30", "phi", "NRf", "NRc", "BPR", "farB", "htBleed", "Nf_dmd", "PCNfR_dmd", "W31", "W32"]
col_names = index_names + settings + sensors

dftrain = pd.read_csv("inputs\\train_FD001.txt", sep=" ", header=None, index_col=False, names=col_names)
dftest = pd.read_csv("inputs\\test_FD001.txt", sep=" ", header=None, index_col=False, names=col_names)
dfvalid = pd.read_csv("inputs\\RUL_FD001.txt", sep=" ", header=None, index_col=False, names=['RUL'])

print("Form des Train-Datensatzes: ", dftrain.shape)
print("Form des Test-Datensatzes: ", dftest.shape)
print("Form des Valid-Datensatzes: ", dfvalid.shape)

# Sind NaN-Werte in den Daten vorhanden?
print('Anzahl der NaN-Werte:\n', dftrain.isna().sum())      # -> Nein

# Statistische Information über die ersten beiden Spalten der Daten
print(dftrain.loc[:, ['unit_number', 'time_in_cycles']].describe())

# Statistische Informationen über die Sensoren
print(dftrain.loc[:, "T2":].describe().transpose())


##### Datenvisualisierung #####

"""# Im Balkendiagramm für alle Sensoren
max_time_cycles = dftrain[index_names].groupby('unit_number').max()
plt.figure(figsize = (10,10))
ax = max_time_cycles['time_in_cycles'].plot(kind = 'barh', width = 0.8, stacked = True, align = 'center')
plt.title('Strahltriebwerk Lebenszyklus', fontweight = 'bold', size = 15)
plt.xlabel('Zeitzyklus', fontweight = 'bold', size = 10)
plt.xticks(size = 10)
plt.ylabel('Unit', fontweight = 'bold', size = 10)
plt.yticks(size = 10)
plt.grid(True)
plt.tight_layout()
plt.show()"""


# Anzahl vs Zeitzyklen
max_time_cycles = dftrain[index_names].groupby('unit_number').max()
sns.displot(max_time_cycles['time_in_cycles'], kde=True, bins=20, height=6, aspect=2)
plt.xlabel("Maximaler Zeitzyklus")
plt.ylabel("Anzahl")
plt.title("Verteilung aller Lebenszyklen", fontweight = 'bold', size = 15)
plt.show()