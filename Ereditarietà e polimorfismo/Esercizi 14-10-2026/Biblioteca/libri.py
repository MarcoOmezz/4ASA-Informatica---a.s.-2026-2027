'''
Scrivi un programma che simula un semplice sistema di gestioni libri di una biblioteca. I libri devono
possedere tutti un titolo, un autore e un anno di pubblicazione. Inoltre tutti i libri si distinguono in
Romanzi (che possiedono un attributo genere) e Saggi (che devono avere un attributo tema). Ogni
oggetto di tipo libro dovrà sovrascrivere il metodo __str__() per stampare un messaggio che includa
tutti gli attributi. Ogni libro dovrà inoltre possedere un metodo che ritorni la stringa rappresentativa
per permettere il salvataggio su file delle informazioni.
'''

class Libro:
    def __init__(self, titolo:str, autore:str, anno_pubblicazione:int):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

class Romanzo(Libro):
    def __init__(self, titolo:str, autore:str, anno_pubblicazione:int, genere:str):
        super().__init__(titolo, autore, anno_pubblicazione)
        self.genere = genere

    #questo serve principalmente per print e rappresentazione dell'oggetto nel programma
    def __str__(self):
        return f"Titolo: {self.titolo} ({self.autore} - {self.anno_pubblicazione}) - Genere: {self.genere}"

    #questo serve per la stampa formale dell'oggetto in un file
    def stringaFile(self):
        return f"{self.titolo};{self.autore};{self.anno_pubblicazione};{self.genere}"


class Saggio(Libro):
    def __init__(self, titolo:str, autore:str, anno_pubblicazione:int, tema:str):
            super().__init__(titolo, autore, anno_pubblicazione)
            self.tema = tema
    
    #questo serve principalmente per print e rappresentazione dell'oggetto nel programma
    def __str__(self):
        return f"Titolo: {self.titolo} ({self.autore} - {self.anno_pubblicazione}) - Tema: {self.tema}"

    #questo serve per la stampa formale dell'oggetto in un file
    def stringaFile(self):
        return f"{self.titolo};{self.autore};{self.anno_pubblicazione};{self.tema}"