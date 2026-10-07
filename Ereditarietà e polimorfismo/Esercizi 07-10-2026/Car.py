'''
Definisci la classe Car, per rappresentare un’auto con gli attributi make (marca dell’auto), model
(modello), year (anno di produzione), max_speed (velocità massima) e speed (velocità, che può
andare da 0 fino a max_speed). Aggiungi poi il metodo change_speed(diff) che aggiorna la
velocità della macchina di diff km/h (assicurandosi che non diventi un valore negativo) e
get_speed(), che restituisce la velocità corrente dell’auto. Create anche un metodo che stampa
tutti gli attributi dell'auto.
'''
class Car:
    def __init__(self, marca, modello, year, max_speed, speed):
        self.marca = marca
        self.modello = modello
        self.year = year
        self.max_speed = max_speed
        self.setSpeed(speed)

    def setSpeed(self, speed):
        if speed >= 0:
            self.__speed = speed
        elif speed > self.max_speed:
            self.__speed = self.max_speed
        else:
            self.__speed = 0

    def getSpeed(self):
        return self.__speed

    def change_speed(self, diff:float):
        self.setSpeed(self.__speed+diff)

    def stampaAuto(self):
        print(f"{self.marca}-{self.modello}-{self.year}-{self.max_speed}-{self.__speed}")

def main():
    c = Car("Ferrari", "F40", 1986, 325, 0)
    c.stampaAuto()
    c.change_speed(20)
    c.stampaAuto()
    c.change_speed(-50)
    c.stampaAuto()

if __name__=="__main__":
    main()