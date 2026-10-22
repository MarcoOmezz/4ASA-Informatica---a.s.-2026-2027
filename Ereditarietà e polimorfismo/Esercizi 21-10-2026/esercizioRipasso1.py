'''
Un istituto vuole gestire un archivio di persone, alcune delle quali sono studenti. Il file di origine dei dati contiene il seguente testo:

P;Mario;Rossi;45
S;Luca;Bianchi;17;4A;7.5
P;Anna;Verdi;38
S;Sara;Neri;18;4B;8.2
S;Marco;Gialli;17;4A;6.4

Il primo campo indica se si tratta di una Persona oppure uno Studente. Crea due classi, una Persona (definita da nome, cognome, età e metodo descrivi()) e una classe Studente, derivata da Persona, con attributi classe_frequentata, media voti e override della funzione descrivi().

Nel main crea una lista chiamata persone, con dentro sia oggetti di tipo Persone che di tipo Studenti. Calcola poi la media dei voti di tutti gli studenti, e inserisci in un nuovo file (studenti_bravi.txt) solo quelli con una media maggiore o uguale ad 8 (crea tutti i metodi necessari per svolgere questa operazione).
'''

class Persona:
    def __init__(self, nome:str, cognome:str, eta:int):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def decrivi(self):
        return f"{self.nome}, {self.cognome}, {self.eta}"

class Studente(Persona):
    def __init__(self, nome, cognome, eta, classe:str, media:float):
        super().__init__(nome, cognome, eta)
        self.classe = classe
        self.media = media

    def descrivi(self):
        studenteStr = super().descrivi() + f", {self.classe}, {self.media}"
        return studenteStr


def main():
    persone = []
    #carico l'elenco di persone dal file
    with open("Ereditarietà e polimorfismo\\Esercizi 21-10-2026\\persone.txt", "r") as file:
        contenuto = file.read()
        righe = contenuto.split("\n") #estraggo una lista di tutte le righe
        for riga in righe:
            #ogni riga contiene le informazioni, devo dividerle tra persone e studenti
            caratteristiche = riga.split(";")
            if riga[0] == "P":
                #persona
                persona = Persona(caratteristiche[1], caratteristiche[2], caratteristiche[3])
                persone.append(persona)
            else:
                #studente
                studente = Studente(caratteristiche[1], caratteristiche[2], caratteristiche[3], caratteristiche[4], caratteristiche[5])
                persone.append(studente)

        somma = 0
        conta = 0
        for p in persone:
            #se p è uno studente
            if isinstance(p, Studente): #controlla se p è di tipo Studente
                #aggiungo valore per il calcolo della media
                somma += float(p.media)
                conta += 1

        media = somma/conta
        print(f"Media: {media:.2f}")

if __name__=="__main__":
    main()