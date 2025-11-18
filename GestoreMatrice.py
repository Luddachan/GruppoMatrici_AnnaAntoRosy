#CLASSE BASE: Gestore Matrice

class GestoreMatrice:
    def __init__(self, dati): #inizializza l'attributo "dati" 
        self.dati = dati
    def stampa_matrice(self): #stampa la matrice in modo leggibile
        for riga in self.dati:
            for elemento in riga:
                print(elemento, end=" ")
            print()
            
    def valida_matrice (self): #controlla se la matrice è valida (tutte le righe hanno la stessa lunghezza)
        lunghezza_riga = len(self.dati[0])
        for riga in self.dati:
            if len(riga) != lunghezza_riga:
                return False
        return True
