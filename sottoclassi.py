#Sottoclasse per le operazioni matematiche: Eredita da GestoreMatrice.
from GestoreMatrice import GestoreMatrice
class ElaboratoreMatematico(GestoreMatrice):
    def trasponi(self):
        if not self.valida_matrice():
            return None
        if not self.dati or not self.dati[0]: #Controlla se la matrice è vuota
            return []
        N = len(self.dati)
        M = len(self.dati[0])
        matrice_trasposta = [[0] * N for _ in range(M)] #Crea una matrice vuota di dimensioni MxN
        for i in range(N):
            for j in range(M):
                matrice_trasposta[j][i] = self.dati[i][j]
        print("\nTrasposizione completata.")
        return matrice_trasposta
    def moltiplica_per_scalare(self, k):
        if not self.valida_matrice():
            return None
        nuova_matrice = []
        for riga in self.dati:
            nuova_riga = [elemento * k for elemento in riga]
            nuova_matrice.append(nuova_riga)
        print(f"\nMoltiplicazione per lo scalare {k} completata.")
        return nuova_matrice