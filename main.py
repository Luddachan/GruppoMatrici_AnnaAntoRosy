from GestoreMatrice import GestoreMatrice
from sottoclassi import *


matrice = [
    [1, 5, -4],
    [3, 2, 1]
]

# --- Test GestoreMatrice ---
gestore = GestoreMatrice(matrice)
print("Matrice originale")

gestore.stampa_matrice()
print(gestore.valida_matrice())


# --- Test ElaboratoreMatematico ---
elaboratore = ElaboratoreStatistico(matrice)
print("Il valore massimo della matrice è: ", elaboratore.trova_massimo())
print("Valore medio della riga 0 ", elaboratore.media_riga(0))

# --- Test Filtro Matrice ---
filtro = FiltroMatrice(matrice)
filtro.azzera_negativi()

print("Matrice azzerata: ")
b = filtro.stampa_matrice()

a = filtro.appiattisci()
print("Matrice appiattita: ", a)
