# classe derivate

#Sottoclasse per le operazioni matematiche: Eredita da GestoreMatrice.
from matrici.GestoreMatrice import GestoreMatrice
# definizione classe elaboratore matematico 
class ElaboratoreMatematico(GestoreMatrice):
    def trasponi(self):
        righe = len(self.dati)
        colonne = len(self.dati[0])
        trasposta = [[self.dati[i][j]] for i in range (righe) for j in range (colonne)]
        return trasposta 
    
    def moltiplica_per_scalare(self, k):
        return [[elemento * k for elemento in riga] for riga in self.dati]
    
    
# trova il massimo della matrice 
class ElaboratoreStatistico(GestoreMatrice):
    def trova_massimo(self):
        massimo = self.dati[0][0]
        for riga in self.dati:
            for valore in riga:
                if valore > massimo:
                    massimo = valore 
        return massimo 
    
    # trova valore media 
    def media_riga(self, indice_riga):
        riga= self.dati[indice_riga]
        return sum(riga) / len(riga)
    
# classe filtro matrice 
class FiltroMatrice(GestoreMatrice):
    def azzera_negativi(self):
        for i in range(len(self.dati)):
            for j in range(len(self.dati[i])):
                if self.dati[i][j] < 0:
                    self.dati[i][j] = 0
                    
                    
    def appiattisci(self):
        lista = []
        for riga in self.dati:
            for elemento in riga:
                lista.append(elemento)
        return lista
                    

    
    

        