import tkinter as tk

numero1 = 0
numero2 = 0
operazione = ""

def cliccato(valore):
    testoAttuale = display.cget("text") #ci prendiamo il valore di text della label
    if testoAttuale == "0":
        testoAttuale = str(valore)
    else:
        testoAttuale = testoAttuale + str(valore)
    display.config(text=testoAttuale)

def cancellaUltimo():
    #leggere il contenuto della label, trasformarlo in stringa e rimuovere solo l'ultimo elemento
    testoAttuale = display.cget("text")
    if len(testoAttuale) > 1:
        testoAttuale = testoAttuale[0:len(testoAttuale)-1] #prendo dal primo carattere al penultimo
    else:
        testoAttuale = "0"

    display.config(text=testoAttuale)

def operazione(op: str):
    global numero1, numero2, operazione #rendo globali e accessibili anche in chiamate successive queste variabili
    numeroAttuale = float(display.cget("text"))
    numero1 = numeroAttuale
    operazione = op
    #svuoto il display
    display.config(text="0")

def calcolaRisultato():
    global numero1, numero2, operazione
    numeroAttuale = float(display.cget("text"))
    numero2 = numeroAttuale
    risultato = 0
    if operazione == "+":
        risultato = numero1+numero2
    #aggiorno l'interfaccia
    display.config(text=f"R = {risultato}")

root = tk.Tk()
root.geometry("400x600")
root.title("Calcolatrice")

frame_display = tk.Frame(root)
frame_display.pack()

frame_pulsanti = tk.Frame(root)
frame_pulsanti.pack()

#creo il display
display = tk.Label(frame_display, text="0", font=("Arial", 20))
display.grid(row=0, column=0, sticky="e")

elimaUltimo = tk.Button(frame_display, text="<", font=("Arial", 15), command=cancellaUltimo)
elimaUltimo.grid(row=0, column=1, padx=10, pady=10, ipadx=5, ipady=5, sticky="w")

frame_display.columnconfigure(0, weight=3)
frame_display.columnconfigure(1, weight=1)

#griglia
numero = 1
for i in range(0, 3):
    for j in range(0, 3):
        pulsante = tk.Button(frame_pulsanti, text=f"{numero}", command=lambda n=numero: cliccato(n))
        pulsante.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        numero += 1

virgola = tk.Button(frame_pulsanti, text=",")
virgola.grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=10)

zero = tk.Button(frame_pulsanti, text="0", command=lambda: cliccato(0))
zero.grid(row=3, column=1, padx=10, pady=10, ipadx=10, ipady=10)

uguale = tk.Button(frame_pulsanti, text="=", command=calcolaRisultato)
uguale.grid(row=3, column=2, padx=10, pady=10, ipadx=10, ipady=10)

diviso = tk.Button(frame_pulsanti, text="/")
diviso.grid(row=3, column=3, padx=10, pady=10, ipadx=10, ipady=10)

piu = tk.Button(frame_pulsanti, text="+", command=lambda: operazione("+"))
piu.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=10)

meno = tk.Button(frame_pulsanti, text="-")
meno.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)

per = tk.Button(frame_pulsanti, text="x")
per.grid(row=2, column=3, padx=10, pady=10, ipadx=10, ipady=10)

root.mainloop()