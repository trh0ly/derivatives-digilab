import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def alternative_smile():
    # Datensatz einlesen
    data2 = pd.read_csv('calls17march.txt', # Datensatz
                        delimiter='\t', # Seperator 
                        skiprows=1, # Überspringe die erste Zeile
                        usecols=['Strike','Implied Volatility']) # Auswahl der einzulesenden Spalten

    x = data2['Strike'] # Speichere die eingelesenen Daten aus der Spalte 'Strike' als die Variable x
    y0 = data2['Implied Volatility'] # Überführe die eingelesenen Daten aus der Spalte 'Implied Volatility' in eine Liste
    n = len(y0) # Bestimme die länge der Liste y0 und speichere diese als die Variable n
    y = [] # Lege die leere Liste y an

    # Führe die folgende Operation n mal durch
    for i in np.arange(n):
        a = float(y0[i].replace("%","")) / 100.0 # Entferne für jedes Element in der Liste y0 das Prozentzeichen und teile den Wert durch 100
        y.append(a) # Füge den modifizierten Wert der Liste y an
        
    plt.title('Volatility smile - IBM Calls mit Fälligkeit: 3/17/2017') # Titel der Grafik
    plt.ylabel('Volatilität') # Beschriftung Y-Achse
    plt.xlabel('Preis des Strikes') # Beschriftung X-Achse
    plt.plot(x,y,'o') # Plotten der Datenpunkte
    plt.grid() # Gitternetz
    plt.show() # Funktion zum anzeigen der Grafik

alternative_smile()