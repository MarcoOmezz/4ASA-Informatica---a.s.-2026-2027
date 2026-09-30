import random

class Personaggio:
    def __init__(self, nome:str, pv:int, difesa:int, livello:int):
        self.nome = nome
        self.pv = pv
        self.difesa = difesa
        self.livello = livello

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

    def stampaStato(self):
        print(f"Personaggio {self.nome} (lv. {self.livello}):\nPV: {self.pv}\nDifesa: {self.difesa}")


def main():
    p = Personaggio("Gigi", 15, 4, 1)
    p.stampaStato()

if __name__=="__main__": #esegui questo codice se il programma è quello principale
    main()