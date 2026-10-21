'''
Dovrai creare una classe biblioteca che contiene una lista di libri. La biblioteca dovrà inoltre
possedere i seguenti metodi: aggiungi_libro(), visualizza_libri(), salva_su_file() e carica_da_file().
Nel main dovrai creare un ciclo infinito che permette di scegliere una delle operazioni indicate sopra
per l’oggetto biblioteca ed eventualmente stampare a video le informazioni richieste.
'''

#importare la libreria dei libri

from libri import Saggio, Romanzo

#classi

class Biblioteca:
    def __init__(self):
        self.lista_libri = []

    def aggiungi_libro(self):
        libro = None
        tipologia = input("Inserisci romanzo o saggio: ")

        if tipologia=="romanzo":
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore: ")
            anno = int(input("Inserisci l'anno di pubblicazione: "))
            genere = input("Inserisci il genere: ")
            if len(titolo) <= 0 or len(autore) <= 0:
                return None #errore
            #creazione oggetto
            libro = Romanzo(titolo, autore, anno, genere)
            
        elif tipologia=="saggio":
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore: ")
            anno = int(input("Inserisci l'anno di pubblicazione: "))
            tema = input("Inserisci il tema: ")
            if len(titolo) <= 0 or len(autore) <= 0:
                return None #errore

            libro = Saggio(titolo, autore, anno, tema)
        else:
            return None #errore

        self.lista_libri.append(libro) #aggiunta all'elenco attuale di libri
        return 1 #tutto a posto

    def visualizza_libri(self):
        for libro in self.lista_libri:
            print(libro) #richiama la __str__ dei libri che abbiamo già definito


#main
def main():
    biblioteca = Biblioteca() #la creo intanto

    operazione = 0
    while operazione != -1:
        operazione = int(input("Inserisci 1 per aggiungere un libro, 2 per vedere la lista, 3 per caricare da file e 4 per salvare la lista su file: "))
        if operazione == 1:
            #inserimento del libro
            if biblioteca.aggiungi_libro() != None:
                print("Libro aggiunto con successo!")
            else:
                print("Errore, libro non aggiunto, riprova!")
        elif operazione == 2:
            #voglio stampare la lista di libri
            biblioteca.visualizza_libri()

if __name__ == "__main__":
    main()