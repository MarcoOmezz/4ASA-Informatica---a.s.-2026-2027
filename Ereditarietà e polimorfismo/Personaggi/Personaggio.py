import random

class Personaggio:
    def __init__(self, nome:str, pv:int, difesa:int, livello:int):
        self.nome = nome
        self.pv = pv
        self.difesa = difesa
        self.livello = livello
        self.inventario = []

    def attacca(self):
        #casuale = random.randint(1,10)
        #return casuale
        return random.randint(1,10)
    
    def subisciDanno(self, danno:int):
        if danno <= self.pv:
            self.pv -= danno
        else:
            self.pv = 0
            print("Colpo mortale!")

    def cura(self, valore:int):
        self.pv += valore

    def isVivo(self):
        if self.pv > 0:
            return True
        else:
            return 

    def convertiInStringa(self):
        return f"{self.nome};{self.pv};{self.difesa};{self.livello}"

    def stampaStato(self):
        print(f"Personaggio {self.nome} (lv. {self.livello}):\nPV: {self.pv}\nDifesa: {self.difesa}")

    def stampaInventario(self):
        for oggetto in self.inventario:
            print(oggetto)

class Mago(Personaggio):
    def __init__(self, nome:str, pv:int, difesa:int, livello:int, mana:int):
        super().__init__(nome, pv, difesa, livello)
        self.mana = mana


    #esercizio per casa
    def lancia_magia(self):
        if self.mana >= 10:
            #lancio la magia
            danno = random.randint(1, 10)
            return danno
        else:
            print("Non puoi lanciare la magia!")
        return

class Goblin(Personaggio):
    pass

class Guerriero(Personaggio):
    def __init__(self, nome:str, pv:int, difesa:int, livello:int, forza:int):
        super().__init__(nome, pv, difesa, livello)
        self.forza = forza

    def attacco(self):
        danno = random.randint(1,10) + self.forza
        return danno

def main():
    m = Mago("Gigi", 15, 4, 1, 100)
    m.stampaStato()
    #chiamata alla lancia magia
    danno = m.lancia_magia()
    if danno==None:
        pass #indica un errore nel lancio della magia
    else:
        pass #posso continuare con la logica dell'attacco e del danno

    m.inventario.append("Bastone del mago")
    m.inventario.append("Pozione di cura")

    m.stampaInventario()

if __name__=="__main__": #esegui questo codice se il programma è quello principale
    main()