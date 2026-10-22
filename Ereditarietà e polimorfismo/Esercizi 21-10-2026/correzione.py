class ContoBancario:
    def __init__(self, intestatario, saldo_iniziale=0):
        self.intestatario = intestatario
        self.saldo = saldo_iniziale
        self.movimenti = {}
        self.contatore = 1

    def _genera_codice(self):
        codice = f"OP{self.contatore:02d}"
        self.contatore += 1
        return codice

    def versa(self, importo):
        self.saldo += importo
        self.movimenti[self._genera_codice()] = importo

    def preleva(self, importo):
        self.saldo -= importo
        self.movimenti[self._genera_codice()] = -importo

    def mostra_movimenti(self):
        for codice, movimento in self.movimenti.items():
            print(f"{codice}: {movimento}")

    def calcola_costi(self):
        totale = sum(self.movimenti.values())
        print(f"Saldo attuale: {self.saldo}€ | Bilancio operazioni: {totale}€")

# Esempio di utilizzo:
conto = ContoBancario("Mario Rossi", 1000)
conto.versa(200)
conto.preleva(150)
conto.mostra_movimenti()
conto.calcola_costi()