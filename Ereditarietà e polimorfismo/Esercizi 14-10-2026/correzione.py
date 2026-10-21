class Veicolo:
    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello

    def descrizione(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}")


class Auto(Veicolo):
    def __init__(self, marca, modello, porte):
        super().__init__(marca, modello)
        self.porte = porte

    def descrizione(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Porte: {self.porte}")

    def dettagli(self):
        return f"{self.marca}-{self.modello}-{self.porte}"


class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo

    def descrizione(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Tipo: {self.tipo}")

def main():
    auto1 = Auto("Ferrari", "F40", 3)
    auto2 = Auto("Brabus", "Bodo", 3)

    moto1 = Moto("Honda", "PCX 125", "Scooter")

    auto1.descrizione()
    auto2.descrizione()
    moto1.descrizione()

    with open("veicoli.txt", "w", encoding="utf-8") as file:
        file.write(auto1.dettagli() + "\n")
        file.write(auto2.dettagli())

if __name__ == "__main__":
    main()
    